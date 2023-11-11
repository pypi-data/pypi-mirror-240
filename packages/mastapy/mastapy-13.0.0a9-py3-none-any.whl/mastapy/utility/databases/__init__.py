"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1821 import Database
    from ._1822 import DatabaseConnectionSettings
    from ._1823 import DatabaseKey
    from ._1824 import DatabaseSettings
    from ._1825 import NamedDatabase
    from ._1826 import NamedDatabaseItem
    from ._1827 import NamedKey
    from ._1828 import SQLDatabase
else:
    import_structure = {
        "_1821": ["Database"],
        "_1822": ["DatabaseConnectionSettings"],
        "_1823": ["DatabaseKey"],
        "_1824": ["DatabaseSettings"],
        "_1825": ["NamedDatabase"],
        "_1826": ["NamedDatabaseItem"],
        "_1827": ["NamedKey"],
        "_1828": ["SQLDatabase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Database",
    "DatabaseConnectionSettings",
    "DatabaseKey",
    "DatabaseSettings",
    "NamedDatabase",
    "NamedDatabaseItem",
    "NamedKey",
    "SQLDatabase",
)
