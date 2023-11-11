"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2132 import AngularContactBallBearing
    from ._2133 import AngularContactThrustBallBearing
    from ._2134 import AsymmetricSphericalRollerBearing
    from ._2135 import AxialThrustCylindricalRollerBearing
    from ._2136 import AxialThrustNeedleRollerBearing
    from ._2137 import BallBearing
    from ._2138 import BallBearingShoulderDefinition
    from ._2139 import BarrelRollerBearing
    from ._2140 import BearingProtection
    from ._2141 import BearingProtectionDetailsModifier
    from ._2142 import BearingProtectionLevel
    from ._2143 import BearingTypeExtraInformation
    from ._2144 import CageBridgeShape
    from ._2145 import CrossedRollerBearing
    from ._2146 import CylindricalRollerBearing
    from ._2147 import DeepGrooveBallBearing
    from ._2148 import DiameterSeries
    from ._2149 import FatigueLoadLimitCalculationMethodEnum
    from ._2150 import FourPointContactAngleDefinition
    from ._2151 import FourPointContactBallBearing
    from ._2152 import GeometricConstants
    from ._2153 import GeometricConstantsForRollingFrictionalMoments
    from ._2154 import GeometricConstantsForSlidingFrictionalMoments
    from ._2155 import HeightSeries
    from ._2156 import MultiPointContactBallBearing
    from ._2157 import NeedleRollerBearing
    from ._2158 import NonBarrelRollerBearing
    from ._2159 import RollerBearing
    from ._2160 import RollerEndShape
    from ._2161 import RollerRibDetail
    from ._2162 import RollingBearing
    from ._2163 import SelfAligningBallBearing
    from ._2164 import SKFSealFrictionalMomentConstants
    from ._2165 import SleeveType
    from ._2166 import SphericalRollerBearing
    from ._2167 import SphericalRollerThrustBearing
    from ._2168 import TaperRollerBearing
    from ._2169 import ThreePointContactBallBearing
    from ._2170 import ThrustBallBearing
    from ._2171 import ToroidalRollerBearing
    from ._2172 import WidthSeries
else:
    import_structure = {
        "_2132": ["AngularContactBallBearing"],
        "_2133": ["AngularContactThrustBallBearing"],
        "_2134": ["AsymmetricSphericalRollerBearing"],
        "_2135": ["AxialThrustCylindricalRollerBearing"],
        "_2136": ["AxialThrustNeedleRollerBearing"],
        "_2137": ["BallBearing"],
        "_2138": ["BallBearingShoulderDefinition"],
        "_2139": ["BarrelRollerBearing"],
        "_2140": ["BearingProtection"],
        "_2141": ["BearingProtectionDetailsModifier"],
        "_2142": ["BearingProtectionLevel"],
        "_2143": ["BearingTypeExtraInformation"],
        "_2144": ["CageBridgeShape"],
        "_2145": ["CrossedRollerBearing"],
        "_2146": ["CylindricalRollerBearing"],
        "_2147": ["DeepGrooveBallBearing"],
        "_2148": ["DiameterSeries"],
        "_2149": ["FatigueLoadLimitCalculationMethodEnum"],
        "_2150": ["FourPointContactAngleDefinition"],
        "_2151": ["FourPointContactBallBearing"],
        "_2152": ["GeometricConstants"],
        "_2153": ["GeometricConstantsForRollingFrictionalMoments"],
        "_2154": ["GeometricConstantsForSlidingFrictionalMoments"],
        "_2155": ["HeightSeries"],
        "_2156": ["MultiPointContactBallBearing"],
        "_2157": ["NeedleRollerBearing"],
        "_2158": ["NonBarrelRollerBearing"],
        "_2159": ["RollerBearing"],
        "_2160": ["RollerEndShape"],
        "_2161": ["RollerRibDetail"],
        "_2162": ["RollingBearing"],
        "_2163": ["SelfAligningBallBearing"],
        "_2164": ["SKFSealFrictionalMomentConstants"],
        "_2165": ["SleeveType"],
        "_2166": ["SphericalRollerBearing"],
        "_2167": ["SphericalRollerThrustBearing"],
        "_2168": ["TaperRollerBearing"],
        "_2169": ["ThreePointContactBallBearing"],
        "_2170": ["ThrustBallBearing"],
        "_2171": ["ToroidalRollerBearing"],
        "_2172": ["WidthSeries"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AngularContactBallBearing",
    "AngularContactThrustBallBearing",
    "AsymmetricSphericalRollerBearing",
    "AxialThrustCylindricalRollerBearing",
    "AxialThrustNeedleRollerBearing",
    "BallBearing",
    "BallBearingShoulderDefinition",
    "BarrelRollerBearing",
    "BearingProtection",
    "BearingProtectionDetailsModifier",
    "BearingProtectionLevel",
    "BearingTypeExtraInformation",
    "CageBridgeShape",
    "CrossedRollerBearing",
    "CylindricalRollerBearing",
    "DeepGrooveBallBearing",
    "DiameterSeries",
    "FatigueLoadLimitCalculationMethodEnum",
    "FourPointContactAngleDefinition",
    "FourPointContactBallBearing",
    "GeometricConstants",
    "GeometricConstantsForRollingFrictionalMoments",
    "GeometricConstantsForSlidingFrictionalMoments",
    "HeightSeries",
    "MultiPointContactBallBearing",
    "NeedleRollerBearing",
    "NonBarrelRollerBearing",
    "RollerBearing",
    "RollerEndShape",
    "RollerRibDetail",
    "RollingBearing",
    "SelfAligningBallBearing",
    "SKFSealFrictionalMomentConstants",
    "SleeveType",
    "SphericalRollerBearing",
    "SphericalRollerThrustBearing",
    "TaperRollerBearing",
    "ThreePointContactBallBearing",
    "ThrustBallBearing",
    "ToroidalRollerBearing",
    "WidthSeries",
)
