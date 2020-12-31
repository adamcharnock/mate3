import dataclasses as dc
from typing import Any, Dict, Iterable, List, Optional

from loguru import logger

from mate3.field_values import FieldValue, ModelValues
from mate3.sunspec.fields import IntegerField, Mode
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

    def update(
        self, all_model_field_values: Dict[Model, List[FieldValue]], model_addresses: Dict[Model, List[int]]
    ) -> None:
        """
        This is the key method, and is used to update the state of the devices with new values.
        """

        # Check that all values for each model have a different port:
        for model, model_field_values in all_model_field_values.items():
            ports = []
            for field_reads in model_field_values:
                port_field = field_reads.get("port_number")
                if port_field:
                    ports.append(port_field.value)
            if len(set(ports)) < len(ports):
                raise RuntimeError(f"Multiple devices with the same (including missing) port for model {model}")

        # Update mate:
        self._update_model_and_config(
            all_model_field_values=all_model_field_values,
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
            all_model_field_values=all_model_field_values,
            model_class=ChargeControllerModel,
            config_class=ChargeControllerConfigurationModel,
            config_values_class=ChargeControllerConfigurationValues,
            target=self.charge_controllers,
            device_class=ChargeControllerDeviceValues,
            model_addresses=model_addresses,
        )

        # FNDCs
        self._update_model_and_config(
            all_model_field_values=all_model_field_values,
            model_class=FLEXnetDCRealTimeModel,
            config_class=FLEXnetDCConfigurationModel,
            config_values_class=FLEXnetDCConfigurationValues,
            target=self.fndcs,
            device_class=FNDCDeviceValues,
            model_addresses=model_addresses,
        )

        # FX inverters
        self._update_model_and_config(
            all_model_field_values=all_model_field_values,
            model_class=FXInverterRealTimeModel,
            config_class=FXInverterConfigurationModel,
            config_values_class=FXInverterConfigurationValues,
            target=self.fx_inverters,
            device_class=FXInverterDeviceValues,
            model_addresses=model_addresses,
        )

        # Single phase radian inverters
        self._update_model_and_config(
            all_model_field_values=all_model_field_values,
            model_class=SinglePhaseRadianInverterRealTimeModel,
            config_class=RadianInverterConfigurationModel,
            config_values_class=RadianInverterConfigurationValues,
            target=self.single_phase_radian_inverters,
            device_class=SinglePhaseRadianInverterDeviceValues,
            model_addresses=model_addresses,
        )

        # Split phase radian inverters
        self._update_model_and_config(
            all_model_field_values=all_model_field_values,
            model_class=SplitPhaseRadianInverterRealTimeModel,
            config_class=RadianInverterConfigurationModel,
            config_values_class=RadianInverterConfigurationValues,
            target=self.split_phase_radian_inverters,
            device_class=SplitPhaseRadianInverterDeviceValues,
            model_addresses=model_addresses,
        )

    def _update_model_and_config(
        self,
        all_model_field_values: Dict[str, FieldValue],
        model_class: Model,
        config_class: Model,
        config_values_class: ModelValues,
        target: Dict[int, ModelValues],
        device_class: ModelValues,
        model_addresses: Dict[Model, List[int]],
        device_has_port: bool = True,
    ) -> None:

        model_field_values = all_model_field_values.get(model_class)
        config_field_values = all_model_field_values.get(config_class)

        # OK, there's a few options around whether the above variables contain anything.
        # - Both present, then we're good - continue. All devices should have a configuration class.
        # - Model isn't present - this means the device itself wasn't detected, so ignore. Note that usually this would
        #   imply the config class is null (since the config shouldn't be there if the device isn't) except in the case
        #   of Radian inverters, as the same config class is shared across both single and split phase devices (so that
        #   if only one type is present, the other will have empty model values and non-empty config).
        # - Both are missing - this is covered by the above.
        # So, the short summary is we only care about devices where the model field values are present, and in all other
        # cases there *should* be config field values too.
        if model_field_values is None:
            return
        else:
            if config_field_values is None:
                logger.warning(
                    (
                        f"Only model ({model_class}) field values and no config ({config_class}) fields were read. This"
                        f" is undefined behaviour, so ignoring {model_class}."
                    )
                )
                return

        if device_has_port:
            # Let's check ports. Keep in mind that we should be getting all devices of this type, across all ports, and
            # not just one, as you can't specify to only read off one port. E.g. if you've got two inverters on separate
            # ports then you'll always get both, not just one. This may change in future.
            def check_ports(all_field_values):
                ports = [fv["port_number"].value for fv in all_field_values]
                if len(ports) > len(set(ports)):
                    raise RuntimeError("Multiple models for the same port!")
                return set(ports)

            model_ports = check_ports(model_field_values)
            config_ports = check_ports(config_field_values)

            # The ports should be the same between model and config (since the separation of the model and config are
            # just implementation details of the Outback SunSpec - they're still the same device, so should have the
            # same port).
            if set(model_ports).symmetric_difference(set(config_ports)):
                raise RuntimeError("Config and models have different ports!")
            ports = model_ports

            # OK, now get field values per port:
            model_values_per_port = {fv["port_number"].value: fv for fv in model_field_values}
            config_values_per_port = {fv["port_number"].value: fv for fv in config_field_values}

        else:
            ports = set([None])
            if len(model_field_values) != 1 or len(config_field_values) != 1:
                raise RuntimeError("Can't use device_has_port=False unless there's only one model and config.")

            # OK, now get field values per 'port' - just get the first item from the list (as we know it's only one)
            model_values_per_port = {None: model_field_values[0]}
            config_values_per_port = {None: config_field_values[0]}

        # Create/update any devices for the given ports:
        for port in ports:
            model_values_this_port = model_values_per_port[port]
            config_values_this_port = config_values_per_port[port]
            if port in target:
                # Cool, just update the field values:
                for field_name, field_value in model_values_this_port.items():
                    target[port][field_name] = field_value
                for field_name, field_value in config_values_this_port.items():
                    target[port]["config"][field_name] = field_value
            else:
                # OK, it's new - create it:
                config_values = self._create_new_model_values(
                    model=config_class, readable_fields=config_values_this_port, values_class=config_values_class
                )
                target[port] = self._create_new_model_values(
                    model=model_class,
                    readable_fields=model_values_this_port,
                    values_class=device_class,
                    config=config_values,
                )

        # If there are any ports that were used for this device, but are no longer, remove them:
        old_device_ports = set(list(target.keys())) - set(ports)
        for port in old_device_ports:
            logger.warning(
                f"Device(s) of model {model_class} on ports {old_device_ports} have disappeared. These will be ignored."
            )
            del target[port]

    def _create_new_model_values(
        self,
        model: Model,
        readable_fields: Dict[str, FieldValue],
        values_class: ModelValues,
        config: Optional[ModelValues] = None,
    ):
        unreadable_field_values = {}
        for field in model.fields():
            if field.mode not in (Mode.R, Mode.RW):
                # To get the address, do something gross ...
                address = readable_fields["did"].address + field.start - 1
                # Get scale factor:
                scale_factor = None
                if isinstance(field, IntegerField) and field.scale_factor is not None:
                    scale_factor = readable_fields[field.scale_factor.name]
                unreadable_field_values[field.name] = FieldValue(
                    client=self,
                    field=field,
                    address=address,
                    scale_factor=scale_factor,
                    raw_value=None,
                    implemented=True,
                )
        kwargs = {**readable_fields, **unreadable_field_values}
        kwargs["model"] = model
        kwargs["address"] = readable_fields["did"].address
        return values_class(**kwargs) if config is None else values_class(**kwargs, config=config)
