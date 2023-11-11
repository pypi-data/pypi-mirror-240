"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1599 import DegreesMinutesSeconds
    from ._1600 import EnumUnit
    from ._1601 import InverseUnit
    from ._1602 import MeasurementBase
    from ._1603 import MeasurementSettings
    from ._1604 import MeasurementSystem
    from ._1605 import SafetyFactorUnit
    from ._1606 import TimeUnit
    from ._1607 import Unit
    from ._1608 import UnitGradient
else:
    import_structure = {
        "_1599": ["DegreesMinutesSeconds"],
        "_1600": ["EnumUnit"],
        "_1601": ["InverseUnit"],
        "_1602": ["MeasurementBase"],
        "_1603": ["MeasurementSettings"],
        "_1604": ["MeasurementSystem"],
        "_1605": ["SafetyFactorUnit"],
        "_1606": ["TimeUnit"],
        "_1607": ["Unit"],
        "_1608": ["UnitGradient"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DegreesMinutesSeconds",
    "EnumUnit",
    "InverseUnit",
    "MeasurementBase",
    "MeasurementSettings",
    "MeasurementSystem",
    "SafetyFactorUnit",
    "TimeUnit",
    "Unit",
    "UnitGradient",
)
