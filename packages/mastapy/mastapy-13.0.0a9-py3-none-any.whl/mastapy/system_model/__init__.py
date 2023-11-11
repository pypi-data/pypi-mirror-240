"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2197 import Design
    from ._2198 import ComponentDampingOption
    from ._2199 import ConceptCouplingSpeedRatioSpecificationMethod
    from ._2200 import DesignEntity
    from ._2201 import DesignEntityId
    from ._2202 import DesignSettings
    from ._2203 import DutyCycleImporter
    from ._2204 import DutyCycleImporterDesignEntityMatch
    from ._2205 import ElectricMachineGroup
    from ._2206 import ExternalFullFELoader
    from ._2207 import HypoidWindUpRemovalMethod
    from ._2208 import IncludeDutyCycleOption
    from ._2209 import MASTASettings
    from ._2210 import MemorySummary
    from ._2211 import MeshStiffnessModel
    from ._2212 import PlanetPinManufacturingErrorsCoordinateSystem
    from ._2213 import PowerLoadDragTorqueSpecificationMethod
    from ._2214 import PowerLoadInputTorqueSpecificationMethod
    from ._2215 import PowerLoadPIDControlSpeedInputType
    from ._2216 import PowerLoadType
    from ._2217 import RelativeComponentAlignment
    from ._2218 import RelativeOffsetOption
    from ._2219 import SystemReporting
    from ._2220 import ThermalExpansionOptionForGroundedNodes
    from ._2221 import TransmissionTemperatureSet
else:
    import_structure = {
        "_2197": ["Design"],
        "_2198": ["ComponentDampingOption"],
        "_2199": ["ConceptCouplingSpeedRatioSpecificationMethod"],
        "_2200": ["DesignEntity"],
        "_2201": ["DesignEntityId"],
        "_2202": ["DesignSettings"],
        "_2203": ["DutyCycleImporter"],
        "_2204": ["DutyCycleImporterDesignEntityMatch"],
        "_2205": ["ElectricMachineGroup"],
        "_2206": ["ExternalFullFELoader"],
        "_2207": ["HypoidWindUpRemovalMethod"],
        "_2208": ["IncludeDutyCycleOption"],
        "_2209": ["MASTASettings"],
        "_2210": ["MemorySummary"],
        "_2211": ["MeshStiffnessModel"],
        "_2212": ["PlanetPinManufacturingErrorsCoordinateSystem"],
        "_2213": ["PowerLoadDragTorqueSpecificationMethod"],
        "_2214": ["PowerLoadInputTorqueSpecificationMethod"],
        "_2215": ["PowerLoadPIDControlSpeedInputType"],
        "_2216": ["PowerLoadType"],
        "_2217": ["RelativeComponentAlignment"],
        "_2218": ["RelativeOffsetOption"],
        "_2219": ["SystemReporting"],
        "_2220": ["ThermalExpansionOptionForGroundedNodes"],
        "_2221": ["TransmissionTemperatureSet"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Design",
    "ComponentDampingOption",
    "ConceptCouplingSpeedRatioSpecificationMethod",
    "DesignEntity",
    "DesignEntityId",
    "DesignSettings",
    "DutyCycleImporter",
    "DutyCycleImporterDesignEntityMatch",
    "ElectricMachineGroup",
    "ExternalFullFELoader",
    "HypoidWindUpRemovalMethod",
    "IncludeDutyCycleOption",
    "MASTASettings",
    "MemorySummary",
    "MeshStiffnessModel",
    "PlanetPinManufacturingErrorsCoordinateSystem",
    "PowerLoadDragTorqueSpecificationMethod",
    "PowerLoadInputTorqueSpecificationMethod",
    "PowerLoadPIDControlSpeedInputType",
    "PowerLoadType",
    "RelativeComponentAlignment",
    "RelativeOffsetOption",
    "SystemReporting",
    "ThermalExpansionOptionForGroundedNodes",
    "TransmissionTemperatureSet",
)
