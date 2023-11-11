"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1241 import AbstractStator
    from ._1242 import AbstractToothAndSlot
    from ._1243 import AirGapPartition
    from ._1244 import CADConductor
    from ._1245 import CADElectricMachineDetail
    from ._1246 import CADMagnetsForLayer
    from ._1247 import CADRotor
    from ._1248 import CADStator
    from ._1249 import CADToothAndSlot
    from ._1250 import Coil
    from ._1251 import CoilPositionInSlot
    from ._1252 import CoolingDuctLayerSpecification
    from ._1253 import CoolingDuctShape
    from ._1254 import CoreLossBuildFactorSpecificationMethod
    from ._1255 import CoreLossCoefficients
    from ._1256 import DoubleLayerWindingSlotPositions
    from ._1257 import DQAxisConvention
    from ._1258 import Eccentricity
    from ._1259 import ElectricMachineDetail
    from ._1260 import ElectricMachineDetailInitialInformation
    from ._1261 import ElectricMachineMechanicalAnalysisMeshingOptions
    from ._1262 import ElectricMachineMeshingOptions
    from ._1263 import ElectricMachineMeshingOptionsBase
    from ._1264 import ElectricMachineSetup
    from ._1265 import ElectricMachineType
    from ._1266 import FillFactorSpecificationMethod
    from ._1267 import FluxBarrierOrWeb
    from ._1268 import FluxBarrierStyle
    from ._1269 import HairpinConductor
    from ._1270 import HarmonicLoadDataControlExcitationOptionForElectricMachineMode
    from ._1271 import IndividualConductorSpecificationSource
    from ._1272 import InteriorPermanentMagnetAndSynchronousReluctanceRotor
    from ._1273 import InteriorPermanentMagnetMachine
    from ._1274 import IronLossCoefficientSpecificationMethod
    from ._1275 import MagnetClearance
    from ._1276 import MagnetConfiguration
    from ._1277 import MagnetDesign
    from ._1278 import MagnetForLayer
    from ._1279 import MagnetMaterial
    from ._1280 import MagnetMaterialDatabase
    from ._1281 import MotorRotorSideFaceDetail
    from ._1282 import NonCADElectricMachineDetail
    from ._1283 import NotchShape
    from ._1284 import NotchSpecification
    from ._1285 import PermanentMagnetAssistedSynchronousReluctanceMachine
    from ._1286 import PermanentMagnetRotor
    from ._1287 import Phase
    from ._1288 import RegionID
    from ._1289 import Rotor
    from ._1290 import RotorInternalLayerSpecification
    from ._1291 import RotorSkewSlice
    from ._1292 import RotorType
    from ._1293 import SingleOrDoubleLayerWindings
    from ._1294 import SlotSectionDetail
    from ._1295 import Stator
    from ._1296 import StatorCutOutSpecification
    from ._1297 import StatorRotorMaterial
    from ._1298 import StatorRotorMaterialDatabase
    from ._1299 import SurfacePermanentMagnetMachine
    from ._1300 import SurfacePermanentMagnetRotor
    from ._1301 import SynchronousReluctanceMachine
    from ._1302 import ToothAndSlot
    from ._1303 import ToothSlotStyle
    from ._1304 import ToothTaperSpecification
    from ._1305 import TwoDimensionalFEModelForAnalysis
    from ._1306 import UShapedLayerSpecification
    from ._1307 import VShapedMagnetLayerSpecification
    from ._1308 import WindingConductor
    from ._1309 import WindingConnection
    from ._1310 import WindingMaterial
    from ._1311 import WindingMaterialDatabase
    from ._1312 import Windings
    from ._1313 import WindingsViewer
    from ._1314 import WindingType
    from ._1315 import WireSizeSpecificationMethod
    from ._1316 import WoundFieldSynchronousMachine
else:
    import_structure = {
        "_1241": ["AbstractStator"],
        "_1242": ["AbstractToothAndSlot"],
        "_1243": ["AirGapPartition"],
        "_1244": ["CADConductor"],
        "_1245": ["CADElectricMachineDetail"],
        "_1246": ["CADMagnetsForLayer"],
        "_1247": ["CADRotor"],
        "_1248": ["CADStator"],
        "_1249": ["CADToothAndSlot"],
        "_1250": ["Coil"],
        "_1251": ["CoilPositionInSlot"],
        "_1252": ["CoolingDuctLayerSpecification"],
        "_1253": ["CoolingDuctShape"],
        "_1254": ["CoreLossBuildFactorSpecificationMethod"],
        "_1255": ["CoreLossCoefficients"],
        "_1256": ["DoubleLayerWindingSlotPositions"],
        "_1257": ["DQAxisConvention"],
        "_1258": ["Eccentricity"],
        "_1259": ["ElectricMachineDetail"],
        "_1260": ["ElectricMachineDetailInitialInformation"],
        "_1261": ["ElectricMachineMechanicalAnalysisMeshingOptions"],
        "_1262": ["ElectricMachineMeshingOptions"],
        "_1263": ["ElectricMachineMeshingOptionsBase"],
        "_1264": ["ElectricMachineSetup"],
        "_1265": ["ElectricMachineType"],
        "_1266": ["FillFactorSpecificationMethod"],
        "_1267": ["FluxBarrierOrWeb"],
        "_1268": ["FluxBarrierStyle"],
        "_1269": ["HairpinConductor"],
        "_1270": ["HarmonicLoadDataControlExcitationOptionForElectricMachineMode"],
        "_1271": ["IndividualConductorSpecificationSource"],
        "_1272": ["InteriorPermanentMagnetAndSynchronousReluctanceRotor"],
        "_1273": ["InteriorPermanentMagnetMachine"],
        "_1274": ["IronLossCoefficientSpecificationMethod"],
        "_1275": ["MagnetClearance"],
        "_1276": ["MagnetConfiguration"],
        "_1277": ["MagnetDesign"],
        "_1278": ["MagnetForLayer"],
        "_1279": ["MagnetMaterial"],
        "_1280": ["MagnetMaterialDatabase"],
        "_1281": ["MotorRotorSideFaceDetail"],
        "_1282": ["NonCADElectricMachineDetail"],
        "_1283": ["NotchShape"],
        "_1284": ["NotchSpecification"],
        "_1285": ["PermanentMagnetAssistedSynchronousReluctanceMachine"],
        "_1286": ["PermanentMagnetRotor"],
        "_1287": ["Phase"],
        "_1288": ["RegionID"],
        "_1289": ["Rotor"],
        "_1290": ["RotorInternalLayerSpecification"],
        "_1291": ["RotorSkewSlice"],
        "_1292": ["RotorType"],
        "_1293": ["SingleOrDoubleLayerWindings"],
        "_1294": ["SlotSectionDetail"],
        "_1295": ["Stator"],
        "_1296": ["StatorCutOutSpecification"],
        "_1297": ["StatorRotorMaterial"],
        "_1298": ["StatorRotorMaterialDatabase"],
        "_1299": ["SurfacePermanentMagnetMachine"],
        "_1300": ["SurfacePermanentMagnetRotor"],
        "_1301": ["SynchronousReluctanceMachine"],
        "_1302": ["ToothAndSlot"],
        "_1303": ["ToothSlotStyle"],
        "_1304": ["ToothTaperSpecification"],
        "_1305": ["TwoDimensionalFEModelForAnalysis"],
        "_1306": ["UShapedLayerSpecification"],
        "_1307": ["VShapedMagnetLayerSpecification"],
        "_1308": ["WindingConductor"],
        "_1309": ["WindingConnection"],
        "_1310": ["WindingMaterial"],
        "_1311": ["WindingMaterialDatabase"],
        "_1312": ["Windings"],
        "_1313": ["WindingsViewer"],
        "_1314": ["WindingType"],
        "_1315": ["WireSizeSpecificationMethod"],
        "_1316": ["WoundFieldSynchronousMachine"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractStator",
    "AbstractToothAndSlot",
    "AirGapPartition",
    "CADConductor",
    "CADElectricMachineDetail",
    "CADMagnetsForLayer",
    "CADRotor",
    "CADStator",
    "CADToothAndSlot",
    "Coil",
    "CoilPositionInSlot",
    "CoolingDuctLayerSpecification",
    "CoolingDuctShape",
    "CoreLossBuildFactorSpecificationMethod",
    "CoreLossCoefficients",
    "DoubleLayerWindingSlotPositions",
    "DQAxisConvention",
    "Eccentricity",
    "ElectricMachineDetail",
    "ElectricMachineDetailInitialInformation",
    "ElectricMachineMechanicalAnalysisMeshingOptions",
    "ElectricMachineMeshingOptions",
    "ElectricMachineMeshingOptionsBase",
    "ElectricMachineSetup",
    "ElectricMachineType",
    "FillFactorSpecificationMethod",
    "FluxBarrierOrWeb",
    "FluxBarrierStyle",
    "HairpinConductor",
    "HarmonicLoadDataControlExcitationOptionForElectricMachineMode",
    "IndividualConductorSpecificationSource",
    "InteriorPermanentMagnetAndSynchronousReluctanceRotor",
    "InteriorPermanentMagnetMachine",
    "IronLossCoefficientSpecificationMethod",
    "MagnetClearance",
    "MagnetConfiguration",
    "MagnetDesign",
    "MagnetForLayer",
    "MagnetMaterial",
    "MagnetMaterialDatabase",
    "MotorRotorSideFaceDetail",
    "NonCADElectricMachineDetail",
    "NotchShape",
    "NotchSpecification",
    "PermanentMagnetAssistedSynchronousReluctanceMachine",
    "PermanentMagnetRotor",
    "Phase",
    "RegionID",
    "Rotor",
    "RotorInternalLayerSpecification",
    "RotorSkewSlice",
    "RotorType",
    "SingleOrDoubleLayerWindings",
    "SlotSectionDetail",
    "Stator",
    "StatorCutOutSpecification",
    "StatorRotorMaterial",
    "StatorRotorMaterialDatabase",
    "SurfacePermanentMagnetMachine",
    "SurfacePermanentMagnetRotor",
    "SynchronousReluctanceMachine",
    "ToothAndSlot",
    "ToothSlotStyle",
    "ToothTaperSpecification",
    "TwoDimensionalFEModelForAnalysis",
    "UShapedLayerSpecification",
    "VShapedMagnetLayerSpecification",
    "WindingConductor",
    "WindingConnection",
    "WindingMaterial",
    "WindingMaterialDatabase",
    "Windings",
    "WindingsViewer",
    "WindingType",
    "WireSizeSpecificationMethod",
    "WoundFieldSynchronousMachine",
)
