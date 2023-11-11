"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5668 import AbstractAssemblyStaticLoadCaseGroup
    from ._5669 import ComponentStaticLoadCaseGroup
    from ._5670 import ConnectionStaticLoadCaseGroup
    from ._5671 import DesignEntityStaticLoadCaseGroup
    from ._5672 import GearSetStaticLoadCaseGroup
    from ._5673 import PartStaticLoadCaseGroup
else:
    import_structure = {
        "_5668": ["AbstractAssemblyStaticLoadCaseGroup"],
        "_5669": ["ComponentStaticLoadCaseGroup"],
        "_5670": ["ConnectionStaticLoadCaseGroup"],
        "_5671": ["DesignEntityStaticLoadCaseGroup"],
        "_5672": ["GearSetStaticLoadCaseGroup"],
        "_5673": ["PartStaticLoadCaseGroup"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyStaticLoadCaseGroup",
    "ComponentStaticLoadCaseGroup",
    "ConnectionStaticLoadCaseGroup",
    "DesignEntityStaticLoadCaseGroup",
    "GearSetStaticLoadCaseGroup",
    "PartStaticLoadCaseGroup",
)
