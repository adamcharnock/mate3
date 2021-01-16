from dataclasses import dataclass
from datetime import datetime
from typing import Iterable, List

from loguru import logger
from pymodbus.constants import Defaults, Endian
from pymodbus.payload import BinaryPayloadDecoder

from mate3.devices import DeviceValues
from mate3.modbus_client import CachingModbusClient, ModbusTcpClient, NonCachingModbusClient
from mate3.read import AllModelReads, ModelRead
from mate3.sunspec.fields import Field, FieldRead, Mode, Uint16Field, Uint32Field
from mate3.sunspec.models import MODEL_DEVICE_IDS, SunSpecEndModel, SunSpecHeaderModel


@dataclass(frozen=False)
class ReadingRange:
    """
    Mate's work better reading a contiguous range of values at once as opposed to indivudally. This is a simple wrapper
    for such a contiguous range.
    """

    fields: List[Field]
    start: int
    size: int

    @property
    def end(self):
        return self.start + self.size

    def extend(self, field: Field):
        self.fields.append(field)
        self.size += field.size


class Mate3Client:
    """
    The main Mate3 object users will interact with. Can (and should) be used as a context manager.
    """

    sunspec_register: int = 40000

    def __init__(
        self,
        host: str,
        port: int = Defaults.Port,
        cache_path: str = None,
        cache_only: bool = False,
        cache_writeable: bool = False,
    ):
        self.host: str = host
        self.port: int = port
        self._cache_path: str = cache_path
        self._cache_only: bool = cache_only
        self._cache_writeable: bool = cache_writeable
        self._client: ModbusTcpClient = None
        self._devices: DeviceValues = None

    def connect(self):
        """
        Connect to the mate over modbus.
        """
        if self._cache_path is not None:
            self._client = CachingModbusClient(
                host=self.host,
                port=self.port,
                cache_path=self._cache_path,
                cache_only=self._cache_only,
                writeable=self._cache_writeable,
            )
        else:
            self._client = NonCachingModbusClient(self.host, self.port)

        # Now read everything. Why? Because most use of the API assumes fields have already been read (e.g. to get
        # the devices, or the addresses of fields, etc.)
        self.read_all()

    def close(self):
        """
        Close the modbus connection to the mate.
        """
        self._client.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def devices(self) -> DeviceValues:
        if self._devices is None:
            raise RuntimeError("Can't access devices until after first read")
        return self._devices

    def _read_contiguous_fields(self, address: int, fields: Iterable[Field]):

        # First, read the registers:
        count = sum(f.size for f in fields)
        registers = self._client.read_holding_registers(address=address, count=count)
        read_time = datetime.now()

        # Now use the decoder to decode the fields:
        decoder = BinaryPayloadDecoder.fromRegisters(registers=registers, byteorder=Endian.Big, wordorder=Endian.Big)
        registers_pointer = 0
        for field in fields:
            end_register_pointer = registers_pointer + field.size
            field.last_read = FieldRead(
                registers=registers[registers_pointer:end_register_pointer],
                address=address + registers_pointer,
                time=read_time,
            )

            # Bump our register pointer forward
            registers_pointer = end_register_pointer

    def _read_model(self, device_address: int, first: bool):
        """
        Read an individual model at `address`. Use `first` to specify that this is the first block - see comment below.
        By default reads everything in the model - use `only` to specify a list of Fields to read, if you want to limit.
        """
        # Read the first register for the device ID:
        registers = self._client.read_holding_registers(address=device_address, count=2)
        decoder = BinaryPayloadDecoder.fromRegisters(registers, byteorder=Endian.Big, wordorder=Endian.Big)

        # If first, then this is the SunSpecHeaderModel, which has a device ID of Uint32 type not Uint16 like the rest.
        if first:
            device_id = decoder.decode_32bit_uint()
        else:
            device_id = decoder.decode_16bit_uint()

        if device_id not in MODEL_DEVICE_IDS:
            logger.warning(f"Unknown model type with device ID {device_id}")
            return None

        # Instantiate the model:
        model = MODEL_DEVICE_IDS[device_id]()

        # TODO: Make sure we don't read past the end of length (as reported by device). This shouldn't happen except in
        # e.g. a case where the (old) device model firmware returns only 10 fields, and then 'new' one (whatever we're
        # using in our spec) specifies 11, then we'd accidentally try to read one more.

        # Get the readable fields:
        fields = model.fields(modes=(Mode.R, Mode.RW))

        # Get the ranges of registers which can be read as a contiguous block, which  allows for greater performance
        # than reading a single register at a time. (NB: the fields aren't contiguous at the moment as we've ignored
        # e.g. write-only fields.) The mate3s gets unhappy if one tries to read too much at once, so limit to no more
        # than 100 registers read at once.
        max_range_size = 100
        block_fields = []
        blocks = []
        block_size = 0
        for field in sorted(fields, key=lambda x: x.start):
            if (not block_fields) or block_fields[-1].end != field.start or block_size + field.size >= max_range_size:
                # OK, we're done with this batch, so create a new one:
                block_fields = [field]
                blocks.append(block_fields)
                # Reset:
                block_size = 0
            else:
                block_fields.append(field)
                block_size += field.size

        # Get registers in large ranges, as this drastically improves performance and isn't so demanding of the mate3
        for block_fields in blocks:
            start_address = device_address + block_fields[0].start - 1  # -1 as starts are 1-indexed in fields
            count = sum(f.size for f in fields)
            logger.debug(f"Reading block of {len(block_fields)} fields from {start_address} (count={count})")
            self._read_contiguous_fields(address=start_address, fields=block_fields)

        # TODO: scale factors

        return model

    def read_all(self):
        """
        Read all values from all devices. If you want to read only specified fields use e.g.
            client.devices.mate3.system_name.read()
        This method, however, is optimised for reading everything.
        """
        register = self.sunspec_register
        max_models = 30
        first = True
        models = []
        # all_reads = AllModelReads()
        for _ in range(max_models):
            model = self._read_model(register, first)
            first = False

            # Unknown device
            if model is None:
                continue

            # No more blocks to read
            if isinstance(model, SunSpecEndModel):
                break

            # Save the model:
            models.append(model)

            # Move register to next block - that is, add the length of the block, which is what follows after the length
            # field. For normal fields, we'll already have read 2 registers (DI and length) so we must add this to our
            # total increment. For the SunSpecHeaderModel, we need to add 4 as DID is a UInt32 in this case (i.e. 2
            # registers) and there's a model ID field (1 register) and length (1 register)
            register += model.length.value + (4 if isinstance(model, SunSpecHeaderModel) else 2)

        # create devices if needed:
        if self._devices is None:
            self._devices = DeviceValues(client=self)

        # update:
        self._devices.update(models)

    # def read_all_modbus_values_unparsed(self):
    #     """
    #     This method just reads all of the values from the modbus devices, with no care about parsing them. All it
    #     assumes is the standard structure of two registers (DID + length), except for the header.
    #     """
    #     register = self.sunspec_register
    #     max_models = 30
    #     first = True
    #     reads = {}
    #     for _ in range(max_models):
    #         # Data starts generally at 3rd register, except for start (SunSpecHeaderModel) where it starts at 5th
    #         data_offset = 4 if first else 2
    #         registers = self._client.read_holding_registers(address=register, count=data_offset)
    #         # The length is the last register (i.e. the one before data)
    #         _, length = Uint16Field._from_registers(None, registers[-1:])

    #         # We're done when length == 0 i.e. SunSpecEndModel
    #         if length == 0:
    #             break

    #         # Now read everything (in maximum bunches of 100)
    #         batch = 100
    #         for start_offset in range(0, length, batch):
    #             count = min(batch, length - start_offset)
    #             registers = self._client.read_holding_registers(
    #                 address=register + data_offset + start_offset, count=count
    #             )
    #             addresses = [register + i for i in range(count)]
    #             for addr, bites in zip(addresses, registers):
    #                 reads[addr] = bites

    #         # See comment in self.read re the increment of 2 or 4
    #         register += length + (4 if first else 2)
    #         first = False

    #     return reads
