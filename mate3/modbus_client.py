import json
from hashlib import md5
from pathlib import Path

from loguru import logger
from pymodbus.client.sync import ModbusTcpClient


class NonCachingModbusClient(ModbusTcpClient):
    """
    Let's raise errors nicely at this stage, and just get registers from the response:
    """

    def read_holding_registers(self, *args, **kwargs):
        response = super().read_holding_registers(*args, **kwargs)
        if isinstance(response, Exception):
            raise response
        return response.registers


class CachingModbusClient(NonCachingModbusClient):
    """
    This is a simple wrapper around ModbusClient that can cache values during use, write them to disk, and then read
    those values. It's particularly useful for:

        - Testing/debugging if you don't have the same physical Outback gear as others.
        - Not hammering your Mate3 while developing, and continually having to restart it!

    If cache_only is False, the cache will be continually updated with anything not in the cache, whereas if True, then
    the cache won't be updated i.e. it'll never hit the Mate3 directly and only rely on the cache.

    If writeable is False, then writes can still be done when in caching mode, but it won't actually persist those
    changes to the cache on disk. This is useful mostly for integration testing etc. - you can check a `write` 'works'
    without changing your cache.
    """

    def __init__(self, cache_path: str, *args, cache_only: bool = False, writeable: bool = False, **kwargs):
        self._cache_path = Path(cache_path)
        self._cache = {}
        self._cache_only = cache_only
        self._writeable = writeable
        self._original_cache_hash = None
        if self._cache_path.exists():
            self._cache = self._read_cache()
            self._original_cache_hash = self._hash()
        else:
            if self._cache_only:
                raise RuntimeError("Cache doesn't exist!")
        self._cache_only = cache_only
        if not self._cache_only:
            super().__init__(*args, **kwargs)

    def _read_cache(self):
        with open(self._cache_path) as f:
            cache = json.load(f)
            cache = {int(addr): val for addr, val in cache.items()}
        return cache

    def _write_cache(self):
        # Only write if changes:
        if self._hash() == self._original_cache_hash:
            logger.debug("No changes to cache so not saving")
            return

        # Only write to disk if writeable
        if not self._writeable:
            logger.info("Not persisting any changes to cache on client close as writeable is False")
        else:
            with open(self._cache_path, "w") as f:
                json.dump(self._cache, f, indent=2)

    def _hash(self):
        """
        Return a hash of the current cache
        """
        hsh = md5()
        for k, v in self._cache.items():
            hsh.update(k.to_bytes(32, byteorder="little", signed=False))
            hsh.update(v.to_bytes(32, byteorder="little", signed=False))
        return hsh.hexdigest()

    def read_holding_registers(self, address, count):
        """
        Replace the existing method with our own to do the caching.
        """
        # Get all the addresses:
        addresses = [address + i for i in range(count)]
        # If there are any uncached, then we read the whole lot again:
        if any(addr not in self._cache for addr in addresses):
            if self._cache_only:
                # If we're cache_only, then cache miss is an error
                raise ValueError(
                    f"Uncached lookup at addresses {[addr for addr in addresses if addr not in self._cache]}"
                )
            registers = super().read_holding_registers(address=address, count=count)
            for addr, bites in zip(addresses, registers):
                self._cache[addr] = bites
        # Return results from cache:
        return [self._cache[addr] for addr in addresses]

    def write_registers(self, address, registers):
        """
        On write, add to cache, then do the usual write (unless self._cache_only)
        """

        # Cache it:
        for i, register in enumerate(registers):
            self._cache[address + i] = register

        # Write to device if not cache_only:
        if not self._cache_only:
            return super().write_registers(address=address, registers=registers)

        # And now update the cache (if needed):
        self._write_cache()

    def close(self, *args, **kwargs):
        """
        On close, write the cache then close properly.
        """
        self._write_cache()
        if not self._cache_only:
            super().close(*args, **kwargs)
