"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2223 import ConicalGearOptimisationStrategy
    from ._2224 import ConicalGearOptimizationStep
    from ._2225 import ConicalGearOptimizationStrategyDatabase
    from ._2226 import CylindricalGearOptimisationStrategy
    from ._2227 import CylindricalGearOptimizationStep
    from ._2228 import MeasuredAndFactorViewModel
    from ._2229 import MicroGeometryOptimisationTarget
    from ._2230 import OptimizationStep
    from ._2231 import OptimizationStrategy
    from ._2232 import OptimizationStrategyBase
    from ._2233 import OptimizationStrategyDatabase
else:
    import_structure = {
        "_2223": ["ConicalGearOptimisationStrategy"],
        "_2224": ["ConicalGearOptimizationStep"],
        "_2225": ["ConicalGearOptimizationStrategyDatabase"],
        "_2226": ["CylindricalGearOptimisationStrategy"],
        "_2227": ["CylindricalGearOptimizationStep"],
        "_2228": ["MeasuredAndFactorViewModel"],
        "_2229": ["MicroGeometryOptimisationTarget"],
        "_2230": ["OptimizationStep"],
        "_2231": ["OptimizationStrategy"],
        "_2232": ["OptimizationStrategyBase"],
        "_2233": ["OptimizationStrategyDatabase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearOptimisationStrategy",
    "ConicalGearOptimizationStep",
    "ConicalGearOptimizationStrategyDatabase",
    "CylindricalGearOptimisationStrategy",
    "CylindricalGearOptimizationStep",
    "MeasuredAndFactorViewModel",
    "MicroGeometryOptimisationTarget",
    "OptimizationStep",
    "OptimizationStrategy",
    "OptimizationStrategyBase",
    "OptimizationStrategyDatabase",
)
