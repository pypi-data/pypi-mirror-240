"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7558 import ApiEnumForAttribute
    from ._7559 import ApiVersion
    from ._7560 import SMTBitmap
    from ._7562 import MastaPropertyAttribute
    from ._7563 import PythonCommand
    from ._7564 import ScriptingCommand
    from ._7565 import ScriptingExecutionCommand
    from ._7566 import ScriptingObjectCommand
    from ._7567 import ApiVersioning
else:
    import_structure = {
        "_7558": ["ApiEnumForAttribute"],
        "_7559": ["ApiVersion"],
        "_7560": ["SMTBitmap"],
        "_7562": ["MastaPropertyAttribute"],
        "_7563": ["PythonCommand"],
        "_7564": ["ScriptingCommand"],
        "_7565": ["ScriptingExecutionCommand"],
        "_7566": ["ScriptingObjectCommand"],
        "_7567": ["ApiVersioning"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ApiEnumForAttribute",
    "ApiVersion",
    "SMTBitmap",
    "MastaPropertyAttribute",
    "PythonCommand",
    "ScriptingCommand",
    "ScriptingExecutionCommand",
    "ScriptingObjectCommand",
    "ApiVersioning",
)
