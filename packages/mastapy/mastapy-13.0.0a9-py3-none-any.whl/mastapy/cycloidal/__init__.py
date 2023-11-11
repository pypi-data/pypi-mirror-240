"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1447 import ContactSpecification
    from ._1448 import CrowningSpecificationMethod
    from ._1449 import CycloidalAssemblyDesign
    from ._1450 import CycloidalDiscDesign
    from ._1451 import CycloidalDiscDesignExporter
    from ._1452 import CycloidalDiscMaterial
    from ._1453 import CycloidalDiscMaterialDatabase
    from ._1454 import CycloidalDiscModificationsSpecification
    from ._1455 import DirectionOfMeasuredModifications
    from ._1456 import GeometryToExport
    from ._1457 import NamedDiscPhase
    from ._1458 import RingPinsDesign
    from ._1459 import RingPinsMaterial
    from ._1460 import RingPinsMaterialDatabase
else:
    import_structure = {
        "_1447": ["ContactSpecification"],
        "_1448": ["CrowningSpecificationMethod"],
        "_1449": ["CycloidalAssemblyDesign"],
        "_1450": ["CycloidalDiscDesign"],
        "_1451": ["CycloidalDiscDesignExporter"],
        "_1452": ["CycloidalDiscMaterial"],
        "_1453": ["CycloidalDiscMaterialDatabase"],
        "_1454": ["CycloidalDiscModificationsSpecification"],
        "_1455": ["DirectionOfMeasuredModifications"],
        "_1456": ["GeometryToExport"],
        "_1457": ["NamedDiscPhase"],
        "_1458": ["RingPinsDesign"],
        "_1459": ["RingPinsMaterial"],
        "_1460": ["RingPinsMaterialDatabase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ContactSpecification",
    "CrowningSpecificationMethod",
    "CycloidalAssemblyDesign",
    "CycloidalDiscDesign",
    "CycloidalDiscDesignExporter",
    "CycloidalDiscMaterial",
    "CycloidalDiscMaterialDatabase",
    "CycloidalDiscModificationsSpecification",
    "DirectionOfMeasuredModifications",
    "GeometryToExport",
    "NamedDiscPhase",
    "RingPinsDesign",
    "RingPinsMaterial",
    "RingPinsMaterialDatabase",
)
