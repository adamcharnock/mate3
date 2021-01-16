from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Iterable, List, Optional

from loguru import logger
from pymodbus.constants import Defaults, Endian
from pymodbus.payload import BinaryPayloadDecoder

from mate3.devices import (
    DEVICE_IDS,
    ChargeControllerDevice,
    FNDCDevice,
    FXInverterDevice,
    Mate3Device,
    OPTICSDevice,
    SinglePhaseRadianInverterDevice,
    SplitPhaseRadianInverterDevice,
)
from mate3.modbus_client import CachingModbusClient, ModbusTcpClient, NonCachingModbusClient
from mate3.sunspec.fields import Field, FieldRead, Mode
from mate3.sunspec.model_base import Model
from mate3.sunspec.models import (
    ChargeControllerConfigurationModel,
    FLEXnetDCConfigurationModel,
    FXInverterConfigurationModel,
    OutBackSystemControlModel,
    RadianInverterConfigurationModel,
    SunSpecEndModel,
    SunSpecHeaderModel,
)


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

        # Set up devices
        self.mate3s: Dict[None, Mate3Device] = {}
        self.charge_controllers: Dict[int, ChargeControllerDevice] = {}
        self.fndcs: Dict[int, FNDCDevice] = {}
        self.fx_inverters: Dict[int, FXInverterDevice] = {}
        self.single_phase_radian_inverters: Dict[int, SinglePhaseRadianInverterDevice] = {}
        self.split_phase_radian_inverters: Dict[int, SplitPhaseRadianInverterDevice] = {}
        self.opticses: Dict[int, OPTICSDevice] = {}

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

        # Now read everything and initialise with the devices. NB - yes, this should only happen once on connection.
        self._read_all_devices_and_initialise()

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

    def _get_single_device(self, name: str) -> Model:
        """
        Helper function so that e.g. if there's only one charge controller in self.charge_controllers, you can call
        self.charge_controller to get it.
        """
        devices = getattr(self, f"{name}es" if name.endswith("s") else f"{name}s")
        if len(devices) != 1:
            raise RuntimeError(
                (
                    f"Must be one, and only one, {name} device to be able to use `{name}` attribute - but there are "
                    f"{len(devices)}"
                )
            )
        return list(devices.values())[0]

    @property
    def connected_devices(self) -> Iterable[Model]:
        # First ones which should only have a single device:
        yield self.mate3

        # And those without a config, but per port:
        if self.opticses:
            yield from self.opticses.values()

        # Now those with device and config. (NB: we're explicit here as opposed to relying on hasattr(device, 'config')
        # just in case a model actually had a 'config' field.)
        for d in (
            "charge_controllers",
            "fndcs",
            "fx_inverters",
            "single_phase_radian_inverters",
            "split_phase_radian_inverters",
        ):
            for device in getattr(self, d).values():
                yield device
                yield device.config

    @property
    def mate3(self) -> Mate3Device:
        """
        Return the mate3.
        """
        return self._get_single_device("mate3")

    @property
    def charge_controller(self) -> ChargeControllerDevice:
        """
        Return the charge controller if there's only one.
        """
        return self._get_single_device("charge_controller")

    @property
    def fndc(self) -> FNDCDevice:
        """
        Return the FNDC if there's only one.
        """
        return self._get_single_device("fndc")

    @property
    def fx_inverter(self) -> FXInverterDevice:
        """
        Return the FX inverter if there's only one.
        """
        return self._get_single_device("fx_inverter")

    @property
    def single_phase_radian_inverter(self) -> SinglePhaseRadianInverterDevice:
        """
        Return the single phase radian inverter if there's only one.
        """
        return self._get_single_device("single_phase_radian_inverter")

    @property
    def split_phase_radian_inverter(self) -> SplitPhaseRadianInverterDevice:
        """
        Return the split phase radian inverter if there's only one.
        """
        return self._get_single_device("split_phase_radian_inverter")

    @property
    def optics(self) -> OPTICSDevice:
        """
        Return the OPTICS if there's only one.
        """
        return self._get_single_device("optics")

    def _read_contiguous_fields(self, address: int, fields: Iterable[Field]):

        # First, read the registers:
        count = sum(f.size for f in fields)
        registers = self._client.read_holding_registers(address=address, count=count)
        read_time = datetime.now()

        # Now use the decoder to decode the fields:
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

        if device_id not in DEVICE_IDS:
            logger.warning(f"Unknown model type with device ID {device_id}")
            return None

        # Instantiate the model:
        model = DEVICE_IDS[device_id]()

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

        # Now read:
        for block_fields in blocks:
            start_address = device_address + block_fields[0].start - 1  # -1 as starts are 1-indexed in fields
            count = sum(f.size for f in fields)
            logger.debug(f"Reading block of {len(block_fields)} fields from {start_address} (count={count})")
            self._read_contiguous_fields(address=start_address, fields=block_fields)

        return model

    def _read_all_devices_and_initialise(self):
        """
        On set up, read all devices so we know about them. In general, you should only do this once, and afterward read/
        write on each individual field. If, for some reason, you want to re-read everything (e.g. you just plugged in a
        new device), then you should just re-create a new Mate3Client.
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

        # OK, now assign everything:
        self._update_device(models, self.mate3s, Mate3Device, OutBackSystemControlModel)
        self._update_device(models, self.charge_controllers, ChargeControllerDevice, ChargeControllerConfigurationModel)
        self._update_device(models, self.fndcs, FNDCDevice, FLEXnetDCConfigurationModel)
        self._update_device(models, self.fx_inverters, FXInverterDevice, FXInverterConfigurationModel)
        self._update_device(
            models,
            self.single_phase_radian_inverters,
            SinglePhaseRadianInverterDevice,
            RadianInverterConfigurationModel,
        )
        self._update_device(
            models, self.split_phase_radian_inverters, SplitPhaseRadianInverterDevice, RadianInverterConfigurationModel
        )
        self._update_device(models, self.opticses, OPTICSDevice, None)

    def _update_device(
        self,
        models: List[Model],
        devices_per_port_attr: Dict[int, Model],
        model_class: Model,
        config_class: Optional[Model],
    ) -> None:

        # Since we're starting from scratch, ensure there are no current devices:
        if devices_per_port_attr:
            raise RuntimeError(f"devices_by_port should be empty!")

        devices_per_port = self._get_models_per_port(models, model_class)

        # If config_class is None, then the class has no config, so easy:
        if config_class is None:
            for port, device in devices_per_port.items():
                devices_per_port_attr[port] = device
            return

        configs_per_port = self._get_models_per_port(models, config_class)

        # OK, there's a few options around whether the above variables contain anything.
        # - Both present, then we're good - continue. All devices should have a configuration class.
        # - Device isn't present - this means the device itself wasn't detected, so ignore. Note that usually this would
        #   imply the config class is null (since the config shouldn't be there if the device isn't) except in the case
        #   of Radian inverters, as the same config class is shared across both single and split phase devices (so that
        #   if only one type is present, the other will have empty model values and non-empty config).
        # - Both are missing - this is covered by the above.
        # So, the short summary is we only care about devices where the devices are present, and in all other cases
        # there *should* be config field values too.
        if not devices_per_port:
            return
        else:
            if not configs_per_port:
                logger.warning(
                    (
                        f"Only model ({model_class}) field values and no config ({config_class}) fields were read. This"
                        f" is undefined behaviour, so ignoring {model_class}."
                    )
                )
                return

        # Check model and config have the same ports:
        if set(devices_per_port).symmetric_difference(set(configs_per_port)):
            raise RuntimeError("Config and models have different ports!")

        # Assign any devices for the given ports:
        for port in devices_per_port:

            # Fail if it already exists ... since we're starting from scratch there shouldn't be anything in there.
            if port in devices_per_port_attr:
                raise RuntimeError(f"Device already at port {port}!")

            device = devices_per_port_attr[port] = devices_per_port[port]
            device.config = configs_per_port[port]

    def _get_models_per_port(self, models: List[Model], model_class: Model):
        """
        Generally there are multiple devices for a given model (e.g. multiple FX inverters), and the way we delineate
        them is by the port (which they are plugged into the Hub with). So it's pretty common to want to get, for each
        model, the models in a dict <port>: <model_read>.
        """

        # Filter to only the model we care about:
        models_per_port = {}
        ports = []
        for model in models:
            if isinstance(model, model_class):
                port = None
                if hasattr(model, "port_number"):
                    port = model.port_number.value
                models_per_port[port] = model
                ports.append(port)

        # Check we don't have multiple devices with the same port:
        if len(ports) > len(set(ports)):
            raise RuntimeError(f"Multiple {model_class} models have the same port!")

        return models_per_port

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
