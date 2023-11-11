"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2339 import ClutchConnection
    from ._2340 import ClutchSocket
    from ._2341 import ConceptCouplingConnection
    from ._2342 import ConceptCouplingSocket
    from ._2343 import CouplingConnection
    from ._2344 import CouplingSocket
    from ._2345 import PartToPartShearCouplingConnection
    from ._2346 import PartToPartShearCouplingSocket
    from ._2347 import SpringDamperConnection
    from ._2348 import SpringDamperSocket
    from ._2349 import TorqueConverterConnection
    from ._2350 import TorqueConverterPumpSocket
    from ._2351 import TorqueConverterTurbineSocket
else:
    import_structure = {
        "_2339": ["ClutchConnection"],
        "_2340": ["ClutchSocket"],
        "_2341": ["ConceptCouplingConnection"],
        "_2342": ["ConceptCouplingSocket"],
        "_2343": ["CouplingConnection"],
        "_2344": ["CouplingSocket"],
        "_2345": ["PartToPartShearCouplingConnection"],
        "_2346": ["PartToPartShearCouplingSocket"],
        "_2347": ["SpringDamperConnection"],
        "_2348": ["SpringDamperSocket"],
        "_2349": ["TorqueConverterConnection"],
        "_2350": ["TorqueConverterPumpSocket"],
        "_2351": ["TorqueConverterTurbineSocket"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ClutchConnection",
    "ClutchSocket",
    "ConceptCouplingConnection",
    "ConceptCouplingSocket",
    "CouplingConnection",
    "CouplingSocket",
    "PartToPartShearCouplingConnection",
    "PartToPartShearCouplingSocket",
    "SpringDamperConnection",
    "SpringDamperSocket",
    "TorqueConverterConnection",
    "TorqueConverterPumpSocket",
    "TorqueConverterTurbineSocket",
)
