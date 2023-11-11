"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2352 import AlignConnectedComponentOptions
    from ._2353 import AlignmentMethod
    from ._2354 import AlignmentMethodForRaceBearing
    from ._2355 import AlignmentUsingAxialNodePositions
    from ._2356 import AngleSource
    from ._2357 import BaseFEWithSelection
    from ._2358 import BatchOperations
    from ._2359 import BearingNodeAlignmentOption
    from ._2360 import BearingNodeOption
    from ._2361 import BearingRaceNodeLink
    from ._2362 import BearingRacePosition
    from ._2363 import ComponentOrientationOption
    from ._2364 import ContactPairWithSelection
    from ._2365 import CoordinateSystemWithSelection
    from ._2366 import CreateConnectedComponentOptions
    from ._2367 import DegreeOfFreedomBoundaryCondition
    from ._2368 import DegreeOfFreedomBoundaryConditionAngular
    from ._2369 import DegreeOfFreedomBoundaryConditionLinear
    from ._2370 import ElectricMachineDataSet
    from ._2371 import ElectricMachineDynamicLoadData
    from ._2372 import ElementFaceGroupWithSelection
    from ._2373 import ElementPropertiesWithSelection
    from ._2374 import FEEntityGroupWithSelection
    from ._2375 import FEExportSettings
    from ._2376 import FEPartDRIVASurfaceSelection
    from ._2377 import FEPartWithBatchOptions
    from ._2378 import FEStiffnessGeometry
    from ._2379 import FEStiffnessTester
    from ._2380 import FESubstructure
    from ._2381 import FESubstructureExportOptions
    from ._2382 import FESubstructureNode
    from ._2383 import FESubstructureNodeModeShape
    from ._2384 import FESubstructureNodeModeShapes
    from ._2385 import FESubstructureType
    from ._2386 import FESubstructureWithBatchOptions
    from ._2387 import FESubstructureWithSelection
    from ._2388 import FESubstructureWithSelectionComponents
    from ._2389 import FESubstructureWithSelectionForHarmonicAnalysis
    from ._2390 import FESubstructureWithSelectionForModalAnalysis
    from ._2391 import FESubstructureWithSelectionForStaticAnalysis
    from ._2392 import GearMeshingOptions
    from ._2393 import IndependentMASTACreatedCondensationNode
    from ._2394 import LinkComponentAxialPositionErrorReporter
    from ._2395 import LinkNodeSource
    from ._2396 import MaterialPropertiesWithSelection
    from ._2397 import NodeBoundaryConditionStaticAnalysis
    from ._2398 import NodeGroupWithSelection
    from ._2399 import NodeSelectionDepthOption
    from ._2400 import OptionsWhenExternalFEFileAlreadyExists
    from ._2401 import PerLinkExportOptions
    from ._2402 import PerNodeExportOptions
    from ._2403 import RaceBearingFE
    from ._2404 import RaceBearingFESystemDeflection
    from ._2405 import RaceBearingFEWithSelection
    from ._2406 import ReplacedShaftSelectionHelper
    from ._2407 import SystemDeflectionFEExportOptions
    from ._2408 import ThermalExpansionOption
else:
    import_structure = {
        "_2352": ["AlignConnectedComponentOptions"],
        "_2353": ["AlignmentMethod"],
        "_2354": ["AlignmentMethodForRaceBearing"],
        "_2355": ["AlignmentUsingAxialNodePositions"],
        "_2356": ["AngleSource"],
        "_2357": ["BaseFEWithSelection"],
        "_2358": ["BatchOperations"],
        "_2359": ["BearingNodeAlignmentOption"],
        "_2360": ["BearingNodeOption"],
        "_2361": ["BearingRaceNodeLink"],
        "_2362": ["BearingRacePosition"],
        "_2363": ["ComponentOrientationOption"],
        "_2364": ["ContactPairWithSelection"],
        "_2365": ["CoordinateSystemWithSelection"],
        "_2366": ["CreateConnectedComponentOptions"],
        "_2367": ["DegreeOfFreedomBoundaryCondition"],
        "_2368": ["DegreeOfFreedomBoundaryConditionAngular"],
        "_2369": ["DegreeOfFreedomBoundaryConditionLinear"],
        "_2370": ["ElectricMachineDataSet"],
        "_2371": ["ElectricMachineDynamicLoadData"],
        "_2372": ["ElementFaceGroupWithSelection"],
        "_2373": ["ElementPropertiesWithSelection"],
        "_2374": ["FEEntityGroupWithSelection"],
        "_2375": ["FEExportSettings"],
        "_2376": ["FEPartDRIVASurfaceSelection"],
        "_2377": ["FEPartWithBatchOptions"],
        "_2378": ["FEStiffnessGeometry"],
        "_2379": ["FEStiffnessTester"],
        "_2380": ["FESubstructure"],
        "_2381": ["FESubstructureExportOptions"],
        "_2382": ["FESubstructureNode"],
        "_2383": ["FESubstructureNodeModeShape"],
        "_2384": ["FESubstructureNodeModeShapes"],
        "_2385": ["FESubstructureType"],
        "_2386": ["FESubstructureWithBatchOptions"],
        "_2387": ["FESubstructureWithSelection"],
        "_2388": ["FESubstructureWithSelectionComponents"],
        "_2389": ["FESubstructureWithSelectionForHarmonicAnalysis"],
        "_2390": ["FESubstructureWithSelectionForModalAnalysis"],
        "_2391": ["FESubstructureWithSelectionForStaticAnalysis"],
        "_2392": ["GearMeshingOptions"],
        "_2393": ["IndependentMASTACreatedCondensationNode"],
        "_2394": ["LinkComponentAxialPositionErrorReporter"],
        "_2395": ["LinkNodeSource"],
        "_2396": ["MaterialPropertiesWithSelection"],
        "_2397": ["NodeBoundaryConditionStaticAnalysis"],
        "_2398": ["NodeGroupWithSelection"],
        "_2399": ["NodeSelectionDepthOption"],
        "_2400": ["OptionsWhenExternalFEFileAlreadyExists"],
        "_2401": ["PerLinkExportOptions"],
        "_2402": ["PerNodeExportOptions"],
        "_2403": ["RaceBearingFE"],
        "_2404": ["RaceBearingFESystemDeflection"],
        "_2405": ["RaceBearingFEWithSelection"],
        "_2406": ["ReplacedShaftSelectionHelper"],
        "_2407": ["SystemDeflectionFEExportOptions"],
        "_2408": ["ThermalExpansionOption"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AlignConnectedComponentOptions",
    "AlignmentMethod",
    "AlignmentMethodForRaceBearing",
    "AlignmentUsingAxialNodePositions",
    "AngleSource",
    "BaseFEWithSelection",
    "BatchOperations",
    "BearingNodeAlignmentOption",
    "BearingNodeOption",
    "BearingRaceNodeLink",
    "BearingRacePosition",
    "ComponentOrientationOption",
    "ContactPairWithSelection",
    "CoordinateSystemWithSelection",
    "CreateConnectedComponentOptions",
    "DegreeOfFreedomBoundaryCondition",
    "DegreeOfFreedomBoundaryConditionAngular",
    "DegreeOfFreedomBoundaryConditionLinear",
    "ElectricMachineDataSet",
    "ElectricMachineDynamicLoadData",
    "ElementFaceGroupWithSelection",
    "ElementPropertiesWithSelection",
    "FEEntityGroupWithSelection",
    "FEExportSettings",
    "FEPartDRIVASurfaceSelection",
    "FEPartWithBatchOptions",
    "FEStiffnessGeometry",
    "FEStiffnessTester",
    "FESubstructure",
    "FESubstructureExportOptions",
    "FESubstructureNode",
    "FESubstructureNodeModeShape",
    "FESubstructureNodeModeShapes",
    "FESubstructureType",
    "FESubstructureWithBatchOptions",
    "FESubstructureWithSelection",
    "FESubstructureWithSelectionComponents",
    "FESubstructureWithSelectionForHarmonicAnalysis",
    "FESubstructureWithSelectionForModalAnalysis",
    "FESubstructureWithSelectionForStaticAnalysis",
    "GearMeshingOptions",
    "IndependentMASTACreatedCondensationNode",
    "LinkComponentAxialPositionErrorReporter",
    "LinkNodeSource",
    "MaterialPropertiesWithSelection",
    "NodeBoundaryConditionStaticAnalysis",
    "NodeGroupWithSelection",
    "NodeSelectionDepthOption",
    "OptionsWhenExternalFEFileAlreadyExists",
    "PerLinkExportOptions",
    "PerNodeExportOptions",
    "RaceBearingFE",
    "RaceBearingFESystemDeflection",
    "RaceBearingFEWithSelection",
    "ReplacedShaftSelectionHelper",
    "SystemDeflectionFEExportOptions",
    "ThermalExpansionOption",
)
