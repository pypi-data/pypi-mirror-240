"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6533 import ExcelBatchDutyCycleCreator
    from ._6534 import ExcelBatchDutyCycleSpectraCreatorDetails
    from ._6535 import ExcelFileDetails
    from ._6536 import ExcelSheet
    from ._6537 import ExcelSheetDesignStateSelector
    from ._6538 import MASTAFileDetails
else:
    import_structure = {
        "_6533": ["ExcelBatchDutyCycleCreator"],
        "_6534": ["ExcelBatchDutyCycleSpectraCreatorDetails"],
        "_6535": ["ExcelFileDetails"],
        "_6536": ["ExcelSheet"],
        "_6537": ["ExcelSheetDesignStateSelector"],
        "_6538": ["MASTAFileDetails"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ExcelBatchDutyCycleCreator",
    "ExcelBatchDutyCycleSpectraCreatorDetails",
    "ExcelFileDetails",
    "ExcelSheet",
    "ExcelSheetDesignStateSelector",
    "MASTAFileDetails",
)
