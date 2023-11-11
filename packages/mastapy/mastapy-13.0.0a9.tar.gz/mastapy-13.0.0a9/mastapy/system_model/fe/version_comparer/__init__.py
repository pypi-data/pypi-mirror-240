"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2409 import DesignResults
    from ._2410 import FESubstructureResults
    from ._2411 import FESubstructureVersionComparer
    from ._2412 import LoadCaseResults
    from ._2413 import LoadCasesToRun
    from ._2414 import NodeComparisonResult
else:
    import_structure = {
        "_2409": ["DesignResults"],
        "_2410": ["FESubstructureResults"],
        "_2411": ["FESubstructureVersionComparer"],
        "_2412": ["LoadCaseResults"],
        "_2413": ["LoadCasesToRun"],
        "_2414": ["NodeComparisonResult"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DesignResults",
    "FESubstructureResults",
    "FESubstructureVersionComparer",
    "LoadCaseResults",
    "LoadCasesToRun",
    "NodeComparisonResult",
)
