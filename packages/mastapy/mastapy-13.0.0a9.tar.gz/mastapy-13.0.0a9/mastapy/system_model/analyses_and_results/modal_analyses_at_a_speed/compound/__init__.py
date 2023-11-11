"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5243 import AbstractAssemblyCompoundModalAnalysisAtASpeed
    from ._5244 import AbstractShaftCompoundModalAnalysisAtASpeed
    from ._5245 import AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
    from ._5246 import (
        AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed,
    )
    from ._5247 import AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
    from ._5248 import AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed
    from ._5249 import AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
    from ._5250 import AssemblyCompoundModalAnalysisAtASpeed
    from ._5251 import BearingCompoundModalAnalysisAtASpeed
    from ._5252 import BeltConnectionCompoundModalAnalysisAtASpeed
    from ._5253 import BeltDriveCompoundModalAnalysisAtASpeed
    from ._5254 import BevelDifferentialGearCompoundModalAnalysisAtASpeed
    from ._5255 import BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed
    from ._5256 import BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
    from ._5257 import BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
    from ._5258 import BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
    from ._5259 import BevelGearCompoundModalAnalysisAtASpeed
    from ._5260 import BevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5261 import BevelGearSetCompoundModalAnalysisAtASpeed
    from ._5262 import BoltCompoundModalAnalysisAtASpeed
    from ._5263 import BoltedJointCompoundModalAnalysisAtASpeed
    from ._5264 import ClutchCompoundModalAnalysisAtASpeed
    from ._5265 import ClutchConnectionCompoundModalAnalysisAtASpeed
    from ._5266 import ClutchHalfCompoundModalAnalysisAtASpeed
    from ._5267 import CoaxialConnectionCompoundModalAnalysisAtASpeed
    from ._5268 import ComponentCompoundModalAnalysisAtASpeed
    from ._5269 import ConceptCouplingCompoundModalAnalysisAtASpeed
    from ._5270 import ConceptCouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5271 import ConceptCouplingHalfCompoundModalAnalysisAtASpeed
    from ._5272 import ConceptGearCompoundModalAnalysisAtASpeed
    from ._5273 import ConceptGearMeshCompoundModalAnalysisAtASpeed
    from ._5274 import ConceptGearSetCompoundModalAnalysisAtASpeed
    from ._5275 import ConicalGearCompoundModalAnalysisAtASpeed
    from ._5276 import ConicalGearMeshCompoundModalAnalysisAtASpeed
    from ._5277 import ConicalGearSetCompoundModalAnalysisAtASpeed
    from ._5278 import ConnectionCompoundModalAnalysisAtASpeed
    from ._5279 import ConnectorCompoundModalAnalysisAtASpeed
    from ._5280 import CouplingCompoundModalAnalysisAtASpeed
    from ._5281 import CouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5282 import CouplingHalfCompoundModalAnalysisAtASpeed
    from ._5283 import CVTBeltConnectionCompoundModalAnalysisAtASpeed
    from ._5284 import CVTCompoundModalAnalysisAtASpeed
    from ._5285 import CVTPulleyCompoundModalAnalysisAtASpeed
    from ._5286 import CycloidalAssemblyCompoundModalAnalysisAtASpeed
    from ._5287 import (
        CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed,
    )
    from ._5288 import CycloidalDiscCompoundModalAnalysisAtASpeed
    from ._5289 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed,
    )
    from ._5290 import CylindricalGearCompoundModalAnalysisAtASpeed
    from ._5291 import CylindricalGearMeshCompoundModalAnalysisAtASpeed
    from ._5292 import CylindricalGearSetCompoundModalAnalysisAtASpeed
    from ._5293 import CylindricalPlanetGearCompoundModalAnalysisAtASpeed
    from ._5294 import DatumCompoundModalAnalysisAtASpeed
    from ._5295 import ExternalCADModelCompoundModalAnalysisAtASpeed
    from ._5296 import FaceGearCompoundModalAnalysisAtASpeed
    from ._5297 import FaceGearMeshCompoundModalAnalysisAtASpeed
    from ._5298 import FaceGearSetCompoundModalAnalysisAtASpeed
    from ._5299 import FEPartCompoundModalAnalysisAtASpeed
    from ._5300 import FlexiblePinAssemblyCompoundModalAnalysisAtASpeed
    from ._5301 import GearCompoundModalAnalysisAtASpeed
    from ._5302 import GearMeshCompoundModalAnalysisAtASpeed
    from ._5303 import GearSetCompoundModalAnalysisAtASpeed
    from ._5304 import GuideDxfModelCompoundModalAnalysisAtASpeed
    from ._5305 import HypoidGearCompoundModalAnalysisAtASpeed
    from ._5306 import HypoidGearMeshCompoundModalAnalysisAtASpeed
    from ._5307 import HypoidGearSetCompoundModalAnalysisAtASpeed
    from ._5308 import InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
    from ._5309 import KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed
    from ._5310 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed,
    )
    from ._5311 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed,
    )
    from ._5312 import KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed
    from ._5313 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed,
    )
    from ._5314 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed,
    )
    from ._5315 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed,
    )
    from ._5316 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed,
    )
    from ._5317 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed,
    )
    from ._5318 import MassDiscCompoundModalAnalysisAtASpeed
    from ._5319 import MeasurementComponentCompoundModalAnalysisAtASpeed
    from ._5320 import MountableComponentCompoundModalAnalysisAtASpeed
    from ._5321 import OilSealCompoundModalAnalysisAtASpeed
    from ._5322 import PartCompoundModalAnalysisAtASpeed
    from ._5323 import PartToPartShearCouplingCompoundModalAnalysisAtASpeed
    from ._5324 import PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5325 import PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed
    from ._5326 import PlanetaryConnectionCompoundModalAnalysisAtASpeed
    from ._5327 import PlanetaryGearSetCompoundModalAnalysisAtASpeed
    from ._5328 import PlanetCarrierCompoundModalAnalysisAtASpeed
    from ._5329 import PointLoadCompoundModalAnalysisAtASpeed
    from ._5330 import PowerLoadCompoundModalAnalysisAtASpeed
    from ._5331 import PulleyCompoundModalAnalysisAtASpeed
    from ._5332 import RingPinsCompoundModalAnalysisAtASpeed
    from ._5333 import RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed
    from ._5334 import RollingRingAssemblyCompoundModalAnalysisAtASpeed
    from ._5335 import RollingRingCompoundModalAnalysisAtASpeed
    from ._5336 import RollingRingConnectionCompoundModalAnalysisAtASpeed
    from ._5337 import RootAssemblyCompoundModalAnalysisAtASpeed
    from ._5338 import ShaftCompoundModalAnalysisAtASpeed
    from ._5339 import ShaftHubConnectionCompoundModalAnalysisAtASpeed
    from ._5340 import ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
    from ._5341 import SpecialisedAssemblyCompoundModalAnalysisAtASpeed
    from ._5342 import SpiralBevelGearCompoundModalAnalysisAtASpeed
    from ._5343 import SpiralBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5344 import SpiralBevelGearSetCompoundModalAnalysisAtASpeed
    from ._5345 import SpringDamperCompoundModalAnalysisAtASpeed
    from ._5346 import SpringDamperConnectionCompoundModalAnalysisAtASpeed
    from ._5347 import SpringDamperHalfCompoundModalAnalysisAtASpeed
    from ._5348 import StraightBevelDiffGearCompoundModalAnalysisAtASpeed
    from ._5349 import StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed
    from ._5350 import StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
    from ._5351 import StraightBevelGearCompoundModalAnalysisAtASpeed
    from ._5352 import StraightBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5353 import StraightBevelGearSetCompoundModalAnalysisAtASpeed
    from ._5354 import StraightBevelPlanetGearCompoundModalAnalysisAtASpeed
    from ._5355 import StraightBevelSunGearCompoundModalAnalysisAtASpeed
    from ._5356 import SynchroniserCompoundModalAnalysisAtASpeed
    from ._5357 import SynchroniserHalfCompoundModalAnalysisAtASpeed
    from ._5358 import SynchroniserPartCompoundModalAnalysisAtASpeed
    from ._5359 import SynchroniserSleeveCompoundModalAnalysisAtASpeed
    from ._5360 import TorqueConverterCompoundModalAnalysisAtASpeed
    from ._5361 import TorqueConverterConnectionCompoundModalAnalysisAtASpeed
    from ._5362 import TorqueConverterPumpCompoundModalAnalysisAtASpeed
    from ._5363 import TorqueConverterTurbineCompoundModalAnalysisAtASpeed
    from ._5364 import UnbalancedMassCompoundModalAnalysisAtASpeed
    from ._5365 import VirtualComponentCompoundModalAnalysisAtASpeed
    from ._5366 import WormGearCompoundModalAnalysisAtASpeed
    from ._5367 import WormGearMeshCompoundModalAnalysisAtASpeed
    from ._5368 import WormGearSetCompoundModalAnalysisAtASpeed
    from ._5369 import ZerolBevelGearCompoundModalAnalysisAtASpeed
    from ._5370 import ZerolBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5371 import ZerolBevelGearSetCompoundModalAnalysisAtASpeed
else:
    import_structure = {
        "_5243": ["AbstractAssemblyCompoundModalAnalysisAtASpeed"],
        "_5244": ["AbstractShaftCompoundModalAnalysisAtASpeed"],
        "_5245": ["AbstractShaftOrHousingCompoundModalAnalysisAtASpeed"],
        "_5246": [
            "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed"
        ],
        "_5247": ["AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed"],
        "_5248": ["AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed"],
        "_5249": ["AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed"],
        "_5250": ["AssemblyCompoundModalAnalysisAtASpeed"],
        "_5251": ["BearingCompoundModalAnalysisAtASpeed"],
        "_5252": ["BeltConnectionCompoundModalAnalysisAtASpeed"],
        "_5253": ["BeltDriveCompoundModalAnalysisAtASpeed"],
        "_5254": ["BevelDifferentialGearCompoundModalAnalysisAtASpeed"],
        "_5255": ["BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed"],
        "_5256": ["BevelDifferentialGearSetCompoundModalAnalysisAtASpeed"],
        "_5257": ["BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed"],
        "_5258": ["BevelDifferentialSunGearCompoundModalAnalysisAtASpeed"],
        "_5259": ["BevelGearCompoundModalAnalysisAtASpeed"],
        "_5260": ["BevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5261": ["BevelGearSetCompoundModalAnalysisAtASpeed"],
        "_5262": ["BoltCompoundModalAnalysisAtASpeed"],
        "_5263": ["BoltedJointCompoundModalAnalysisAtASpeed"],
        "_5264": ["ClutchCompoundModalAnalysisAtASpeed"],
        "_5265": ["ClutchConnectionCompoundModalAnalysisAtASpeed"],
        "_5266": ["ClutchHalfCompoundModalAnalysisAtASpeed"],
        "_5267": ["CoaxialConnectionCompoundModalAnalysisAtASpeed"],
        "_5268": ["ComponentCompoundModalAnalysisAtASpeed"],
        "_5269": ["ConceptCouplingCompoundModalAnalysisAtASpeed"],
        "_5270": ["ConceptCouplingConnectionCompoundModalAnalysisAtASpeed"],
        "_5271": ["ConceptCouplingHalfCompoundModalAnalysisAtASpeed"],
        "_5272": ["ConceptGearCompoundModalAnalysisAtASpeed"],
        "_5273": ["ConceptGearMeshCompoundModalAnalysisAtASpeed"],
        "_5274": ["ConceptGearSetCompoundModalAnalysisAtASpeed"],
        "_5275": ["ConicalGearCompoundModalAnalysisAtASpeed"],
        "_5276": ["ConicalGearMeshCompoundModalAnalysisAtASpeed"],
        "_5277": ["ConicalGearSetCompoundModalAnalysisAtASpeed"],
        "_5278": ["ConnectionCompoundModalAnalysisAtASpeed"],
        "_5279": ["ConnectorCompoundModalAnalysisAtASpeed"],
        "_5280": ["CouplingCompoundModalAnalysisAtASpeed"],
        "_5281": ["CouplingConnectionCompoundModalAnalysisAtASpeed"],
        "_5282": ["CouplingHalfCompoundModalAnalysisAtASpeed"],
        "_5283": ["CVTBeltConnectionCompoundModalAnalysisAtASpeed"],
        "_5284": ["CVTCompoundModalAnalysisAtASpeed"],
        "_5285": ["CVTPulleyCompoundModalAnalysisAtASpeed"],
        "_5286": ["CycloidalAssemblyCompoundModalAnalysisAtASpeed"],
        "_5287": ["CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed"],
        "_5288": ["CycloidalDiscCompoundModalAnalysisAtASpeed"],
        "_5289": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed"
        ],
        "_5290": ["CylindricalGearCompoundModalAnalysisAtASpeed"],
        "_5291": ["CylindricalGearMeshCompoundModalAnalysisAtASpeed"],
        "_5292": ["CylindricalGearSetCompoundModalAnalysisAtASpeed"],
        "_5293": ["CylindricalPlanetGearCompoundModalAnalysisAtASpeed"],
        "_5294": ["DatumCompoundModalAnalysisAtASpeed"],
        "_5295": ["ExternalCADModelCompoundModalAnalysisAtASpeed"],
        "_5296": ["FaceGearCompoundModalAnalysisAtASpeed"],
        "_5297": ["FaceGearMeshCompoundModalAnalysisAtASpeed"],
        "_5298": ["FaceGearSetCompoundModalAnalysisAtASpeed"],
        "_5299": ["FEPartCompoundModalAnalysisAtASpeed"],
        "_5300": ["FlexiblePinAssemblyCompoundModalAnalysisAtASpeed"],
        "_5301": ["GearCompoundModalAnalysisAtASpeed"],
        "_5302": ["GearMeshCompoundModalAnalysisAtASpeed"],
        "_5303": ["GearSetCompoundModalAnalysisAtASpeed"],
        "_5304": ["GuideDxfModelCompoundModalAnalysisAtASpeed"],
        "_5305": ["HypoidGearCompoundModalAnalysisAtASpeed"],
        "_5306": ["HypoidGearMeshCompoundModalAnalysisAtASpeed"],
        "_5307": ["HypoidGearSetCompoundModalAnalysisAtASpeed"],
        "_5308": ["InterMountableComponentConnectionCompoundModalAnalysisAtASpeed"],
        "_5309": ["KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed"],
        "_5310": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed"
        ],
        "_5311": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed"
        ],
        "_5312": ["KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed"],
        "_5313": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed"
        ],
        "_5314": ["KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed"],
        "_5315": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed"
        ],
        "_5316": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed"
        ],
        "_5317": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed"
        ],
        "_5318": ["MassDiscCompoundModalAnalysisAtASpeed"],
        "_5319": ["MeasurementComponentCompoundModalAnalysisAtASpeed"],
        "_5320": ["MountableComponentCompoundModalAnalysisAtASpeed"],
        "_5321": ["OilSealCompoundModalAnalysisAtASpeed"],
        "_5322": ["PartCompoundModalAnalysisAtASpeed"],
        "_5323": ["PartToPartShearCouplingCompoundModalAnalysisAtASpeed"],
        "_5324": ["PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed"],
        "_5325": ["PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed"],
        "_5326": ["PlanetaryConnectionCompoundModalAnalysisAtASpeed"],
        "_5327": ["PlanetaryGearSetCompoundModalAnalysisAtASpeed"],
        "_5328": ["PlanetCarrierCompoundModalAnalysisAtASpeed"],
        "_5329": ["PointLoadCompoundModalAnalysisAtASpeed"],
        "_5330": ["PowerLoadCompoundModalAnalysisAtASpeed"],
        "_5331": ["PulleyCompoundModalAnalysisAtASpeed"],
        "_5332": ["RingPinsCompoundModalAnalysisAtASpeed"],
        "_5333": ["RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed"],
        "_5334": ["RollingRingAssemblyCompoundModalAnalysisAtASpeed"],
        "_5335": ["RollingRingCompoundModalAnalysisAtASpeed"],
        "_5336": ["RollingRingConnectionCompoundModalAnalysisAtASpeed"],
        "_5337": ["RootAssemblyCompoundModalAnalysisAtASpeed"],
        "_5338": ["ShaftCompoundModalAnalysisAtASpeed"],
        "_5339": ["ShaftHubConnectionCompoundModalAnalysisAtASpeed"],
        "_5340": ["ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed"],
        "_5341": ["SpecialisedAssemblyCompoundModalAnalysisAtASpeed"],
        "_5342": ["SpiralBevelGearCompoundModalAnalysisAtASpeed"],
        "_5343": ["SpiralBevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5344": ["SpiralBevelGearSetCompoundModalAnalysisAtASpeed"],
        "_5345": ["SpringDamperCompoundModalAnalysisAtASpeed"],
        "_5346": ["SpringDamperConnectionCompoundModalAnalysisAtASpeed"],
        "_5347": ["SpringDamperHalfCompoundModalAnalysisAtASpeed"],
        "_5348": ["StraightBevelDiffGearCompoundModalAnalysisAtASpeed"],
        "_5349": ["StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed"],
        "_5350": ["StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed"],
        "_5351": ["StraightBevelGearCompoundModalAnalysisAtASpeed"],
        "_5352": ["StraightBevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5353": ["StraightBevelGearSetCompoundModalAnalysisAtASpeed"],
        "_5354": ["StraightBevelPlanetGearCompoundModalAnalysisAtASpeed"],
        "_5355": ["StraightBevelSunGearCompoundModalAnalysisAtASpeed"],
        "_5356": ["SynchroniserCompoundModalAnalysisAtASpeed"],
        "_5357": ["SynchroniserHalfCompoundModalAnalysisAtASpeed"],
        "_5358": ["SynchroniserPartCompoundModalAnalysisAtASpeed"],
        "_5359": ["SynchroniserSleeveCompoundModalAnalysisAtASpeed"],
        "_5360": ["TorqueConverterCompoundModalAnalysisAtASpeed"],
        "_5361": ["TorqueConverterConnectionCompoundModalAnalysisAtASpeed"],
        "_5362": ["TorqueConverterPumpCompoundModalAnalysisAtASpeed"],
        "_5363": ["TorqueConverterTurbineCompoundModalAnalysisAtASpeed"],
        "_5364": ["UnbalancedMassCompoundModalAnalysisAtASpeed"],
        "_5365": ["VirtualComponentCompoundModalAnalysisAtASpeed"],
        "_5366": ["WormGearCompoundModalAnalysisAtASpeed"],
        "_5367": ["WormGearMeshCompoundModalAnalysisAtASpeed"],
        "_5368": ["WormGearSetCompoundModalAnalysisAtASpeed"],
        "_5369": ["ZerolBevelGearCompoundModalAnalysisAtASpeed"],
        "_5370": ["ZerolBevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5371": ["ZerolBevelGearSetCompoundModalAnalysisAtASpeed"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundModalAnalysisAtASpeed",
    "AbstractShaftCompoundModalAnalysisAtASpeed",
    "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
    "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
    "AssemblyCompoundModalAnalysisAtASpeed",
    "BearingCompoundModalAnalysisAtASpeed",
    "BeltConnectionCompoundModalAnalysisAtASpeed",
    "BeltDriveCompoundModalAnalysisAtASpeed",
    "BevelDifferentialGearCompoundModalAnalysisAtASpeed",
    "BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed",
    "BevelDifferentialGearSetCompoundModalAnalysisAtASpeed",
    "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
    "BevelDifferentialSunGearCompoundModalAnalysisAtASpeed",
    "BevelGearCompoundModalAnalysisAtASpeed",
    "BevelGearMeshCompoundModalAnalysisAtASpeed",
    "BevelGearSetCompoundModalAnalysisAtASpeed",
    "BoltCompoundModalAnalysisAtASpeed",
    "BoltedJointCompoundModalAnalysisAtASpeed",
    "ClutchCompoundModalAnalysisAtASpeed",
    "ClutchConnectionCompoundModalAnalysisAtASpeed",
    "ClutchHalfCompoundModalAnalysisAtASpeed",
    "CoaxialConnectionCompoundModalAnalysisAtASpeed",
    "ComponentCompoundModalAnalysisAtASpeed",
    "ConceptCouplingCompoundModalAnalysisAtASpeed",
    "ConceptCouplingConnectionCompoundModalAnalysisAtASpeed",
    "ConceptCouplingHalfCompoundModalAnalysisAtASpeed",
    "ConceptGearCompoundModalAnalysisAtASpeed",
    "ConceptGearMeshCompoundModalAnalysisAtASpeed",
    "ConceptGearSetCompoundModalAnalysisAtASpeed",
    "ConicalGearCompoundModalAnalysisAtASpeed",
    "ConicalGearMeshCompoundModalAnalysisAtASpeed",
    "ConicalGearSetCompoundModalAnalysisAtASpeed",
    "ConnectionCompoundModalAnalysisAtASpeed",
    "ConnectorCompoundModalAnalysisAtASpeed",
    "CouplingCompoundModalAnalysisAtASpeed",
    "CouplingConnectionCompoundModalAnalysisAtASpeed",
    "CouplingHalfCompoundModalAnalysisAtASpeed",
    "CVTBeltConnectionCompoundModalAnalysisAtASpeed",
    "CVTCompoundModalAnalysisAtASpeed",
    "CVTPulleyCompoundModalAnalysisAtASpeed",
    "CycloidalAssemblyCompoundModalAnalysisAtASpeed",
    "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed",
    "CycloidalDiscCompoundModalAnalysisAtASpeed",
    "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed",
    "CylindricalGearCompoundModalAnalysisAtASpeed",
    "CylindricalGearMeshCompoundModalAnalysisAtASpeed",
    "CylindricalGearSetCompoundModalAnalysisAtASpeed",
    "CylindricalPlanetGearCompoundModalAnalysisAtASpeed",
    "DatumCompoundModalAnalysisAtASpeed",
    "ExternalCADModelCompoundModalAnalysisAtASpeed",
    "FaceGearCompoundModalAnalysisAtASpeed",
    "FaceGearMeshCompoundModalAnalysisAtASpeed",
    "FaceGearSetCompoundModalAnalysisAtASpeed",
    "FEPartCompoundModalAnalysisAtASpeed",
    "FlexiblePinAssemblyCompoundModalAnalysisAtASpeed",
    "GearCompoundModalAnalysisAtASpeed",
    "GearMeshCompoundModalAnalysisAtASpeed",
    "GearSetCompoundModalAnalysisAtASpeed",
    "GuideDxfModelCompoundModalAnalysisAtASpeed",
    "HypoidGearCompoundModalAnalysisAtASpeed",
    "HypoidGearMeshCompoundModalAnalysisAtASpeed",
    "HypoidGearSetCompoundModalAnalysisAtASpeed",
    "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",
    "MassDiscCompoundModalAnalysisAtASpeed",
    "MeasurementComponentCompoundModalAnalysisAtASpeed",
    "MountableComponentCompoundModalAnalysisAtASpeed",
    "OilSealCompoundModalAnalysisAtASpeed",
    "PartCompoundModalAnalysisAtASpeed",
    "PartToPartShearCouplingCompoundModalAnalysisAtASpeed",
    "PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed",
    "PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed",
    "PlanetaryConnectionCompoundModalAnalysisAtASpeed",
    "PlanetaryGearSetCompoundModalAnalysisAtASpeed",
    "PlanetCarrierCompoundModalAnalysisAtASpeed",
    "PointLoadCompoundModalAnalysisAtASpeed",
    "PowerLoadCompoundModalAnalysisAtASpeed",
    "PulleyCompoundModalAnalysisAtASpeed",
    "RingPinsCompoundModalAnalysisAtASpeed",
    "RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed",
    "RollingRingAssemblyCompoundModalAnalysisAtASpeed",
    "RollingRingCompoundModalAnalysisAtASpeed",
    "RollingRingConnectionCompoundModalAnalysisAtASpeed",
    "RootAssemblyCompoundModalAnalysisAtASpeed",
    "ShaftCompoundModalAnalysisAtASpeed",
    "ShaftHubConnectionCompoundModalAnalysisAtASpeed",
    "ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    "SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
    "SpiralBevelGearCompoundModalAnalysisAtASpeed",
    "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
    "SpiralBevelGearSetCompoundModalAnalysisAtASpeed",
    "SpringDamperCompoundModalAnalysisAtASpeed",
    "SpringDamperConnectionCompoundModalAnalysisAtASpeed",
    "SpringDamperHalfCompoundModalAnalysisAtASpeed",
    "StraightBevelDiffGearCompoundModalAnalysisAtASpeed",
    "StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed",
    "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed",
    "StraightBevelGearCompoundModalAnalysisAtASpeed",
    "StraightBevelGearMeshCompoundModalAnalysisAtASpeed",
    "StraightBevelGearSetCompoundModalAnalysisAtASpeed",
    "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",
    "StraightBevelSunGearCompoundModalAnalysisAtASpeed",
    "SynchroniserCompoundModalAnalysisAtASpeed",
    "SynchroniserHalfCompoundModalAnalysisAtASpeed",
    "SynchroniserPartCompoundModalAnalysisAtASpeed",
    "SynchroniserSleeveCompoundModalAnalysisAtASpeed",
    "TorqueConverterCompoundModalAnalysisAtASpeed",
    "TorqueConverterConnectionCompoundModalAnalysisAtASpeed",
    "TorqueConverterPumpCompoundModalAnalysisAtASpeed",
    "TorqueConverterTurbineCompoundModalAnalysisAtASpeed",
    "UnbalancedMassCompoundModalAnalysisAtASpeed",
    "VirtualComponentCompoundModalAnalysisAtASpeed",
    "WormGearCompoundModalAnalysisAtASpeed",
    "WormGearMeshCompoundModalAnalysisAtASpeed",
    "WormGearSetCompoundModalAnalysisAtASpeed",
    "ZerolBevelGearCompoundModalAnalysisAtASpeed",
    "ZerolBevelGearMeshCompoundModalAnalysisAtASpeed",
    "ZerolBevelGearSetCompoundModalAnalysisAtASpeed",
)
