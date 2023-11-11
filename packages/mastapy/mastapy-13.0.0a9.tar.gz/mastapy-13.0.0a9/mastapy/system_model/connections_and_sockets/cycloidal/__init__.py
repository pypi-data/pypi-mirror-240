"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2330 import CycloidalDiscAxialLeftSocket
    from ._2331 import CycloidalDiscAxialRightSocket
    from ._2332 import CycloidalDiscCentralBearingConnection
    from ._2333 import CycloidalDiscInnerSocket
    from ._2334 import CycloidalDiscOuterSocket
    from ._2335 import CycloidalDiscPlanetaryBearingConnection
    from ._2336 import CycloidalDiscPlanetaryBearingSocket
    from ._2337 import RingPinsSocket
    from ._2338 import RingPinsToDiscConnection
else:
    import_structure = {
        "_2330": ["CycloidalDiscAxialLeftSocket"],
        "_2331": ["CycloidalDiscAxialRightSocket"],
        "_2332": ["CycloidalDiscCentralBearingConnection"],
        "_2333": ["CycloidalDiscInnerSocket"],
        "_2334": ["CycloidalDiscOuterSocket"],
        "_2335": ["CycloidalDiscPlanetaryBearingConnection"],
        "_2336": ["CycloidalDiscPlanetaryBearingSocket"],
        "_2337": ["RingPinsSocket"],
        "_2338": ["RingPinsToDiscConnection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CycloidalDiscAxialLeftSocket",
    "CycloidalDiscAxialRightSocket",
    "CycloidalDiscCentralBearingConnection",
    "CycloidalDiscInnerSocket",
    "CycloidalDiscOuterSocket",
    "CycloidalDiscPlanetaryBearingConnection",
    "CycloidalDiscPlanetaryBearingSocket",
    "RingPinsSocket",
    "RingPinsToDiscConnection",
)
