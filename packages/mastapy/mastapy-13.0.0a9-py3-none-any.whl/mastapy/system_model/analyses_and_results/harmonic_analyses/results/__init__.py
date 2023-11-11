"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5840 import ConnectedComponentType
    from ._5841 import ExcitationSourceSelection
    from ._5842 import ExcitationSourceSelectionBase
    from ._5843 import ExcitationSourceSelectionGroup
    from ._5844 import HarmonicSelection
    from ._5845 import ModalContributionDisplayMethod
    from ._5846 import ModalContributionFilteringMethod
    from ._5847 import ResultLocationSelectionGroup
    from ._5848 import ResultLocationSelectionGroups
    from ._5849 import ResultNodeSelection
else:
    import_structure = {
        "_5840": ["ConnectedComponentType"],
        "_5841": ["ExcitationSourceSelection"],
        "_5842": ["ExcitationSourceSelectionBase"],
        "_5843": ["ExcitationSourceSelectionGroup"],
        "_5844": ["HarmonicSelection"],
        "_5845": ["ModalContributionDisplayMethod"],
        "_5846": ["ModalContributionFilteringMethod"],
        "_5847": ["ResultLocationSelectionGroup"],
        "_5848": ["ResultLocationSelectionGroups"],
        "_5849": ["ResultNodeSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConnectedComponentType",
    "ExcitationSourceSelection",
    "ExcitationSourceSelectionBase",
    "ExcitationSourceSelectionGroup",
    "HarmonicSelection",
    "ModalContributionDisplayMethod",
    "ModalContributionFilteringMethod",
    "ResultLocationSelectionGroup",
    "ResultLocationSelectionGroups",
    "ResultNodeSelection",
)
