"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2608 import ActiveFESubstructureSelection
    from ._2609 import ActiveFESubstructureSelectionGroup
    from ._2610 import ActiveShaftDesignSelection
    from ._2611 import ActiveShaftDesignSelectionGroup
    from ._2612 import BearingDetailConfiguration
    from ._2613 import BearingDetailSelection
    from ._2614 import PartDetailConfiguration
    from ._2615 import PartDetailSelection
else:
    import_structure = {
        "_2608": ["ActiveFESubstructureSelection"],
        "_2609": ["ActiveFESubstructureSelectionGroup"],
        "_2610": ["ActiveShaftDesignSelection"],
        "_2611": ["ActiveShaftDesignSelectionGroup"],
        "_2612": ["BearingDetailConfiguration"],
        "_2613": ["BearingDetailSelection"],
        "_2614": ["PartDetailConfiguration"],
        "_2615": ["PartDetailSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveFESubstructureSelection",
    "ActiveFESubstructureSelectionGroup",
    "ActiveShaftDesignSelection",
    "ActiveShaftDesignSelectionGroup",
    "BearingDetailConfiguration",
    "BearingDetailSelection",
    "PartDetailConfiguration",
    "PartDetailSelection",
)
