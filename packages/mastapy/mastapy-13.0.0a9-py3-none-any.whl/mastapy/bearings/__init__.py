"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1866 import BearingCatalog
    from ._1867 import BasicDynamicLoadRatingCalculationMethod
    from ._1868 import BasicStaticLoadRatingCalculationMethod
    from ._1869 import BearingCageMaterial
    from ._1870 import BearingDampingMatrixOption
    from ._1871 import BearingLoadCaseResultsForPST
    from ._1872 import BearingLoadCaseResultsLightweight
    from ._1873 import BearingMeasurementType
    from ._1874 import BearingModel
    from ._1875 import BearingRow
    from ._1876 import BearingSettings
    from ._1877 import BearingSettingsDatabase
    from ._1878 import BearingSettingsItem
    from ._1879 import BearingStiffnessMatrixOption
    from ._1880 import ExponentAndReductionFactorsInISO16281Calculation
    from ._1881 import FluidFilmTemperatureOptions
    from ._1882 import HybridSteelAll
    from ._1883 import JournalBearingType
    from ._1884 import JournalOilFeedType
    from ._1885 import MountingPointSurfaceFinishes
    from ._1886 import OuterRingMounting
    from ._1887 import RatingLife
    from ._1888 import RollerBearingProfileTypes
    from ._1889 import RollingBearingArrangement
    from ._1890 import RollingBearingDatabase
    from ._1891 import RollingBearingKey
    from ._1892 import RollingBearingRaceType
    from ._1893 import RollingBearingType
    from ._1894 import RotationalDirections
    from ._1895 import SealLocation
    from ._1896 import SKFSettings
    from ._1897 import TiltingPadTypes
else:
    import_structure = {
        "_1866": ["BearingCatalog"],
        "_1867": ["BasicDynamicLoadRatingCalculationMethod"],
        "_1868": ["BasicStaticLoadRatingCalculationMethod"],
        "_1869": ["BearingCageMaterial"],
        "_1870": ["BearingDampingMatrixOption"],
        "_1871": ["BearingLoadCaseResultsForPST"],
        "_1872": ["BearingLoadCaseResultsLightweight"],
        "_1873": ["BearingMeasurementType"],
        "_1874": ["BearingModel"],
        "_1875": ["BearingRow"],
        "_1876": ["BearingSettings"],
        "_1877": ["BearingSettingsDatabase"],
        "_1878": ["BearingSettingsItem"],
        "_1879": ["BearingStiffnessMatrixOption"],
        "_1880": ["ExponentAndReductionFactorsInISO16281Calculation"],
        "_1881": ["FluidFilmTemperatureOptions"],
        "_1882": ["HybridSteelAll"],
        "_1883": ["JournalBearingType"],
        "_1884": ["JournalOilFeedType"],
        "_1885": ["MountingPointSurfaceFinishes"],
        "_1886": ["OuterRingMounting"],
        "_1887": ["RatingLife"],
        "_1888": ["RollerBearingProfileTypes"],
        "_1889": ["RollingBearingArrangement"],
        "_1890": ["RollingBearingDatabase"],
        "_1891": ["RollingBearingKey"],
        "_1892": ["RollingBearingRaceType"],
        "_1893": ["RollingBearingType"],
        "_1894": ["RotationalDirections"],
        "_1895": ["SealLocation"],
        "_1896": ["SKFSettings"],
        "_1897": ["TiltingPadTypes"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingCatalog",
    "BasicDynamicLoadRatingCalculationMethod",
    "BasicStaticLoadRatingCalculationMethod",
    "BearingCageMaterial",
    "BearingDampingMatrixOption",
    "BearingLoadCaseResultsForPST",
    "BearingLoadCaseResultsLightweight",
    "BearingMeasurementType",
    "BearingModel",
    "BearingRow",
    "BearingSettings",
    "BearingSettingsDatabase",
    "BearingSettingsItem",
    "BearingStiffnessMatrixOption",
    "ExponentAndReductionFactorsInISO16281Calculation",
    "FluidFilmTemperatureOptions",
    "HybridSteelAll",
    "JournalBearingType",
    "JournalOilFeedType",
    "MountingPointSurfaceFinishes",
    "OuterRingMounting",
    "RatingLife",
    "RollerBearingProfileTypes",
    "RollingBearingArrangement",
    "RollingBearingDatabase",
    "RollingBearingKey",
    "RollingBearingRaceType",
    "RollingBearingType",
    "RotationalDirections",
    "SealLocation",
    "SKFSettings",
    "TiltingPadTypes",
)
