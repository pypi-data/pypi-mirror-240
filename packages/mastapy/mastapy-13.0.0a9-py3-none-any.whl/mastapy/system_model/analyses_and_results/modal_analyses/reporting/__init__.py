"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4712 import CalculateFullFEResultsForMode
    from ._4713 import CampbellDiagramReport
    from ._4714 import ComponentPerModeResult
    from ._4715 import DesignEntityModalAnalysisGroupResults
    from ._4716 import ModalCMSResultsForModeAndFE
    from ._4717 import PerModeResultsReport
    from ._4718 import RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis
    from ._4719 import RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis
    from ._4720 import RigidlyConnectedDesignEntityGroupModalAnalysis
    from ._4721 import ShaftPerModeResult
    from ._4722 import SingleExcitationResultsModalAnalysis
    from ._4723 import SingleModeResults
else:
    import_structure = {
        "_4712": ["CalculateFullFEResultsForMode"],
        "_4713": ["CampbellDiagramReport"],
        "_4714": ["ComponentPerModeResult"],
        "_4715": ["DesignEntityModalAnalysisGroupResults"],
        "_4716": ["ModalCMSResultsForModeAndFE"],
        "_4717": ["PerModeResultsReport"],
        "_4718": ["RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis"],
        "_4719": ["RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis"],
        "_4720": ["RigidlyConnectedDesignEntityGroupModalAnalysis"],
        "_4721": ["ShaftPerModeResult"],
        "_4722": ["SingleExcitationResultsModalAnalysis"],
        "_4723": ["SingleModeResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CalculateFullFEResultsForMode",
    "CampbellDiagramReport",
    "ComponentPerModeResult",
    "DesignEntityModalAnalysisGroupResults",
    "ModalCMSResultsForModeAndFE",
    "PerModeResultsReport",
    "RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis",
    "RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis",
    "RigidlyConnectedDesignEntityGroupModalAnalysis",
    "ShaftPerModeResult",
    "SingleExcitationResultsModalAnalysis",
    "SingleModeResults",
)
