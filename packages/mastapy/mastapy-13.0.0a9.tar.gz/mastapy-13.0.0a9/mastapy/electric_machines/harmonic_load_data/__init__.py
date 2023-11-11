"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1374 import ElectricMachineHarmonicLoadDataBase
    from ._1375 import ForceDisplayOption
    from ._1376 import HarmonicLoadDataBase
    from ._1377 import HarmonicLoadDataControlExcitationOptionBase
    from ._1378 import HarmonicLoadDataType
    from ._1379 import SpeedDependentHarmonicLoadData
    from ._1380 import StatorToothInterpolator
    from ._1381 import StatorToothLoadInterpolator
    from ._1382 import StatorToothMomentInterpolator
else:
    import_structure = {
        "_1374": ["ElectricMachineHarmonicLoadDataBase"],
        "_1375": ["ForceDisplayOption"],
        "_1376": ["HarmonicLoadDataBase"],
        "_1377": ["HarmonicLoadDataControlExcitationOptionBase"],
        "_1378": ["HarmonicLoadDataType"],
        "_1379": ["SpeedDependentHarmonicLoadData"],
        "_1380": ["StatorToothInterpolator"],
        "_1381": ["StatorToothLoadInterpolator"],
        "_1382": ["StatorToothMomentInterpolator"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ElectricMachineHarmonicLoadDataBase",
    "ForceDisplayOption",
    "HarmonicLoadDataBase",
    "HarmonicLoadDataControlExcitationOptionBase",
    "HarmonicLoadDataType",
    "SpeedDependentHarmonicLoadData",
    "StatorToothInterpolator",
    "StatorToothLoadInterpolator",
    "StatorToothMomentInterpolator",
)
