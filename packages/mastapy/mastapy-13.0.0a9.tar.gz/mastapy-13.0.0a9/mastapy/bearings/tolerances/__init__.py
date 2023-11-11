"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1898 import BearingConnectionComponent
    from ._1899 import InternalClearanceClass
    from ._1900 import BearingToleranceClass
    from ._1901 import BearingToleranceDefinitionOptions
    from ._1902 import FitType
    from ._1903 import InnerRingTolerance
    from ._1904 import InnerSupportTolerance
    from ._1905 import InterferenceDetail
    from ._1906 import InterferenceTolerance
    from ._1907 import ITDesignation
    from ._1908 import MountingSleeveDiameterDetail
    from ._1909 import OuterRingTolerance
    from ._1910 import OuterSupportTolerance
    from ._1911 import RaceDetail
    from ._1912 import RaceRoundnessAtAngle
    from ._1913 import RadialSpecificationMethod
    from ._1914 import RingTolerance
    from ._1915 import RoundnessSpecification
    from ._1916 import RoundnessSpecificationType
    from ._1917 import SupportDetail
    from ._1918 import SupportMaterialSource
    from ._1919 import SupportTolerance
    from ._1920 import SupportToleranceLocationDesignation
    from ._1921 import ToleranceCombination
    from ._1922 import TypeOfFit
else:
    import_structure = {
        "_1898": ["BearingConnectionComponent"],
        "_1899": ["InternalClearanceClass"],
        "_1900": ["BearingToleranceClass"],
        "_1901": ["BearingToleranceDefinitionOptions"],
        "_1902": ["FitType"],
        "_1903": ["InnerRingTolerance"],
        "_1904": ["InnerSupportTolerance"],
        "_1905": ["InterferenceDetail"],
        "_1906": ["InterferenceTolerance"],
        "_1907": ["ITDesignation"],
        "_1908": ["MountingSleeveDiameterDetail"],
        "_1909": ["OuterRingTolerance"],
        "_1910": ["OuterSupportTolerance"],
        "_1911": ["RaceDetail"],
        "_1912": ["RaceRoundnessAtAngle"],
        "_1913": ["RadialSpecificationMethod"],
        "_1914": ["RingTolerance"],
        "_1915": ["RoundnessSpecification"],
        "_1916": ["RoundnessSpecificationType"],
        "_1917": ["SupportDetail"],
        "_1918": ["SupportMaterialSource"],
        "_1919": ["SupportTolerance"],
        "_1920": ["SupportToleranceLocationDesignation"],
        "_1921": ["ToleranceCombination"],
        "_1922": ["TypeOfFit"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingConnectionComponent",
    "InternalClearanceClass",
    "BearingToleranceClass",
    "BearingToleranceDefinitionOptions",
    "FitType",
    "InnerRingTolerance",
    "InnerSupportTolerance",
    "InterferenceDetail",
    "InterferenceTolerance",
    "ITDesignation",
    "MountingSleeveDiameterDetail",
    "OuterRingTolerance",
    "OuterSupportTolerance",
    "RaceDetail",
    "RaceRoundnessAtAngle",
    "RadialSpecificationMethod",
    "RingTolerance",
    "RoundnessSpecification",
    "RoundnessSpecificationType",
    "SupportDetail",
    "SupportMaterialSource",
    "SupportTolerance",
    "SupportToleranceLocationDesignation",
    "ToleranceCombination",
    "TypeOfFit",
)
