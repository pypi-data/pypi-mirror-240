"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1831 import EnumWithSelectedValue
    from ._1833 import DeletableCollectionMember
    from ._1834 import DutyCyclePropertySummary
    from ._1835 import DutyCyclePropertySummaryForce
    from ._1836 import DutyCyclePropertySummaryPercentage
    from ._1837 import DutyCyclePropertySummarySmallAngle
    from ._1838 import DutyCyclePropertySummaryStress
    from ._1839 import DutyCyclePropertySummaryVeryShortLength
    from ._1840 import EnumWithBoolean
    from ._1841 import NamedRangeWithOverridableMinAndMax
    from ._1842 import TypedObjectsWithOption
else:
    import_structure = {
        "_1831": ["EnumWithSelectedValue"],
        "_1833": ["DeletableCollectionMember"],
        "_1834": ["DutyCyclePropertySummary"],
        "_1835": ["DutyCyclePropertySummaryForce"],
        "_1836": ["DutyCyclePropertySummaryPercentage"],
        "_1837": ["DutyCyclePropertySummarySmallAngle"],
        "_1838": ["DutyCyclePropertySummaryStress"],
        "_1839": ["DutyCyclePropertySummaryVeryShortLength"],
        "_1840": ["EnumWithBoolean"],
        "_1841": ["NamedRangeWithOverridableMinAndMax"],
        "_1842": ["TypedObjectsWithOption"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "EnumWithSelectedValue",
    "DeletableCollectionMember",
    "DutyCyclePropertySummary",
    "DutyCyclePropertySummaryForce",
    "DutyCyclePropertySummaryPercentage",
    "DutyCyclePropertySummarySmallAngle",
    "DutyCyclePropertySummaryStress",
    "DutyCyclePropertySummaryVeryShortLength",
    "EnumWithBoolean",
    "NamedRangeWithOverridableMinAndMax",
    "TypedObjectsWithOption",
)
