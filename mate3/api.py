import logging
from typing import Union, Iterable, List, Tuple, Dict

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.constants import Defaults

from mate3.base_parser import parse, Field, Mode
from mate3.io import read_block_information, SUNSPEC_REGISTER_OFFSET, combine_ints, split_int
from mate3.structures import *


AnyBlock = Union[
    SunspecCommonModelBlock,
    SunspecInverterSinglePhaseBlock,
    SunspecInverterSplitPhaseBlock,
    SunspecInverterThreePhaseBlock,
    Mate3Block,
    ChargeControllerBlock,
    ChargeControllerConfigurationBlock,
    FxInverterBlock,
    FxInverterConfigurationBlock,
    SplitPhaseRadianInverterBlock,
    RadianInverterConfigurationBlock,
    SinglePhaseRadianInverterBlock,
    FlexnetDcBlock,
    FlexnetDcConfigurationBlock,
    OutbackSystemControlBlock,
]

logger = logging.getLogger(__name__)


class Mate3Factory(object):

    def __init__(self, host: str, port: int=Defaults.Port):
        self.host = host
        self.port = port

    def __enter__(self) -> "Mate3":
        self.client = ModbusClient(self.host, self.port)
        return Mate3(self.client)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()


mate3_connection = Mate3Factory


class Mate3(object):
    def __init__(self, client: ModbusClient):
        self.client = client

    def _block_information(self) -> List[Tuple[Device, int]]:
        """Get information for all available blocks

        Returns a list of 2-tuples. The first value is the Device instance, the
        second is the starting modbus register for that device
        """
        register: int = SUNSPEC_REGISTER_OFFSET
        blocks = []
        for _ in range(0, 30):
            block_size, device = read_block_information(self.client, register)

            if device is Device.end_of_sun_spec:
                # No more blocks to read
                break

            if not device:
                # Unknown device
                continue

            blocks.append((device, register))

            register = register + block_size + 2

        return blocks

    def all_blocks(self) -> Iterable[AnyBlock]:
        """Get all blocks from the mate3

        This gets all available information
        """
        for device, start_register in self._block_information():
            structure = parse(device, self.client, start_register)
            if structure:
                yield structure

    def get_device_blocks(self, device: Device) -> Iterable[AnyBlock]:
        """Get all blocks for devices of the specified type

        Multiple blocks will be returned if you have multiple devices
        of that type attached to your Mate3s.
        """
        for device, start_register in self._block_information():
            if device != device:
                continue

            structure = parse(device, self.client, start_register)
            if structure:
                yield structure

    def get_values(self, *fields: Field) -> Dict[Field, List]:
        """Get specific values for the specified fields

        Returns a dictionary indexed by field object. THe dictionary values
        are lists. A list will have a value for every device.

        Example:

            >>> values = client.get_values(
            ...    ChargeControllerParser.battery_current,
            ...    ChargeControllerParser.battery_voltage
            ... )
            {
                Field(name='battery_current', ...): [297, 284],
                Field(name='battery_voltage', ...): [319, 319]
            }

        In the above example we have two charge controllers, were therefore
        have two values for each field.

        """
        fields_by_device: Dict[Device, List[Field]] = {}
        values_by_field: Dict[Field, List] = {}

        for field in fields:
            fields_by_device.setdefault(field.device, [])
            fields_by_device[field.device].append(field)

        for device, start_register in self._block_information():
            if device not in fields_by_device:
                continue

            fields_ = fields_by_device[device]
            structure = parse(device, self.client, start_register, only_fields=fields_)
            for field in fields_:
                values_by_field.setdefault(field, [])
                values_by_field[field].append(getattr(structure, field.name))

        return values_by_field

    def set_value(self, field: Field, value: int, port: int = None):
        """Set the value for the specified field

        The value must be an integer. To discover the correct format for this
        integer you should read the data using all_blocks().

        Example:

            >>> client.set_value(
            >>>     field=ChargeControllerConfigurationParser.absorb_volts,
            >>>     value=330,  # 33.0 volts
            >>>     port=3,  # Optional, required when multiple devices of the same type are present
            >>> )

        Warning:

            Ensure you have read the LICENSE file before using this feature. Note the
            section which begins:

                THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
                EXPRESS OR IMPLIED

            Specifically, it is quite possible that you can cause damage to your equipment
            through use of this feature. Be careful!

        """
        if field.mode == Mode.R:
            raise Exception(f"{field.name} is read-only. You cannot set the value of this field.")

        # Look for devices which math the field and port (if specified)
        found_devices = []
        for device, start_register in self._block_information():
            if field.device != device:
                continue

            parser = get_parser(device)
            if hasattr(parser, 'port_number'):
                structure = parse(device, self.client, start_register, only_fields=[parser.port_number])
                if port is not None and structure.port_number != port:
                    continue

                found_devices.append(start_register)
            else:
                found_devices.append(start_register)

        # Throw some sensible errors
        if not found_devices:
            raise Exception(f"No device of type {field.device.name} found on hub port {port}")
        if len(found_devices) > 1:
            if port:
                raise Exception(
                    f"Multiple devices of type {field.device.name} found on hub port {port}. "
                    f"This is very unexpected, please raise an issue in GitHub if you see this, "
                    f"including details of the device you are trying to set values on."
                )
            else:
                raise Exception(
                    f"Multiple devices of type {field.device.name} found. Please specify a hub port number "
                    f"using the `port` parameter."
                )

        # What register do we need to write to?
        field_register = found_devices[0] + field.start - 1

        # Split the integer into multiple values according to the field's type.
        # This will also raise an error if the provided value is to big/small.
        prepared_values = split_int(value, field.type)

        logger.debug(
            f"Setting register {field_register} to value {value} "
            f"(which is a {field.type.__name__} represented as {len(prepared_values)} values: {prepared_values})"
        )

        # Do the write
        self.client.write_registers(field_register, prepared_values)
