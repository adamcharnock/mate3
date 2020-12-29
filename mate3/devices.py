import dataclasses as dc
from typing import Any, Dict, Iterable, List, Optional

from loguru import logger

from mate3.field_values import FieldValue, ModelValues
from mate3.sunspec.model_base import Model
from mate3.sunspec.models import (
    ChargeControllerConfigurationModel,
    ChargeControllerModel,
    FLEXnetDCConfigurationModel,
    FLEXnetDCRealTimeModel,
    FXInverterConfigurationModel,
    FXInverterRealTimeModel,
    OutBackModel,
    OutBackSystemControlModel,
    RadianInverterConfigurationModel,
    SinglePhaseRadianInverterRealTimeModel,
    SplitPhaseRadianInverterRealTimeModel,
)
from mate3.sunspec.values import (
    ChargeControllerConfigurationValues,
    ChargeControllerValues,
    FLEXnetDCConfigurationValues,
    FLEXnetDCRealTimeValues,
    FXInverterConfigurationValues,
    FXInverterRealTimeValues,
    OPTICSPacketStatisticsValues,
    OutBackSystemControlValues,
    OutBackValues,
    RadianInverterConfigurationValues,
    SinglePhaseRadianInverterRealTimeValues,
    SplitPhaseRadianInverterRealTimeValues,
)


@dc.dataclass
class ChargeControllerDeviceValues(ChargeControllerValues):
    """
    Simple wrapper to combine the value and config models.
    """

    config: ChargeControllerConfigurationValues = dc.field(metadata={"field": False})


@dc.dataclass
class FNDCDeviceValues(FLEXnetDCRealTimeValues):
    """
    Simple wrapper to combine the real-time and config models.
    """

    config: FLEXnetDCConfigurationValues = dc.field(metadata={"field": False})


@dc.dataclass
class FXInverterDeviceValues(FXInverterRealTimeValues):
    """
    Simple wrapper to combine the real-time and config models.
    """

    config: FXInverterConfigurationValues = dc.field(metadata={"field": False})


@dc.dataclass
class SinglePhaseRadianInverterDeviceValues(SinglePhaseRadianInverterRealTimeValues):
    """
    Simple wrapper to combine the real-time and config models.
    """

    config: RadianInverterConfigurationValues = dc.field(metadata={"field": False})


@dc.dataclass
class SplitPhaseRadianInverterDeviceValues(SplitPhaseRadianInverterRealTimeValues):
    """
    Simple wrapper to combine the real-time and config models.
    """

    config: RadianInverterConfigurationValues = dc.field(metadata={"field": False})


@dc.dataclass
class Mate3DeviceValues(OutBackValues):
    """
    Simple wrapper to combine the value and config models.
    """

    config: OutBackSystemControlValues = dc.field(metadata={"field": False})


class DeviceValues:
    """
    This is basically a way for storing state (i.e. current values) about all devices. It's the main interface for users
    to access values etc.
    """

    def __init__(self):
        self.mate3s: Dict[None, Mate3DeviceValues] = {}
        self.charge_controllers: Dict[int, ChargeControllerDeviceValues] = {}
        self.fndcs: Dict[int, FNDCDeviceValues] = {}
        self.fx_inverters: Dict[int, FXInverterDeviceValues] = {}
        self.single_phase_radian_inverters: Dict[int, SinglePhaseRadianInverterDeviceValues] = {}
        self.split_phase_radian_inverters: Dict[int, SplitPhaseRadianInverterDeviceValues] = {}
        self.optics: Optional[OPTICSPacketStatisticsValues] = None

    @property
    def connected_devices(self) -> Iterable[ModelValues]:
        # First ones with only a single device:
        for d in ("mate3", "optics"):
            device = getattr(self, d)
            if device:
                yield device

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

    def _get_single_device(self, name: str) -> ModelValues:
        """
        Helper function so that e.g. if there's only one charge controller in self.charge_controllers, you can call
        self.charge_controller to get it.
        """
        devices = getattr(self, f"{name}s")
        if len(devices) != 1:
            raise RuntimeError(
                (
                    f"Must be one, and only one, {name} device to be able to use `{name}` attribute - but there are "
                    f"{len(devices)}"
                )
            )
        return list(devices.values())[0]

    @property
    def mate3(self) -> Mate3DeviceValues:
        """
        Return the mate3.
        """
        return self._get_single_device("mate3")

    @property
    def charge_controller(self) -> ChargeControllerDeviceValues:
        """
        Return the charge controller if there's only one.
        """
        return self._get_single_device("charge_controller")

    @property
    def fndc(self) -> FNDCDeviceValues:
        """
        Return the FNDC if there's only one.
        """
        return self._get_single_device("fndc")

    @property
    def fx_inverter(self) -> FXInverterDeviceValues:
        """
        Return the FX inverter if there's only one.
        """
        return self._get_single_device("fx_inverter")

    @property
    def single_phase_radian_inverter(self) -> SinglePhaseRadianInverterDeviceValues:
        """
        Return the single phase radian inverter if there's only one.
        """
        return self._get_single_device("single_phase_radian_inverter")

    @property
    def split_phase_radian_inverter(self) -> SplitPhaseRadianInverterDeviceValues:
        """
        Return the split phase radian inverter if there's only one.
        """
        return self._get_single_device("split_phase_radian_inverter")

    def update(self, all_model_field_reads: Dict[Model, List[Any]], model_addresses: Dict[Model, List[int]]) -> None:
        """
        This is the key method, and is used to update the state of the devices with new values.
        """

        # Check that all values for each model have a different port:
        for model, model_field_reads in all_model_field_reads.items():
            ports = []
            for field_reads in model_field_reads:
                port_field = field_reads.get("port_number")
                if port_field:
                    ports.append(port_field.value)
            if len(set(ports)) < len(ports):
                raise RuntimeError(f"Multiple devices with the same (including missing) port for model {model}")

        # Update mate:
        self._update_model_and_config(
            all_model_field_reads=all_model_field_reads,
            model_class=OutBackModel,
            config_class=OutBackSystemControlModel,
            config_values_class=OutBackSystemControlValues,
            target=self.mate3s,
            device_class=Mate3DeviceValues,
            device_has_port=False,
            model_addresses=model_addresses,
        )

        # Charge controller
        self._update_model_and_config(
            all_model_field_reads=all_model_field_reads,
            model_class=ChargeControllerModel,
            config_class=ChargeControllerConfigurationModel,
            config_values_class=ChargeControllerConfigurationValues,
            target=self.charge_controllers,
            device_class=ChargeControllerDeviceValues,
            model_addresses=model_addresses,
        )

        # FNDCs
        self._update_model_and_config(
            all_model_field_reads=all_model_field_reads,
            model_class=FLEXnetDCRealTimeModel,
            config_class=FLEXnetDCConfigurationModel,
            config_values_class=FLEXnetDCConfigurationValues,
            target=self.fndcs,
            device_class=FNDCDeviceValues,
            model_addresses=model_addresses,
        )

        # FX inverters
        self._update_model_and_config(
            all_model_field_reads=all_model_field_reads,
            model_class=FXInverterRealTimeModel,
            config_class=FXInverterConfigurationModel,
            config_values_class=FXInverterConfigurationValues,
            target=self.fx_inverters,
            device_class=FXInverterDeviceValues,
            model_addresses=model_addresses,
        )

        # Single phase radian inverters
        self._update_model_and_config(
            all_model_field_reads=all_model_field_reads,
            model_class=SinglePhaseRadianInverterRealTimeModel,
            config_class=RadianInverterConfigurationModel,
            config_values_class=RadianInverterConfigurationValues,
            target=self.single_phase_radian_inverters,
            device_class=SinglePhaseRadianInverterDeviceValues,
            model_addresses=model_addresses,
        )

        # Split phase radian inverters
        self._update_model_and_config(
            all_model_field_reads=all_model_field_reads,
            model_class=SplitPhaseRadianInverterRealTimeModel,
            config_class=RadianInverterConfigurationModel,
            config_values_class=RadianInverterConfigurationValues,
            target=self.split_phase_radian_inverters,
            device_class=SplitPhaseRadianInverterDeviceValues,
            model_addresses=model_addresses,
        )

    def _update_model_and_config(
        self,
        all_model_field_reads: Dict,
        model_class: Model,
        config_class: Model,
        config_values_class: ModelValues,
        target: Dict[int, ModelValues],
        device_class: ModelValues,
        model_addresses: Dict[Model, List[int]],
        device_has_port: bool = True,
    ) -> None:
        """
        Note that all connected devices should always be updated, as every read loop we still read the length and port
        of each device, regardless of what `only` fields were specified in `read`. Note that not all devices will be
        connected, in which case neither will be in the reads.
        """

        model_field_reads = all_model_field_reads.get(model_class)
        config_field_reads = all_model_field_reads.get(config_class)

        # Check we see both model and config or none:
        number_missing = sum([model_field_reads is None, config_field_reads is None])
        if number_missing == 2:
            # Nothing to do - neither is present which means there are no devices.
            return
        elif number_missing == 1:
            raise RuntimeError("Only one of config and values is present, and both should be!")

        if device_has_port:
            # Let's check ports. Keep in mind that we should be getting all devices of this type, across all ports, and
            # not just one, as you can't specify to only read off one port. E.g. if you've got two inverters on separate
            # ports then you'll always get both, not just one. This may change in future.
            def check_ports(all_field_reads):
                ports = {field_reads["port_number"].value for field_reads in all_field_reads}
                if len(ports) > len(set(ports)):
                    raise RuntimeError("Multiple models for the same port!")
                return ports

            model_ports = check_ports(model_field_reads)
            config_ports = check_ports(config_field_reads)

            # The ports should be the same between model and config (since the separation of the model and config are
            # just implementation details of the Outback SunSpec - they're still the same device, so should have the
            # same port).
            if model_ports.symmetric_difference(config_ports):
                raise RuntimeError("Config and models have different ports!")

            ports = model_ports
        else:
            ports = set([None])
            if len(model_field_reads) != 1 or len(config_field_reads) != 1:
                raise RuntimeError("Can't use device_has_port=False unless there's only one model and config.")

        # Create any new devices for the given ports.
        for port in ports:
            if port not in target:
                config_values = self._create_empty_model_values(model=config_class, values_cls=config_values_class)
                target[port] = self._create_empty_model_values(
                    model=model_class, values_cls=device_class, config=config_values
                )

        # If there are any ports that were used for this device, but are no longer, remove them:
        old_device_ports = set(list(target.keys())) - set(ports)
        for port in old_device_ports:
            logger.warning(
                f"Device(s) of model {model_class} on ports {old_device_ports} have disappeared. These will be ignored."
            )
            del target[port]

        # OK, we're done creating/deleting the device containers - now update their values with the field reads:
        def update_values(cls, is_config):
            for field_reads, address in zip(all_model_field_reads[cls], model_addresses[cls]):
                port = field_reads["port_number"].value if "port_number" in field_reads else None
                device = target[port]
                if is_config:
                    device = device.config
                for field_name, read in field_reads.items():
                    getattr(device, field_name)._update_on_read(read)
                # Update addresses:
                if device.address is not None and address != device.address:
                    logger.warning(
                        (
                            f"The address of {model_class} on port={port} has changed from {device.address} to "
                            f"{address}. It will be updated to the new value, but this is could lead to unexpected "
                            "behaviour e.g. if you've switched the ports of two inverters."
                        )
                    )

                device.address = address

        update_values(model_class, False)
        update_values(config_class, True)

    def _create_empty_model_values(self, model: Model, values_cls: ModelValues, config: Optional[Model] = None):
        values = {field.name: FieldValue(field) for field in model.fields()}
        values["model"] = model
        values["address"] = None
        return values_cls(**values) if config is None else values_cls(**values, config=config)
