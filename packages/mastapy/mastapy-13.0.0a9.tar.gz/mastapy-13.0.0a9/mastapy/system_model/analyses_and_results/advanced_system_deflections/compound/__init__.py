"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7402 import AbstractAssemblyCompoundAdvancedSystemDeflection
    from ._7403 import AbstractShaftCompoundAdvancedSystemDeflection
    from ._7404 import AbstractShaftOrHousingCompoundAdvancedSystemDeflection
    from ._7405 import (
        AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7406 import AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
    from ._7407 import AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
    from ._7408 import AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
    from ._7409 import AssemblyCompoundAdvancedSystemDeflection
    from ._7410 import BearingCompoundAdvancedSystemDeflection
    from ._7411 import BeltConnectionCompoundAdvancedSystemDeflection
    from ._7412 import BeltDriveCompoundAdvancedSystemDeflection
    from ._7413 import BevelDifferentialGearCompoundAdvancedSystemDeflection
    from ._7414 import BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
    from ._7415 import BevelDifferentialGearSetCompoundAdvancedSystemDeflection
    from ._7416 import BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
    from ._7417 import BevelDifferentialSunGearCompoundAdvancedSystemDeflection
    from ._7418 import BevelGearCompoundAdvancedSystemDeflection
    from ._7419 import BevelGearMeshCompoundAdvancedSystemDeflection
    from ._7420 import BevelGearSetCompoundAdvancedSystemDeflection
    from ._7421 import BoltCompoundAdvancedSystemDeflection
    from ._7422 import BoltedJointCompoundAdvancedSystemDeflection
    from ._7423 import ClutchCompoundAdvancedSystemDeflection
    from ._7424 import ClutchConnectionCompoundAdvancedSystemDeflection
    from ._7425 import ClutchHalfCompoundAdvancedSystemDeflection
    from ._7426 import CoaxialConnectionCompoundAdvancedSystemDeflection
    from ._7427 import ComponentCompoundAdvancedSystemDeflection
    from ._7428 import ConceptCouplingCompoundAdvancedSystemDeflection
    from ._7429 import ConceptCouplingConnectionCompoundAdvancedSystemDeflection
    from ._7430 import ConceptCouplingHalfCompoundAdvancedSystemDeflection
    from ._7431 import ConceptGearCompoundAdvancedSystemDeflection
    from ._7432 import ConceptGearMeshCompoundAdvancedSystemDeflection
    from ._7433 import ConceptGearSetCompoundAdvancedSystemDeflection
    from ._7434 import ConicalGearCompoundAdvancedSystemDeflection
    from ._7435 import ConicalGearMeshCompoundAdvancedSystemDeflection
    from ._7436 import ConicalGearSetCompoundAdvancedSystemDeflection
    from ._7437 import ConnectionCompoundAdvancedSystemDeflection
    from ._7438 import ConnectorCompoundAdvancedSystemDeflection
    from ._7439 import CouplingCompoundAdvancedSystemDeflection
    from ._7440 import CouplingConnectionCompoundAdvancedSystemDeflection
    from ._7441 import CouplingHalfCompoundAdvancedSystemDeflection
    from ._7442 import CVTBeltConnectionCompoundAdvancedSystemDeflection
    from ._7443 import CVTCompoundAdvancedSystemDeflection
    from ._7444 import CVTPulleyCompoundAdvancedSystemDeflection
    from ._7445 import CycloidalAssemblyCompoundAdvancedSystemDeflection
    from ._7446 import (
        CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7447 import CycloidalDiscCompoundAdvancedSystemDeflection
    from ._7448 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7449 import CylindricalGearCompoundAdvancedSystemDeflection
    from ._7450 import CylindricalGearMeshCompoundAdvancedSystemDeflection
    from ._7451 import CylindricalGearSetCompoundAdvancedSystemDeflection
    from ._7452 import CylindricalPlanetGearCompoundAdvancedSystemDeflection
    from ._7453 import DatumCompoundAdvancedSystemDeflection
    from ._7454 import ExternalCADModelCompoundAdvancedSystemDeflection
    from ._7455 import FaceGearCompoundAdvancedSystemDeflection
    from ._7456 import FaceGearMeshCompoundAdvancedSystemDeflection
    from ._7457 import FaceGearSetCompoundAdvancedSystemDeflection
    from ._7458 import FEPartCompoundAdvancedSystemDeflection
    from ._7459 import FlexiblePinAssemblyCompoundAdvancedSystemDeflection
    from ._7460 import GearCompoundAdvancedSystemDeflection
    from ._7461 import GearMeshCompoundAdvancedSystemDeflection
    from ._7462 import GearSetCompoundAdvancedSystemDeflection
    from ._7463 import GuideDxfModelCompoundAdvancedSystemDeflection
    from ._7464 import HypoidGearCompoundAdvancedSystemDeflection
    from ._7465 import HypoidGearMeshCompoundAdvancedSystemDeflection
    from ._7466 import HypoidGearSetCompoundAdvancedSystemDeflection
    from ._7467 import InterMountableComponentConnectionCompoundAdvancedSystemDeflection
    from ._7468 import (
        KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection,
    )
    from ._7469 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection,
    )
    from ._7470 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection,
    )
    from ._7471 import (
        KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection,
    )
    from ._7472 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection,
    )
    from ._7473 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection,
    )
    from ._7474 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection,
    )
    from ._7475 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection,
    )
    from ._7476 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection,
    )
    from ._7477 import MassDiscCompoundAdvancedSystemDeflection
    from ._7478 import MeasurementComponentCompoundAdvancedSystemDeflection
    from ._7479 import MountableComponentCompoundAdvancedSystemDeflection
    from ._7480 import OilSealCompoundAdvancedSystemDeflection
    from ._7481 import PartCompoundAdvancedSystemDeflection
    from ._7482 import PartToPartShearCouplingCompoundAdvancedSystemDeflection
    from ._7483 import PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection
    from ._7484 import PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
    from ._7485 import PlanetaryConnectionCompoundAdvancedSystemDeflection
    from ._7486 import PlanetaryGearSetCompoundAdvancedSystemDeflection
    from ._7487 import PlanetCarrierCompoundAdvancedSystemDeflection
    from ._7488 import PointLoadCompoundAdvancedSystemDeflection
    from ._7489 import PowerLoadCompoundAdvancedSystemDeflection
    from ._7490 import PulleyCompoundAdvancedSystemDeflection
    from ._7491 import RingPinsCompoundAdvancedSystemDeflection
    from ._7492 import RingPinsToDiscConnectionCompoundAdvancedSystemDeflection
    from ._7493 import RollingRingAssemblyCompoundAdvancedSystemDeflection
    from ._7494 import RollingRingCompoundAdvancedSystemDeflection
    from ._7495 import RollingRingConnectionCompoundAdvancedSystemDeflection
    from ._7496 import RootAssemblyCompoundAdvancedSystemDeflection
    from ._7497 import ShaftCompoundAdvancedSystemDeflection
    from ._7498 import ShaftHubConnectionCompoundAdvancedSystemDeflection
    from ._7499 import (
        ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7500 import SpecialisedAssemblyCompoundAdvancedSystemDeflection
    from ._7501 import SpiralBevelGearCompoundAdvancedSystemDeflection
    from ._7502 import SpiralBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7503 import SpiralBevelGearSetCompoundAdvancedSystemDeflection
    from ._7504 import SpringDamperCompoundAdvancedSystemDeflection
    from ._7505 import SpringDamperConnectionCompoundAdvancedSystemDeflection
    from ._7506 import SpringDamperHalfCompoundAdvancedSystemDeflection
    from ._7507 import StraightBevelDiffGearCompoundAdvancedSystemDeflection
    from ._7508 import StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection
    from ._7509 import StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
    from ._7510 import StraightBevelGearCompoundAdvancedSystemDeflection
    from ._7511 import StraightBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7512 import StraightBevelGearSetCompoundAdvancedSystemDeflection
    from ._7513 import StraightBevelPlanetGearCompoundAdvancedSystemDeflection
    from ._7514 import StraightBevelSunGearCompoundAdvancedSystemDeflection
    from ._7515 import SynchroniserCompoundAdvancedSystemDeflection
    from ._7516 import SynchroniserHalfCompoundAdvancedSystemDeflection
    from ._7517 import SynchroniserPartCompoundAdvancedSystemDeflection
    from ._7518 import SynchroniserSleeveCompoundAdvancedSystemDeflection
    from ._7519 import TorqueConverterCompoundAdvancedSystemDeflection
    from ._7520 import TorqueConverterConnectionCompoundAdvancedSystemDeflection
    from ._7521 import TorqueConverterPumpCompoundAdvancedSystemDeflection
    from ._7522 import TorqueConverterTurbineCompoundAdvancedSystemDeflection
    from ._7523 import UnbalancedMassCompoundAdvancedSystemDeflection
    from ._7524 import VirtualComponentCompoundAdvancedSystemDeflection
    from ._7525 import WormGearCompoundAdvancedSystemDeflection
    from ._7526 import WormGearMeshCompoundAdvancedSystemDeflection
    from ._7527 import WormGearSetCompoundAdvancedSystemDeflection
    from ._7528 import ZerolBevelGearCompoundAdvancedSystemDeflection
    from ._7529 import ZerolBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7530 import ZerolBevelGearSetCompoundAdvancedSystemDeflection
else:
    import_structure = {
        "_7402": ["AbstractAssemblyCompoundAdvancedSystemDeflection"],
        "_7403": ["AbstractShaftCompoundAdvancedSystemDeflection"],
        "_7404": ["AbstractShaftOrHousingCompoundAdvancedSystemDeflection"],
        "_7405": [
            "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7406": ["AGMAGleasonConicalGearCompoundAdvancedSystemDeflection"],
        "_7407": ["AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection"],
        "_7408": ["AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection"],
        "_7409": ["AssemblyCompoundAdvancedSystemDeflection"],
        "_7410": ["BearingCompoundAdvancedSystemDeflection"],
        "_7411": ["BeltConnectionCompoundAdvancedSystemDeflection"],
        "_7412": ["BeltDriveCompoundAdvancedSystemDeflection"],
        "_7413": ["BevelDifferentialGearCompoundAdvancedSystemDeflection"],
        "_7414": ["BevelDifferentialGearMeshCompoundAdvancedSystemDeflection"],
        "_7415": ["BevelDifferentialGearSetCompoundAdvancedSystemDeflection"],
        "_7416": ["BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection"],
        "_7417": ["BevelDifferentialSunGearCompoundAdvancedSystemDeflection"],
        "_7418": ["BevelGearCompoundAdvancedSystemDeflection"],
        "_7419": ["BevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7420": ["BevelGearSetCompoundAdvancedSystemDeflection"],
        "_7421": ["BoltCompoundAdvancedSystemDeflection"],
        "_7422": ["BoltedJointCompoundAdvancedSystemDeflection"],
        "_7423": ["ClutchCompoundAdvancedSystemDeflection"],
        "_7424": ["ClutchConnectionCompoundAdvancedSystemDeflection"],
        "_7425": ["ClutchHalfCompoundAdvancedSystemDeflection"],
        "_7426": ["CoaxialConnectionCompoundAdvancedSystemDeflection"],
        "_7427": ["ComponentCompoundAdvancedSystemDeflection"],
        "_7428": ["ConceptCouplingCompoundAdvancedSystemDeflection"],
        "_7429": ["ConceptCouplingConnectionCompoundAdvancedSystemDeflection"],
        "_7430": ["ConceptCouplingHalfCompoundAdvancedSystemDeflection"],
        "_7431": ["ConceptGearCompoundAdvancedSystemDeflection"],
        "_7432": ["ConceptGearMeshCompoundAdvancedSystemDeflection"],
        "_7433": ["ConceptGearSetCompoundAdvancedSystemDeflection"],
        "_7434": ["ConicalGearCompoundAdvancedSystemDeflection"],
        "_7435": ["ConicalGearMeshCompoundAdvancedSystemDeflection"],
        "_7436": ["ConicalGearSetCompoundAdvancedSystemDeflection"],
        "_7437": ["ConnectionCompoundAdvancedSystemDeflection"],
        "_7438": ["ConnectorCompoundAdvancedSystemDeflection"],
        "_7439": ["CouplingCompoundAdvancedSystemDeflection"],
        "_7440": ["CouplingConnectionCompoundAdvancedSystemDeflection"],
        "_7441": ["CouplingHalfCompoundAdvancedSystemDeflection"],
        "_7442": ["CVTBeltConnectionCompoundAdvancedSystemDeflection"],
        "_7443": ["CVTCompoundAdvancedSystemDeflection"],
        "_7444": ["CVTPulleyCompoundAdvancedSystemDeflection"],
        "_7445": ["CycloidalAssemblyCompoundAdvancedSystemDeflection"],
        "_7446": [
            "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7447": ["CycloidalDiscCompoundAdvancedSystemDeflection"],
        "_7448": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7449": ["CylindricalGearCompoundAdvancedSystemDeflection"],
        "_7450": ["CylindricalGearMeshCompoundAdvancedSystemDeflection"],
        "_7451": ["CylindricalGearSetCompoundAdvancedSystemDeflection"],
        "_7452": ["CylindricalPlanetGearCompoundAdvancedSystemDeflection"],
        "_7453": ["DatumCompoundAdvancedSystemDeflection"],
        "_7454": ["ExternalCADModelCompoundAdvancedSystemDeflection"],
        "_7455": ["FaceGearCompoundAdvancedSystemDeflection"],
        "_7456": ["FaceGearMeshCompoundAdvancedSystemDeflection"],
        "_7457": ["FaceGearSetCompoundAdvancedSystemDeflection"],
        "_7458": ["FEPartCompoundAdvancedSystemDeflection"],
        "_7459": ["FlexiblePinAssemblyCompoundAdvancedSystemDeflection"],
        "_7460": ["GearCompoundAdvancedSystemDeflection"],
        "_7461": ["GearMeshCompoundAdvancedSystemDeflection"],
        "_7462": ["GearSetCompoundAdvancedSystemDeflection"],
        "_7463": ["GuideDxfModelCompoundAdvancedSystemDeflection"],
        "_7464": ["HypoidGearCompoundAdvancedSystemDeflection"],
        "_7465": ["HypoidGearMeshCompoundAdvancedSystemDeflection"],
        "_7466": ["HypoidGearSetCompoundAdvancedSystemDeflection"],
        "_7467": ["InterMountableComponentConnectionCompoundAdvancedSystemDeflection"],
        "_7468": [
            "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection"
        ],
        "_7469": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection"
        ],
        "_7470": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection"
        ],
        "_7471": ["KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection"],
        "_7472": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection"
        ],
        "_7473": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection"
        ],
        "_7474": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection"
        ],
        "_7475": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection"
        ],
        "_7476": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection"
        ],
        "_7477": ["MassDiscCompoundAdvancedSystemDeflection"],
        "_7478": ["MeasurementComponentCompoundAdvancedSystemDeflection"],
        "_7479": ["MountableComponentCompoundAdvancedSystemDeflection"],
        "_7480": ["OilSealCompoundAdvancedSystemDeflection"],
        "_7481": ["PartCompoundAdvancedSystemDeflection"],
        "_7482": ["PartToPartShearCouplingCompoundAdvancedSystemDeflection"],
        "_7483": ["PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection"],
        "_7484": ["PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection"],
        "_7485": ["PlanetaryConnectionCompoundAdvancedSystemDeflection"],
        "_7486": ["PlanetaryGearSetCompoundAdvancedSystemDeflection"],
        "_7487": ["PlanetCarrierCompoundAdvancedSystemDeflection"],
        "_7488": ["PointLoadCompoundAdvancedSystemDeflection"],
        "_7489": ["PowerLoadCompoundAdvancedSystemDeflection"],
        "_7490": ["PulleyCompoundAdvancedSystemDeflection"],
        "_7491": ["RingPinsCompoundAdvancedSystemDeflection"],
        "_7492": ["RingPinsToDiscConnectionCompoundAdvancedSystemDeflection"],
        "_7493": ["RollingRingAssemblyCompoundAdvancedSystemDeflection"],
        "_7494": ["RollingRingCompoundAdvancedSystemDeflection"],
        "_7495": ["RollingRingConnectionCompoundAdvancedSystemDeflection"],
        "_7496": ["RootAssemblyCompoundAdvancedSystemDeflection"],
        "_7497": ["ShaftCompoundAdvancedSystemDeflection"],
        "_7498": ["ShaftHubConnectionCompoundAdvancedSystemDeflection"],
        "_7499": [
            "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7500": ["SpecialisedAssemblyCompoundAdvancedSystemDeflection"],
        "_7501": ["SpiralBevelGearCompoundAdvancedSystemDeflection"],
        "_7502": ["SpiralBevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7503": ["SpiralBevelGearSetCompoundAdvancedSystemDeflection"],
        "_7504": ["SpringDamperCompoundAdvancedSystemDeflection"],
        "_7505": ["SpringDamperConnectionCompoundAdvancedSystemDeflection"],
        "_7506": ["SpringDamperHalfCompoundAdvancedSystemDeflection"],
        "_7507": ["StraightBevelDiffGearCompoundAdvancedSystemDeflection"],
        "_7508": ["StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection"],
        "_7509": ["StraightBevelDiffGearSetCompoundAdvancedSystemDeflection"],
        "_7510": ["StraightBevelGearCompoundAdvancedSystemDeflection"],
        "_7511": ["StraightBevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7512": ["StraightBevelGearSetCompoundAdvancedSystemDeflection"],
        "_7513": ["StraightBevelPlanetGearCompoundAdvancedSystemDeflection"],
        "_7514": ["StraightBevelSunGearCompoundAdvancedSystemDeflection"],
        "_7515": ["SynchroniserCompoundAdvancedSystemDeflection"],
        "_7516": ["SynchroniserHalfCompoundAdvancedSystemDeflection"],
        "_7517": ["SynchroniserPartCompoundAdvancedSystemDeflection"],
        "_7518": ["SynchroniserSleeveCompoundAdvancedSystemDeflection"],
        "_7519": ["TorqueConverterCompoundAdvancedSystemDeflection"],
        "_7520": ["TorqueConverterConnectionCompoundAdvancedSystemDeflection"],
        "_7521": ["TorqueConverterPumpCompoundAdvancedSystemDeflection"],
        "_7522": ["TorqueConverterTurbineCompoundAdvancedSystemDeflection"],
        "_7523": ["UnbalancedMassCompoundAdvancedSystemDeflection"],
        "_7524": ["VirtualComponentCompoundAdvancedSystemDeflection"],
        "_7525": ["WormGearCompoundAdvancedSystemDeflection"],
        "_7526": ["WormGearMeshCompoundAdvancedSystemDeflection"],
        "_7527": ["WormGearSetCompoundAdvancedSystemDeflection"],
        "_7528": ["ZerolBevelGearCompoundAdvancedSystemDeflection"],
        "_7529": ["ZerolBevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7530": ["ZerolBevelGearSetCompoundAdvancedSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundAdvancedSystemDeflection",
    "AbstractShaftCompoundAdvancedSystemDeflection",
    "AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
    "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
    "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
    "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
    "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
    "AssemblyCompoundAdvancedSystemDeflection",
    "BearingCompoundAdvancedSystemDeflection",
    "BeltConnectionCompoundAdvancedSystemDeflection",
    "BeltDriveCompoundAdvancedSystemDeflection",
    "BevelDifferentialGearCompoundAdvancedSystemDeflection",
    "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection",
    "BevelDifferentialGearSetCompoundAdvancedSystemDeflection",
    "BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection",
    "BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
    "BevelGearCompoundAdvancedSystemDeflection",
    "BevelGearMeshCompoundAdvancedSystemDeflection",
    "BevelGearSetCompoundAdvancedSystemDeflection",
    "BoltCompoundAdvancedSystemDeflection",
    "BoltedJointCompoundAdvancedSystemDeflection",
    "ClutchCompoundAdvancedSystemDeflection",
    "ClutchConnectionCompoundAdvancedSystemDeflection",
    "ClutchHalfCompoundAdvancedSystemDeflection",
    "CoaxialConnectionCompoundAdvancedSystemDeflection",
    "ComponentCompoundAdvancedSystemDeflection",
    "ConceptCouplingCompoundAdvancedSystemDeflection",
    "ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
    "ConceptCouplingHalfCompoundAdvancedSystemDeflection",
    "ConceptGearCompoundAdvancedSystemDeflection",
    "ConceptGearMeshCompoundAdvancedSystemDeflection",
    "ConceptGearSetCompoundAdvancedSystemDeflection",
    "ConicalGearCompoundAdvancedSystemDeflection",
    "ConicalGearMeshCompoundAdvancedSystemDeflection",
    "ConicalGearSetCompoundAdvancedSystemDeflection",
    "ConnectionCompoundAdvancedSystemDeflection",
    "ConnectorCompoundAdvancedSystemDeflection",
    "CouplingCompoundAdvancedSystemDeflection",
    "CouplingConnectionCompoundAdvancedSystemDeflection",
    "CouplingHalfCompoundAdvancedSystemDeflection",
    "CVTBeltConnectionCompoundAdvancedSystemDeflection",
    "CVTCompoundAdvancedSystemDeflection",
    "CVTPulleyCompoundAdvancedSystemDeflection",
    "CycloidalAssemblyCompoundAdvancedSystemDeflection",
    "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
    "CycloidalDiscCompoundAdvancedSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection",
    "CylindricalGearCompoundAdvancedSystemDeflection",
    "CylindricalGearMeshCompoundAdvancedSystemDeflection",
    "CylindricalGearSetCompoundAdvancedSystemDeflection",
    "CylindricalPlanetGearCompoundAdvancedSystemDeflection",
    "DatumCompoundAdvancedSystemDeflection",
    "ExternalCADModelCompoundAdvancedSystemDeflection",
    "FaceGearCompoundAdvancedSystemDeflection",
    "FaceGearMeshCompoundAdvancedSystemDeflection",
    "FaceGearSetCompoundAdvancedSystemDeflection",
    "FEPartCompoundAdvancedSystemDeflection",
    "FlexiblePinAssemblyCompoundAdvancedSystemDeflection",
    "GearCompoundAdvancedSystemDeflection",
    "GearMeshCompoundAdvancedSystemDeflection",
    "GearSetCompoundAdvancedSystemDeflection",
    "GuideDxfModelCompoundAdvancedSystemDeflection",
    "HypoidGearCompoundAdvancedSystemDeflection",
    "HypoidGearMeshCompoundAdvancedSystemDeflection",
    "HypoidGearSetCompoundAdvancedSystemDeflection",
    "InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection",
    "MassDiscCompoundAdvancedSystemDeflection",
    "MeasurementComponentCompoundAdvancedSystemDeflection",
    "MountableComponentCompoundAdvancedSystemDeflection",
    "OilSealCompoundAdvancedSystemDeflection",
    "PartCompoundAdvancedSystemDeflection",
    "PartToPartShearCouplingCompoundAdvancedSystemDeflection",
    "PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection",
    "PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection",
    "PlanetaryConnectionCompoundAdvancedSystemDeflection",
    "PlanetaryGearSetCompoundAdvancedSystemDeflection",
    "PlanetCarrierCompoundAdvancedSystemDeflection",
    "PointLoadCompoundAdvancedSystemDeflection",
    "PowerLoadCompoundAdvancedSystemDeflection",
    "PulleyCompoundAdvancedSystemDeflection",
    "RingPinsCompoundAdvancedSystemDeflection",
    "RingPinsToDiscConnectionCompoundAdvancedSystemDeflection",
    "RollingRingAssemblyCompoundAdvancedSystemDeflection",
    "RollingRingCompoundAdvancedSystemDeflection",
    "RollingRingConnectionCompoundAdvancedSystemDeflection",
    "RootAssemblyCompoundAdvancedSystemDeflection",
    "ShaftCompoundAdvancedSystemDeflection",
    "ShaftHubConnectionCompoundAdvancedSystemDeflection",
    "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
    "SpecialisedAssemblyCompoundAdvancedSystemDeflection",
    "SpiralBevelGearCompoundAdvancedSystemDeflection",
    "SpiralBevelGearMeshCompoundAdvancedSystemDeflection",
    "SpiralBevelGearSetCompoundAdvancedSystemDeflection",
    "SpringDamperCompoundAdvancedSystemDeflection",
    "SpringDamperConnectionCompoundAdvancedSystemDeflection",
    "SpringDamperHalfCompoundAdvancedSystemDeflection",
    "StraightBevelDiffGearCompoundAdvancedSystemDeflection",
    "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection",
    "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",
    "StraightBevelGearCompoundAdvancedSystemDeflection",
    "StraightBevelGearMeshCompoundAdvancedSystemDeflection",
    "StraightBevelGearSetCompoundAdvancedSystemDeflection",
    "StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
    "StraightBevelSunGearCompoundAdvancedSystemDeflection",
    "SynchroniserCompoundAdvancedSystemDeflection",
    "SynchroniserHalfCompoundAdvancedSystemDeflection",
    "SynchroniserPartCompoundAdvancedSystemDeflection",
    "SynchroniserSleeveCompoundAdvancedSystemDeflection",
    "TorqueConverterCompoundAdvancedSystemDeflection",
    "TorqueConverterConnectionCompoundAdvancedSystemDeflection",
    "TorqueConverterPumpCompoundAdvancedSystemDeflection",
    "TorqueConverterTurbineCompoundAdvancedSystemDeflection",
    "UnbalancedMassCompoundAdvancedSystemDeflection",
    "VirtualComponentCompoundAdvancedSystemDeflection",
    "WormGearCompoundAdvancedSystemDeflection",
    "WormGearMeshCompoundAdvancedSystemDeflection",
    "WormGearSetCompoundAdvancedSystemDeflection",
    "ZerolBevelGearCompoundAdvancedSystemDeflection",
    "ZerolBevelGearMeshCompoundAdvancedSystemDeflection",
    "ZerolBevelGearSetCompoundAdvancedSystemDeflection",
)
