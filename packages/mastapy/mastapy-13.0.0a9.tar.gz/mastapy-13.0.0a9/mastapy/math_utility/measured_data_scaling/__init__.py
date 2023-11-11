"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1566 import DataScalingOptions
    from ._1567 import DataScalingReferenceValues
    from ._1568 import DataScalingReferenceValuesBase
else:
    import_structure = {
        "_1566": ["DataScalingOptions"],
        "_1567": ["DataScalingReferenceValues"],
        "_1568": ["DataScalingReferenceValuesBase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DataScalingOptions",
    "DataScalingReferenceValues",
    "DataScalingReferenceValuesBase",
)
