"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1535 import AbstractOptimisable
    from ._1536 import DesignSpaceSearchStrategyDatabase
    from ._1537 import InputSetter
    from ._1538 import MicroGeometryDesignSpaceSearchStrategyDatabase
    from ._1539 import Optimisable
    from ._1540 import OptimisationHistory
    from ._1541 import OptimizationInput
    from ._1542 import OptimizationVariable
    from ._1543 import ParetoOptimisationFilter
    from ._1544 import ParetoOptimisationInput
    from ._1545 import ParetoOptimisationOutput
    from ._1546 import ParetoOptimisationStrategy
    from ._1547 import ParetoOptimisationStrategyBars
    from ._1548 import ParetoOptimisationStrategyChartInformation
    from ._1549 import ParetoOptimisationStrategyDatabase
    from ._1550 import ParetoOptimisationVariable
    from ._1551 import ParetoOptimisationVariableBase
    from ._1552 import PropertyTargetForDominantCandidateSearch
    from ._1553 import ReportingOptimizationInput
    from ._1554 import SpecifyOptimisationInputAs
    from ._1555 import TargetingPropertyTo
else:
    import_structure = {
        "_1535": ["AbstractOptimisable"],
        "_1536": ["DesignSpaceSearchStrategyDatabase"],
        "_1537": ["InputSetter"],
        "_1538": ["MicroGeometryDesignSpaceSearchStrategyDatabase"],
        "_1539": ["Optimisable"],
        "_1540": ["OptimisationHistory"],
        "_1541": ["OptimizationInput"],
        "_1542": ["OptimizationVariable"],
        "_1543": ["ParetoOptimisationFilter"],
        "_1544": ["ParetoOptimisationInput"],
        "_1545": ["ParetoOptimisationOutput"],
        "_1546": ["ParetoOptimisationStrategy"],
        "_1547": ["ParetoOptimisationStrategyBars"],
        "_1548": ["ParetoOptimisationStrategyChartInformation"],
        "_1549": ["ParetoOptimisationStrategyDatabase"],
        "_1550": ["ParetoOptimisationVariable"],
        "_1551": ["ParetoOptimisationVariableBase"],
        "_1552": ["PropertyTargetForDominantCandidateSearch"],
        "_1553": ["ReportingOptimizationInput"],
        "_1554": ["SpecifyOptimisationInputAs"],
        "_1555": ["TargetingPropertyTo"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractOptimisable",
    "DesignSpaceSearchStrategyDatabase",
    "InputSetter",
    "MicroGeometryDesignSpaceSearchStrategyDatabase",
    "Optimisable",
    "OptimisationHistory",
    "OptimizationInput",
    "OptimizationVariable",
    "ParetoOptimisationFilter",
    "ParetoOptimisationInput",
    "ParetoOptimisationOutput",
    "ParetoOptimisationStrategy",
    "ParetoOptimisationStrategyBars",
    "ParetoOptimisationStrategyChartInformation",
    "ParetoOptimisationStrategyDatabase",
    "ParetoOptimisationVariable",
    "ParetoOptimisationVariableBase",
    "PropertyTargetForDominantCandidateSearch",
    "ReportingOptimizationInput",
    "SpecifyOptimisationInputAs",
    "TargetingPropertyTo",
)
