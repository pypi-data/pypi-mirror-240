"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2296 import AGMAGleasonConicalGearMesh
    from ._2297 import AGMAGleasonConicalGearTeethSocket
    from ._2298 import BevelDifferentialGearMesh
    from ._2299 import BevelDifferentialGearTeethSocket
    from ._2300 import BevelGearMesh
    from ._2301 import BevelGearTeethSocket
    from ._2302 import ConceptGearMesh
    from ._2303 import ConceptGearTeethSocket
    from ._2304 import ConicalGearMesh
    from ._2305 import ConicalGearTeethSocket
    from ._2306 import CylindricalGearMesh
    from ._2307 import CylindricalGearTeethSocket
    from ._2308 import FaceGearMesh
    from ._2309 import FaceGearTeethSocket
    from ._2310 import GearMesh
    from ._2311 import GearTeethSocket
    from ._2312 import HypoidGearMesh
    from ._2313 import HypoidGearTeethSocket
    from ._2314 import KlingelnbergConicalGearTeethSocket
    from ._2315 import KlingelnbergCycloPalloidConicalGearMesh
    from ._2316 import KlingelnbergCycloPalloidHypoidGearMesh
    from ._2317 import KlingelnbergCycloPalloidSpiralBevelGearMesh
    from ._2318 import KlingelnbergHypoidGearTeethSocket
    from ._2319 import KlingelnbergSpiralBevelGearTeethSocket
    from ._2320 import SpiralBevelGearMesh
    from ._2321 import SpiralBevelGearTeethSocket
    from ._2322 import StraightBevelDiffGearMesh
    from ._2323 import StraightBevelDiffGearTeethSocket
    from ._2324 import StraightBevelGearMesh
    from ._2325 import StraightBevelGearTeethSocket
    from ._2326 import WormGearMesh
    from ._2327 import WormGearTeethSocket
    from ._2328 import ZerolBevelGearMesh
    from ._2329 import ZerolBevelGearTeethSocket
else:
    import_structure = {
        "_2296": ["AGMAGleasonConicalGearMesh"],
        "_2297": ["AGMAGleasonConicalGearTeethSocket"],
        "_2298": ["BevelDifferentialGearMesh"],
        "_2299": ["BevelDifferentialGearTeethSocket"],
        "_2300": ["BevelGearMesh"],
        "_2301": ["BevelGearTeethSocket"],
        "_2302": ["ConceptGearMesh"],
        "_2303": ["ConceptGearTeethSocket"],
        "_2304": ["ConicalGearMesh"],
        "_2305": ["ConicalGearTeethSocket"],
        "_2306": ["CylindricalGearMesh"],
        "_2307": ["CylindricalGearTeethSocket"],
        "_2308": ["FaceGearMesh"],
        "_2309": ["FaceGearTeethSocket"],
        "_2310": ["GearMesh"],
        "_2311": ["GearTeethSocket"],
        "_2312": ["HypoidGearMesh"],
        "_2313": ["HypoidGearTeethSocket"],
        "_2314": ["KlingelnbergConicalGearTeethSocket"],
        "_2315": ["KlingelnbergCycloPalloidConicalGearMesh"],
        "_2316": ["KlingelnbergCycloPalloidHypoidGearMesh"],
        "_2317": ["KlingelnbergCycloPalloidSpiralBevelGearMesh"],
        "_2318": ["KlingelnbergHypoidGearTeethSocket"],
        "_2319": ["KlingelnbergSpiralBevelGearTeethSocket"],
        "_2320": ["SpiralBevelGearMesh"],
        "_2321": ["SpiralBevelGearTeethSocket"],
        "_2322": ["StraightBevelDiffGearMesh"],
        "_2323": ["StraightBevelDiffGearTeethSocket"],
        "_2324": ["StraightBevelGearMesh"],
        "_2325": ["StraightBevelGearTeethSocket"],
        "_2326": ["WormGearMesh"],
        "_2327": ["WormGearTeethSocket"],
        "_2328": ["ZerolBevelGearMesh"],
        "_2329": ["ZerolBevelGearTeethSocket"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAGleasonConicalGearMesh",
    "AGMAGleasonConicalGearTeethSocket",
    "BevelDifferentialGearMesh",
    "BevelDifferentialGearTeethSocket",
    "BevelGearMesh",
    "BevelGearTeethSocket",
    "ConceptGearMesh",
    "ConceptGearTeethSocket",
    "ConicalGearMesh",
    "ConicalGearTeethSocket",
    "CylindricalGearMesh",
    "CylindricalGearTeethSocket",
    "FaceGearMesh",
    "FaceGearTeethSocket",
    "GearMesh",
    "GearTeethSocket",
    "HypoidGearMesh",
    "HypoidGearTeethSocket",
    "KlingelnbergConicalGearTeethSocket",
    "KlingelnbergCycloPalloidConicalGearMesh",
    "KlingelnbergCycloPalloidHypoidGearMesh",
    "KlingelnbergCycloPalloidSpiralBevelGearMesh",
    "KlingelnbergHypoidGearTeethSocket",
    "KlingelnbergSpiralBevelGearTeethSocket",
    "SpiralBevelGearMesh",
    "SpiralBevelGearTeethSocket",
    "StraightBevelDiffGearMesh",
    "StraightBevelDiffGearTeethSocket",
    "StraightBevelGearMesh",
    "StraightBevelGearTeethSocket",
    "WormGearMesh",
    "WormGearTeethSocket",
    "ZerolBevelGearMesh",
    "ZerolBevelGearTeethSocket",
)
