"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2507 import ActiveCylindricalGearSetDesignSelection
    from ._2508 import ActiveGearSetDesignSelection
    from ._2509 import ActiveGearSetDesignSelectionGroup
    from ._2510 import AGMAGleasonConicalGear
    from ._2511 import AGMAGleasonConicalGearSet
    from ._2512 import BevelDifferentialGear
    from ._2513 import BevelDifferentialGearSet
    from ._2514 import BevelDifferentialPlanetGear
    from ._2515 import BevelDifferentialSunGear
    from ._2516 import BevelGear
    from ._2517 import BevelGearSet
    from ._2518 import ConceptGear
    from ._2519 import ConceptGearSet
    from ._2520 import ConicalGear
    from ._2521 import ConicalGearSet
    from ._2522 import CylindricalGear
    from ._2523 import CylindricalGearSet
    from ._2524 import CylindricalPlanetGear
    from ._2525 import FaceGear
    from ._2526 import FaceGearSet
    from ._2527 import Gear
    from ._2528 import GearOrientations
    from ._2529 import GearSet
    from ._2530 import GearSetConfiguration
    from ._2531 import HypoidGear
    from ._2532 import HypoidGearSet
    from ._2533 import KlingelnbergCycloPalloidConicalGear
    from ._2534 import KlingelnbergCycloPalloidConicalGearSet
    from ._2535 import KlingelnbergCycloPalloidHypoidGear
    from ._2536 import KlingelnbergCycloPalloidHypoidGearSet
    from ._2537 import KlingelnbergCycloPalloidSpiralBevelGear
    from ._2538 import KlingelnbergCycloPalloidSpiralBevelGearSet
    from ._2539 import PlanetaryGearSet
    from ._2540 import SpiralBevelGear
    from ._2541 import SpiralBevelGearSet
    from ._2542 import StraightBevelDiffGear
    from ._2543 import StraightBevelDiffGearSet
    from ._2544 import StraightBevelGear
    from ._2545 import StraightBevelGearSet
    from ._2546 import StraightBevelPlanetGear
    from ._2547 import StraightBevelSunGear
    from ._2548 import WormGear
    from ._2549 import WormGearSet
    from ._2550 import ZerolBevelGear
    from ._2551 import ZerolBevelGearSet
else:
    import_structure = {
        "_2507": ["ActiveCylindricalGearSetDesignSelection"],
        "_2508": ["ActiveGearSetDesignSelection"],
        "_2509": ["ActiveGearSetDesignSelectionGroup"],
        "_2510": ["AGMAGleasonConicalGear"],
        "_2511": ["AGMAGleasonConicalGearSet"],
        "_2512": ["BevelDifferentialGear"],
        "_2513": ["BevelDifferentialGearSet"],
        "_2514": ["BevelDifferentialPlanetGear"],
        "_2515": ["BevelDifferentialSunGear"],
        "_2516": ["BevelGear"],
        "_2517": ["BevelGearSet"],
        "_2518": ["ConceptGear"],
        "_2519": ["ConceptGearSet"],
        "_2520": ["ConicalGear"],
        "_2521": ["ConicalGearSet"],
        "_2522": ["CylindricalGear"],
        "_2523": ["CylindricalGearSet"],
        "_2524": ["CylindricalPlanetGear"],
        "_2525": ["FaceGear"],
        "_2526": ["FaceGearSet"],
        "_2527": ["Gear"],
        "_2528": ["GearOrientations"],
        "_2529": ["GearSet"],
        "_2530": ["GearSetConfiguration"],
        "_2531": ["HypoidGear"],
        "_2532": ["HypoidGearSet"],
        "_2533": ["KlingelnbergCycloPalloidConicalGear"],
        "_2534": ["KlingelnbergCycloPalloidConicalGearSet"],
        "_2535": ["KlingelnbergCycloPalloidHypoidGear"],
        "_2536": ["KlingelnbergCycloPalloidHypoidGearSet"],
        "_2537": ["KlingelnbergCycloPalloidSpiralBevelGear"],
        "_2538": ["KlingelnbergCycloPalloidSpiralBevelGearSet"],
        "_2539": ["PlanetaryGearSet"],
        "_2540": ["SpiralBevelGear"],
        "_2541": ["SpiralBevelGearSet"],
        "_2542": ["StraightBevelDiffGear"],
        "_2543": ["StraightBevelDiffGearSet"],
        "_2544": ["StraightBevelGear"],
        "_2545": ["StraightBevelGearSet"],
        "_2546": ["StraightBevelPlanetGear"],
        "_2547": ["StraightBevelSunGear"],
        "_2548": ["WormGear"],
        "_2549": ["WormGearSet"],
        "_2550": ["ZerolBevelGear"],
        "_2551": ["ZerolBevelGearSet"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveCylindricalGearSetDesignSelection",
    "ActiveGearSetDesignSelection",
    "ActiveGearSetDesignSelectionGroup",
    "AGMAGleasonConicalGear",
    "AGMAGleasonConicalGearSet",
    "BevelDifferentialGear",
    "BevelDifferentialGearSet",
    "BevelDifferentialPlanetGear",
    "BevelDifferentialSunGear",
    "BevelGear",
    "BevelGearSet",
    "ConceptGear",
    "ConceptGearSet",
    "ConicalGear",
    "ConicalGearSet",
    "CylindricalGear",
    "CylindricalGearSet",
    "CylindricalPlanetGear",
    "FaceGear",
    "FaceGearSet",
    "Gear",
    "GearOrientations",
    "GearSet",
    "GearSetConfiguration",
    "HypoidGear",
    "HypoidGearSet",
    "KlingelnbergCycloPalloidConicalGear",
    "KlingelnbergCycloPalloidConicalGearSet",
    "KlingelnbergCycloPalloidHypoidGear",
    "KlingelnbergCycloPalloidHypoidGearSet",
    "KlingelnbergCycloPalloidSpiralBevelGear",
    "KlingelnbergCycloPalloidSpiralBevelGearSet",
    "PlanetaryGearSet",
    "SpiralBevelGear",
    "SpiralBevelGearSet",
    "StraightBevelDiffGear",
    "StraightBevelDiffGearSet",
    "StraightBevelGear",
    "StraightBevelGearSet",
    "StraightBevelPlanetGear",
    "StraightBevelSunGear",
    "WormGear",
    "WormGearSet",
    "ZerolBevelGear",
    "ZerolBevelGearSet",
)
