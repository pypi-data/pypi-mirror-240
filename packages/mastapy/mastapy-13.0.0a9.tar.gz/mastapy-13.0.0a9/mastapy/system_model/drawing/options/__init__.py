"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2258 import AdvancedTimeSteppingAnalysisForModulationModeViewOptions
    from ._2259 import ExcitationAnalysisViewOption
    from ._2260 import ModalContributionViewOptions
else:
    import_structure = {
        "_2258": ["AdvancedTimeSteppingAnalysisForModulationModeViewOptions"],
        "_2259": ["ExcitationAnalysisViewOption"],
        "_2260": ["ModalContributionViewOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdvancedTimeSteppingAnalysisForModulationModeViewOptions",
    "ExcitationAnalysisViewOption",
    "ModalContributionViewOptions",
)
