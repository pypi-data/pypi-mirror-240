"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1461 import AxialLoadType
    from ._1462 import BoltedJointMaterial
    from ._1463 import BoltedJointMaterialDatabase
    from ._1464 import BoltGeometry
    from ._1465 import BoltGeometryDatabase
    from ._1466 import BoltMaterial
    from ._1467 import BoltMaterialDatabase
    from ._1468 import BoltSection
    from ._1469 import BoltShankType
    from ._1470 import BoltTypes
    from ._1471 import ClampedSection
    from ._1472 import ClampedSectionMaterialDatabase
    from ._1473 import DetailedBoltDesign
    from ._1474 import DetailedBoltedJointDesign
    from ._1475 import HeadCapTypes
    from ._1476 import JointGeometries
    from ._1477 import JointTypes
    from ._1478 import LoadedBolt
    from ._1479 import RolledBeforeOrAfterHeatTreatment
    from ._1480 import StandardSizes
    from ._1481 import StrengthGrades
    from ._1482 import ThreadTypes
    from ._1483 import TighteningTechniques
else:
    import_structure = {
        "_1461": ["AxialLoadType"],
        "_1462": ["BoltedJointMaterial"],
        "_1463": ["BoltedJointMaterialDatabase"],
        "_1464": ["BoltGeometry"],
        "_1465": ["BoltGeometryDatabase"],
        "_1466": ["BoltMaterial"],
        "_1467": ["BoltMaterialDatabase"],
        "_1468": ["BoltSection"],
        "_1469": ["BoltShankType"],
        "_1470": ["BoltTypes"],
        "_1471": ["ClampedSection"],
        "_1472": ["ClampedSectionMaterialDatabase"],
        "_1473": ["DetailedBoltDesign"],
        "_1474": ["DetailedBoltedJointDesign"],
        "_1475": ["HeadCapTypes"],
        "_1476": ["JointGeometries"],
        "_1477": ["JointTypes"],
        "_1478": ["LoadedBolt"],
        "_1479": ["RolledBeforeOrAfterHeatTreatment"],
        "_1480": ["StandardSizes"],
        "_1481": ["StrengthGrades"],
        "_1482": ["ThreadTypes"],
        "_1483": ["TighteningTechniques"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AxialLoadType",
    "BoltedJointMaterial",
    "BoltedJointMaterialDatabase",
    "BoltGeometry",
    "BoltGeometryDatabase",
    "BoltMaterial",
    "BoltMaterialDatabase",
    "BoltSection",
    "BoltShankType",
    "BoltTypes",
    "ClampedSection",
    "ClampedSectionMaterialDatabase",
    "DetailedBoltDesign",
    "DetailedBoltedJointDesign",
    "HeadCapTypes",
    "JointGeometries",
    "JointTypes",
    "LoadedBolt",
    "RolledBeforeOrAfterHeatTreatment",
    "StandardSizes",
    "StrengthGrades",
    "ThreadTypes",
    "TighteningTechniques",
)
