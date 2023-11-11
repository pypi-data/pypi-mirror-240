"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2073 import AdjustedSpeed
    from ._2074 import AdjustmentFactors
    from ._2075 import BearingLoads
    from ._2076 import BearingRatingLife
    from ._2077 import DynamicAxialLoadCarryingCapacity
    from ._2078 import Frequencies
    from ._2079 import FrequencyOfOverRolling
    from ._2080 import Friction
    from ._2081 import FrictionalMoment
    from ._2082 import FrictionSources
    from ._2083 import Grease
    from ._2084 import GreaseLifeAndRelubricationInterval
    from ._2085 import GreaseQuantity
    from ._2086 import InitialFill
    from ._2087 import LifeModel
    from ._2088 import MinimumLoad
    from ._2089 import OperatingViscosity
    from ._2090 import PermissibleAxialLoad
    from ._2091 import RotationalFrequency
    from ._2092 import SKFAuthentication
    from ._2093 import SKFCalculationResult
    from ._2094 import SKFCredentials
    from ._2095 import SKFModuleResults
    from ._2096 import StaticSafetyFactors
    from ._2097 import Viscosities
else:
    import_structure = {
        "_2073": ["AdjustedSpeed"],
        "_2074": ["AdjustmentFactors"],
        "_2075": ["BearingLoads"],
        "_2076": ["BearingRatingLife"],
        "_2077": ["DynamicAxialLoadCarryingCapacity"],
        "_2078": ["Frequencies"],
        "_2079": ["FrequencyOfOverRolling"],
        "_2080": ["Friction"],
        "_2081": ["FrictionalMoment"],
        "_2082": ["FrictionSources"],
        "_2083": ["Grease"],
        "_2084": ["GreaseLifeAndRelubricationInterval"],
        "_2085": ["GreaseQuantity"],
        "_2086": ["InitialFill"],
        "_2087": ["LifeModel"],
        "_2088": ["MinimumLoad"],
        "_2089": ["OperatingViscosity"],
        "_2090": ["PermissibleAxialLoad"],
        "_2091": ["RotationalFrequency"],
        "_2092": ["SKFAuthentication"],
        "_2093": ["SKFCalculationResult"],
        "_2094": ["SKFCredentials"],
        "_2095": ["SKFModuleResults"],
        "_2096": ["StaticSafetyFactors"],
        "_2097": ["Viscosities"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdjustedSpeed",
    "AdjustmentFactors",
    "BearingLoads",
    "BearingRatingLife",
    "DynamicAxialLoadCarryingCapacity",
    "Frequencies",
    "FrequencyOfOverRolling",
    "Friction",
    "FrictionalMoment",
    "FrictionSources",
    "Grease",
    "GreaseLifeAndRelubricationInterval",
    "GreaseQuantity",
    "InitialFill",
    "LifeModel",
    "MinimumLoad",
    "OperatingViscosity",
    "PermissibleAxialLoad",
    "RotationalFrequency",
    "SKFAuthentication",
    "SKFCalculationResult",
    "SKFCredentials",
    "SKFModuleResults",
    "StaticSafetyFactors",
    "Viscosities",
)
