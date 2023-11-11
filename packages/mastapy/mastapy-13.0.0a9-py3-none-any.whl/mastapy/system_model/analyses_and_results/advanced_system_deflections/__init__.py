"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7266 import AbstractAssemblyAdvancedSystemDeflection
    from ._7267 import AbstractShaftAdvancedSystemDeflection
    from ._7268 import AbstractShaftOrHousingAdvancedSystemDeflection
    from ._7269 import (
        AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection,
    )
    from ._7270 import AdvancedSystemDeflection
    from ._7271 import AdvancedSystemDeflectionOptions
    from ._7272 import AdvancedSystemDeflectionSubAnalysis
    from ._7273 import AGMAGleasonConicalGearAdvancedSystemDeflection
    from ._7274 import AGMAGleasonConicalGearMeshAdvancedSystemDeflection
    from ._7275 import AGMAGleasonConicalGearSetAdvancedSystemDeflection
    from ._7276 import AssemblyAdvancedSystemDeflection
    from ._7277 import BearingAdvancedSystemDeflection
    from ._7278 import BeltConnectionAdvancedSystemDeflection
    from ._7279 import BeltDriveAdvancedSystemDeflection
    from ._7280 import BevelDifferentialGearAdvancedSystemDeflection
    from ._7281 import BevelDifferentialGearMeshAdvancedSystemDeflection
    from ._7282 import BevelDifferentialGearSetAdvancedSystemDeflection
    from ._7283 import BevelDifferentialPlanetGearAdvancedSystemDeflection
    from ._7284 import BevelDifferentialSunGearAdvancedSystemDeflection
    from ._7285 import BevelGearAdvancedSystemDeflection
    from ._7286 import BevelGearMeshAdvancedSystemDeflection
    from ._7287 import BevelGearSetAdvancedSystemDeflection
    from ._7288 import BoltAdvancedSystemDeflection
    from ._7289 import BoltedJointAdvancedSystemDeflection
    from ._7290 import ClutchAdvancedSystemDeflection
    from ._7291 import ClutchConnectionAdvancedSystemDeflection
    from ._7292 import ClutchHalfAdvancedSystemDeflection
    from ._7293 import CoaxialConnectionAdvancedSystemDeflection
    from ._7294 import ComponentAdvancedSystemDeflection
    from ._7295 import ConceptCouplingAdvancedSystemDeflection
    from ._7296 import ConceptCouplingConnectionAdvancedSystemDeflection
    from ._7297 import ConceptCouplingHalfAdvancedSystemDeflection
    from ._7298 import ConceptGearAdvancedSystemDeflection
    from ._7299 import ConceptGearMeshAdvancedSystemDeflection
    from ._7300 import ConceptGearSetAdvancedSystemDeflection
    from ._7301 import ConicalGearAdvancedSystemDeflection
    from ._7302 import ConicalGearMeshAdvancedSystemDeflection
    from ._7303 import ConicalGearSetAdvancedSystemDeflection
    from ._7304 import ConnectionAdvancedSystemDeflection
    from ._7305 import ConnectorAdvancedSystemDeflection
    from ._7306 import ContactChartPerToothPass
    from ._7307 import CouplingAdvancedSystemDeflection
    from ._7308 import CouplingConnectionAdvancedSystemDeflection
    from ._7309 import CouplingHalfAdvancedSystemDeflection
    from ._7310 import CVTAdvancedSystemDeflection
    from ._7311 import CVTBeltConnectionAdvancedSystemDeflection
    from ._7312 import CVTPulleyAdvancedSystemDeflection
    from ._7313 import CycloidalAssemblyAdvancedSystemDeflection
    from ._7314 import CycloidalDiscAdvancedSystemDeflection
    from ._7315 import CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection
    from ._7316 import CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection
    from ._7317 import CylindricalGearAdvancedSystemDeflection
    from ._7318 import CylindricalGearMeshAdvancedSystemDeflection
    from ._7319 import CylindricalGearSetAdvancedSystemDeflection
    from ._7320 import CylindricalMeshedGearAdvancedSystemDeflection
    from ._7321 import CylindricalPlanetGearAdvancedSystemDeflection
    from ._7322 import DatumAdvancedSystemDeflection
    from ._7323 import ExternalCADModelAdvancedSystemDeflection
    from ._7324 import FaceGearAdvancedSystemDeflection
    from ._7325 import FaceGearMeshAdvancedSystemDeflection
    from ._7326 import FaceGearSetAdvancedSystemDeflection
    from ._7327 import FEPartAdvancedSystemDeflection
    from ._7328 import FlexiblePinAssemblyAdvancedSystemDeflection
    from ._7329 import GearAdvancedSystemDeflection
    from ._7330 import GearMeshAdvancedSystemDeflection
    from ._7331 import GearSetAdvancedSystemDeflection
    from ._7332 import GuideDxfModelAdvancedSystemDeflection
    from ._7333 import HypoidGearAdvancedSystemDeflection
    from ._7334 import HypoidGearMeshAdvancedSystemDeflection
    from ._7335 import HypoidGearSetAdvancedSystemDeflection
    from ._7336 import InterMountableComponentConnectionAdvancedSystemDeflection
    from ._7337 import KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
    from ._7338 import KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection
    from ._7339 import KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
    from ._7340 import KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
    from ._7341 import KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection
    from ._7342 import KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
    from ._7343 import KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
    from ._7344 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection,
    )
    from ._7345 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection,
    )
    from ._7346 import UseLtcaInAsdOption
    from ._7347 import MassDiscAdvancedSystemDeflection
    from ._7348 import MeasurementComponentAdvancedSystemDeflection
    from ._7349 import MountableComponentAdvancedSystemDeflection
    from ._7350 import OilSealAdvancedSystemDeflection
    from ._7351 import PartAdvancedSystemDeflection
    from ._7352 import PartToPartShearCouplingAdvancedSystemDeflection
    from ._7353 import PartToPartShearCouplingConnectionAdvancedSystemDeflection
    from ._7354 import PartToPartShearCouplingHalfAdvancedSystemDeflection
    from ._7355 import PlanetaryConnectionAdvancedSystemDeflection
    from ._7356 import PlanetaryGearSetAdvancedSystemDeflection
    from ._7357 import PlanetCarrierAdvancedSystemDeflection
    from ._7358 import PointLoadAdvancedSystemDeflection
    from ._7359 import PowerLoadAdvancedSystemDeflection
    from ._7360 import PulleyAdvancedSystemDeflection
    from ._7361 import RingPinsAdvancedSystemDeflection
    from ._7362 import RingPinsToDiscConnectionAdvancedSystemDeflection
    from ._7363 import RollingRingAdvancedSystemDeflection
    from ._7364 import RollingRingAssemblyAdvancedSystemDeflection
    from ._7365 import RollingRingConnectionAdvancedSystemDeflection
    from ._7366 import RootAssemblyAdvancedSystemDeflection
    from ._7367 import ShaftAdvancedSystemDeflection
    from ._7368 import ShaftHubConnectionAdvancedSystemDeflection
    from ._7369 import ShaftToMountableComponentConnectionAdvancedSystemDeflection
    from ._7370 import SpecialisedAssemblyAdvancedSystemDeflection
    from ._7371 import SpiralBevelGearAdvancedSystemDeflection
    from ._7372 import SpiralBevelGearMeshAdvancedSystemDeflection
    from ._7373 import SpiralBevelGearSetAdvancedSystemDeflection
    from ._7374 import SpringDamperAdvancedSystemDeflection
    from ._7375 import SpringDamperConnectionAdvancedSystemDeflection
    from ._7376 import SpringDamperHalfAdvancedSystemDeflection
    from ._7377 import StraightBevelDiffGearAdvancedSystemDeflection
    from ._7378 import StraightBevelDiffGearMeshAdvancedSystemDeflection
    from ._7379 import StraightBevelDiffGearSetAdvancedSystemDeflection
    from ._7380 import StraightBevelGearAdvancedSystemDeflection
    from ._7381 import StraightBevelGearMeshAdvancedSystemDeflection
    from ._7382 import StraightBevelGearSetAdvancedSystemDeflection
    from ._7383 import StraightBevelPlanetGearAdvancedSystemDeflection
    from ._7384 import StraightBevelSunGearAdvancedSystemDeflection
    from ._7385 import SynchroniserAdvancedSystemDeflection
    from ._7386 import SynchroniserHalfAdvancedSystemDeflection
    from ._7387 import SynchroniserPartAdvancedSystemDeflection
    from ._7388 import SynchroniserSleeveAdvancedSystemDeflection
    from ._7389 import TorqueConverterAdvancedSystemDeflection
    from ._7390 import TorqueConverterConnectionAdvancedSystemDeflection
    from ._7391 import TorqueConverterPumpAdvancedSystemDeflection
    from ._7392 import TorqueConverterTurbineAdvancedSystemDeflection
    from ._7393 import TransmissionErrorToOtherPowerLoad
    from ._7394 import UnbalancedMassAdvancedSystemDeflection
    from ._7395 import VirtualComponentAdvancedSystemDeflection
    from ._7396 import WormGearAdvancedSystemDeflection
    from ._7397 import WormGearMeshAdvancedSystemDeflection
    from ._7398 import WormGearSetAdvancedSystemDeflection
    from ._7399 import ZerolBevelGearAdvancedSystemDeflection
    from ._7400 import ZerolBevelGearMeshAdvancedSystemDeflection
    from ._7401 import ZerolBevelGearSetAdvancedSystemDeflection
else:
    import_structure = {
        "_7266": ["AbstractAssemblyAdvancedSystemDeflection"],
        "_7267": ["AbstractShaftAdvancedSystemDeflection"],
        "_7268": ["AbstractShaftOrHousingAdvancedSystemDeflection"],
        "_7269": [
            "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection"
        ],
        "_7270": ["AdvancedSystemDeflection"],
        "_7271": ["AdvancedSystemDeflectionOptions"],
        "_7272": ["AdvancedSystemDeflectionSubAnalysis"],
        "_7273": ["AGMAGleasonConicalGearAdvancedSystemDeflection"],
        "_7274": ["AGMAGleasonConicalGearMeshAdvancedSystemDeflection"],
        "_7275": ["AGMAGleasonConicalGearSetAdvancedSystemDeflection"],
        "_7276": ["AssemblyAdvancedSystemDeflection"],
        "_7277": ["BearingAdvancedSystemDeflection"],
        "_7278": ["BeltConnectionAdvancedSystemDeflection"],
        "_7279": ["BeltDriveAdvancedSystemDeflection"],
        "_7280": ["BevelDifferentialGearAdvancedSystemDeflection"],
        "_7281": ["BevelDifferentialGearMeshAdvancedSystemDeflection"],
        "_7282": ["BevelDifferentialGearSetAdvancedSystemDeflection"],
        "_7283": ["BevelDifferentialPlanetGearAdvancedSystemDeflection"],
        "_7284": ["BevelDifferentialSunGearAdvancedSystemDeflection"],
        "_7285": ["BevelGearAdvancedSystemDeflection"],
        "_7286": ["BevelGearMeshAdvancedSystemDeflection"],
        "_7287": ["BevelGearSetAdvancedSystemDeflection"],
        "_7288": ["BoltAdvancedSystemDeflection"],
        "_7289": ["BoltedJointAdvancedSystemDeflection"],
        "_7290": ["ClutchAdvancedSystemDeflection"],
        "_7291": ["ClutchConnectionAdvancedSystemDeflection"],
        "_7292": ["ClutchHalfAdvancedSystemDeflection"],
        "_7293": ["CoaxialConnectionAdvancedSystemDeflection"],
        "_7294": ["ComponentAdvancedSystemDeflection"],
        "_7295": ["ConceptCouplingAdvancedSystemDeflection"],
        "_7296": ["ConceptCouplingConnectionAdvancedSystemDeflection"],
        "_7297": ["ConceptCouplingHalfAdvancedSystemDeflection"],
        "_7298": ["ConceptGearAdvancedSystemDeflection"],
        "_7299": ["ConceptGearMeshAdvancedSystemDeflection"],
        "_7300": ["ConceptGearSetAdvancedSystemDeflection"],
        "_7301": ["ConicalGearAdvancedSystemDeflection"],
        "_7302": ["ConicalGearMeshAdvancedSystemDeflection"],
        "_7303": ["ConicalGearSetAdvancedSystemDeflection"],
        "_7304": ["ConnectionAdvancedSystemDeflection"],
        "_7305": ["ConnectorAdvancedSystemDeflection"],
        "_7306": ["ContactChartPerToothPass"],
        "_7307": ["CouplingAdvancedSystemDeflection"],
        "_7308": ["CouplingConnectionAdvancedSystemDeflection"],
        "_7309": ["CouplingHalfAdvancedSystemDeflection"],
        "_7310": ["CVTAdvancedSystemDeflection"],
        "_7311": ["CVTBeltConnectionAdvancedSystemDeflection"],
        "_7312": ["CVTPulleyAdvancedSystemDeflection"],
        "_7313": ["CycloidalAssemblyAdvancedSystemDeflection"],
        "_7314": ["CycloidalDiscAdvancedSystemDeflection"],
        "_7315": ["CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection"],
        "_7316": ["CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection"],
        "_7317": ["CylindricalGearAdvancedSystemDeflection"],
        "_7318": ["CylindricalGearMeshAdvancedSystemDeflection"],
        "_7319": ["CylindricalGearSetAdvancedSystemDeflection"],
        "_7320": ["CylindricalMeshedGearAdvancedSystemDeflection"],
        "_7321": ["CylindricalPlanetGearAdvancedSystemDeflection"],
        "_7322": ["DatumAdvancedSystemDeflection"],
        "_7323": ["ExternalCADModelAdvancedSystemDeflection"],
        "_7324": ["FaceGearAdvancedSystemDeflection"],
        "_7325": ["FaceGearMeshAdvancedSystemDeflection"],
        "_7326": ["FaceGearSetAdvancedSystemDeflection"],
        "_7327": ["FEPartAdvancedSystemDeflection"],
        "_7328": ["FlexiblePinAssemblyAdvancedSystemDeflection"],
        "_7329": ["GearAdvancedSystemDeflection"],
        "_7330": ["GearMeshAdvancedSystemDeflection"],
        "_7331": ["GearSetAdvancedSystemDeflection"],
        "_7332": ["GuideDxfModelAdvancedSystemDeflection"],
        "_7333": ["HypoidGearAdvancedSystemDeflection"],
        "_7334": ["HypoidGearMeshAdvancedSystemDeflection"],
        "_7335": ["HypoidGearSetAdvancedSystemDeflection"],
        "_7336": ["InterMountableComponentConnectionAdvancedSystemDeflection"],
        "_7337": ["KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection"],
        "_7338": ["KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection"],
        "_7339": ["KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection"],
        "_7340": ["KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection"],
        "_7341": ["KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection"],
        "_7342": ["KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection"],
        "_7343": ["KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection"],
        "_7344": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection"
        ],
        "_7345": ["KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection"],
        "_7346": ["UseLtcaInAsdOption"],
        "_7347": ["MassDiscAdvancedSystemDeflection"],
        "_7348": ["MeasurementComponentAdvancedSystemDeflection"],
        "_7349": ["MountableComponentAdvancedSystemDeflection"],
        "_7350": ["OilSealAdvancedSystemDeflection"],
        "_7351": ["PartAdvancedSystemDeflection"],
        "_7352": ["PartToPartShearCouplingAdvancedSystemDeflection"],
        "_7353": ["PartToPartShearCouplingConnectionAdvancedSystemDeflection"],
        "_7354": ["PartToPartShearCouplingHalfAdvancedSystemDeflection"],
        "_7355": ["PlanetaryConnectionAdvancedSystemDeflection"],
        "_7356": ["PlanetaryGearSetAdvancedSystemDeflection"],
        "_7357": ["PlanetCarrierAdvancedSystemDeflection"],
        "_7358": ["PointLoadAdvancedSystemDeflection"],
        "_7359": ["PowerLoadAdvancedSystemDeflection"],
        "_7360": ["PulleyAdvancedSystemDeflection"],
        "_7361": ["RingPinsAdvancedSystemDeflection"],
        "_7362": ["RingPinsToDiscConnectionAdvancedSystemDeflection"],
        "_7363": ["RollingRingAdvancedSystemDeflection"],
        "_7364": ["RollingRingAssemblyAdvancedSystemDeflection"],
        "_7365": ["RollingRingConnectionAdvancedSystemDeflection"],
        "_7366": ["RootAssemblyAdvancedSystemDeflection"],
        "_7367": ["ShaftAdvancedSystemDeflection"],
        "_7368": ["ShaftHubConnectionAdvancedSystemDeflection"],
        "_7369": ["ShaftToMountableComponentConnectionAdvancedSystemDeflection"],
        "_7370": ["SpecialisedAssemblyAdvancedSystemDeflection"],
        "_7371": ["SpiralBevelGearAdvancedSystemDeflection"],
        "_7372": ["SpiralBevelGearMeshAdvancedSystemDeflection"],
        "_7373": ["SpiralBevelGearSetAdvancedSystemDeflection"],
        "_7374": ["SpringDamperAdvancedSystemDeflection"],
        "_7375": ["SpringDamperConnectionAdvancedSystemDeflection"],
        "_7376": ["SpringDamperHalfAdvancedSystemDeflection"],
        "_7377": ["StraightBevelDiffGearAdvancedSystemDeflection"],
        "_7378": ["StraightBevelDiffGearMeshAdvancedSystemDeflection"],
        "_7379": ["StraightBevelDiffGearSetAdvancedSystemDeflection"],
        "_7380": ["StraightBevelGearAdvancedSystemDeflection"],
        "_7381": ["StraightBevelGearMeshAdvancedSystemDeflection"],
        "_7382": ["StraightBevelGearSetAdvancedSystemDeflection"],
        "_7383": ["StraightBevelPlanetGearAdvancedSystemDeflection"],
        "_7384": ["StraightBevelSunGearAdvancedSystemDeflection"],
        "_7385": ["SynchroniserAdvancedSystemDeflection"],
        "_7386": ["SynchroniserHalfAdvancedSystemDeflection"],
        "_7387": ["SynchroniserPartAdvancedSystemDeflection"],
        "_7388": ["SynchroniserSleeveAdvancedSystemDeflection"],
        "_7389": ["TorqueConverterAdvancedSystemDeflection"],
        "_7390": ["TorqueConverterConnectionAdvancedSystemDeflection"],
        "_7391": ["TorqueConverterPumpAdvancedSystemDeflection"],
        "_7392": ["TorqueConverterTurbineAdvancedSystemDeflection"],
        "_7393": ["TransmissionErrorToOtherPowerLoad"],
        "_7394": ["UnbalancedMassAdvancedSystemDeflection"],
        "_7395": ["VirtualComponentAdvancedSystemDeflection"],
        "_7396": ["WormGearAdvancedSystemDeflection"],
        "_7397": ["WormGearMeshAdvancedSystemDeflection"],
        "_7398": ["WormGearSetAdvancedSystemDeflection"],
        "_7399": ["ZerolBevelGearAdvancedSystemDeflection"],
        "_7400": ["ZerolBevelGearMeshAdvancedSystemDeflection"],
        "_7401": ["ZerolBevelGearSetAdvancedSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyAdvancedSystemDeflection",
    "AbstractShaftAdvancedSystemDeflection",
    "AbstractShaftOrHousingAdvancedSystemDeflection",
    "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
    "AdvancedSystemDeflection",
    "AdvancedSystemDeflectionOptions",
    "AdvancedSystemDeflectionSubAnalysis",
    "AGMAGleasonConicalGearAdvancedSystemDeflection",
    "AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
    "AGMAGleasonConicalGearSetAdvancedSystemDeflection",
    "AssemblyAdvancedSystemDeflection",
    "BearingAdvancedSystemDeflection",
    "BeltConnectionAdvancedSystemDeflection",
    "BeltDriveAdvancedSystemDeflection",
    "BevelDifferentialGearAdvancedSystemDeflection",
    "BevelDifferentialGearMeshAdvancedSystemDeflection",
    "BevelDifferentialGearSetAdvancedSystemDeflection",
    "BevelDifferentialPlanetGearAdvancedSystemDeflection",
    "BevelDifferentialSunGearAdvancedSystemDeflection",
    "BevelGearAdvancedSystemDeflection",
    "BevelGearMeshAdvancedSystemDeflection",
    "BevelGearSetAdvancedSystemDeflection",
    "BoltAdvancedSystemDeflection",
    "BoltedJointAdvancedSystemDeflection",
    "ClutchAdvancedSystemDeflection",
    "ClutchConnectionAdvancedSystemDeflection",
    "ClutchHalfAdvancedSystemDeflection",
    "CoaxialConnectionAdvancedSystemDeflection",
    "ComponentAdvancedSystemDeflection",
    "ConceptCouplingAdvancedSystemDeflection",
    "ConceptCouplingConnectionAdvancedSystemDeflection",
    "ConceptCouplingHalfAdvancedSystemDeflection",
    "ConceptGearAdvancedSystemDeflection",
    "ConceptGearMeshAdvancedSystemDeflection",
    "ConceptGearSetAdvancedSystemDeflection",
    "ConicalGearAdvancedSystemDeflection",
    "ConicalGearMeshAdvancedSystemDeflection",
    "ConicalGearSetAdvancedSystemDeflection",
    "ConnectionAdvancedSystemDeflection",
    "ConnectorAdvancedSystemDeflection",
    "ContactChartPerToothPass",
    "CouplingAdvancedSystemDeflection",
    "CouplingConnectionAdvancedSystemDeflection",
    "CouplingHalfAdvancedSystemDeflection",
    "CVTAdvancedSystemDeflection",
    "CVTBeltConnectionAdvancedSystemDeflection",
    "CVTPulleyAdvancedSystemDeflection",
    "CycloidalAssemblyAdvancedSystemDeflection",
    "CycloidalDiscAdvancedSystemDeflection",
    "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection",
    "CylindricalGearAdvancedSystemDeflection",
    "CylindricalGearMeshAdvancedSystemDeflection",
    "CylindricalGearSetAdvancedSystemDeflection",
    "CylindricalMeshedGearAdvancedSystemDeflection",
    "CylindricalPlanetGearAdvancedSystemDeflection",
    "DatumAdvancedSystemDeflection",
    "ExternalCADModelAdvancedSystemDeflection",
    "FaceGearAdvancedSystemDeflection",
    "FaceGearMeshAdvancedSystemDeflection",
    "FaceGearSetAdvancedSystemDeflection",
    "FEPartAdvancedSystemDeflection",
    "FlexiblePinAssemblyAdvancedSystemDeflection",
    "GearAdvancedSystemDeflection",
    "GearMeshAdvancedSystemDeflection",
    "GearSetAdvancedSystemDeflection",
    "GuideDxfModelAdvancedSystemDeflection",
    "HypoidGearAdvancedSystemDeflection",
    "HypoidGearMeshAdvancedSystemDeflection",
    "HypoidGearSetAdvancedSystemDeflection",
    "InterMountableComponentConnectionAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
    "UseLtcaInAsdOption",
    "MassDiscAdvancedSystemDeflection",
    "MeasurementComponentAdvancedSystemDeflection",
    "MountableComponentAdvancedSystemDeflection",
    "OilSealAdvancedSystemDeflection",
    "PartAdvancedSystemDeflection",
    "PartToPartShearCouplingAdvancedSystemDeflection",
    "PartToPartShearCouplingConnectionAdvancedSystemDeflection",
    "PartToPartShearCouplingHalfAdvancedSystemDeflection",
    "PlanetaryConnectionAdvancedSystemDeflection",
    "PlanetaryGearSetAdvancedSystemDeflection",
    "PlanetCarrierAdvancedSystemDeflection",
    "PointLoadAdvancedSystemDeflection",
    "PowerLoadAdvancedSystemDeflection",
    "PulleyAdvancedSystemDeflection",
    "RingPinsAdvancedSystemDeflection",
    "RingPinsToDiscConnectionAdvancedSystemDeflection",
    "RollingRingAdvancedSystemDeflection",
    "RollingRingAssemblyAdvancedSystemDeflection",
    "RollingRingConnectionAdvancedSystemDeflection",
    "RootAssemblyAdvancedSystemDeflection",
    "ShaftAdvancedSystemDeflection",
    "ShaftHubConnectionAdvancedSystemDeflection",
    "ShaftToMountableComponentConnectionAdvancedSystemDeflection",
    "SpecialisedAssemblyAdvancedSystemDeflection",
    "SpiralBevelGearAdvancedSystemDeflection",
    "SpiralBevelGearMeshAdvancedSystemDeflection",
    "SpiralBevelGearSetAdvancedSystemDeflection",
    "SpringDamperAdvancedSystemDeflection",
    "SpringDamperConnectionAdvancedSystemDeflection",
    "SpringDamperHalfAdvancedSystemDeflection",
    "StraightBevelDiffGearAdvancedSystemDeflection",
    "StraightBevelDiffGearMeshAdvancedSystemDeflection",
    "StraightBevelDiffGearSetAdvancedSystemDeflection",
    "StraightBevelGearAdvancedSystemDeflection",
    "StraightBevelGearMeshAdvancedSystemDeflection",
    "StraightBevelGearSetAdvancedSystemDeflection",
    "StraightBevelPlanetGearAdvancedSystemDeflection",
    "StraightBevelSunGearAdvancedSystemDeflection",
    "SynchroniserAdvancedSystemDeflection",
    "SynchroniserHalfAdvancedSystemDeflection",
    "SynchroniserPartAdvancedSystemDeflection",
    "SynchroniserSleeveAdvancedSystemDeflection",
    "TorqueConverterAdvancedSystemDeflection",
    "TorqueConverterConnectionAdvancedSystemDeflection",
    "TorqueConverterPumpAdvancedSystemDeflection",
    "TorqueConverterTurbineAdvancedSystemDeflection",
    "TransmissionErrorToOtherPowerLoad",
    "UnbalancedMassAdvancedSystemDeflection",
    "VirtualComponentAdvancedSystemDeflection",
    "WormGearAdvancedSystemDeflection",
    "WormGearMeshAdvancedSystemDeflection",
    "WormGearSetAdvancedSystemDeflection",
    "ZerolBevelGearAdvancedSystemDeflection",
    "ZerolBevelGearMeshAdvancedSystemDeflection",
    "ZerolBevelGearSetAdvancedSystemDeflection",
)
