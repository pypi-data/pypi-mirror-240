"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2098 import BallISO2812007Results
    from ._2099 import BallISOTS162812008Results
    from ._2100 import ISO2812007Results
    from ._2101 import ISO762006Results
    from ._2102 import ISOResults
    from ._2103 import ISOTS162812008Results
    from ._2104 import RollerISO2812007Results
    from ._2105 import RollerISOTS162812008Results
    from ._2106 import StressConcentrationMethod
else:
    import_structure = {
        "_2098": ["BallISO2812007Results"],
        "_2099": ["BallISOTS162812008Results"],
        "_2100": ["ISO2812007Results"],
        "_2101": ["ISO762006Results"],
        "_2102": ["ISOResults"],
        "_2103": ["ISOTS162812008Results"],
        "_2104": ["RollerISO2812007Results"],
        "_2105": ["RollerISOTS162812008Results"],
        "_2106": ["StressConcentrationMethod"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BallISO2812007Results",
    "BallISOTS162812008Results",
    "ISO2812007Results",
    "ISO762006Results",
    "ISOResults",
    "ISOTS162812008Results",
    "RollerISO2812007Results",
    "RollerISOTS162812008Results",
    "StressConcentrationMethod",
)
