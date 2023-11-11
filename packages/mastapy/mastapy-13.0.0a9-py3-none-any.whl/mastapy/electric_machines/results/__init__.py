"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1317 import DynamicForceResults
    from ._1318 import EfficiencyResults
    from ._1319 import ElectricMachineDQModel
    from ._1320 import ElectricMachineMechanicalResults
    from ._1321 import ElectricMachineMechanicalResultsViewable
    from ._1322 import ElectricMachineResults
    from ._1323 import ElectricMachineResultsForConductorTurn
    from ._1324 import ElectricMachineResultsForConductorTurnAtTimeStep
    from ._1325 import ElectricMachineResultsForLineToLine
    from ._1326 import ElectricMachineResultsForOpenCircuitAndOnLoad
    from ._1327 import ElectricMachineResultsForPhase
    from ._1328 import ElectricMachineResultsForPhaseAtTimeStep
    from ._1329 import ElectricMachineResultsForStatorToothAtTimeStep
    from ._1330 import ElectricMachineResultsLineToLineAtTimeStep
    from ._1331 import ElectricMachineResultsTimeStep
    from ._1332 import ElectricMachineResultsTimeStepAtLocation
    from ._1333 import ElectricMachineResultsViewable
    from ._1334 import ElectricMachineForceViewOptions
    from ._1336 import LinearDQModel
    from ._1337 import MaximumTorqueResultsPoints
    from ._1338 import NonLinearDQModel
    from ._1339 import NonLinearDQModelGeneratorSettings
    from ._1340 import OnLoadElectricMachineResults
    from ._1341 import OpenCircuitElectricMachineResults
else:
    import_structure = {
        "_1317": ["DynamicForceResults"],
        "_1318": ["EfficiencyResults"],
        "_1319": ["ElectricMachineDQModel"],
        "_1320": ["ElectricMachineMechanicalResults"],
        "_1321": ["ElectricMachineMechanicalResultsViewable"],
        "_1322": ["ElectricMachineResults"],
        "_1323": ["ElectricMachineResultsForConductorTurn"],
        "_1324": ["ElectricMachineResultsForConductorTurnAtTimeStep"],
        "_1325": ["ElectricMachineResultsForLineToLine"],
        "_1326": ["ElectricMachineResultsForOpenCircuitAndOnLoad"],
        "_1327": ["ElectricMachineResultsForPhase"],
        "_1328": ["ElectricMachineResultsForPhaseAtTimeStep"],
        "_1329": ["ElectricMachineResultsForStatorToothAtTimeStep"],
        "_1330": ["ElectricMachineResultsLineToLineAtTimeStep"],
        "_1331": ["ElectricMachineResultsTimeStep"],
        "_1332": ["ElectricMachineResultsTimeStepAtLocation"],
        "_1333": ["ElectricMachineResultsViewable"],
        "_1334": ["ElectricMachineForceViewOptions"],
        "_1336": ["LinearDQModel"],
        "_1337": ["MaximumTorqueResultsPoints"],
        "_1338": ["NonLinearDQModel"],
        "_1339": ["NonLinearDQModelGeneratorSettings"],
        "_1340": ["OnLoadElectricMachineResults"],
        "_1341": ["OpenCircuitElectricMachineResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DynamicForceResults",
    "EfficiencyResults",
    "ElectricMachineDQModel",
    "ElectricMachineMechanicalResults",
    "ElectricMachineMechanicalResultsViewable",
    "ElectricMachineResults",
    "ElectricMachineResultsForConductorTurn",
    "ElectricMachineResultsForConductorTurnAtTimeStep",
    "ElectricMachineResultsForLineToLine",
    "ElectricMachineResultsForOpenCircuitAndOnLoad",
    "ElectricMachineResultsForPhase",
    "ElectricMachineResultsForPhaseAtTimeStep",
    "ElectricMachineResultsForStatorToothAtTimeStep",
    "ElectricMachineResultsLineToLineAtTimeStep",
    "ElectricMachineResultsTimeStep",
    "ElectricMachineResultsTimeStepAtLocation",
    "ElectricMachineResultsViewable",
    "ElectricMachineForceViewOptions",
    "LinearDQModel",
    "MaximumTorqueResultsPoints",
    "NonLinearDQModel",
    "NonLinearDQModelGeneratorSettings",
    "OnLoadElectricMachineResults",
    "OpenCircuitElectricMachineResults",
)
