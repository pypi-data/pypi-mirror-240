"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5850 import AbstractSingleWhineAnalysisResultsPropertyAccessor
    from ._5851 import DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic
    from ._5852 import DataPointForResponseOfANodeAtAFrequencyToAHarmonic
    from ._5853 import FEPartHarmonicAnalysisResultsPropertyAccessor
    from ._5854 import FEPartSingleWhineAnalysisResultsPropertyAccessor
    from ._5855 import HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic
    from ._5856 import HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic
    from ._5857 import HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic
    from ._5858 import HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic
    from ._5859 import HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic
    from ._5860 import HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic
    from ._5861 import HarmonicAnalysisResultsPropertyAccessor
    from ._5862 import ResultsForMultipleOrders
    from ._5863 import ResultsForMultipleOrdersForFESurface
    from ._5864 import ResultsForMultipleOrdersForGroups
    from ._5865 import ResultsForOrder
    from ._5866 import ResultsForOrderIncludingGroups
    from ._5867 import ResultsForOrderIncludingNodes
    from ._5868 import ResultsForOrderIncludingSurfaces
    from ._5869 import ResultsForResponseOfAComponentOrSurfaceInAHarmonic
    from ._5870 import ResultsForResponseOfANodeOnAHarmonic
    from ._5871 import ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic
    from ._5872 import RootAssemblyHarmonicAnalysisResultsPropertyAccessor
    from ._5873 import RootAssemblySingleWhineAnalysisResultsPropertyAccessor
    from ._5874 import SingleWhineAnalysisResultsPropertyAccessor
else:
    import_structure = {
        "_5850": ["AbstractSingleWhineAnalysisResultsPropertyAccessor"],
        "_5851": ["DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic"],
        "_5852": ["DataPointForResponseOfANodeAtAFrequencyToAHarmonic"],
        "_5853": ["FEPartHarmonicAnalysisResultsPropertyAccessor"],
        "_5854": ["FEPartSingleWhineAnalysisResultsPropertyAccessor"],
        "_5855": ["HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic"],
        "_5856": ["HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic"],
        "_5857": ["HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic"],
        "_5858": ["HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic"],
        "_5859": ["HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic"],
        "_5860": ["HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic"],
        "_5861": ["HarmonicAnalysisResultsPropertyAccessor"],
        "_5862": ["ResultsForMultipleOrders"],
        "_5863": ["ResultsForMultipleOrdersForFESurface"],
        "_5864": ["ResultsForMultipleOrdersForGroups"],
        "_5865": ["ResultsForOrder"],
        "_5866": ["ResultsForOrderIncludingGroups"],
        "_5867": ["ResultsForOrderIncludingNodes"],
        "_5868": ["ResultsForOrderIncludingSurfaces"],
        "_5869": ["ResultsForResponseOfAComponentOrSurfaceInAHarmonic"],
        "_5870": ["ResultsForResponseOfANodeOnAHarmonic"],
        "_5871": ["ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic"],
        "_5872": ["RootAssemblyHarmonicAnalysisResultsPropertyAccessor"],
        "_5873": ["RootAssemblySingleWhineAnalysisResultsPropertyAccessor"],
        "_5874": ["SingleWhineAnalysisResultsPropertyAccessor"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractSingleWhineAnalysisResultsPropertyAccessor",
    "DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic",
    "DataPointForResponseOfANodeAtAFrequencyToAHarmonic",
    "FEPartHarmonicAnalysisResultsPropertyAccessor",
    "FEPartSingleWhineAnalysisResultsPropertyAccessor",
    "HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic",
    "HarmonicAnalysisResultsPropertyAccessor",
    "ResultsForMultipleOrders",
    "ResultsForMultipleOrdersForFESurface",
    "ResultsForMultipleOrdersForGroups",
    "ResultsForOrder",
    "ResultsForOrderIncludingGroups",
    "ResultsForOrderIncludingNodes",
    "ResultsForOrderIncludingSurfaces",
    "ResultsForResponseOfAComponentOrSurfaceInAHarmonic",
    "ResultsForResponseOfANodeOnAHarmonic",
    "ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic",
    "RootAssemblyHarmonicAnalysisResultsPropertyAccessor",
    "RootAssemblySingleWhineAnalysisResultsPropertyAccessor",
    "SingleWhineAnalysisResultsPropertyAccessor",
)
