import dataclasses as dc
from typing import Any, Dict, Iterable, List, Optional

from loguru import logger

from mate3.field_values import FieldValue, ModelValues
from mate3.read import AllModelReads
from mate3.sunspec.fields import IntegerField
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

    def __init__(self, client):
        self._client = client
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

    def update(self, all_reads: AllModelReads) -> None:
        """
        This is the key method, and is used to update the state of the devices with new values.
        """

        # Update mate:
        self._update_model_and_config(
            all_reads=all_reads,
            model_class=OutBackModel,
            config_class=OutBackSystemControlModel,
            config_values_class=OutBackSystemControlValues,
            target=self.mate3s,
            device_class=Mate3DeviceValues,
        )

        # Charge controller
        self._update_model_and_config(
            all_reads=all_reads,
            model_class=ChargeControllerModel,
            config_class=ChargeControllerConfigurationModel,
            config_values_class=ChargeControllerConfigurationValues,
            target=self.charge_controllers,
            device_class=ChargeControllerDeviceValues,
        )

        # FNDCs
        self._update_model_and_config(
            all_reads=all_reads,
            model_class=FLEXnetDCRealTimeModel,
            config_class=FLEXnetDCConfigurationModel,
            config_values_class=FLEXnetDCConfigurationValues,
            target=self.fndcs,
            device_class=FNDCDeviceValues,
        )

        # FX inverters
        self._update_model_and_config(
            all_reads=all_reads,
            model_class=FXInverterRealTimeModel,
            config_class=FXInverterConfigurationModel,
            config_values_class=FXInverterConfigurationValues,
            target=self.fx_inverters,
            device_class=FXInverterDeviceValues,
        )

        # Single phase radian inverters
        self._update_model_and_config(
            all_reads=all_reads,
            model_class=SinglePhaseRadianInverterRealTimeModel,
            config_class=RadianInverterConfigurationModel,
            config_values_class=RadianInverterConfigurationValues,
            target=self.single_phase_radian_inverters,
            device_class=SinglePhaseRadianInverterDeviceValues,
        )

        # Split phase radian inverters
        self._update_model_and_config(
            all_reads=all_reads,
            model_class=SplitPhaseRadianInverterRealTimeModel,
            config_class=RadianInverterConfigurationModel,
            config_values_class=RadianInverterConfigurationValues,
            target=self.split_phase_radian_inverters,
            device_class=SplitPhaseRadianInverterDeviceValues,
        )

    def _update_model_and_config(
        self,
        all_reads: AllModelReads,
        model_class: Model,
        config_class: Model,
        config_values_class: ModelValues,
        target: Dict[int, ModelValues],
        device_class: ModelValues,
    ) -> None:

        model_field_reads_per_port = all_reads.get_reads_per_model_by_port(model_class)
        config_field_reads_per_port = all_reads.get_reads_per_model_by_port(config_class)

        # OK, there's a few options around whether the above variables contain anything.
        # - Both present, then we're good - continue. All devices should have a configuration class.
        # - Model isn't present - this means the device itself wasn't detected, so ignore. Note that usually this would
        #   imply the config class is null (since the config shouldn't be there if the device isn't) except in the case
        #   of Radian inverters, as the same config class is shared across both single and split phase devices (so that
        #   if only one type is present, the other will have empty model values and non-empty config).
        # - Both are missing - this is covered by the above.
        # So, the short summary is we only care about devices where the model field values are present, and in all other
        # cases there *should* be config field values too.
        if model_field_reads_per_port is None:
            return
        else:
            if config_field_reads_per_port is None:
                logger.warning(
                    (
                        f"Only model ({model_class}) field values and no config ({config_class}) fields were read. This"
                        f" is undefined behaviour, so ignoring {model_class}."
                    )
                )
                return

        # Check model and config have the same ports:
        if set(model_field_reads_per_port).symmetric_difference(set(config_field_reads_per_port)):
            raise RuntimeError("Config and models have different ports!")

        # Create/update any devices for the given ports:
        for port in model_field_reads_per_port:
            model_reads_this_port = model_field_reads_per_port[port]
            config_reads_this_port = config_field_reads_per_port[port]
            if port not in target:
                # OK, it's new - create it:
                config_values = self._create_new_model_values(
                    model=config_class,
                    values_class=config_values_class,
                    device_address=config_reads_this_port["did"].address,
                )
                target[port] = self._create_new_model_values(
                    model=model_class,
                    values_class=device_class,
                    device_address=model_reads_this_port["did"].address,
                    config=config_values,
                )
            # Either way, update the field values:
            for field_name, field_read in model_reads_this_port.items():
                field_value = getattr(target[port], field_name)
                field_value._raw_value = field_read.raw_value
                field_value._implemented = field_read.implemented
                field_value._last_read = field_read.time
            for field_name, field_read in config_reads_this_port.items():
                field_value = getattr(target[port].config, field_name)
                field_value._raw_value = field_read.raw_value
                field_value._implemented = field_read.implemented
                field_value._last_read = field_read.time

        # If there are any ports that were used for this device, but are no longer, remove them:
        old_device_ports = set(list(target.keys())) - set(model_field_reads_per_port.keys())
        for port in old_device_ports:
            logger.warning(
                f"Device(s) of model {model_class} on ports {old_device_ports} have disappeared. These will be ignored."
            )
            del target[port]

    def _create_new_model_values(
        self, model: Model, values_class: ModelValues, device_address: int, config: Optional[ModelValues] = None
    ):

        # Create empty FieldValues
        field_values = {}
        scale_factors = {}
        for field in model.fields():
            address = device_address + field.start - 1
            field_values[field.name] = FieldValue(
                client=self._client,
                field=field,
                address=address,
                scale_factor=None,
                raw_value=None,
                implemented=True,
                read_time=None,
            )
            if isinstance(field, IntegerField) and field.scale_factor is not None:
                scale_factors[field.name] = field.scale_factor.name

        # Now assign scale factors:
        for field, scale_factor in scale_factors.items():
            field_values[field]._scale_factor = field_values[scale_factor]

        kwargs = {"model": model, "address": device_address, **field_values}
        return values_class(**kwargs) if config is None else values_class(config=config, **kwargs)
