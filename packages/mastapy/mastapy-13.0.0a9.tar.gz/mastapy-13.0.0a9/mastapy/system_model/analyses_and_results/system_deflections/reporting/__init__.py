"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2839 import CylindricalGearMeshMisalignmentValue
    from ._2840 import FlexibleGearChart
    from ._2841 import GearInMeshDeflectionResults
    from ._2842 import MeshDeflectionResults
    from ._2843 import PlanetCarrierWindup
    from ._2844 import PlanetPinWindup
    from ._2845 import RigidlyConnectedComponentGroupSystemDeflection
    from ._2846 import ShaftSystemDeflectionSectionsReport
    from ._2847 import SplineFlankContactReporting
else:
    import_structure = {
        "_2839": ["CylindricalGearMeshMisalignmentValue"],
        "_2840": ["FlexibleGearChart"],
        "_2841": ["GearInMeshDeflectionResults"],
        "_2842": ["MeshDeflectionResults"],
        "_2843": ["PlanetCarrierWindup"],
        "_2844": ["PlanetPinWindup"],
        "_2845": ["RigidlyConnectedComponentGroupSystemDeflection"],
        "_2846": ["ShaftSystemDeflectionSectionsReport"],
        "_2847": ["SplineFlankContactReporting"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearMeshMisalignmentValue",
    "FlexibleGearChart",
    "GearInMeshDeflectionResults",
    "MeshDeflectionResults",
    "PlanetCarrierWindup",
    "PlanetPinWindup",
    "RigidlyConnectedComponentGroupSystemDeflection",
    "ShaftSystemDeflectionSectionsReport",
    "SplineFlankContactReporting",
)
