"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1385 import CustomSplineHalfDesign
    from ._1386 import CustomSplineJointDesign
    from ._1387 import DetailedSplineJointSettings
    from ._1388 import DIN5480SplineHalfDesign
    from ._1389 import DIN5480SplineJointDesign
    from ._1390 import DudleyEffectiveLengthApproximationOption
    from ._1391 import FitTypes
    from ._1392 import GBT3478SplineHalfDesign
    from ._1393 import GBT3478SplineJointDesign
    from ._1394 import HeatTreatmentTypes
    from ._1395 import ISO4156SplineHalfDesign
    from ._1396 import ISO4156SplineJointDesign
    from ._1397 import JISB1603SplineJointDesign
    from ._1398 import ManufacturingTypes
    from ._1399 import Modules
    from ._1400 import PressureAngleTypes
    from ._1401 import RootTypes
    from ._1402 import SAEFatigueLifeFactorTypes
    from ._1403 import SAESplineHalfDesign
    from ._1404 import SAESplineJointDesign
    from ._1405 import SAETorqueCycles
    from ._1406 import SplineDesignTypes
    from ._1407 import FinishingMethods
    from ._1408 import SplineFitClassType
    from ._1409 import SplineFixtureTypes
    from ._1410 import SplineHalfDesign
    from ._1411 import SplineJointDesign
    from ._1412 import SplineMaterial
    from ._1413 import SplineRatingTypes
    from ._1414 import SplineToleranceClassTypes
    from ._1415 import StandardSplineHalfDesign
    from ._1416 import StandardSplineJointDesign
else:
    import_structure = {
        "_1385": ["CustomSplineHalfDesign"],
        "_1386": ["CustomSplineJointDesign"],
        "_1387": ["DetailedSplineJointSettings"],
        "_1388": ["DIN5480SplineHalfDesign"],
        "_1389": ["DIN5480SplineJointDesign"],
        "_1390": ["DudleyEffectiveLengthApproximationOption"],
        "_1391": ["FitTypes"],
        "_1392": ["GBT3478SplineHalfDesign"],
        "_1393": ["GBT3478SplineJointDesign"],
        "_1394": ["HeatTreatmentTypes"],
        "_1395": ["ISO4156SplineHalfDesign"],
        "_1396": ["ISO4156SplineJointDesign"],
        "_1397": ["JISB1603SplineJointDesign"],
        "_1398": ["ManufacturingTypes"],
        "_1399": ["Modules"],
        "_1400": ["PressureAngleTypes"],
        "_1401": ["RootTypes"],
        "_1402": ["SAEFatigueLifeFactorTypes"],
        "_1403": ["SAESplineHalfDesign"],
        "_1404": ["SAESplineJointDesign"],
        "_1405": ["SAETorqueCycles"],
        "_1406": ["SplineDesignTypes"],
        "_1407": ["FinishingMethods"],
        "_1408": ["SplineFitClassType"],
        "_1409": ["SplineFixtureTypes"],
        "_1410": ["SplineHalfDesign"],
        "_1411": ["SplineJointDesign"],
        "_1412": ["SplineMaterial"],
        "_1413": ["SplineRatingTypes"],
        "_1414": ["SplineToleranceClassTypes"],
        "_1415": ["StandardSplineHalfDesign"],
        "_1416": ["StandardSplineJointDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CustomSplineHalfDesign",
    "CustomSplineJointDesign",
    "DetailedSplineJointSettings",
    "DIN5480SplineHalfDesign",
    "DIN5480SplineJointDesign",
    "DudleyEffectiveLengthApproximationOption",
    "FitTypes",
    "GBT3478SplineHalfDesign",
    "GBT3478SplineJointDesign",
    "HeatTreatmentTypes",
    "ISO4156SplineHalfDesign",
    "ISO4156SplineJointDesign",
    "JISB1603SplineJointDesign",
    "ManufacturingTypes",
    "Modules",
    "PressureAngleTypes",
    "RootTypes",
    "SAEFatigueLifeFactorTypes",
    "SAESplineHalfDesign",
    "SAESplineJointDesign",
    "SAETorqueCycles",
    "SplineDesignTypes",
    "FinishingMethods",
    "SplineFitClassType",
    "SplineFixtureTypes",
    "SplineHalfDesign",
    "SplineJointDesign",
    "SplineMaterial",
    "SplineRatingTypes",
    "SplineToleranceClassTypes",
    "StandardSplineHalfDesign",
    "StandardSplineJointDesign",
)
