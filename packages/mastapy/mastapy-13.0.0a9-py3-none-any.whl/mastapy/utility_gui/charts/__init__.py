"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1849 import BubbleChartDefinition
    from ._1850 import ConstantLine
    from ._1851 import CustomLineChart
    from ._1852 import CustomTableAndChart
    from ._1853 import LegacyChartMathChartDefinition
    from ._1854 import MatrixVisualisationDefinition
    from ._1855 import ModeConstantLine
    from ._1856 import NDChartDefinition
    from ._1857 import ParallelCoordinatesChartDefinition
    from ._1858 import PointsForSurface
    from ._1859 import ScatterChartDefinition
    from ._1860 import Series2D
    from ._1861 import SMTAxis
    from ._1862 import ThreeDChartDefinition
    from ._1863 import ThreeDVectorChartDefinition
    from ._1864 import TwoDChartDefinition
else:
    import_structure = {
        "_1849": ["BubbleChartDefinition"],
        "_1850": ["ConstantLine"],
        "_1851": ["CustomLineChart"],
        "_1852": ["CustomTableAndChart"],
        "_1853": ["LegacyChartMathChartDefinition"],
        "_1854": ["MatrixVisualisationDefinition"],
        "_1855": ["ModeConstantLine"],
        "_1856": ["NDChartDefinition"],
        "_1857": ["ParallelCoordinatesChartDefinition"],
        "_1858": ["PointsForSurface"],
        "_1859": ["ScatterChartDefinition"],
        "_1860": ["Series2D"],
        "_1861": ["SMTAxis"],
        "_1862": ["ThreeDChartDefinition"],
        "_1863": ["ThreeDVectorChartDefinition"],
        "_1864": ["TwoDChartDefinition"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BubbleChartDefinition",
    "ConstantLine",
    "CustomLineChart",
    "CustomTableAndChart",
    "LegacyChartMathChartDefinition",
    "MatrixVisualisationDefinition",
    "ModeConstantLine",
    "NDChartDefinition",
    "ParallelCoordinatesChartDefinition",
    "PointsForSurface",
    "ScatterChartDefinition",
    "Series2D",
    "SMTAxis",
    "ThreeDChartDefinition",
    "ThreeDVectorChartDefinition",
    "TwoDChartDefinition",
)
