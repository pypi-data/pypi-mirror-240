"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2552 import BoostPressureInputOptions
    from ._2553 import InputPowerInputOptions
    from ._2554 import PressureRatioInputOptions
    from ._2555 import RotorSetDataInputFileOptions
    from ._2556 import RotorSetMeasuredPoint
    from ._2557 import RotorSpeedInputOptions
    from ._2558 import SuperchargerMap
    from ._2559 import SuperchargerMaps
    from ._2560 import SuperchargerRotorSet
    from ._2561 import SuperchargerRotorSetDatabase
    from ._2562 import YVariableForImportedData
else:
    import_structure = {
        "_2552": ["BoostPressureInputOptions"],
        "_2553": ["InputPowerInputOptions"],
        "_2554": ["PressureRatioInputOptions"],
        "_2555": ["RotorSetDataInputFileOptions"],
        "_2556": ["RotorSetMeasuredPoint"],
        "_2557": ["RotorSpeedInputOptions"],
        "_2558": ["SuperchargerMap"],
        "_2559": ["SuperchargerMaps"],
        "_2560": ["SuperchargerRotorSet"],
        "_2561": ["SuperchargerRotorSetDatabase"],
        "_2562": ["YVariableForImportedData"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BoostPressureInputOptions",
    "InputPowerInputOptions",
    "PressureRatioInputOptions",
    "RotorSetDataInputFileOptions",
    "RotorSetMeasuredPoint",
    "RotorSpeedInputOptions",
    "SuperchargerMap",
    "SuperchargerMaps",
    "SuperchargerRotorSet",
    "SuperchargerRotorSetDatabase",
    "YVariableForImportedData",
)
