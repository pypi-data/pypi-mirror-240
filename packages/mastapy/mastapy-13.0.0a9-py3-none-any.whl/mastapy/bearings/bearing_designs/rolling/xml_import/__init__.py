"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2173 import AbstractXmlVariableAssignment
    from ._2174 import BearingImportFile
    from ._2175 import RollingBearingImporter
    from ._2176 import XmlBearingTypeMapping
    from ._2177 import XMLVariableAssignment
else:
    import_structure = {
        "_2173": ["AbstractXmlVariableAssignment"],
        "_2174": ["BearingImportFile"],
        "_2175": ["RollingBearingImporter"],
        "_2176": ["XmlBearingTypeMapping"],
        "_2177": ["XMLVariableAssignment"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractXmlVariableAssignment",
    "BearingImportFile",
    "RollingBearingImporter",
    "XmlBearingTypeMapping",
    "XMLVariableAssignment",
)
