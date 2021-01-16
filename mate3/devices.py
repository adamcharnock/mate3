from copy import deepcopy
from typing import Optional

from mate3.sunspec.models import (
    MODEL_DEVICE_IDS,
    ChargeControllerConfigurationModel,
    ChargeControllerModel,
    FLEXnetDCConfigurationModel,
    FLEXnetDCRealTimeModel,
    FXInverterConfigurationModel,
    FXInverterRealTimeModel,
    OPTICSPacketStatisticsModel,
    OutBackModel,
    OutBackSystemControlModel,
    RadianInverterConfigurationModel,
    SinglePhaseRadianInverterRealTimeModel,
    SplitPhaseRadianInverterRealTimeModel,
)


class Mate3Device(OutBackModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config: Optional[OutBackSystemControlModel] = None


class ChargeControllerDevice(ChargeControllerModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config: Optional[ChargeControllerConfigurationModel] = None


class FNDCDevice(FLEXnetDCRealTimeModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config: Optional[FLEXnetDCConfigurationModel] = None


class FXInverterDevice(FXInverterRealTimeModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config: Optional[FXInverterConfigurationModel] = None


class SinglePhaseRadianInverterDevice(SinglePhaseRadianInverterRealTimeModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config: Optional[RadianInverterConfigurationModel] = None


class SplitPhaseRadianInverterDevice(SplitPhaseRadianInverterRealTimeModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config: Optional[RadianInverterConfigurationModel] = None


class OPTICSDevice(OPTICSPacketStatisticsModel):
    """
    No config ...
    """

    pass


DEVICE_IDS = deepcopy(MODEL_DEVICE_IDS)
reverse_models_device_ids = {v: k for k, v in MODEL_DEVICE_IDS.items()}
for (model, device) in (
    (OutBackModel, Mate3Device),
    (ChargeControllerModel, ChargeControllerDevice),
    (FLEXnetDCRealTimeModel, FNDCDevice),
    (FXInverterRealTimeModel, FXInverterDevice),
    (SinglePhaseRadianInverterRealTimeModel, SinglePhaseRadianInverterDevice),
    (SplitPhaseRadianInverterRealTimeModel, SplitPhaseRadianInverterDevice),
    (OPTICSPacketStatisticsModel, OPTICSDevice),
):
    did = reverse_models_device_ids[model]
    DEVICE_IDS[did] = device
