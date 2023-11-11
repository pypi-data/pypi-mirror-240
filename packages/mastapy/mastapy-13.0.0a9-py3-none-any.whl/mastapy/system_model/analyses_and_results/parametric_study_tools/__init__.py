"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4292 import AbstractAssemblyParametricStudyTool
    from ._4293 import AbstractShaftOrHousingParametricStudyTool
    from ._4294 import AbstractShaftParametricStudyTool
    from ._4295 import AbstractShaftToMountableComponentConnectionParametricStudyTool
    from ._4296 import AGMAGleasonConicalGearMeshParametricStudyTool
    from ._4297 import AGMAGleasonConicalGearParametricStudyTool
    from ._4298 import AGMAGleasonConicalGearSetParametricStudyTool
    from ._4299 import AssemblyParametricStudyTool
    from ._4300 import BearingParametricStudyTool
    from ._4301 import BeltConnectionParametricStudyTool
    from ._4302 import BeltDriveParametricStudyTool
    from ._4303 import BevelDifferentialGearMeshParametricStudyTool
    from ._4304 import BevelDifferentialGearParametricStudyTool
    from ._4305 import BevelDifferentialGearSetParametricStudyTool
    from ._4306 import BevelDifferentialPlanetGearParametricStudyTool
    from ._4307 import BevelDifferentialSunGearParametricStudyTool
    from ._4308 import BevelGearMeshParametricStudyTool
    from ._4309 import BevelGearParametricStudyTool
    from ._4310 import BevelGearSetParametricStudyTool
    from ._4311 import BoltedJointParametricStudyTool
    from ._4312 import BoltParametricStudyTool
    from ._4313 import ClutchConnectionParametricStudyTool
    from ._4314 import ClutchHalfParametricStudyTool
    from ._4315 import ClutchParametricStudyTool
    from ._4316 import CoaxialConnectionParametricStudyTool
    from ._4317 import ComponentParametricStudyTool
    from ._4318 import ConceptCouplingConnectionParametricStudyTool
    from ._4319 import ConceptCouplingHalfParametricStudyTool
    from ._4320 import ConceptCouplingParametricStudyTool
    from ._4321 import ConceptGearMeshParametricStudyTool
    from ._4322 import ConceptGearParametricStudyTool
    from ._4323 import ConceptGearSetParametricStudyTool
    from ._4324 import ConicalGearMeshParametricStudyTool
    from ._4325 import ConicalGearParametricStudyTool
    from ._4326 import ConicalGearSetParametricStudyTool
    from ._4327 import ConnectionParametricStudyTool
    from ._4328 import ConnectorParametricStudyTool
    from ._4329 import CouplingConnectionParametricStudyTool
    from ._4330 import CouplingHalfParametricStudyTool
    from ._4331 import CouplingParametricStudyTool
    from ._4332 import CVTBeltConnectionParametricStudyTool
    from ._4333 import CVTParametricStudyTool
    from ._4334 import CVTPulleyParametricStudyTool
    from ._4335 import CycloidalAssemblyParametricStudyTool
    from ._4336 import CycloidalDiscCentralBearingConnectionParametricStudyTool
    from ._4337 import CycloidalDiscParametricStudyTool
    from ._4338 import CycloidalDiscPlanetaryBearingConnectionParametricStudyTool
    from ._4339 import CylindricalGearMeshParametricStudyTool
    from ._4340 import CylindricalGearParametricStudyTool
    from ._4341 import CylindricalGearSetParametricStudyTool
    from ._4342 import CylindricalPlanetGearParametricStudyTool
    from ._4343 import DatumParametricStudyTool
    from ._4344 import DesignOfExperimentsVariableSetter
    from ._4345 import DoeValueSpecificationOption
    from ._4346 import DutyCycleResultsForAllComponents
    from ._4347 import DutyCycleResultsForAllGearSets
    from ._4348 import DutyCycleResultsForRootAssembly
    from ._4349 import DutyCycleResultsForSingleBearing
    from ._4350 import DutyCycleResultsForSingleShaft
    from ._4351 import ExternalCADModelParametricStudyTool
    from ._4352 import FaceGearMeshParametricStudyTool
    from ._4353 import FaceGearParametricStudyTool
    from ._4354 import FaceGearSetParametricStudyTool
    from ._4355 import FEPartParametricStudyTool
    from ._4356 import FlexiblePinAssemblyParametricStudyTool
    from ._4357 import GearMeshParametricStudyTool
    from ._4358 import GearParametricStudyTool
    from ._4359 import GearSetParametricStudyTool
    from ._4360 import GuideDxfModelParametricStudyTool
    from ._4361 import HypoidGearMeshParametricStudyTool
    from ._4362 import HypoidGearParametricStudyTool
    from ._4363 import HypoidGearSetParametricStudyTool
    from ._4364 import InterMountableComponentConnectionParametricStudyTool
    from ._4365 import KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool
    from ._4366 import KlingelnbergCycloPalloidConicalGearParametricStudyTool
    from ._4367 import KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
    from ._4368 import KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool
    from ._4369 import KlingelnbergCycloPalloidHypoidGearParametricStudyTool
    from ._4370 import KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
    from ._4371 import KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool
    from ._4372 import KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
    from ._4373 import KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
    from ._4374 import MassDiscParametricStudyTool
    from ._4375 import MeasurementComponentParametricStudyTool
    from ._4376 import MonteCarloDistribution
    from ._4377 import MountableComponentParametricStudyTool
    from ._4378 import OilSealParametricStudyTool
    from ._4379 import ParametricStudyDimension
    from ._4380 import ParametricStudyDOEResultVariable
    from ._4381 import ParametricStudyDOEResultVariableForParallelCoordinatesPlot
    from ._4382 import ParametricStudyHistogram
    from ._4383 import ParametricStudyStaticLoad
    from ._4384 import ParametricStudyTool
    from ._4385 import ParametricStudyToolOptions
    from ._4386 import ParametricStudyToolResultsForReporting
    from ._4387 import ParametricStudyToolStepResult
    from ._4388 import ParametricStudyVariable
    from ._4389 import PartParametricStudyTool
    from ._4390 import PartToPartShearCouplingConnectionParametricStudyTool
    from ._4391 import PartToPartShearCouplingHalfParametricStudyTool
    from ._4392 import PartToPartShearCouplingParametricStudyTool
    from ._4393 import PlanetaryConnectionParametricStudyTool
    from ._4394 import PlanetaryGearSetParametricStudyTool
    from ._4395 import PlanetCarrierParametricStudyTool
    from ._4396 import PointLoadParametricStudyTool
    from ._4397 import PowerLoadParametricStudyTool
    from ._4398 import PulleyParametricStudyTool
    from ._4399 import RingPinsParametricStudyTool
    from ._4400 import RingPinsToDiscConnectionParametricStudyTool
    from ._4401 import RollingRingAssemblyParametricStudyTool
    from ._4402 import RollingRingConnectionParametricStudyTool
    from ._4403 import RollingRingParametricStudyTool
    from ._4404 import RootAssemblyParametricStudyTool
    from ._4405 import ShaftHubConnectionParametricStudyTool
    from ._4406 import ShaftParametricStudyTool
    from ._4407 import ShaftToMountableComponentConnectionParametricStudyTool
    from ._4408 import SpecialisedAssemblyParametricStudyTool
    from ._4409 import SpiralBevelGearMeshParametricStudyTool
    from ._4410 import SpiralBevelGearParametricStudyTool
    from ._4411 import SpiralBevelGearSetParametricStudyTool
    from ._4412 import SpringDamperConnectionParametricStudyTool
    from ._4413 import SpringDamperHalfParametricStudyTool
    from ._4414 import SpringDamperParametricStudyTool
    from ._4415 import StraightBevelDiffGearMeshParametricStudyTool
    from ._4416 import StraightBevelDiffGearParametricStudyTool
    from ._4417 import StraightBevelDiffGearSetParametricStudyTool
    from ._4418 import StraightBevelGearMeshParametricStudyTool
    from ._4419 import StraightBevelGearParametricStudyTool
    from ._4420 import StraightBevelGearSetParametricStudyTool
    from ._4421 import StraightBevelPlanetGearParametricStudyTool
    from ._4422 import StraightBevelSunGearParametricStudyTool
    from ._4423 import SynchroniserHalfParametricStudyTool
    from ._4424 import SynchroniserParametricStudyTool
    from ._4425 import SynchroniserPartParametricStudyTool
    from ._4426 import SynchroniserSleeveParametricStudyTool
    from ._4427 import TorqueConverterConnectionParametricStudyTool
    from ._4428 import TorqueConverterParametricStudyTool
    from ._4429 import TorqueConverterPumpParametricStudyTool
    from ._4430 import TorqueConverterTurbineParametricStudyTool
    from ._4431 import UnbalancedMassParametricStudyTool
    from ._4432 import VirtualComponentParametricStudyTool
    from ._4433 import WormGearMeshParametricStudyTool
    from ._4434 import WormGearParametricStudyTool
    from ._4435 import WormGearSetParametricStudyTool
    from ._4436 import ZerolBevelGearMeshParametricStudyTool
    from ._4437 import ZerolBevelGearParametricStudyTool
    from ._4438 import ZerolBevelGearSetParametricStudyTool
else:
    import_structure = {
        "_4292": ["AbstractAssemblyParametricStudyTool"],
        "_4293": ["AbstractShaftOrHousingParametricStudyTool"],
        "_4294": ["AbstractShaftParametricStudyTool"],
        "_4295": ["AbstractShaftToMountableComponentConnectionParametricStudyTool"],
        "_4296": ["AGMAGleasonConicalGearMeshParametricStudyTool"],
        "_4297": ["AGMAGleasonConicalGearParametricStudyTool"],
        "_4298": ["AGMAGleasonConicalGearSetParametricStudyTool"],
        "_4299": ["AssemblyParametricStudyTool"],
        "_4300": ["BearingParametricStudyTool"],
        "_4301": ["BeltConnectionParametricStudyTool"],
        "_4302": ["BeltDriveParametricStudyTool"],
        "_4303": ["BevelDifferentialGearMeshParametricStudyTool"],
        "_4304": ["BevelDifferentialGearParametricStudyTool"],
        "_4305": ["BevelDifferentialGearSetParametricStudyTool"],
        "_4306": ["BevelDifferentialPlanetGearParametricStudyTool"],
        "_4307": ["BevelDifferentialSunGearParametricStudyTool"],
        "_4308": ["BevelGearMeshParametricStudyTool"],
        "_4309": ["BevelGearParametricStudyTool"],
        "_4310": ["BevelGearSetParametricStudyTool"],
        "_4311": ["BoltedJointParametricStudyTool"],
        "_4312": ["BoltParametricStudyTool"],
        "_4313": ["ClutchConnectionParametricStudyTool"],
        "_4314": ["ClutchHalfParametricStudyTool"],
        "_4315": ["ClutchParametricStudyTool"],
        "_4316": ["CoaxialConnectionParametricStudyTool"],
        "_4317": ["ComponentParametricStudyTool"],
        "_4318": ["ConceptCouplingConnectionParametricStudyTool"],
        "_4319": ["ConceptCouplingHalfParametricStudyTool"],
        "_4320": ["ConceptCouplingParametricStudyTool"],
        "_4321": ["ConceptGearMeshParametricStudyTool"],
        "_4322": ["ConceptGearParametricStudyTool"],
        "_4323": ["ConceptGearSetParametricStudyTool"],
        "_4324": ["ConicalGearMeshParametricStudyTool"],
        "_4325": ["ConicalGearParametricStudyTool"],
        "_4326": ["ConicalGearSetParametricStudyTool"],
        "_4327": ["ConnectionParametricStudyTool"],
        "_4328": ["ConnectorParametricStudyTool"],
        "_4329": ["CouplingConnectionParametricStudyTool"],
        "_4330": ["CouplingHalfParametricStudyTool"],
        "_4331": ["CouplingParametricStudyTool"],
        "_4332": ["CVTBeltConnectionParametricStudyTool"],
        "_4333": ["CVTParametricStudyTool"],
        "_4334": ["CVTPulleyParametricStudyTool"],
        "_4335": ["CycloidalAssemblyParametricStudyTool"],
        "_4336": ["CycloidalDiscCentralBearingConnectionParametricStudyTool"],
        "_4337": ["CycloidalDiscParametricStudyTool"],
        "_4338": ["CycloidalDiscPlanetaryBearingConnectionParametricStudyTool"],
        "_4339": ["CylindricalGearMeshParametricStudyTool"],
        "_4340": ["CylindricalGearParametricStudyTool"],
        "_4341": ["CylindricalGearSetParametricStudyTool"],
        "_4342": ["CylindricalPlanetGearParametricStudyTool"],
        "_4343": ["DatumParametricStudyTool"],
        "_4344": ["DesignOfExperimentsVariableSetter"],
        "_4345": ["DoeValueSpecificationOption"],
        "_4346": ["DutyCycleResultsForAllComponents"],
        "_4347": ["DutyCycleResultsForAllGearSets"],
        "_4348": ["DutyCycleResultsForRootAssembly"],
        "_4349": ["DutyCycleResultsForSingleBearing"],
        "_4350": ["DutyCycleResultsForSingleShaft"],
        "_4351": ["ExternalCADModelParametricStudyTool"],
        "_4352": ["FaceGearMeshParametricStudyTool"],
        "_4353": ["FaceGearParametricStudyTool"],
        "_4354": ["FaceGearSetParametricStudyTool"],
        "_4355": ["FEPartParametricStudyTool"],
        "_4356": ["FlexiblePinAssemblyParametricStudyTool"],
        "_4357": ["GearMeshParametricStudyTool"],
        "_4358": ["GearParametricStudyTool"],
        "_4359": ["GearSetParametricStudyTool"],
        "_4360": ["GuideDxfModelParametricStudyTool"],
        "_4361": ["HypoidGearMeshParametricStudyTool"],
        "_4362": ["HypoidGearParametricStudyTool"],
        "_4363": ["HypoidGearSetParametricStudyTool"],
        "_4364": ["InterMountableComponentConnectionParametricStudyTool"],
        "_4365": ["KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool"],
        "_4366": ["KlingelnbergCycloPalloidConicalGearParametricStudyTool"],
        "_4367": ["KlingelnbergCycloPalloidConicalGearSetParametricStudyTool"],
        "_4368": ["KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool"],
        "_4369": ["KlingelnbergCycloPalloidHypoidGearParametricStudyTool"],
        "_4370": ["KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool"],
        "_4371": ["KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool"],
        "_4372": ["KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool"],
        "_4373": ["KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool"],
        "_4374": ["MassDiscParametricStudyTool"],
        "_4375": ["MeasurementComponentParametricStudyTool"],
        "_4376": ["MonteCarloDistribution"],
        "_4377": ["MountableComponentParametricStudyTool"],
        "_4378": ["OilSealParametricStudyTool"],
        "_4379": ["ParametricStudyDimension"],
        "_4380": ["ParametricStudyDOEResultVariable"],
        "_4381": ["ParametricStudyDOEResultVariableForParallelCoordinatesPlot"],
        "_4382": ["ParametricStudyHistogram"],
        "_4383": ["ParametricStudyStaticLoad"],
        "_4384": ["ParametricStudyTool"],
        "_4385": ["ParametricStudyToolOptions"],
        "_4386": ["ParametricStudyToolResultsForReporting"],
        "_4387": ["ParametricStudyToolStepResult"],
        "_4388": ["ParametricStudyVariable"],
        "_4389": ["PartParametricStudyTool"],
        "_4390": ["PartToPartShearCouplingConnectionParametricStudyTool"],
        "_4391": ["PartToPartShearCouplingHalfParametricStudyTool"],
        "_4392": ["PartToPartShearCouplingParametricStudyTool"],
        "_4393": ["PlanetaryConnectionParametricStudyTool"],
        "_4394": ["PlanetaryGearSetParametricStudyTool"],
        "_4395": ["PlanetCarrierParametricStudyTool"],
        "_4396": ["PointLoadParametricStudyTool"],
        "_4397": ["PowerLoadParametricStudyTool"],
        "_4398": ["PulleyParametricStudyTool"],
        "_4399": ["RingPinsParametricStudyTool"],
        "_4400": ["RingPinsToDiscConnectionParametricStudyTool"],
        "_4401": ["RollingRingAssemblyParametricStudyTool"],
        "_4402": ["RollingRingConnectionParametricStudyTool"],
        "_4403": ["RollingRingParametricStudyTool"],
        "_4404": ["RootAssemblyParametricStudyTool"],
        "_4405": ["ShaftHubConnectionParametricStudyTool"],
        "_4406": ["ShaftParametricStudyTool"],
        "_4407": ["ShaftToMountableComponentConnectionParametricStudyTool"],
        "_4408": ["SpecialisedAssemblyParametricStudyTool"],
        "_4409": ["SpiralBevelGearMeshParametricStudyTool"],
        "_4410": ["SpiralBevelGearParametricStudyTool"],
        "_4411": ["SpiralBevelGearSetParametricStudyTool"],
        "_4412": ["SpringDamperConnectionParametricStudyTool"],
        "_4413": ["SpringDamperHalfParametricStudyTool"],
        "_4414": ["SpringDamperParametricStudyTool"],
        "_4415": ["StraightBevelDiffGearMeshParametricStudyTool"],
        "_4416": ["StraightBevelDiffGearParametricStudyTool"],
        "_4417": ["StraightBevelDiffGearSetParametricStudyTool"],
        "_4418": ["StraightBevelGearMeshParametricStudyTool"],
        "_4419": ["StraightBevelGearParametricStudyTool"],
        "_4420": ["StraightBevelGearSetParametricStudyTool"],
        "_4421": ["StraightBevelPlanetGearParametricStudyTool"],
        "_4422": ["StraightBevelSunGearParametricStudyTool"],
        "_4423": ["SynchroniserHalfParametricStudyTool"],
        "_4424": ["SynchroniserParametricStudyTool"],
        "_4425": ["SynchroniserPartParametricStudyTool"],
        "_4426": ["SynchroniserSleeveParametricStudyTool"],
        "_4427": ["TorqueConverterConnectionParametricStudyTool"],
        "_4428": ["TorqueConverterParametricStudyTool"],
        "_4429": ["TorqueConverterPumpParametricStudyTool"],
        "_4430": ["TorqueConverterTurbineParametricStudyTool"],
        "_4431": ["UnbalancedMassParametricStudyTool"],
        "_4432": ["VirtualComponentParametricStudyTool"],
        "_4433": ["WormGearMeshParametricStudyTool"],
        "_4434": ["WormGearParametricStudyTool"],
        "_4435": ["WormGearSetParametricStudyTool"],
        "_4436": ["ZerolBevelGearMeshParametricStudyTool"],
        "_4437": ["ZerolBevelGearParametricStudyTool"],
        "_4438": ["ZerolBevelGearSetParametricStudyTool"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyParametricStudyTool",
    "AbstractShaftOrHousingParametricStudyTool",
    "AbstractShaftParametricStudyTool",
    "AbstractShaftToMountableComponentConnectionParametricStudyTool",
    "AGMAGleasonConicalGearMeshParametricStudyTool",
    "AGMAGleasonConicalGearParametricStudyTool",
    "AGMAGleasonConicalGearSetParametricStudyTool",
    "AssemblyParametricStudyTool",
    "BearingParametricStudyTool",
    "BeltConnectionParametricStudyTool",
    "BeltDriveParametricStudyTool",
    "BevelDifferentialGearMeshParametricStudyTool",
    "BevelDifferentialGearParametricStudyTool",
    "BevelDifferentialGearSetParametricStudyTool",
    "BevelDifferentialPlanetGearParametricStudyTool",
    "BevelDifferentialSunGearParametricStudyTool",
    "BevelGearMeshParametricStudyTool",
    "BevelGearParametricStudyTool",
    "BevelGearSetParametricStudyTool",
    "BoltedJointParametricStudyTool",
    "BoltParametricStudyTool",
    "ClutchConnectionParametricStudyTool",
    "ClutchHalfParametricStudyTool",
    "ClutchParametricStudyTool",
    "CoaxialConnectionParametricStudyTool",
    "ComponentParametricStudyTool",
    "ConceptCouplingConnectionParametricStudyTool",
    "ConceptCouplingHalfParametricStudyTool",
    "ConceptCouplingParametricStudyTool",
    "ConceptGearMeshParametricStudyTool",
    "ConceptGearParametricStudyTool",
    "ConceptGearSetParametricStudyTool",
    "ConicalGearMeshParametricStudyTool",
    "ConicalGearParametricStudyTool",
    "ConicalGearSetParametricStudyTool",
    "ConnectionParametricStudyTool",
    "ConnectorParametricStudyTool",
    "CouplingConnectionParametricStudyTool",
    "CouplingHalfParametricStudyTool",
    "CouplingParametricStudyTool",
    "CVTBeltConnectionParametricStudyTool",
    "CVTParametricStudyTool",
    "CVTPulleyParametricStudyTool",
    "CycloidalAssemblyParametricStudyTool",
    "CycloidalDiscCentralBearingConnectionParametricStudyTool",
    "CycloidalDiscParametricStudyTool",
    "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
    "CylindricalGearMeshParametricStudyTool",
    "CylindricalGearParametricStudyTool",
    "CylindricalGearSetParametricStudyTool",
    "CylindricalPlanetGearParametricStudyTool",
    "DatumParametricStudyTool",
    "DesignOfExperimentsVariableSetter",
    "DoeValueSpecificationOption",
    "DutyCycleResultsForAllComponents",
    "DutyCycleResultsForAllGearSets",
    "DutyCycleResultsForRootAssembly",
    "DutyCycleResultsForSingleBearing",
    "DutyCycleResultsForSingleShaft",
    "ExternalCADModelParametricStudyTool",
    "FaceGearMeshParametricStudyTool",
    "FaceGearParametricStudyTool",
    "FaceGearSetParametricStudyTool",
    "FEPartParametricStudyTool",
    "FlexiblePinAssemblyParametricStudyTool",
    "GearMeshParametricStudyTool",
    "GearParametricStudyTool",
    "GearSetParametricStudyTool",
    "GuideDxfModelParametricStudyTool",
    "HypoidGearMeshParametricStudyTool",
    "HypoidGearParametricStudyTool",
    "HypoidGearSetParametricStudyTool",
    "InterMountableComponentConnectionParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool",
    "MassDiscParametricStudyTool",
    "MeasurementComponentParametricStudyTool",
    "MonteCarloDistribution",
    "MountableComponentParametricStudyTool",
    "OilSealParametricStudyTool",
    "ParametricStudyDimension",
    "ParametricStudyDOEResultVariable",
    "ParametricStudyDOEResultVariableForParallelCoordinatesPlot",
    "ParametricStudyHistogram",
    "ParametricStudyStaticLoad",
    "ParametricStudyTool",
    "ParametricStudyToolOptions",
    "ParametricStudyToolResultsForReporting",
    "ParametricStudyToolStepResult",
    "ParametricStudyVariable",
    "PartParametricStudyTool",
    "PartToPartShearCouplingConnectionParametricStudyTool",
    "PartToPartShearCouplingHalfParametricStudyTool",
    "PartToPartShearCouplingParametricStudyTool",
    "PlanetaryConnectionParametricStudyTool",
    "PlanetaryGearSetParametricStudyTool",
    "PlanetCarrierParametricStudyTool",
    "PointLoadParametricStudyTool",
    "PowerLoadParametricStudyTool",
    "PulleyParametricStudyTool",
    "RingPinsParametricStudyTool",
    "RingPinsToDiscConnectionParametricStudyTool",
    "RollingRingAssemblyParametricStudyTool",
    "RollingRingConnectionParametricStudyTool",
    "RollingRingParametricStudyTool",
    "RootAssemblyParametricStudyTool",
    "ShaftHubConnectionParametricStudyTool",
    "ShaftParametricStudyTool",
    "ShaftToMountableComponentConnectionParametricStudyTool",
    "SpecialisedAssemblyParametricStudyTool",
    "SpiralBevelGearMeshParametricStudyTool",
    "SpiralBevelGearParametricStudyTool",
    "SpiralBevelGearSetParametricStudyTool",
    "SpringDamperConnectionParametricStudyTool",
    "SpringDamperHalfParametricStudyTool",
    "SpringDamperParametricStudyTool",
    "StraightBevelDiffGearMeshParametricStudyTool",
    "StraightBevelDiffGearParametricStudyTool",
    "StraightBevelDiffGearSetParametricStudyTool",
    "StraightBevelGearMeshParametricStudyTool",
    "StraightBevelGearParametricStudyTool",
    "StraightBevelGearSetParametricStudyTool",
    "StraightBevelPlanetGearParametricStudyTool",
    "StraightBevelSunGearParametricStudyTool",
    "SynchroniserHalfParametricStudyTool",
    "SynchroniserParametricStudyTool",
    "SynchroniserPartParametricStudyTool",
    "SynchroniserSleeveParametricStudyTool",
    "TorqueConverterConnectionParametricStudyTool",
    "TorqueConverterParametricStudyTool",
    "TorqueConverterPumpParametricStudyTool",
    "TorqueConverterTurbineParametricStudyTool",
    "UnbalancedMassParametricStudyTool",
    "VirtualComponentParametricStudyTool",
    "WormGearMeshParametricStudyTool",
    "WormGearParametricStudyTool",
    "WormGearSetParametricStudyTool",
    "ZerolBevelGearMeshParametricStudyTool",
    "ZerolBevelGearParametricStudyTool",
    "ZerolBevelGearSetParametricStudyTool",
)
