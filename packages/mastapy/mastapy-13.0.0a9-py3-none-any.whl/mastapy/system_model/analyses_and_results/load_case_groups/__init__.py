"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5654 import AbstractDesignStateLoadCaseGroup
    from ._5655 import AbstractLoadCaseGroup
    from ._5656 import AbstractStaticLoadCaseGroup
    from ._5657 import ClutchEngagementStatus
    from ._5658 import ConceptSynchroGearEngagementStatus
    from ._5659 import DesignState
    from ._5660 import DutyCycle
    from ._5661 import GenericClutchEngagementStatus
    from ._5662 import LoadCaseGroupHistograms
    from ._5663 import SubGroupInSingleDesignState
    from ._5664 import SystemOptimisationGearSet
    from ._5665 import SystemOptimiserGearSetOptimisation
    from ._5666 import SystemOptimiserTargets
    from ._5667 import TimeSeriesLoadCaseGroup
else:
    import_structure = {
        "_5654": ["AbstractDesignStateLoadCaseGroup"],
        "_5655": ["AbstractLoadCaseGroup"],
        "_5656": ["AbstractStaticLoadCaseGroup"],
        "_5657": ["ClutchEngagementStatus"],
        "_5658": ["ConceptSynchroGearEngagementStatus"],
        "_5659": ["DesignState"],
        "_5660": ["DutyCycle"],
        "_5661": ["GenericClutchEngagementStatus"],
        "_5662": ["LoadCaseGroupHistograms"],
        "_5663": ["SubGroupInSingleDesignState"],
        "_5664": ["SystemOptimisationGearSet"],
        "_5665": ["SystemOptimiserGearSetOptimisation"],
        "_5666": ["SystemOptimiserTargets"],
        "_5667": ["TimeSeriesLoadCaseGroup"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractDesignStateLoadCaseGroup",
    "AbstractLoadCaseGroup",
    "AbstractStaticLoadCaseGroup",
    "ClutchEngagementStatus",
    "ConceptSynchroGearEngagementStatus",
    "DesignState",
    "DutyCycle",
    "GenericClutchEngagementStatus",
    "LoadCaseGroupHistograms",
    "SubGroupInSingleDesignState",
    "SystemOptimisationGearSet",
    "SystemOptimiserGearSetOptimisation",
    "SystemOptimiserTargets",
    "TimeSeriesLoadCaseGroup",
)
