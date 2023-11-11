"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3631 import AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3632 import AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3633 import (
        AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3634 import (
        AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3635 import (
        AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3636 import (
        AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3637 import (
        AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3638 import AssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3639 import BearingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3640 import BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3641 import BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3642 import (
        BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3643 import (
        BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3644 import (
        BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3645 import (
        BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3646 import (
        BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3647 import BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3648 import BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3649 import BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3650 import BoltCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3651 import BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3652 import ClutchCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3653 import ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3654 import ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3655 import CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3656 import ComponentCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3657 import ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3658 import (
        ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3659 import ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3660 import ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3661 import ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3662 import ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3663 import ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3664 import ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3665 import ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3666 import ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3667 import ConnectorCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3668 import CouplingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3669 import CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3670 import CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3671 import CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3672 import CVTCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3673 import CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3674 import CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3675 import (
        CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3676 import CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3677 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3678 import CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3679 import CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3680 import CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3681 import (
        CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3682 import DatumCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3683 import ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3684 import FaceGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3685 import FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3686 import FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3687 import FEPartCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3688 import FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3689 import GearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3690 import GearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3691 import GearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3692 import GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3693 import HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3694 import HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3695 import HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3696 import (
        InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3697 import (
        KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3698 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3699 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3700 import (
        KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3701 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3702 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3703 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3704 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3705 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3706 import MassDiscCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3707 import (
        MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3708 import MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3709 import OilSealCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3710 import PartCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3711 import (
        PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3712 import (
        PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3713 import (
        PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3714 import PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3715 import PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3716 import PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3717 import PointLoadCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3718 import PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3719 import PulleyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3720 import RingPinsCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3721 import (
        RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3722 import RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3723 import RollingRingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3724 import (
        RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3725 import RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3726 import ShaftCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3727 import ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3728 import (
        ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3729 import SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3730 import SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3731 import SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3732 import SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3733 import SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3734 import (
        SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3735 import SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3736 import (
        StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3737 import (
        StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3738 import (
        StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3739 import StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3740 import (
        StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3741 import (
        StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3742 import (
        StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3743 import (
        StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3744 import SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3745 import SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3746 import SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3747 import SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3748 import TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3749 import (
        TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3750 import TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3751 import (
        TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3752 import UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3753 import VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3754 import WormGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3755 import WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3756 import WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3757 import ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3758 import ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3759 import ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
else:
    import_structure = {
        "_3631": ["AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3632": ["AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3633": [
            "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3634": [
            "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3635": [
            "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3636": [
            "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3637": [
            "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3638": ["AssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3639": ["BearingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3640": ["BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3641": ["BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3642": [
            "BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3643": [
            "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3644": [
            "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3645": [
            "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3646": [
            "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3647": ["BevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3648": ["BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3649": ["BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3650": ["BoltCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3651": ["BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3652": ["ClutchCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3653": ["ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3654": ["ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3655": ["CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3656": ["ComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3657": ["ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3658": [
            "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3659": ["ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3660": ["ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3661": ["ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3662": ["ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3663": ["ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3664": ["ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3665": ["ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3666": ["ConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3667": ["ConnectorCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3668": ["CouplingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3669": ["CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3670": ["CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3671": ["CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3672": ["CVTCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3673": ["CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3674": ["CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3675": [
            "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3676": ["CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3677": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3678": ["CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3679": ["CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3680": ["CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3681": [
            "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3682": ["DatumCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3683": ["ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3684": ["FaceGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3685": ["FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3686": ["FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3687": ["FEPartCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3688": ["FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3689": ["GearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3690": ["GearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3691": ["GearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3692": ["GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3693": ["HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3694": ["HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3695": ["HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3696": [
            "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3697": [
            "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3698": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3699": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3700": [
            "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3701": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3702": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3703": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3704": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3705": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3706": ["MassDiscCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3707": ["MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3708": ["MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3709": ["OilSealCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3710": ["PartCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3711": [
            "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3712": [
            "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3713": [
            "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3714": ["PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3715": ["PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3716": ["PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3717": ["PointLoadCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3718": ["PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3719": ["PulleyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3720": ["RingPinsCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3721": [
            "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3722": ["RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3723": ["RollingRingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3724": [
            "RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3725": ["RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3726": ["ShaftCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3727": ["ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3728": [
            "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3729": ["SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3730": ["SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3731": ["SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3732": ["SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3733": ["SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3734": [
            "SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3735": ["SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3736": [
            "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3737": [
            "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3738": [
            "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3739": ["StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3740": [
            "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3741": ["StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3742": [
            "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3743": ["StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3744": ["SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3745": ["SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3746": ["SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3747": ["SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3748": ["TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3749": [
            "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3750": ["TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3751": [
            "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3752": ["UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3753": ["VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3754": ["WormGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3755": ["WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3756": ["WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3757": ["ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3758": ["ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3759": ["ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "AssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "BearingCompoundSteadyStateSynchronousResponseAtASpeed",
    "BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "BoltCompoundSteadyStateSynchronousResponseAtASpeed",
    "BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed",
    "ClutchCompoundSteadyStateSynchronousResponseAtASpeed",
    "ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed",
    "CouplingCompoundSteadyStateSynchronousResponseAtASpeed",
    "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CVTCompoundSteadyStateSynchronousResponseAtASpeed",
    "CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "DatumCompoundSteadyStateSynchronousResponseAtASpeed",
    "ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed",
    "FaceGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "FEPartCompoundSteadyStateSynchronousResponseAtASpeed",
    "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "GearCompoundSteadyStateSynchronousResponseAtASpeed",
    "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "MassDiscCompoundSteadyStateSynchronousResponseAtASpeed",
    "MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "OilSealCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed",
    "PointLoadCompoundSteadyStateSynchronousResponseAtASpeed",
    "PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed",
    "PulleyCompoundSteadyStateSynchronousResponseAtASpeed",
    "RingPinsCompoundSteadyStateSynchronousResponseAtASpeed",
    "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "RollingRingCompoundSteadyStateSynchronousResponseAtASpeed",
    "RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "ShaftCompoundSteadyStateSynchronousResponseAtASpeed",
    "ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed",
    "UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed",
    "VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "WormGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
)
