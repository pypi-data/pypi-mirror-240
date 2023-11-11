"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2178 import AxialFeedJournalBearing
    from ._2179 import AxialGrooveJournalBearing
    from ._2180 import AxialHoleJournalBearing
    from ._2181 import CircumferentialFeedJournalBearing
    from ._2182 import CylindricalHousingJournalBearing
    from ._2183 import MachineryEncasedJournalBearing
    from ._2184 import PadFluidFilmBearing
    from ._2185 import PedestalJournalBearing
    from ._2186 import PlainGreaseFilledJournalBearing
    from ._2187 import PlainGreaseFilledJournalBearingHousingType
    from ._2188 import PlainJournalBearing
    from ._2189 import PlainJournalHousing
    from ._2190 import PlainOilFedJournalBearing
    from ._2191 import TiltingPadJournalBearing
    from ._2192 import TiltingPadThrustBearing
else:
    import_structure = {
        "_2178": ["AxialFeedJournalBearing"],
        "_2179": ["AxialGrooveJournalBearing"],
        "_2180": ["AxialHoleJournalBearing"],
        "_2181": ["CircumferentialFeedJournalBearing"],
        "_2182": ["CylindricalHousingJournalBearing"],
        "_2183": ["MachineryEncasedJournalBearing"],
        "_2184": ["PadFluidFilmBearing"],
        "_2185": ["PedestalJournalBearing"],
        "_2186": ["PlainGreaseFilledJournalBearing"],
        "_2187": ["PlainGreaseFilledJournalBearingHousingType"],
        "_2188": ["PlainJournalBearing"],
        "_2189": ["PlainJournalHousing"],
        "_2190": ["PlainOilFedJournalBearing"],
        "_2191": ["TiltingPadJournalBearing"],
        "_2192": ["TiltingPadThrustBearing"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AxialFeedJournalBearing",
    "AxialGrooveJournalBearing",
    "AxialHoleJournalBearing",
    "CircumferentialFeedJournalBearing",
    "CylindricalHousingJournalBearing",
    "MachineryEncasedJournalBearing",
    "PadFluidFilmBearing",
    "PedestalJournalBearing",
    "PlainGreaseFilledJournalBearing",
    "PlainGreaseFilledJournalBearingHousingType",
    "PlainJournalBearing",
    "PlainJournalHousing",
    "PlainOilFedJournalBearing",
    "TiltingPadJournalBearing",
    "TiltingPadThrustBearing",
)
