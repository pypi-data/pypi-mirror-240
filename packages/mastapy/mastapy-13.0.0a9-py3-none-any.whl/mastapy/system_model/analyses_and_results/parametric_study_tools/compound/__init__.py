"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4439 import AbstractAssemblyCompoundParametricStudyTool
    from ._4440 import AbstractShaftCompoundParametricStudyTool
    from ._4441 import AbstractShaftOrHousingCompoundParametricStudyTool
    from ._4442 import (
        AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool,
    )
    from ._4443 import AGMAGleasonConicalGearCompoundParametricStudyTool
    from ._4444 import AGMAGleasonConicalGearMeshCompoundParametricStudyTool
    from ._4445 import AGMAGleasonConicalGearSetCompoundParametricStudyTool
    from ._4446 import AssemblyCompoundParametricStudyTool
    from ._4447 import BearingCompoundParametricStudyTool
    from ._4448 import BeltConnectionCompoundParametricStudyTool
    from ._4449 import BeltDriveCompoundParametricStudyTool
    from ._4450 import BevelDifferentialGearCompoundParametricStudyTool
    from ._4451 import BevelDifferentialGearMeshCompoundParametricStudyTool
    from ._4452 import BevelDifferentialGearSetCompoundParametricStudyTool
    from ._4453 import BevelDifferentialPlanetGearCompoundParametricStudyTool
    from ._4454 import BevelDifferentialSunGearCompoundParametricStudyTool
    from ._4455 import BevelGearCompoundParametricStudyTool
    from ._4456 import BevelGearMeshCompoundParametricStudyTool
    from ._4457 import BevelGearSetCompoundParametricStudyTool
    from ._4458 import BoltCompoundParametricStudyTool
    from ._4459 import BoltedJointCompoundParametricStudyTool
    from ._4460 import ClutchCompoundParametricStudyTool
    from ._4461 import ClutchConnectionCompoundParametricStudyTool
    from ._4462 import ClutchHalfCompoundParametricStudyTool
    from ._4463 import CoaxialConnectionCompoundParametricStudyTool
    from ._4464 import ComponentCompoundParametricStudyTool
    from ._4465 import ConceptCouplingCompoundParametricStudyTool
    from ._4466 import ConceptCouplingConnectionCompoundParametricStudyTool
    from ._4467 import ConceptCouplingHalfCompoundParametricStudyTool
    from ._4468 import ConceptGearCompoundParametricStudyTool
    from ._4469 import ConceptGearMeshCompoundParametricStudyTool
    from ._4470 import ConceptGearSetCompoundParametricStudyTool
    from ._4471 import ConicalGearCompoundParametricStudyTool
    from ._4472 import ConicalGearMeshCompoundParametricStudyTool
    from ._4473 import ConicalGearSetCompoundParametricStudyTool
    from ._4474 import ConnectionCompoundParametricStudyTool
    from ._4475 import ConnectorCompoundParametricStudyTool
    from ._4476 import CouplingCompoundParametricStudyTool
    from ._4477 import CouplingConnectionCompoundParametricStudyTool
    from ._4478 import CouplingHalfCompoundParametricStudyTool
    from ._4479 import CVTBeltConnectionCompoundParametricStudyTool
    from ._4480 import CVTCompoundParametricStudyTool
    from ._4481 import CVTPulleyCompoundParametricStudyTool
    from ._4482 import CycloidalAssemblyCompoundParametricStudyTool
    from ._4483 import CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool
    from ._4484 import CycloidalDiscCompoundParametricStudyTool
    from ._4485 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool,
    )
    from ._4486 import CylindricalGearCompoundParametricStudyTool
    from ._4487 import CylindricalGearMeshCompoundParametricStudyTool
    from ._4488 import CylindricalGearSetCompoundParametricStudyTool
    from ._4489 import CylindricalPlanetGearCompoundParametricStudyTool
    from ._4490 import DatumCompoundParametricStudyTool
    from ._4491 import ExternalCADModelCompoundParametricStudyTool
    from ._4492 import FaceGearCompoundParametricStudyTool
    from ._4493 import FaceGearMeshCompoundParametricStudyTool
    from ._4494 import FaceGearSetCompoundParametricStudyTool
    from ._4495 import FEPartCompoundParametricStudyTool
    from ._4496 import FlexiblePinAssemblyCompoundParametricStudyTool
    from ._4497 import GearCompoundParametricStudyTool
    from ._4498 import GearMeshCompoundParametricStudyTool
    from ._4499 import GearSetCompoundParametricStudyTool
    from ._4500 import GuideDxfModelCompoundParametricStudyTool
    from ._4501 import HypoidGearCompoundParametricStudyTool
    from ._4502 import HypoidGearMeshCompoundParametricStudyTool
    from ._4503 import HypoidGearSetCompoundParametricStudyTool
    from ._4504 import InterMountableComponentConnectionCompoundParametricStudyTool
    from ._4505 import KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
    from ._4506 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool,
    )
    from ._4507 import KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
    from ._4508 import KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
    from ._4509 import KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool
    from ._4510 import KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
    from ._4511 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool,
    )
    from ._4512 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool,
    )
    from ._4513 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool,
    )
    from ._4514 import MassDiscCompoundParametricStudyTool
    from ._4515 import MeasurementComponentCompoundParametricStudyTool
    from ._4516 import MountableComponentCompoundParametricStudyTool
    from ._4517 import OilSealCompoundParametricStudyTool
    from ._4518 import PartCompoundParametricStudyTool
    from ._4519 import PartToPartShearCouplingCompoundParametricStudyTool
    from ._4520 import PartToPartShearCouplingConnectionCompoundParametricStudyTool
    from ._4521 import PartToPartShearCouplingHalfCompoundParametricStudyTool
    from ._4522 import PlanetaryConnectionCompoundParametricStudyTool
    from ._4523 import PlanetaryGearSetCompoundParametricStudyTool
    from ._4524 import PlanetCarrierCompoundParametricStudyTool
    from ._4525 import PointLoadCompoundParametricStudyTool
    from ._4526 import PowerLoadCompoundParametricStudyTool
    from ._4527 import PulleyCompoundParametricStudyTool
    from ._4528 import RingPinsCompoundParametricStudyTool
    from ._4529 import RingPinsToDiscConnectionCompoundParametricStudyTool
    from ._4530 import RollingRingAssemblyCompoundParametricStudyTool
    from ._4531 import RollingRingCompoundParametricStudyTool
    from ._4532 import RollingRingConnectionCompoundParametricStudyTool
    from ._4533 import RootAssemblyCompoundParametricStudyTool
    from ._4534 import ShaftCompoundParametricStudyTool
    from ._4535 import ShaftHubConnectionCompoundParametricStudyTool
    from ._4536 import ShaftToMountableComponentConnectionCompoundParametricStudyTool
    from ._4537 import SpecialisedAssemblyCompoundParametricStudyTool
    from ._4538 import SpiralBevelGearCompoundParametricStudyTool
    from ._4539 import SpiralBevelGearMeshCompoundParametricStudyTool
    from ._4540 import SpiralBevelGearSetCompoundParametricStudyTool
    from ._4541 import SpringDamperCompoundParametricStudyTool
    from ._4542 import SpringDamperConnectionCompoundParametricStudyTool
    from ._4543 import SpringDamperHalfCompoundParametricStudyTool
    from ._4544 import StraightBevelDiffGearCompoundParametricStudyTool
    from ._4545 import StraightBevelDiffGearMeshCompoundParametricStudyTool
    from ._4546 import StraightBevelDiffGearSetCompoundParametricStudyTool
    from ._4547 import StraightBevelGearCompoundParametricStudyTool
    from ._4548 import StraightBevelGearMeshCompoundParametricStudyTool
    from ._4549 import StraightBevelGearSetCompoundParametricStudyTool
    from ._4550 import StraightBevelPlanetGearCompoundParametricStudyTool
    from ._4551 import StraightBevelSunGearCompoundParametricStudyTool
    from ._4552 import SynchroniserCompoundParametricStudyTool
    from ._4553 import SynchroniserHalfCompoundParametricStudyTool
    from ._4554 import SynchroniserPartCompoundParametricStudyTool
    from ._4555 import SynchroniserSleeveCompoundParametricStudyTool
    from ._4556 import TorqueConverterCompoundParametricStudyTool
    from ._4557 import TorqueConverterConnectionCompoundParametricStudyTool
    from ._4558 import TorqueConverterPumpCompoundParametricStudyTool
    from ._4559 import TorqueConverterTurbineCompoundParametricStudyTool
    from ._4560 import UnbalancedMassCompoundParametricStudyTool
    from ._4561 import VirtualComponentCompoundParametricStudyTool
    from ._4562 import WormGearCompoundParametricStudyTool
    from ._4563 import WormGearMeshCompoundParametricStudyTool
    from ._4564 import WormGearSetCompoundParametricStudyTool
    from ._4565 import ZerolBevelGearCompoundParametricStudyTool
    from ._4566 import ZerolBevelGearMeshCompoundParametricStudyTool
    from ._4567 import ZerolBevelGearSetCompoundParametricStudyTool
else:
    import_structure = {
        "_4439": ["AbstractAssemblyCompoundParametricStudyTool"],
        "_4440": ["AbstractShaftCompoundParametricStudyTool"],
        "_4441": ["AbstractShaftOrHousingCompoundParametricStudyTool"],
        "_4442": [
            "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool"
        ],
        "_4443": ["AGMAGleasonConicalGearCompoundParametricStudyTool"],
        "_4444": ["AGMAGleasonConicalGearMeshCompoundParametricStudyTool"],
        "_4445": ["AGMAGleasonConicalGearSetCompoundParametricStudyTool"],
        "_4446": ["AssemblyCompoundParametricStudyTool"],
        "_4447": ["BearingCompoundParametricStudyTool"],
        "_4448": ["BeltConnectionCompoundParametricStudyTool"],
        "_4449": ["BeltDriveCompoundParametricStudyTool"],
        "_4450": ["BevelDifferentialGearCompoundParametricStudyTool"],
        "_4451": ["BevelDifferentialGearMeshCompoundParametricStudyTool"],
        "_4452": ["BevelDifferentialGearSetCompoundParametricStudyTool"],
        "_4453": ["BevelDifferentialPlanetGearCompoundParametricStudyTool"],
        "_4454": ["BevelDifferentialSunGearCompoundParametricStudyTool"],
        "_4455": ["BevelGearCompoundParametricStudyTool"],
        "_4456": ["BevelGearMeshCompoundParametricStudyTool"],
        "_4457": ["BevelGearSetCompoundParametricStudyTool"],
        "_4458": ["BoltCompoundParametricStudyTool"],
        "_4459": ["BoltedJointCompoundParametricStudyTool"],
        "_4460": ["ClutchCompoundParametricStudyTool"],
        "_4461": ["ClutchConnectionCompoundParametricStudyTool"],
        "_4462": ["ClutchHalfCompoundParametricStudyTool"],
        "_4463": ["CoaxialConnectionCompoundParametricStudyTool"],
        "_4464": ["ComponentCompoundParametricStudyTool"],
        "_4465": ["ConceptCouplingCompoundParametricStudyTool"],
        "_4466": ["ConceptCouplingConnectionCompoundParametricStudyTool"],
        "_4467": ["ConceptCouplingHalfCompoundParametricStudyTool"],
        "_4468": ["ConceptGearCompoundParametricStudyTool"],
        "_4469": ["ConceptGearMeshCompoundParametricStudyTool"],
        "_4470": ["ConceptGearSetCompoundParametricStudyTool"],
        "_4471": ["ConicalGearCompoundParametricStudyTool"],
        "_4472": ["ConicalGearMeshCompoundParametricStudyTool"],
        "_4473": ["ConicalGearSetCompoundParametricStudyTool"],
        "_4474": ["ConnectionCompoundParametricStudyTool"],
        "_4475": ["ConnectorCompoundParametricStudyTool"],
        "_4476": ["CouplingCompoundParametricStudyTool"],
        "_4477": ["CouplingConnectionCompoundParametricStudyTool"],
        "_4478": ["CouplingHalfCompoundParametricStudyTool"],
        "_4479": ["CVTBeltConnectionCompoundParametricStudyTool"],
        "_4480": ["CVTCompoundParametricStudyTool"],
        "_4481": ["CVTPulleyCompoundParametricStudyTool"],
        "_4482": ["CycloidalAssemblyCompoundParametricStudyTool"],
        "_4483": ["CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool"],
        "_4484": ["CycloidalDiscCompoundParametricStudyTool"],
        "_4485": ["CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool"],
        "_4486": ["CylindricalGearCompoundParametricStudyTool"],
        "_4487": ["CylindricalGearMeshCompoundParametricStudyTool"],
        "_4488": ["CylindricalGearSetCompoundParametricStudyTool"],
        "_4489": ["CylindricalPlanetGearCompoundParametricStudyTool"],
        "_4490": ["DatumCompoundParametricStudyTool"],
        "_4491": ["ExternalCADModelCompoundParametricStudyTool"],
        "_4492": ["FaceGearCompoundParametricStudyTool"],
        "_4493": ["FaceGearMeshCompoundParametricStudyTool"],
        "_4494": ["FaceGearSetCompoundParametricStudyTool"],
        "_4495": ["FEPartCompoundParametricStudyTool"],
        "_4496": ["FlexiblePinAssemblyCompoundParametricStudyTool"],
        "_4497": ["GearCompoundParametricStudyTool"],
        "_4498": ["GearMeshCompoundParametricStudyTool"],
        "_4499": ["GearSetCompoundParametricStudyTool"],
        "_4500": ["GuideDxfModelCompoundParametricStudyTool"],
        "_4501": ["HypoidGearCompoundParametricStudyTool"],
        "_4502": ["HypoidGearMeshCompoundParametricStudyTool"],
        "_4503": ["HypoidGearSetCompoundParametricStudyTool"],
        "_4504": ["InterMountableComponentConnectionCompoundParametricStudyTool"],
        "_4505": ["KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool"],
        "_4506": ["KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool"],
        "_4507": ["KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool"],
        "_4508": ["KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool"],
        "_4509": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool"],
        "_4510": ["KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool"],
        "_4511": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool"],
        "_4512": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool"
        ],
        "_4513": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool"
        ],
        "_4514": ["MassDiscCompoundParametricStudyTool"],
        "_4515": ["MeasurementComponentCompoundParametricStudyTool"],
        "_4516": ["MountableComponentCompoundParametricStudyTool"],
        "_4517": ["OilSealCompoundParametricStudyTool"],
        "_4518": ["PartCompoundParametricStudyTool"],
        "_4519": ["PartToPartShearCouplingCompoundParametricStudyTool"],
        "_4520": ["PartToPartShearCouplingConnectionCompoundParametricStudyTool"],
        "_4521": ["PartToPartShearCouplingHalfCompoundParametricStudyTool"],
        "_4522": ["PlanetaryConnectionCompoundParametricStudyTool"],
        "_4523": ["PlanetaryGearSetCompoundParametricStudyTool"],
        "_4524": ["PlanetCarrierCompoundParametricStudyTool"],
        "_4525": ["PointLoadCompoundParametricStudyTool"],
        "_4526": ["PowerLoadCompoundParametricStudyTool"],
        "_4527": ["PulleyCompoundParametricStudyTool"],
        "_4528": ["RingPinsCompoundParametricStudyTool"],
        "_4529": ["RingPinsToDiscConnectionCompoundParametricStudyTool"],
        "_4530": ["RollingRingAssemblyCompoundParametricStudyTool"],
        "_4531": ["RollingRingCompoundParametricStudyTool"],
        "_4532": ["RollingRingConnectionCompoundParametricStudyTool"],
        "_4533": ["RootAssemblyCompoundParametricStudyTool"],
        "_4534": ["ShaftCompoundParametricStudyTool"],
        "_4535": ["ShaftHubConnectionCompoundParametricStudyTool"],
        "_4536": ["ShaftToMountableComponentConnectionCompoundParametricStudyTool"],
        "_4537": ["SpecialisedAssemblyCompoundParametricStudyTool"],
        "_4538": ["SpiralBevelGearCompoundParametricStudyTool"],
        "_4539": ["SpiralBevelGearMeshCompoundParametricStudyTool"],
        "_4540": ["SpiralBevelGearSetCompoundParametricStudyTool"],
        "_4541": ["SpringDamperCompoundParametricStudyTool"],
        "_4542": ["SpringDamperConnectionCompoundParametricStudyTool"],
        "_4543": ["SpringDamperHalfCompoundParametricStudyTool"],
        "_4544": ["StraightBevelDiffGearCompoundParametricStudyTool"],
        "_4545": ["StraightBevelDiffGearMeshCompoundParametricStudyTool"],
        "_4546": ["StraightBevelDiffGearSetCompoundParametricStudyTool"],
        "_4547": ["StraightBevelGearCompoundParametricStudyTool"],
        "_4548": ["StraightBevelGearMeshCompoundParametricStudyTool"],
        "_4549": ["StraightBevelGearSetCompoundParametricStudyTool"],
        "_4550": ["StraightBevelPlanetGearCompoundParametricStudyTool"],
        "_4551": ["StraightBevelSunGearCompoundParametricStudyTool"],
        "_4552": ["SynchroniserCompoundParametricStudyTool"],
        "_4553": ["SynchroniserHalfCompoundParametricStudyTool"],
        "_4554": ["SynchroniserPartCompoundParametricStudyTool"],
        "_4555": ["SynchroniserSleeveCompoundParametricStudyTool"],
        "_4556": ["TorqueConverterCompoundParametricStudyTool"],
        "_4557": ["TorqueConverterConnectionCompoundParametricStudyTool"],
        "_4558": ["TorqueConverterPumpCompoundParametricStudyTool"],
        "_4559": ["TorqueConverterTurbineCompoundParametricStudyTool"],
        "_4560": ["UnbalancedMassCompoundParametricStudyTool"],
        "_4561": ["VirtualComponentCompoundParametricStudyTool"],
        "_4562": ["WormGearCompoundParametricStudyTool"],
        "_4563": ["WormGearMeshCompoundParametricStudyTool"],
        "_4564": ["WormGearSetCompoundParametricStudyTool"],
        "_4565": ["ZerolBevelGearCompoundParametricStudyTool"],
        "_4566": ["ZerolBevelGearMeshCompoundParametricStudyTool"],
        "_4567": ["ZerolBevelGearSetCompoundParametricStudyTool"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundParametricStudyTool",
    "AbstractShaftCompoundParametricStudyTool",
    "AbstractShaftOrHousingCompoundParametricStudyTool",
    "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",
    "AGMAGleasonConicalGearCompoundParametricStudyTool",
    "AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
    "AGMAGleasonConicalGearSetCompoundParametricStudyTool",
    "AssemblyCompoundParametricStudyTool",
    "BearingCompoundParametricStudyTool",
    "BeltConnectionCompoundParametricStudyTool",
    "BeltDriveCompoundParametricStudyTool",
    "BevelDifferentialGearCompoundParametricStudyTool",
    "BevelDifferentialGearMeshCompoundParametricStudyTool",
    "BevelDifferentialGearSetCompoundParametricStudyTool",
    "BevelDifferentialPlanetGearCompoundParametricStudyTool",
    "BevelDifferentialSunGearCompoundParametricStudyTool",
    "BevelGearCompoundParametricStudyTool",
    "BevelGearMeshCompoundParametricStudyTool",
    "BevelGearSetCompoundParametricStudyTool",
    "BoltCompoundParametricStudyTool",
    "BoltedJointCompoundParametricStudyTool",
    "ClutchCompoundParametricStudyTool",
    "ClutchConnectionCompoundParametricStudyTool",
    "ClutchHalfCompoundParametricStudyTool",
    "CoaxialConnectionCompoundParametricStudyTool",
    "ComponentCompoundParametricStudyTool",
    "ConceptCouplingCompoundParametricStudyTool",
    "ConceptCouplingConnectionCompoundParametricStudyTool",
    "ConceptCouplingHalfCompoundParametricStudyTool",
    "ConceptGearCompoundParametricStudyTool",
    "ConceptGearMeshCompoundParametricStudyTool",
    "ConceptGearSetCompoundParametricStudyTool",
    "ConicalGearCompoundParametricStudyTool",
    "ConicalGearMeshCompoundParametricStudyTool",
    "ConicalGearSetCompoundParametricStudyTool",
    "ConnectionCompoundParametricStudyTool",
    "ConnectorCompoundParametricStudyTool",
    "CouplingCompoundParametricStudyTool",
    "CouplingConnectionCompoundParametricStudyTool",
    "CouplingHalfCompoundParametricStudyTool",
    "CVTBeltConnectionCompoundParametricStudyTool",
    "CVTCompoundParametricStudyTool",
    "CVTPulleyCompoundParametricStudyTool",
    "CycloidalAssemblyCompoundParametricStudyTool",
    "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
    "CycloidalDiscCompoundParametricStudyTool",
    "CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool",
    "CylindricalGearCompoundParametricStudyTool",
    "CylindricalGearMeshCompoundParametricStudyTool",
    "CylindricalGearSetCompoundParametricStudyTool",
    "CylindricalPlanetGearCompoundParametricStudyTool",
    "DatumCompoundParametricStudyTool",
    "ExternalCADModelCompoundParametricStudyTool",
    "FaceGearCompoundParametricStudyTool",
    "FaceGearMeshCompoundParametricStudyTool",
    "FaceGearSetCompoundParametricStudyTool",
    "FEPartCompoundParametricStudyTool",
    "FlexiblePinAssemblyCompoundParametricStudyTool",
    "GearCompoundParametricStudyTool",
    "GearMeshCompoundParametricStudyTool",
    "GearSetCompoundParametricStudyTool",
    "GuideDxfModelCompoundParametricStudyTool",
    "HypoidGearCompoundParametricStudyTool",
    "HypoidGearMeshCompoundParametricStudyTool",
    "HypoidGearSetCompoundParametricStudyTool",
    "InterMountableComponentConnectionCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool",
    "MassDiscCompoundParametricStudyTool",
    "MeasurementComponentCompoundParametricStudyTool",
    "MountableComponentCompoundParametricStudyTool",
    "OilSealCompoundParametricStudyTool",
    "PartCompoundParametricStudyTool",
    "PartToPartShearCouplingCompoundParametricStudyTool",
    "PartToPartShearCouplingConnectionCompoundParametricStudyTool",
    "PartToPartShearCouplingHalfCompoundParametricStudyTool",
    "PlanetaryConnectionCompoundParametricStudyTool",
    "PlanetaryGearSetCompoundParametricStudyTool",
    "PlanetCarrierCompoundParametricStudyTool",
    "PointLoadCompoundParametricStudyTool",
    "PowerLoadCompoundParametricStudyTool",
    "PulleyCompoundParametricStudyTool",
    "RingPinsCompoundParametricStudyTool",
    "RingPinsToDiscConnectionCompoundParametricStudyTool",
    "RollingRingAssemblyCompoundParametricStudyTool",
    "RollingRingCompoundParametricStudyTool",
    "RollingRingConnectionCompoundParametricStudyTool",
    "RootAssemblyCompoundParametricStudyTool",
    "ShaftCompoundParametricStudyTool",
    "ShaftHubConnectionCompoundParametricStudyTool",
    "ShaftToMountableComponentConnectionCompoundParametricStudyTool",
    "SpecialisedAssemblyCompoundParametricStudyTool",
    "SpiralBevelGearCompoundParametricStudyTool",
    "SpiralBevelGearMeshCompoundParametricStudyTool",
    "SpiralBevelGearSetCompoundParametricStudyTool",
    "SpringDamperCompoundParametricStudyTool",
    "SpringDamperConnectionCompoundParametricStudyTool",
    "SpringDamperHalfCompoundParametricStudyTool",
    "StraightBevelDiffGearCompoundParametricStudyTool",
    "StraightBevelDiffGearMeshCompoundParametricStudyTool",
    "StraightBevelDiffGearSetCompoundParametricStudyTool",
    "StraightBevelGearCompoundParametricStudyTool",
    "StraightBevelGearMeshCompoundParametricStudyTool",
    "StraightBevelGearSetCompoundParametricStudyTool",
    "StraightBevelPlanetGearCompoundParametricStudyTool",
    "StraightBevelSunGearCompoundParametricStudyTool",
    "SynchroniserCompoundParametricStudyTool",
    "SynchroniserHalfCompoundParametricStudyTool",
    "SynchroniserPartCompoundParametricStudyTool",
    "SynchroniserSleeveCompoundParametricStudyTool",
    "TorqueConverterCompoundParametricStudyTool",
    "TorqueConverterConnectionCompoundParametricStudyTool",
    "TorqueConverterPumpCompoundParametricStudyTool",
    "TorqueConverterTurbineCompoundParametricStudyTool",
    "UnbalancedMassCompoundParametricStudyTool",
    "VirtualComponentCompoundParametricStudyTool",
    "WormGearCompoundParametricStudyTool",
    "WormGearMeshCompoundParametricStudyTool",
    "WormGearSetCompoundParametricStudyTool",
    "ZerolBevelGearCompoundParametricStudyTool",
    "ZerolBevelGearMeshCompoundParametricStudyTool",
    "ZerolBevelGearSetCompoundParametricStudyTool",
)
