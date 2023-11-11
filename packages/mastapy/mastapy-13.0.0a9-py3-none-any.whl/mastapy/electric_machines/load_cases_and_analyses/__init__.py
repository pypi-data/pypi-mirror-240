"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1342 import BasicDynamicForceLoadCase
    from ._1343 import DynamicForceAnalysis
    from ._1344 import DynamicForceLoadCase
    from ._1345 import DynamicForcesOperatingPoint
    from ._1346 import EfficiencyMapAnalysis
    from ._1347 import EfficiencyMapLoadCase
    from ._1348 import ElectricMachineAnalysis
    from ._1349 import ElectricMachineBasicMechanicalLossSettings
    from ._1350 import ElectricMachineControlStrategy
    from ._1351 import ElectricMachineEfficiencyMapSettings
    from ._1352 import ElectricMachineFEAnalysis
    from ._1353 import ElectricMachineFEMechanicalAnalysis
    from ._1354 import ElectricMachineLoadCase
    from ._1355 import ElectricMachineLoadCaseBase
    from ._1356 import ElectricMachineLoadCaseGroup
    from ._1357 import ElectricMachineMechanicalLoadCase
    from ._1358 import EndWindingInductanceMethod
    from ._1359 import LeadingOrLagging
    from ._1360 import LoadCaseType
    from ._1361 import LoadCaseTypeSelector
    from ._1362 import MotoringOrGenerating
    from ._1363 import NonLinearDQModelMultipleOperatingPointsLoadCase
    from ._1364 import NumberOfStepsPerOperatingPointSpecificationMethod
    from ._1365 import OperatingPointsSpecificationMethod
    from ._1366 import SingleOperatingPointAnalysis
    from ._1367 import SlotDetailForAnalysis
    from ._1368 import SpecifyTorqueOrCurrent
    from ._1369 import SpeedPointsDistribution
    from ._1370 import SpeedTorqueCurveAnalysis
    from ._1371 import SpeedTorqueCurveLoadCase
    from ._1372 import SpeedTorqueLoadCase
    from ._1373 import Temperatures
else:
    import_structure = {
        "_1342": ["BasicDynamicForceLoadCase"],
        "_1343": ["DynamicForceAnalysis"],
        "_1344": ["DynamicForceLoadCase"],
        "_1345": ["DynamicForcesOperatingPoint"],
        "_1346": ["EfficiencyMapAnalysis"],
        "_1347": ["EfficiencyMapLoadCase"],
        "_1348": ["ElectricMachineAnalysis"],
        "_1349": ["ElectricMachineBasicMechanicalLossSettings"],
        "_1350": ["ElectricMachineControlStrategy"],
        "_1351": ["ElectricMachineEfficiencyMapSettings"],
        "_1352": ["ElectricMachineFEAnalysis"],
        "_1353": ["ElectricMachineFEMechanicalAnalysis"],
        "_1354": ["ElectricMachineLoadCase"],
        "_1355": ["ElectricMachineLoadCaseBase"],
        "_1356": ["ElectricMachineLoadCaseGroup"],
        "_1357": ["ElectricMachineMechanicalLoadCase"],
        "_1358": ["EndWindingInductanceMethod"],
        "_1359": ["LeadingOrLagging"],
        "_1360": ["LoadCaseType"],
        "_1361": ["LoadCaseTypeSelector"],
        "_1362": ["MotoringOrGenerating"],
        "_1363": ["NonLinearDQModelMultipleOperatingPointsLoadCase"],
        "_1364": ["NumberOfStepsPerOperatingPointSpecificationMethod"],
        "_1365": ["OperatingPointsSpecificationMethod"],
        "_1366": ["SingleOperatingPointAnalysis"],
        "_1367": ["SlotDetailForAnalysis"],
        "_1368": ["SpecifyTorqueOrCurrent"],
        "_1369": ["SpeedPointsDistribution"],
        "_1370": ["SpeedTorqueCurveAnalysis"],
        "_1371": ["SpeedTorqueCurveLoadCase"],
        "_1372": ["SpeedTorqueLoadCase"],
        "_1373": ["Temperatures"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BasicDynamicForceLoadCase",
    "DynamicForceAnalysis",
    "DynamicForceLoadCase",
    "DynamicForcesOperatingPoint",
    "EfficiencyMapAnalysis",
    "EfficiencyMapLoadCase",
    "ElectricMachineAnalysis",
    "ElectricMachineBasicMechanicalLossSettings",
    "ElectricMachineControlStrategy",
    "ElectricMachineEfficiencyMapSettings",
    "ElectricMachineFEAnalysis",
    "ElectricMachineFEMechanicalAnalysis",
    "ElectricMachineLoadCase",
    "ElectricMachineLoadCaseBase",
    "ElectricMachineLoadCaseGroup",
    "ElectricMachineMechanicalLoadCase",
    "EndWindingInductanceMethod",
    "LeadingOrLagging",
    "LoadCaseType",
    "LoadCaseTypeSelector",
    "MotoringOrGenerating",
    "NonLinearDQModelMultipleOperatingPointsLoadCase",
    "NumberOfStepsPerOperatingPointSpecificationMethod",
    "OperatingPointsSpecificationMethod",
    "SingleOperatingPointAnalysis",
    "SlotDetailForAnalysis",
    "SpecifyTorqueOrCurrent",
    "SpeedPointsDistribution",
    "SpeedTorqueCurveAnalysis",
    "SpeedTorqueCurveLoadCase",
    "SpeedTorqueLoadCase",
    "Temperatures",
)
