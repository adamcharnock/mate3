import dataclasses as dc
from typing import Dict, Optional

from mate3.sunspec.fields import FieldValue
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

# TODO: tidy up how addresses work ... add an AddressesValues thing? Or add a new field _address to all model values?


@dc.dataclass
class ChargeControllerDeviceValues(ChargeControllerValues):
    config: ChargeControllerConfigurationValues = dc.field(metadata={"field_value": False})


@dc.dataclass
class FNDCDeviceValues(FLEXnetDCRealTimeValues):
    config: FLEXnetDCConfigurationValues = dc.field(metadata={"field_value": False})


@dc.dataclass
class FXInverterDeviceValues(FXInverterRealTimeValues):
    config: FXInverterConfigurationValues = dc.field(metadata={"field_value": False})


@dc.dataclass
class SinglePhaseRadianInverterDeviceValues(SinglePhaseRadianInverterRealTimeValues):
    config: RadianInverterConfigurationValues = dc.field(metadata={"field_value": False})


@dc.dataclass
class SplitPhaseRadianInverterDeviceValues(SplitPhaseRadianInverterRealTimeValues):
    config: RadianInverterConfigurationValues = dc.field(metadata={"field_value": False})


@dc.dataclass
class Mate3DeviceValues(OutBackValues):
    config: OutBackSystemControlValues = dc.field(metadata={"field_value": False})


@dc.dataclass
class DeviceValues:
    mate3: Mate3DeviceValues = dc.field(init=False)
    charge_controllers: Dict[int, ChargeControllerDeviceValues] = dc.field(init=False)
    fndcs: Dict[int, FNDCDeviceValues] = dc.field(init=False)
    fx_inverters: Dict[int, FXInverterDeviceValues] = dc.field(init=False)
    single_phase_radian_inverters: Dict[int, SinglePhaseRadianInverterDeviceValues] = dc.field(init=False)
    split_phase_radian_inverters: Dict[int, SplitPhaseRadianInverterDeviceValues] = dc.field(init=False)
    optics: Optional[OPTICSPacketStatisticsValues] = dc.field(init=False)

    def __post_init__(self):
        self.mate3 = None
        self.charge_controllers = {}
        self.fndcs = {}
        self.fx_inverters = {}
        self.single_phase_radian_inverters = {}
        self.split_phase_radian_inverters = {}
        self.optics = None

    @property
    def connected_devices(self):
        # ones with only a single device:
        for d in ("mate3", "optics"):
            device = getattr(self, d)
            if device:
                yield device
        # ones with multiple (and with config):
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
    def charge_controller(self):
        if len(self.charge_controllers) != 1:
            raise RuntimeError(
                "Must be one, and only one, charge controller device to be able to use `charge_controller` attribute"
            )
        return list(self.charge_controllers.values())[0]

    @property
    def fndc(self):
        if len(self.fndcs) != 1:
            raise RuntimeError("Must be one, and only one, FNDC device to be able to use `fndc` attribute")
        return list(self.fndcs.values())[0]

    @property
    def fx_inverter(self):
        if len(self.fx_inverters) != 1:
            raise RuntimeError(
                "Must be one, and only one, FX inverter device to be able to use `fx_inverter` attribute"
            )
        return list(self.fx_inverters.values())[0]

    @property
    def single_phase_radian_inverter(self):
        if len(self.single_phase_radian_inverters) != 1:
            raise RuntimeError(
                (
                    "Must be one, and only one, single phase radian inverter device to be able to use the"
                    " `single_phase_radian_inverter` attribute"
                )
            )
        return list(self.single_phase_radian_inverters.values())[0]

    @property
    def split_phase_radian_inverter(self):
        if len(self.split_phase_radian_inverters) != 1:
            raise RuntimeError(
                (
                    "Must be one, and only one, split phase radian inverter device to be able to use the"
                    " `split_phase_radian_inverter` attribute"
                )
            )
        return list(self.split_phase_radian_inverters.values())[0]

    def _create_empty_model_values(self, model, address, values_cls, config=None):
        values = {}
        for field in model:
            values[field.name] = FieldValue(field)
        return (
            values_cls(**values, _address=address)
            if config is None
            else values_cls(**values, config=config, _address=address)
        )

    def update(self, model_values):
        # group by model:
        address_and_values_per_model = {}
        for address, model, values in model_values:
            address_and_values_per_model.setdefault(model, [])
            address_and_values_per_model[model].append((address, values))

        # check that all values for each model have a different port:
        for model, address_and_values in address_and_values_per_model.items():
            ports = []
            for addr, values in address_and_values:
                for field, read in values.items():
                    if field.name == "port_number":
                        ports.append(read.value)
            if len(set(ports)) < len(ports):
                raise RuntimeError("Multiple devices with the same (including missing) port!")

        # update mate:
        self._update_mate(address_and_values_per_model)

        # charge controller
        self._update_model_and_config(
            models=address_and_values_per_model,
            model_class=ChargeControllerModel,
            config_class=ChargeControllerConfigurationModel,
            config_values_class=ChargeControllerConfigurationValues,
            target=self.charge_controllers,
            device_class=ChargeControllerDeviceValues,
        )
        # fndcs
        self._update_model_and_config(
            models=address_and_values_per_model,
            model_class=FLEXnetDCRealTimeModel,
            config_class=FLEXnetDCConfigurationModel,
            config_values_class=FLEXnetDCConfigurationValues,
            target=self.fndcs,
            device_class=FNDCDeviceValues,
        )
        # fx inverters
        self._update_model_and_config(
            models=address_and_values_per_model,
            model_class=FXInverterRealTimeModel,
            config_class=FXInverterConfigurationModel,
            config_values_class=FXInverterConfigurationValues,
            target=self.fx_inverters,
            device_class=FXInverterDeviceValues,
        )
        # single phase radian inverters
        self._update_model_and_config(
            models=address_and_values_per_model,
            model_class=SinglePhaseRadianInverterRealTimeModel,
            config_class=RadianInverterConfigurationModel,
            config_values_class=RadianInverterConfigurationValues,
            target=self.single_phase_radian_inverters,
            device_class=SinglePhaseRadianInverterDeviceValues,
        )
        # split phase radian inverters
        self._update_model_and_config(
            models=address_and_values_per_model,
            model_class=SplitPhaseRadianInverterRealTimeModel,
            config_class=RadianInverterConfigurationModel,
            config_values_class=RadianInverterConfigurationValues,
            target=self.split_phase_radian_inverters,
            device_class=SplitPhaseRadianInverterDeviceValues,
        )

    def _update_mate(self, models):

        config_address, config_values = models[OutBackSystemControlModel][0]
        model_address, model_values = models[OutBackModel][0]
        if self.mate3 is None:
            conf = self._create_empty_model_values(
                OutBackSystemControlModel, config_address, OutBackSystemControlValues
            )
            self.mate3 = self._create_empty_model_values(OutBackModel, model_address, Mate3DeviceValues, conf)

        # update stuff:
        for field, read in model_values.items():
            getattr(self.mate3, field.name)._update_on_read(read.value, read.implemented, read.time, read.scale_factor)
        for field, read in config_values.items():
            getattr(self.mate3.config, field.name)._update_on_read(
                read.value, read.implemented, read.time, read.scale_factor
            )

    def _update_model_and_config(self, models, model_class, config_class, config_values_class, target, device_class):

        if not models:
            pass

        n = sum([config_class in models, model_class in models])
        if n == 0:
            # OK, this device doesn't exist, so nothing to do here
            return
        elif n == 1:
            raise RuntimeError("both the config and model class need to be present!")

        config = models[config_class]
        model = models[model_class]

        # run some checks on ports and stuff:
        config_port_values = [
            (address, [read.value for field, read in reads.items() if field.name == "port_number"][0])
            for address, reads in config
        ]
        model_port_values = [
            (address, [read.value for field, read in reads.items() if field.name == "port_number"][0])
            for address, reads in model
        ]
        config_ports = [port for address, port in config_port_values]
        model_ports = [port for address, port in model_port_values]
        if len(config_ports) > len(set(config_ports)):
            raise RuntimeError("Multiple configs for the same port!")
        if len(model_ports) > len(set(model_ports)):
            raise RuntimeError("Multiple models for the same port!")
        if set(config_ports).symmetric_difference(set(model_ports)):
            raise RuntimeError("The ports for model + configuration don't match ...")
        ports = config_ports

        # create any new:
        config_port_addresses = {port: address for address, port in config_port_values}
        model_port_addresses = {port: address for address, port in model_port_values}
        for port in ports:
            if port not in target:
                config_values = self._create_empty_model_values(
                    config_class, config_port_addresses[port], config_values_class
                )
                target[port] = self._create_empty_model_values(
                    model_class, model_port_addresses[port], device_class, config_values
                )

        # remove any old:
        # TODO: this means if they don't do a read, the CC will get dropped
        # TODO: maybe fail here to explicitly prevent users accessing a device after this point which is gone?
        # using this code after losing connection to a device
        old = set(list(target.keys())) - set(ports)
        for port in old:
            # TODO: warning
            del target[port]

        # update stuff:
        for address, values in model:
            port = [v for k, v in values.items() if k.name == "port_number"][0].value
            device = target[port]
            # check address matches:
            if device._address != address:
                raise RuntimeError("TODO")
            for field, read in values.items():
                getattr(device, field.name)._update_on_read(read.value, read.implemented, read.time, read.scale_factor)
        for address, values in config:
            port = [v for k, v in values.items() if k.name == "port_number"][0].value
            device = target[port]
            # check address matches:
            if device.config._address != address:
                raise RuntimeError("TODO")
            for field, read in values.items():
                getattr(device.config, field.name)._update_on_read(
                    read.value, read.implemented, read.time, read.scale_factor
                )
