from dataclasses import dataclass
from typing import Dict, Optional, Any

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


@dataclass
class ChargeControllerDeviceValues(ChargeControllerValues):
    config: ChargeControllerConfigurationValues


@dataclass
class FNDCDeviceValues(FLEXnetDCRealTimeValues):
    config: FLEXnetDCConfigurationValues


@dataclass
class InverterFXDeviceValues(FXInverterRealTimeValues):
    config: FXInverterConfigurationValues


@dataclass
class RadianInverterDeviceValues:
    config: RadianInverterConfigurationValues
    single: SinglePhaseRadianInverterRealTimeValues
    split: SplitPhaseRadianInverterRealTimeValues


@dataclass
class Mate3DeviceValues(OutBackValues):
    config: Optional[OutBackSystemControlValues] = None


@dataclass
class InverterDeviceValues:
    fxs: Dict[int, InverterFXDeviceValues]
    radians: Dict[int, RadianInverterDeviceValues]

    @property
    def fx(self):
        if len(self.fxs) != 1:
            raise RuntimeError("Must be one, and only one, FX inverter device to be able to use `fx` attribute")
        return list(self.fxs.values())[0]

    @property
    def radian(self):
        if len(self.radians) != 1:
            raise RuntimeError("Must be one, and only one, radian inverter device to be able to use `radian` attribute")
        return list(self.radians.values())[0]


@dataclass
class DeviceValues:
    mate3: Optional[Mate3DeviceValues]
    charge_controllers: Dict[int, ChargeControllerDeviceValues]
    fndcs: Dict[int, FNDCDeviceValues]
    inverters: InverterDeviceValues
    optics: Optional[OPTICSPacketStatisticsValues]

    @property
    def connected_devices(self):
        if self.mate3:
            yield self.mate3
        if self.charge_controllers:
            for d in self.charge_controllers.values():
                yield d
                yield d.config
        if self.fndcs:
            for d in self.fndcs.values():
                yield d
                yield d.config
        if self.inverters:
            if self.inverters.fxs:
                for d in self.inverters.fxs.values():
                    yield d
                    yield d.config
            if self.inverters.radians:
                for d in self.inverters.radians.values():
                    yield d
                    yield d.config
        if self.optics:
            yield self.optics

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

    @classmethod
    def create_empty(cls):
        inverters = InverterDeviceValues(fxs={}, radians={})
        return cls(mate3=None, charge_controllers={}, fndcs={}, inverters=inverters, optics=None)

    def _create_empty_model_values(self, model, address, values_cls, config=None):
        values = {}
        for field in model:
            values[field.name] = FieldValue(field.value)
        return (
            values_cls(**values, address=address)
            if config is None
            else values_cls(**values, config=config, address=address)
        )

    def update(self, model_values):
        # group by model:
        address_and_values_per_model = {}
        for address, model, values in model_values:
            address_and_values_per_model.setdefault(model, [])
            address_and_values_per_model[model].append((address, values))

        # check that all values for each model have a different port:
        for model, address_and_values in address_and_values_per_model.items():
            ports = [
                values["port_number"].value if "port_number" in values else None for addr, values in address_and_values
            ]
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
            target=self.inverters.fxs,
            device_class=InverterFXDeviceValues,
        )

        # TODO: radian inverters - gross as not normal config + model pair.

    def _update_mate(self, models):

        config_address, config_values = models[OutBackSystemControlModel][0]
        model_address, model_values = models[OutBackModel][0]
        if self.mate3 is None:
            conf = self._create_empty_model_values(
                OutBackSystemControlModel, config_address, OutBackSystemControlValues
            )
            self.mate3 = self._create_empty_model_values(OutBackModel, model_address, Mate3DeviceValues, conf)

        # update stuff:
        for field_name, read in model_values.items():
            getattr(self.mate3, field_name)._update_on_read(read.value, read.implemented, read.time, read.scale_factor)
        for field_name, read in config_values.items():
            getattr(self.mate3.config, field_name)._update_on_read(
                read.value, read.implemented, read.time, read.scale_factor
            )

    def _update_model_and_config(self, models, model_class, config_class, config_values_class, target, device_class):

        n = sum([config_class in models, model_class in models])
        if n == 0:
            # OK, this device doesn't exist, so nothing to do here
            return
        elif n == 1:
            raise RuntimeError("both the config and model class need to be present!")

        config = models[config_class]
        model = models[model_class]

        # run some checks on ports and stuff:
        config_ports = [d[1]["port_number"].value for d in config]
        model_ports = [d[1]["port_number"].value for d in model]
        if len(config_ports) > len(set(config_ports)):
            raise RuntimeError("Multiple configs for the same port!")
        if len(model_ports) > len(set(model_ports)):
            raise RuntimeError("Multiple models for the same port!")
        if set(config_ports).symmetric_difference(set(model_ports)):
            raise RuntimeError("The ports for model + configuration don't match ...")
        ports = config_ports

        # create any new:
        config_port_addresses = {d[1]["port_number"].value: d[0] for d in config}
        model_port_addresses = {d[1]["port_number"].value: d[0] for d in model}
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
            port = values["port_number"].value
            device = target[port]
            # check address matches:
            if device.address != address:
                raise RuntimeError("TODO")
            for field_name, read in values.items():
                getattr(device, field_name)._update_on_read(read.value, read.implemented, read.time, read.scale_factor)
        for address, values in config:
            port = values["port_number"].value
            device = target[port]
            # check address matches:
            if device.config.address != address:
                raise RuntimeError("TODO")
            for field_name, read in values.items():
                getattr(device.config, field_name)._update_on_read(
                    read.value, read.implemented, read.time, read.scale_factor
                )
