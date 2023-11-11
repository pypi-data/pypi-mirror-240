"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1736 import ScriptingSetup
    from ._1737 import UserDefinedPropertyKey
    from ._1738 import UserSpecifiedData
else:
    import_structure = {
        "_1736": ["ScriptingSetup"],
        "_1737": ["UserDefinedPropertyKey"],
        "_1738": ["UserSpecifiedData"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ScriptingSetup",
    "UserDefinedPropertyKey",
    "UserSpecifiedData",
)
