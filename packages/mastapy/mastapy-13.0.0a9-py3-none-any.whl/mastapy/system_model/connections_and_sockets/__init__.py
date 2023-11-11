"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2262 import AbstractShaftToMountableComponentConnection
    from ._2263 import BearingInnerSocket
    from ._2264 import BearingOuterSocket
    from ._2265 import BeltConnection
    from ._2266 import CoaxialConnection
    from ._2267 import ComponentConnection
    from ._2268 import ComponentMeasurer
    from ._2269 import Connection
    from ._2270 import CVTBeltConnection
    from ._2271 import CVTPulleySocket
    from ._2272 import CylindricalComponentConnection
    from ._2273 import CylindricalSocket
    from ._2274 import DatumMeasurement
    from ._2275 import ElectricMachineStatorSocket
    from ._2276 import InnerShaftSocket
    from ._2277 import InnerShaftSocketBase
    from ._2278 import InterMountableComponentConnection
    from ._2279 import MountableComponentInnerSocket
    from ._2280 import MountableComponentOuterSocket
    from ._2281 import MountableComponentSocket
    from ._2282 import OuterShaftSocket
    from ._2283 import OuterShaftSocketBase
    from ._2284 import PlanetaryConnection
    from ._2285 import PlanetarySocket
    from ._2286 import PlanetarySocketBase
    from ._2287 import PulleySocket
    from ._2288 import RealignmentResult
    from ._2289 import RollingRingConnection
    from ._2290 import RollingRingSocket
    from ._2291 import ShaftSocket
    from ._2292 import ShaftToMountableComponentConnection
    from ._2293 import Socket
    from ._2294 import SocketConnectionOptions
    from ._2295 import SocketConnectionSelection
else:
    import_structure = {
        "_2262": ["AbstractShaftToMountableComponentConnection"],
        "_2263": ["BearingInnerSocket"],
        "_2264": ["BearingOuterSocket"],
        "_2265": ["BeltConnection"],
        "_2266": ["CoaxialConnection"],
        "_2267": ["ComponentConnection"],
        "_2268": ["ComponentMeasurer"],
        "_2269": ["Connection"],
        "_2270": ["CVTBeltConnection"],
        "_2271": ["CVTPulleySocket"],
        "_2272": ["CylindricalComponentConnection"],
        "_2273": ["CylindricalSocket"],
        "_2274": ["DatumMeasurement"],
        "_2275": ["ElectricMachineStatorSocket"],
        "_2276": ["InnerShaftSocket"],
        "_2277": ["InnerShaftSocketBase"],
        "_2278": ["InterMountableComponentConnection"],
        "_2279": ["MountableComponentInnerSocket"],
        "_2280": ["MountableComponentOuterSocket"],
        "_2281": ["MountableComponentSocket"],
        "_2282": ["OuterShaftSocket"],
        "_2283": ["OuterShaftSocketBase"],
        "_2284": ["PlanetaryConnection"],
        "_2285": ["PlanetarySocket"],
        "_2286": ["PlanetarySocketBase"],
        "_2287": ["PulleySocket"],
        "_2288": ["RealignmentResult"],
        "_2289": ["RollingRingConnection"],
        "_2290": ["RollingRingSocket"],
        "_2291": ["ShaftSocket"],
        "_2292": ["ShaftToMountableComponentConnection"],
        "_2293": ["Socket"],
        "_2294": ["SocketConnectionOptions"],
        "_2295": ["SocketConnectionSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractShaftToMountableComponentConnection",
    "BearingInnerSocket",
    "BearingOuterSocket",
    "BeltConnection",
    "CoaxialConnection",
    "ComponentConnection",
    "ComponentMeasurer",
    "Connection",
    "CVTBeltConnection",
    "CVTPulleySocket",
    "CylindricalComponentConnection",
    "CylindricalSocket",
    "DatumMeasurement",
    "ElectricMachineStatorSocket",
    "InnerShaftSocket",
    "InnerShaftSocketBase",
    "InterMountableComponentConnection",
    "MountableComponentInnerSocket",
    "MountableComponentOuterSocket",
    "MountableComponentSocket",
    "OuterShaftSocket",
    "OuterShaftSocketBase",
    "PlanetaryConnection",
    "PlanetarySocket",
    "PlanetarySocketBase",
    "PulleySocket",
    "RealignmentResult",
    "RollingRingConnection",
    "RollingRingSocket",
    "ShaftSocket",
    "ShaftToMountableComponentConnection",
    "Socket",
    "SocketConnectionOptions",
    "SocketConnectionSelection",
)
