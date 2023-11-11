"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6264 import CombinationAnalysis
    from ._6265 import FlexiblePinAnalysis
    from ._6266 import FlexiblePinAnalysisConceptLevel
    from ._6267 import FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass
    from ._6268 import FlexiblePinAnalysisGearAndBearingRating
    from ._6269 import FlexiblePinAnalysisManufactureLevel
    from ._6270 import FlexiblePinAnalysisOptions
    from ._6271 import FlexiblePinAnalysisStopStartAnalysis
    from ._6272 import WindTurbineCertificationReport
else:
    import_structure = {
        "_6264": ["CombinationAnalysis"],
        "_6265": ["FlexiblePinAnalysis"],
        "_6266": ["FlexiblePinAnalysisConceptLevel"],
        "_6267": ["FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass"],
        "_6268": ["FlexiblePinAnalysisGearAndBearingRating"],
        "_6269": ["FlexiblePinAnalysisManufactureLevel"],
        "_6270": ["FlexiblePinAnalysisOptions"],
        "_6271": ["FlexiblePinAnalysisStopStartAnalysis"],
        "_6272": ["WindTurbineCertificationReport"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CombinationAnalysis",
    "FlexiblePinAnalysis",
    "FlexiblePinAnalysisConceptLevel",
    "FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass",
    "FlexiblePinAnalysisGearAndBearingRating",
    "FlexiblePinAnalysisManufactureLevel",
    "FlexiblePinAnalysisOptions",
    "FlexiblePinAnalysisStopStartAnalysis",
    "WindTurbineCertificationReport",
)
