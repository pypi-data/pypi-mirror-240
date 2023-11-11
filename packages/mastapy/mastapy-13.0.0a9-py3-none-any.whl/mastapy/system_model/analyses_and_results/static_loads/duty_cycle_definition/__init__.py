"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6985 import AdditionalForcesObtainedFrom
    from ._6986 import BoostPressureLoadCaseInputOptions
    from ._6987 import DesignStateOptions
    from ._6988 import DestinationDesignState
    from ._6989 import ForceInputOptions
    from ._6990 import GearRatioInputOptions
    from ._6991 import LoadCaseNameOptions
    from ._6992 import MomentInputOptions
    from ._6993 import MultiTimeSeriesDataInputFileOptions
    from ._6994 import PointLoadInputOptions
    from ._6995 import PowerLoadInputOptions
    from ._6996 import RampOrSteadyStateInputOptions
    from ._6997 import SpeedInputOptions
    from ._6998 import TimeSeriesImporter
    from ._6999 import TimeStepInputOptions
    from ._7000 import TorqueInputOptions
    from ._7001 import TorqueValuesObtainedFrom
else:
    import_structure = {
        "_6985": ["AdditionalForcesObtainedFrom"],
        "_6986": ["BoostPressureLoadCaseInputOptions"],
        "_6987": ["DesignStateOptions"],
        "_6988": ["DestinationDesignState"],
        "_6989": ["ForceInputOptions"],
        "_6990": ["GearRatioInputOptions"],
        "_6991": ["LoadCaseNameOptions"],
        "_6992": ["MomentInputOptions"],
        "_6993": ["MultiTimeSeriesDataInputFileOptions"],
        "_6994": ["PointLoadInputOptions"],
        "_6995": ["PowerLoadInputOptions"],
        "_6996": ["RampOrSteadyStateInputOptions"],
        "_6997": ["SpeedInputOptions"],
        "_6998": ["TimeSeriesImporter"],
        "_6999": ["TimeStepInputOptions"],
        "_7000": ["TorqueInputOptions"],
        "_7001": ["TorqueValuesObtainedFrom"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdditionalForcesObtainedFrom",
    "BoostPressureLoadCaseInputOptions",
    "DesignStateOptions",
    "DestinationDesignState",
    "ForceInputOptions",
    "GearRatioInputOptions",
    "LoadCaseNameOptions",
    "MomentInputOptions",
    "MultiTimeSeriesDataInputFileOptions",
    "PointLoadInputOptions",
    "PowerLoadInputOptions",
    "RampOrSteadyStateInputOptions",
    "SpeedInputOptions",
    "TimeSeriesImporter",
    "TimeStepInputOptions",
    "TorqueInputOptions",
    "TorqueValuesObtainedFrom",
)
