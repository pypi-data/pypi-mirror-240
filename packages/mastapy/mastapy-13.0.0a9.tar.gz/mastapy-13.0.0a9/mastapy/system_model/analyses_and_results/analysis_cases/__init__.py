"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7531 import AnalysisCase
    from ._7532 import AbstractAnalysisOptions
    from ._7533 import CompoundAnalysisCase
    from ._7534 import ConnectionAnalysisCase
    from ._7535 import ConnectionCompoundAnalysis
    from ._7536 import ConnectionFEAnalysis
    from ._7537 import ConnectionStaticLoadAnalysisCase
    from ._7538 import ConnectionTimeSeriesLoadAnalysisCase
    from ._7539 import DesignEntityCompoundAnalysis
    from ._7540 import FEAnalysis
    from ._7541 import PartAnalysisCase
    from ._7542 import PartCompoundAnalysis
    from ._7543 import PartFEAnalysis
    from ._7544 import PartStaticLoadAnalysisCase
    from ._7545 import PartTimeSeriesLoadAnalysisCase
    from ._7546 import StaticLoadAnalysisCase
    from ._7547 import TimeSeriesLoadAnalysisCase
else:
    import_structure = {
        "_7531": ["AnalysisCase"],
        "_7532": ["AbstractAnalysisOptions"],
        "_7533": ["CompoundAnalysisCase"],
        "_7534": ["ConnectionAnalysisCase"],
        "_7535": ["ConnectionCompoundAnalysis"],
        "_7536": ["ConnectionFEAnalysis"],
        "_7537": ["ConnectionStaticLoadAnalysisCase"],
        "_7538": ["ConnectionTimeSeriesLoadAnalysisCase"],
        "_7539": ["DesignEntityCompoundAnalysis"],
        "_7540": ["FEAnalysis"],
        "_7541": ["PartAnalysisCase"],
        "_7542": ["PartCompoundAnalysis"],
        "_7543": ["PartFEAnalysis"],
        "_7544": ["PartStaticLoadAnalysisCase"],
        "_7545": ["PartTimeSeriesLoadAnalysisCase"],
        "_7546": ["StaticLoadAnalysisCase"],
        "_7547": ["TimeSeriesLoadAnalysisCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AnalysisCase",
    "AbstractAnalysisOptions",
    "CompoundAnalysisCase",
    "ConnectionAnalysisCase",
    "ConnectionCompoundAnalysis",
    "ConnectionFEAnalysis",
    "ConnectionStaticLoadAnalysisCase",
    "ConnectionTimeSeriesLoadAnalysisCase",
    "DesignEntityCompoundAnalysis",
    "FEAnalysis",
    "PartAnalysisCase",
    "PartCompoundAnalysis",
    "PartFEAnalysis",
    "PartStaticLoadAnalysisCase",
    "PartTimeSeriesLoadAnalysisCase",
    "StaticLoadAnalysisCase",
    "TimeSeriesLoadAnalysisCase",
)
