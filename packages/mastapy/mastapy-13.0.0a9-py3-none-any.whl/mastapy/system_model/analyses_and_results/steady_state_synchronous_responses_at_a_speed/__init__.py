"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3501 import AbstractAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3502 import AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed
    from ._3503 import AbstractShaftSteadyStateSynchronousResponseAtASpeed
    from ._3504 import (
        AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3505 import AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3506 import AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3507 import AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
    from ._3508 import AssemblySteadyStateSynchronousResponseAtASpeed
    from ._3509 import BearingSteadyStateSynchronousResponseAtASpeed
    from ._3510 import BeltConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3511 import BeltDriveSteadyStateSynchronousResponseAtASpeed
    from ._3512 import BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3513 import BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3514 import BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
    from ._3515 import BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed
    from ._3516 import BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed
    from ._3517 import BevelGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3518 import BevelGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3519 import BevelGearSteadyStateSynchronousResponseAtASpeed
    from ._3520 import BoltedJointSteadyStateSynchronousResponseAtASpeed
    from ._3521 import BoltSteadyStateSynchronousResponseAtASpeed
    from ._3522 import ClutchConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3523 import ClutchHalfSteadyStateSynchronousResponseAtASpeed
    from ._3524 import ClutchSteadyStateSynchronousResponseAtASpeed
    from ._3525 import CoaxialConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3526 import ComponentSteadyStateSynchronousResponseAtASpeed
    from ._3527 import ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3528 import ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed
    from ._3529 import ConceptCouplingSteadyStateSynchronousResponseAtASpeed
    from ._3530 import ConceptGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3531 import ConceptGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3532 import ConceptGearSteadyStateSynchronousResponseAtASpeed
    from ._3533 import ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3534 import ConicalGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3535 import ConicalGearSteadyStateSynchronousResponseAtASpeed
    from ._3536 import ConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3537 import ConnectorSteadyStateSynchronousResponseAtASpeed
    from ._3538 import CouplingConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3539 import CouplingHalfSteadyStateSynchronousResponseAtASpeed
    from ._3540 import CouplingSteadyStateSynchronousResponseAtASpeed
    from ._3541 import CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3542 import CVTPulleySteadyStateSynchronousResponseAtASpeed
    from ._3543 import CVTSteadyStateSynchronousResponseAtASpeed
    from ._3544 import CycloidalAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3545 import (
        CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3546 import (
        CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3547 import CycloidalDiscSteadyStateSynchronousResponseAtASpeed
    from ._3548 import CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3549 import CylindricalGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3550 import CylindricalGearSteadyStateSynchronousResponseAtASpeed
    from ._3551 import CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed
    from ._3552 import DatumSteadyStateSynchronousResponseAtASpeed
    from ._3553 import ExternalCADModelSteadyStateSynchronousResponseAtASpeed
    from ._3554 import FaceGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3555 import FaceGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3556 import FaceGearSteadyStateSynchronousResponseAtASpeed
    from ._3557 import FEPartSteadyStateSynchronousResponseAtASpeed
    from ._3558 import FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3559 import GearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3560 import GearSetSteadyStateSynchronousResponseAtASpeed
    from ._3561 import GearSteadyStateSynchronousResponseAtASpeed
    from ._3562 import GuideDxfModelSteadyStateSynchronousResponseAtASpeed
    from ._3563 import HypoidGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3564 import HypoidGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3565 import HypoidGearSteadyStateSynchronousResponseAtASpeed
    from ._3566 import (
        InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3567 import (
        KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3568 import (
        KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3569 import (
        KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3570 import (
        KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3571 import (
        KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3572 import (
        KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3573 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3574 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3575 import (
        KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3576 import MassDiscSteadyStateSynchronousResponseAtASpeed
    from ._3577 import MeasurementComponentSteadyStateSynchronousResponseAtASpeed
    from ._3578 import MountableComponentSteadyStateSynchronousResponseAtASpeed
    from ._3579 import OilSealSteadyStateSynchronousResponseAtASpeed
    from ._3580 import PartSteadyStateSynchronousResponseAtASpeed
    from ._3581 import (
        PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3582 import PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed
    from ._3583 import PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed
    from ._3584 import PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3585 import PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3586 import PlanetCarrierSteadyStateSynchronousResponseAtASpeed
    from ._3587 import PointLoadSteadyStateSynchronousResponseAtASpeed
    from ._3588 import PowerLoadSteadyStateSynchronousResponseAtASpeed
    from ._3589 import PulleySteadyStateSynchronousResponseAtASpeed
    from ._3590 import RingPinsSteadyStateSynchronousResponseAtASpeed
    from ._3591 import RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3592 import RollingRingAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3593 import RollingRingConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3594 import RollingRingSteadyStateSynchronousResponseAtASpeed
    from ._3595 import RootAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3596 import ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3597 import ShaftSteadyStateSynchronousResponseAtASpeed
    from ._3598 import (
        ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3599 import SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
    from ._3600 import SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3601 import SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3602 import SpiralBevelGearSteadyStateSynchronousResponseAtASpeed
    from ._3603 import SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3604 import SpringDamperHalfSteadyStateSynchronousResponseAtASpeed
    from ._3605 import SpringDamperSteadyStateSynchronousResponseAtASpeed
    from ._3606 import SteadyStateSynchronousResponseAtASpeed
    from ._3607 import StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3608 import StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3609 import StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
    from ._3610 import StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3611 import StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3612 import StraightBevelGearSteadyStateSynchronousResponseAtASpeed
    from ._3613 import StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed
    from ._3614 import StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed
    from ._3615 import SynchroniserHalfSteadyStateSynchronousResponseAtASpeed
    from ._3616 import SynchroniserPartSteadyStateSynchronousResponseAtASpeed
    from ._3617 import SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed
    from ._3618 import SynchroniserSteadyStateSynchronousResponseAtASpeed
    from ._3619 import TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed
    from ._3620 import TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed
    from ._3621 import TorqueConverterSteadyStateSynchronousResponseAtASpeed
    from ._3622 import TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed
    from ._3623 import UnbalancedMassSteadyStateSynchronousResponseAtASpeed
    from ._3624 import VirtualComponentSteadyStateSynchronousResponseAtASpeed
    from ._3625 import WormGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3626 import WormGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3627 import WormGearSteadyStateSynchronousResponseAtASpeed
    from ._3628 import ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed
    from ._3629 import ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed
    from ._3630 import ZerolBevelGearSteadyStateSynchronousResponseAtASpeed
else:
    import_structure = {
        "_3501": ["AbstractAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3502": ["AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed"],
        "_3503": ["AbstractShaftSteadyStateSynchronousResponseAtASpeed"],
        "_3504": [
            "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3505": ["AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3506": ["AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3507": ["AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed"],
        "_3508": ["AssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3509": ["BearingSteadyStateSynchronousResponseAtASpeed"],
        "_3510": ["BeltConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3511": ["BeltDriveSteadyStateSynchronousResponseAtASpeed"],
        "_3512": ["BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3513": ["BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3514": ["BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed"],
        "_3515": ["BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed"],
        "_3516": ["BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed"],
        "_3517": ["BevelGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3518": ["BevelGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3519": ["BevelGearSteadyStateSynchronousResponseAtASpeed"],
        "_3520": ["BoltedJointSteadyStateSynchronousResponseAtASpeed"],
        "_3521": ["BoltSteadyStateSynchronousResponseAtASpeed"],
        "_3522": ["ClutchConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3523": ["ClutchHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3524": ["ClutchSteadyStateSynchronousResponseAtASpeed"],
        "_3525": ["CoaxialConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3526": ["ComponentSteadyStateSynchronousResponseAtASpeed"],
        "_3527": ["ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3528": ["ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3529": ["ConceptCouplingSteadyStateSynchronousResponseAtASpeed"],
        "_3530": ["ConceptGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3531": ["ConceptGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3532": ["ConceptGearSteadyStateSynchronousResponseAtASpeed"],
        "_3533": ["ConicalGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3534": ["ConicalGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3535": ["ConicalGearSteadyStateSynchronousResponseAtASpeed"],
        "_3536": ["ConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3537": ["ConnectorSteadyStateSynchronousResponseAtASpeed"],
        "_3538": ["CouplingConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3539": ["CouplingHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3540": ["CouplingSteadyStateSynchronousResponseAtASpeed"],
        "_3541": ["CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3542": ["CVTPulleySteadyStateSynchronousResponseAtASpeed"],
        "_3543": ["CVTSteadyStateSynchronousResponseAtASpeed"],
        "_3544": ["CycloidalAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3545": [
            "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3546": [
            "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3547": ["CycloidalDiscSteadyStateSynchronousResponseAtASpeed"],
        "_3548": ["CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3549": ["CylindricalGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3550": ["CylindricalGearSteadyStateSynchronousResponseAtASpeed"],
        "_3551": ["CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed"],
        "_3552": ["DatumSteadyStateSynchronousResponseAtASpeed"],
        "_3553": ["ExternalCADModelSteadyStateSynchronousResponseAtASpeed"],
        "_3554": ["FaceGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3555": ["FaceGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3556": ["FaceGearSteadyStateSynchronousResponseAtASpeed"],
        "_3557": ["FEPartSteadyStateSynchronousResponseAtASpeed"],
        "_3558": ["FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3559": ["GearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3560": ["GearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3561": ["GearSteadyStateSynchronousResponseAtASpeed"],
        "_3562": ["GuideDxfModelSteadyStateSynchronousResponseAtASpeed"],
        "_3563": ["HypoidGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3564": ["HypoidGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3565": ["HypoidGearSteadyStateSynchronousResponseAtASpeed"],
        "_3566": [
            "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3567": [
            "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3568": [
            "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3569": [
            "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3570": [
            "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3571": [
            "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3572": [
            "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3573": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3574": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3575": [
            "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3576": ["MassDiscSteadyStateSynchronousResponseAtASpeed"],
        "_3577": ["MeasurementComponentSteadyStateSynchronousResponseAtASpeed"],
        "_3578": ["MountableComponentSteadyStateSynchronousResponseAtASpeed"],
        "_3579": ["OilSealSteadyStateSynchronousResponseAtASpeed"],
        "_3580": ["PartSteadyStateSynchronousResponseAtASpeed"],
        "_3581": [
            "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3582": ["PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3583": ["PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed"],
        "_3584": ["PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3585": ["PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3586": ["PlanetCarrierSteadyStateSynchronousResponseAtASpeed"],
        "_3587": ["PointLoadSteadyStateSynchronousResponseAtASpeed"],
        "_3588": ["PowerLoadSteadyStateSynchronousResponseAtASpeed"],
        "_3589": ["PulleySteadyStateSynchronousResponseAtASpeed"],
        "_3590": ["RingPinsSteadyStateSynchronousResponseAtASpeed"],
        "_3591": ["RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3592": ["RollingRingAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3593": ["RollingRingConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3594": ["RollingRingSteadyStateSynchronousResponseAtASpeed"],
        "_3595": ["RootAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3596": ["ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3597": ["ShaftSteadyStateSynchronousResponseAtASpeed"],
        "_3598": [
            "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3599": ["SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed"],
        "_3600": ["SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3601": ["SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3602": ["SpiralBevelGearSteadyStateSynchronousResponseAtASpeed"],
        "_3603": ["SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3604": ["SpringDamperHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3605": ["SpringDamperSteadyStateSynchronousResponseAtASpeed"],
        "_3606": ["SteadyStateSynchronousResponseAtASpeed"],
        "_3607": ["StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3608": ["StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3609": ["StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed"],
        "_3610": ["StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3611": ["StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3612": ["StraightBevelGearSteadyStateSynchronousResponseAtASpeed"],
        "_3613": ["StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed"],
        "_3614": ["StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed"],
        "_3615": ["SynchroniserHalfSteadyStateSynchronousResponseAtASpeed"],
        "_3616": ["SynchroniserPartSteadyStateSynchronousResponseAtASpeed"],
        "_3617": ["SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed"],
        "_3618": ["SynchroniserSteadyStateSynchronousResponseAtASpeed"],
        "_3619": ["TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed"],
        "_3620": ["TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed"],
        "_3621": ["TorqueConverterSteadyStateSynchronousResponseAtASpeed"],
        "_3622": ["TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed"],
        "_3623": ["UnbalancedMassSteadyStateSynchronousResponseAtASpeed"],
        "_3624": ["VirtualComponentSteadyStateSynchronousResponseAtASpeed"],
        "_3625": ["WormGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3626": ["WormGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3627": ["WormGearSteadyStateSynchronousResponseAtASpeed"],
        "_3628": ["ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed"],
        "_3629": ["ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed"],
        "_3630": ["ZerolBevelGearSteadyStateSynchronousResponseAtASpeed"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblySteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed",
    "AssemblySteadyStateSynchronousResponseAtASpeed",
    "BearingSteadyStateSynchronousResponseAtASpeed",
    "BeltConnectionSteadyStateSynchronousResponseAtASpeed",
    "BeltDriveSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed",
    "BevelGearMeshSteadyStateSynchronousResponseAtASpeed",
    "BevelGearSetSteadyStateSynchronousResponseAtASpeed",
    "BevelGearSteadyStateSynchronousResponseAtASpeed",
    "BoltedJointSteadyStateSynchronousResponseAtASpeed",
    "BoltSteadyStateSynchronousResponseAtASpeed",
    "ClutchConnectionSteadyStateSynchronousResponseAtASpeed",
    "ClutchHalfSteadyStateSynchronousResponseAtASpeed",
    "ClutchSteadyStateSynchronousResponseAtASpeed",
    "CoaxialConnectionSteadyStateSynchronousResponseAtASpeed",
    "ComponentSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearMeshSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearSetSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearMeshSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearSetSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearSteadyStateSynchronousResponseAtASpeed",
    "ConnectionSteadyStateSynchronousResponseAtASpeed",
    "ConnectorSteadyStateSynchronousResponseAtASpeed",
    "CouplingConnectionSteadyStateSynchronousResponseAtASpeed",
    "CouplingHalfSteadyStateSynchronousResponseAtASpeed",
    "CouplingSteadyStateSynchronousResponseAtASpeed",
    "CVTBeltConnectionSteadyStateSynchronousResponseAtASpeed",
    "CVTPulleySteadyStateSynchronousResponseAtASpeed",
    "CVTSteadyStateSynchronousResponseAtASpeed",
    "CycloidalAssemblySteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearMeshSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearSetSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearSteadyStateSynchronousResponseAtASpeed",
    "CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed",
    "DatumSteadyStateSynchronousResponseAtASpeed",
    "ExternalCADModelSteadyStateSynchronousResponseAtASpeed",
    "FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
    "FaceGearSetSteadyStateSynchronousResponseAtASpeed",
    "FaceGearSteadyStateSynchronousResponseAtASpeed",
    "FEPartSteadyStateSynchronousResponseAtASpeed",
    "FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed",
    "GearMeshSteadyStateSynchronousResponseAtASpeed",
    "GearSetSteadyStateSynchronousResponseAtASpeed",
    "GearSteadyStateSynchronousResponseAtASpeed",
    "GuideDxfModelSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearSetSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearSteadyStateSynchronousResponseAtASpeed",
    "InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
    "MassDiscSteadyStateSynchronousResponseAtASpeed",
    "MeasurementComponentSteadyStateSynchronousResponseAtASpeed",
    "MountableComponentSteadyStateSynchronousResponseAtASpeed",
    "OilSealSteadyStateSynchronousResponseAtASpeed",
    "PartSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingConnectionSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed",
    "PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed",
    "PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed",
    "PlanetCarrierSteadyStateSynchronousResponseAtASpeed",
    "PointLoadSteadyStateSynchronousResponseAtASpeed",
    "PowerLoadSteadyStateSynchronousResponseAtASpeed",
    "PulleySteadyStateSynchronousResponseAtASpeed",
    "RingPinsSteadyStateSynchronousResponseAtASpeed",
    "RingPinsToDiscConnectionSteadyStateSynchronousResponseAtASpeed",
    "RollingRingAssemblySteadyStateSynchronousResponseAtASpeed",
    "RollingRingConnectionSteadyStateSynchronousResponseAtASpeed",
    "RollingRingSteadyStateSynchronousResponseAtASpeed",
    "RootAssemblySteadyStateSynchronousResponseAtASpeed",
    "ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed",
    "ShaftSteadyStateSynchronousResponseAtASpeed",
    "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
    "SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperConnectionSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperHalfSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperSteadyStateSynchronousResponseAtASpeed",
    "SteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserHalfSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserPartSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterConnectionSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed",
    "UnbalancedMassSteadyStateSynchronousResponseAtASpeed",
    "VirtualComponentSteadyStateSynchronousResponseAtASpeed",
    "WormGearMeshSteadyStateSynchronousResponseAtASpeed",
    "WormGearSetSteadyStateSynchronousResponseAtASpeed",
    "WormGearSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearSteadyStateSynchronousResponseAtASpeed",
)
