"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3760 import AbstractAssemblyStabilityAnalysis
    from ._3761 import AbstractShaftOrHousingStabilityAnalysis
    from ._3762 import AbstractShaftStabilityAnalysis
    from ._3763 import AbstractShaftToMountableComponentConnectionStabilityAnalysis
    from ._3764 import AGMAGleasonConicalGearMeshStabilityAnalysis
    from ._3765 import AGMAGleasonConicalGearSetStabilityAnalysis
    from ._3766 import AGMAGleasonConicalGearStabilityAnalysis
    from ._3767 import AssemblyStabilityAnalysis
    from ._3768 import BearingStabilityAnalysis
    from ._3769 import BeltConnectionStabilityAnalysis
    from ._3770 import BeltDriveStabilityAnalysis
    from ._3771 import BevelDifferentialGearMeshStabilityAnalysis
    from ._3772 import BevelDifferentialGearSetStabilityAnalysis
    from ._3773 import BevelDifferentialGearStabilityAnalysis
    from ._3774 import BevelDifferentialPlanetGearStabilityAnalysis
    from ._3775 import BevelDifferentialSunGearStabilityAnalysis
    from ._3776 import BevelGearMeshStabilityAnalysis
    from ._3777 import BevelGearSetStabilityAnalysis
    from ._3778 import BevelGearStabilityAnalysis
    from ._3779 import BoltedJointStabilityAnalysis
    from ._3780 import BoltStabilityAnalysis
    from ._3781 import ClutchConnectionStabilityAnalysis
    from ._3782 import ClutchHalfStabilityAnalysis
    from ._3783 import ClutchStabilityAnalysis
    from ._3784 import CoaxialConnectionStabilityAnalysis
    from ._3785 import ComponentStabilityAnalysis
    from ._3786 import ConceptCouplingConnectionStabilityAnalysis
    from ._3787 import ConceptCouplingHalfStabilityAnalysis
    from ._3788 import ConceptCouplingStabilityAnalysis
    from ._3789 import ConceptGearMeshStabilityAnalysis
    from ._3790 import ConceptGearSetStabilityAnalysis
    from ._3791 import ConceptGearStabilityAnalysis
    from ._3792 import ConicalGearMeshStabilityAnalysis
    from ._3793 import ConicalGearSetStabilityAnalysis
    from ._3794 import ConicalGearStabilityAnalysis
    from ._3795 import ConnectionStabilityAnalysis
    from ._3796 import ConnectorStabilityAnalysis
    from ._3797 import CouplingConnectionStabilityAnalysis
    from ._3798 import CouplingHalfStabilityAnalysis
    from ._3799 import CouplingStabilityAnalysis
    from ._3800 import CriticalSpeed
    from ._3801 import CVTBeltConnectionStabilityAnalysis
    from ._3802 import CVTPulleyStabilityAnalysis
    from ._3803 import CVTStabilityAnalysis
    from ._3804 import CycloidalAssemblyStabilityAnalysis
    from ._3805 import CycloidalDiscCentralBearingConnectionStabilityAnalysis
    from ._3806 import CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis
    from ._3807 import CycloidalDiscStabilityAnalysis
    from ._3808 import CylindricalGearMeshStabilityAnalysis
    from ._3809 import CylindricalGearSetStabilityAnalysis
    from ._3810 import CylindricalGearStabilityAnalysis
    from ._3811 import CylindricalPlanetGearStabilityAnalysis
    from ._3812 import DatumStabilityAnalysis
    from ._3813 import DynamicModelForStabilityAnalysis
    from ._3814 import ExternalCADModelStabilityAnalysis
    from ._3815 import FaceGearMeshStabilityAnalysis
    from ._3816 import FaceGearSetStabilityAnalysis
    from ._3817 import FaceGearStabilityAnalysis
    from ._3818 import FEPartStabilityAnalysis
    from ._3819 import FlexiblePinAssemblyStabilityAnalysis
    from ._3820 import GearMeshStabilityAnalysis
    from ._3821 import GearSetStabilityAnalysis
    from ._3822 import GearStabilityAnalysis
    from ._3823 import GuideDxfModelStabilityAnalysis
    from ._3824 import HypoidGearMeshStabilityAnalysis
    from ._3825 import HypoidGearSetStabilityAnalysis
    from ._3826 import HypoidGearStabilityAnalysis
    from ._3827 import InterMountableComponentConnectionStabilityAnalysis
    from ._3828 import KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis
    from ._3829 import KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
    from ._3830 import KlingelnbergCycloPalloidConicalGearStabilityAnalysis
    from ._3831 import KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis
    from ._3832 import KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
    from ._3833 import KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
    from ._3834 import KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis
    from ._3835 import KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
    from ._3836 import KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
    from ._3837 import MassDiscStabilityAnalysis
    from ._3838 import MeasurementComponentStabilityAnalysis
    from ._3839 import MountableComponentStabilityAnalysis
    from ._3840 import OilSealStabilityAnalysis
    from ._3841 import PartStabilityAnalysis
    from ._3842 import PartToPartShearCouplingConnectionStabilityAnalysis
    from ._3843 import PartToPartShearCouplingHalfStabilityAnalysis
    from ._3844 import PartToPartShearCouplingStabilityAnalysis
    from ._3845 import PlanetaryConnectionStabilityAnalysis
    from ._3846 import PlanetaryGearSetStabilityAnalysis
    from ._3847 import PlanetCarrierStabilityAnalysis
    from ._3848 import PointLoadStabilityAnalysis
    from ._3849 import PowerLoadStabilityAnalysis
    from ._3850 import PulleyStabilityAnalysis
    from ._3851 import RingPinsStabilityAnalysis
    from ._3852 import RingPinsToDiscConnectionStabilityAnalysis
    from ._3853 import RollingRingAssemblyStabilityAnalysis
    from ._3854 import RollingRingConnectionStabilityAnalysis
    from ._3855 import RollingRingStabilityAnalysis
    from ._3856 import RootAssemblyStabilityAnalysis
    from ._3857 import ShaftHubConnectionStabilityAnalysis
    from ._3858 import ShaftStabilityAnalysis
    from ._3859 import ShaftToMountableComponentConnectionStabilityAnalysis
    from ._3860 import SpecialisedAssemblyStabilityAnalysis
    from ._3861 import SpiralBevelGearMeshStabilityAnalysis
    from ._3862 import SpiralBevelGearSetStabilityAnalysis
    from ._3863 import SpiralBevelGearStabilityAnalysis
    from ._3864 import SpringDamperConnectionStabilityAnalysis
    from ._3865 import SpringDamperHalfStabilityAnalysis
    from ._3866 import SpringDamperStabilityAnalysis
    from ._3867 import StabilityAnalysis
    from ._3868 import StabilityAnalysisDrawStyle
    from ._3869 import StabilityAnalysisOptions
    from ._3870 import StraightBevelDiffGearMeshStabilityAnalysis
    from ._3871 import StraightBevelDiffGearSetStabilityAnalysis
    from ._3872 import StraightBevelDiffGearStabilityAnalysis
    from ._3873 import StraightBevelGearMeshStabilityAnalysis
    from ._3874 import StraightBevelGearSetStabilityAnalysis
    from ._3875 import StraightBevelGearStabilityAnalysis
    from ._3876 import StraightBevelPlanetGearStabilityAnalysis
    from ._3877 import StraightBevelSunGearStabilityAnalysis
    from ._3878 import SynchroniserHalfStabilityAnalysis
    from ._3879 import SynchroniserPartStabilityAnalysis
    from ._3880 import SynchroniserSleeveStabilityAnalysis
    from ._3881 import SynchroniserStabilityAnalysis
    from ._3882 import TorqueConverterConnectionStabilityAnalysis
    from ._3883 import TorqueConverterPumpStabilityAnalysis
    from ._3884 import TorqueConverterStabilityAnalysis
    from ._3885 import TorqueConverterTurbineStabilityAnalysis
    from ._3886 import UnbalancedMassStabilityAnalysis
    from ._3887 import VirtualComponentStabilityAnalysis
    from ._3888 import WormGearMeshStabilityAnalysis
    from ._3889 import WormGearSetStabilityAnalysis
    from ._3890 import WormGearStabilityAnalysis
    from ._3891 import ZerolBevelGearMeshStabilityAnalysis
    from ._3892 import ZerolBevelGearSetStabilityAnalysis
    from ._3893 import ZerolBevelGearStabilityAnalysis
else:
    import_structure = {
        "_3760": ["AbstractAssemblyStabilityAnalysis"],
        "_3761": ["AbstractShaftOrHousingStabilityAnalysis"],
        "_3762": ["AbstractShaftStabilityAnalysis"],
        "_3763": ["AbstractShaftToMountableComponentConnectionStabilityAnalysis"],
        "_3764": ["AGMAGleasonConicalGearMeshStabilityAnalysis"],
        "_3765": ["AGMAGleasonConicalGearSetStabilityAnalysis"],
        "_3766": ["AGMAGleasonConicalGearStabilityAnalysis"],
        "_3767": ["AssemblyStabilityAnalysis"],
        "_3768": ["BearingStabilityAnalysis"],
        "_3769": ["BeltConnectionStabilityAnalysis"],
        "_3770": ["BeltDriveStabilityAnalysis"],
        "_3771": ["BevelDifferentialGearMeshStabilityAnalysis"],
        "_3772": ["BevelDifferentialGearSetStabilityAnalysis"],
        "_3773": ["BevelDifferentialGearStabilityAnalysis"],
        "_3774": ["BevelDifferentialPlanetGearStabilityAnalysis"],
        "_3775": ["BevelDifferentialSunGearStabilityAnalysis"],
        "_3776": ["BevelGearMeshStabilityAnalysis"],
        "_3777": ["BevelGearSetStabilityAnalysis"],
        "_3778": ["BevelGearStabilityAnalysis"],
        "_3779": ["BoltedJointStabilityAnalysis"],
        "_3780": ["BoltStabilityAnalysis"],
        "_3781": ["ClutchConnectionStabilityAnalysis"],
        "_3782": ["ClutchHalfStabilityAnalysis"],
        "_3783": ["ClutchStabilityAnalysis"],
        "_3784": ["CoaxialConnectionStabilityAnalysis"],
        "_3785": ["ComponentStabilityAnalysis"],
        "_3786": ["ConceptCouplingConnectionStabilityAnalysis"],
        "_3787": ["ConceptCouplingHalfStabilityAnalysis"],
        "_3788": ["ConceptCouplingStabilityAnalysis"],
        "_3789": ["ConceptGearMeshStabilityAnalysis"],
        "_3790": ["ConceptGearSetStabilityAnalysis"],
        "_3791": ["ConceptGearStabilityAnalysis"],
        "_3792": ["ConicalGearMeshStabilityAnalysis"],
        "_3793": ["ConicalGearSetStabilityAnalysis"],
        "_3794": ["ConicalGearStabilityAnalysis"],
        "_3795": ["ConnectionStabilityAnalysis"],
        "_3796": ["ConnectorStabilityAnalysis"],
        "_3797": ["CouplingConnectionStabilityAnalysis"],
        "_3798": ["CouplingHalfStabilityAnalysis"],
        "_3799": ["CouplingStabilityAnalysis"],
        "_3800": ["CriticalSpeed"],
        "_3801": ["CVTBeltConnectionStabilityAnalysis"],
        "_3802": ["CVTPulleyStabilityAnalysis"],
        "_3803": ["CVTStabilityAnalysis"],
        "_3804": ["CycloidalAssemblyStabilityAnalysis"],
        "_3805": ["CycloidalDiscCentralBearingConnectionStabilityAnalysis"],
        "_3806": ["CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis"],
        "_3807": ["CycloidalDiscStabilityAnalysis"],
        "_3808": ["CylindricalGearMeshStabilityAnalysis"],
        "_3809": ["CylindricalGearSetStabilityAnalysis"],
        "_3810": ["CylindricalGearStabilityAnalysis"],
        "_3811": ["CylindricalPlanetGearStabilityAnalysis"],
        "_3812": ["DatumStabilityAnalysis"],
        "_3813": ["DynamicModelForStabilityAnalysis"],
        "_3814": ["ExternalCADModelStabilityAnalysis"],
        "_3815": ["FaceGearMeshStabilityAnalysis"],
        "_3816": ["FaceGearSetStabilityAnalysis"],
        "_3817": ["FaceGearStabilityAnalysis"],
        "_3818": ["FEPartStabilityAnalysis"],
        "_3819": ["FlexiblePinAssemblyStabilityAnalysis"],
        "_3820": ["GearMeshStabilityAnalysis"],
        "_3821": ["GearSetStabilityAnalysis"],
        "_3822": ["GearStabilityAnalysis"],
        "_3823": ["GuideDxfModelStabilityAnalysis"],
        "_3824": ["HypoidGearMeshStabilityAnalysis"],
        "_3825": ["HypoidGearSetStabilityAnalysis"],
        "_3826": ["HypoidGearStabilityAnalysis"],
        "_3827": ["InterMountableComponentConnectionStabilityAnalysis"],
        "_3828": ["KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis"],
        "_3829": ["KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis"],
        "_3830": ["KlingelnbergCycloPalloidConicalGearStabilityAnalysis"],
        "_3831": ["KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis"],
        "_3832": ["KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis"],
        "_3833": ["KlingelnbergCycloPalloidHypoidGearStabilityAnalysis"],
        "_3834": ["KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis"],
        "_3835": ["KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis"],
        "_3836": ["KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis"],
        "_3837": ["MassDiscStabilityAnalysis"],
        "_3838": ["MeasurementComponentStabilityAnalysis"],
        "_3839": ["MountableComponentStabilityAnalysis"],
        "_3840": ["OilSealStabilityAnalysis"],
        "_3841": ["PartStabilityAnalysis"],
        "_3842": ["PartToPartShearCouplingConnectionStabilityAnalysis"],
        "_3843": ["PartToPartShearCouplingHalfStabilityAnalysis"],
        "_3844": ["PartToPartShearCouplingStabilityAnalysis"],
        "_3845": ["PlanetaryConnectionStabilityAnalysis"],
        "_3846": ["PlanetaryGearSetStabilityAnalysis"],
        "_3847": ["PlanetCarrierStabilityAnalysis"],
        "_3848": ["PointLoadStabilityAnalysis"],
        "_3849": ["PowerLoadStabilityAnalysis"],
        "_3850": ["PulleyStabilityAnalysis"],
        "_3851": ["RingPinsStabilityAnalysis"],
        "_3852": ["RingPinsToDiscConnectionStabilityAnalysis"],
        "_3853": ["RollingRingAssemblyStabilityAnalysis"],
        "_3854": ["RollingRingConnectionStabilityAnalysis"],
        "_3855": ["RollingRingStabilityAnalysis"],
        "_3856": ["RootAssemblyStabilityAnalysis"],
        "_3857": ["ShaftHubConnectionStabilityAnalysis"],
        "_3858": ["ShaftStabilityAnalysis"],
        "_3859": ["ShaftToMountableComponentConnectionStabilityAnalysis"],
        "_3860": ["SpecialisedAssemblyStabilityAnalysis"],
        "_3861": ["SpiralBevelGearMeshStabilityAnalysis"],
        "_3862": ["SpiralBevelGearSetStabilityAnalysis"],
        "_3863": ["SpiralBevelGearStabilityAnalysis"],
        "_3864": ["SpringDamperConnectionStabilityAnalysis"],
        "_3865": ["SpringDamperHalfStabilityAnalysis"],
        "_3866": ["SpringDamperStabilityAnalysis"],
        "_3867": ["StabilityAnalysis"],
        "_3868": ["StabilityAnalysisDrawStyle"],
        "_3869": ["StabilityAnalysisOptions"],
        "_3870": ["StraightBevelDiffGearMeshStabilityAnalysis"],
        "_3871": ["StraightBevelDiffGearSetStabilityAnalysis"],
        "_3872": ["StraightBevelDiffGearStabilityAnalysis"],
        "_3873": ["StraightBevelGearMeshStabilityAnalysis"],
        "_3874": ["StraightBevelGearSetStabilityAnalysis"],
        "_3875": ["StraightBevelGearStabilityAnalysis"],
        "_3876": ["StraightBevelPlanetGearStabilityAnalysis"],
        "_3877": ["StraightBevelSunGearStabilityAnalysis"],
        "_3878": ["SynchroniserHalfStabilityAnalysis"],
        "_3879": ["SynchroniserPartStabilityAnalysis"],
        "_3880": ["SynchroniserSleeveStabilityAnalysis"],
        "_3881": ["SynchroniserStabilityAnalysis"],
        "_3882": ["TorqueConverterConnectionStabilityAnalysis"],
        "_3883": ["TorqueConverterPumpStabilityAnalysis"],
        "_3884": ["TorqueConverterStabilityAnalysis"],
        "_3885": ["TorqueConverterTurbineStabilityAnalysis"],
        "_3886": ["UnbalancedMassStabilityAnalysis"],
        "_3887": ["VirtualComponentStabilityAnalysis"],
        "_3888": ["WormGearMeshStabilityAnalysis"],
        "_3889": ["WormGearSetStabilityAnalysis"],
        "_3890": ["WormGearStabilityAnalysis"],
        "_3891": ["ZerolBevelGearMeshStabilityAnalysis"],
        "_3892": ["ZerolBevelGearSetStabilityAnalysis"],
        "_3893": ["ZerolBevelGearStabilityAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyStabilityAnalysis",
    "AbstractShaftOrHousingStabilityAnalysis",
    "AbstractShaftStabilityAnalysis",
    "AbstractShaftToMountableComponentConnectionStabilityAnalysis",
    "AGMAGleasonConicalGearMeshStabilityAnalysis",
    "AGMAGleasonConicalGearSetStabilityAnalysis",
    "AGMAGleasonConicalGearStabilityAnalysis",
    "AssemblyStabilityAnalysis",
    "BearingStabilityAnalysis",
    "BeltConnectionStabilityAnalysis",
    "BeltDriveStabilityAnalysis",
    "BevelDifferentialGearMeshStabilityAnalysis",
    "BevelDifferentialGearSetStabilityAnalysis",
    "BevelDifferentialGearStabilityAnalysis",
    "BevelDifferentialPlanetGearStabilityAnalysis",
    "BevelDifferentialSunGearStabilityAnalysis",
    "BevelGearMeshStabilityAnalysis",
    "BevelGearSetStabilityAnalysis",
    "BevelGearStabilityAnalysis",
    "BoltedJointStabilityAnalysis",
    "BoltStabilityAnalysis",
    "ClutchConnectionStabilityAnalysis",
    "ClutchHalfStabilityAnalysis",
    "ClutchStabilityAnalysis",
    "CoaxialConnectionStabilityAnalysis",
    "ComponentStabilityAnalysis",
    "ConceptCouplingConnectionStabilityAnalysis",
    "ConceptCouplingHalfStabilityAnalysis",
    "ConceptCouplingStabilityAnalysis",
    "ConceptGearMeshStabilityAnalysis",
    "ConceptGearSetStabilityAnalysis",
    "ConceptGearStabilityAnalysis",
    "ConicalGearMeshStabilityAnalysis",
    "ConicalGearSetStabilityAnalysis",
    "ConicalGearStabilityAnalysis",
    "ConnectionStabilityAnalysis",
    "ConnectorStabilityAnalysis",
    "CouplingConnectionStabilityAnalysis",
    "CouplingHalfStabilityAnalysis",
    "CouplingStabilityAnalysis",
    "CriticalSpeed",
    "CVTBeltConnectionStabilityAnalysis",
    "CVTPulleyStabilityAnalysis",
    "CVTStabilityAnalysis",
    "CycloidalAssemblyStabilityAnalysis",
    "CycloidalDiscCentralBearingConnectionStabilityAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis",
    "CycloidalDiscStabilityAnalysis",
    "CylindricalGearMeshStabilityAnalysis",
    "CylindricalGearSetStabilityAnalysis",
    "CylindricalGearStabilityAnalysis",
    "CylindricalPlanetGearStabilityAnalysis",
    "DatumStabilityAnalysis",
    "DynamicModelForStabilityAnalysis",
    "ExternalCADModelStabilityAnalysis",
    "FaceGearMeshStabilityAnalysis",
    "FaceGearSetStabilityAnalysis",
    "FaceGearStabilityAnalysis",
    "FEPartStabilityAnalysis",
    "FlexiblePinAssemblyStabilityAnalysis",
    "GearMeshStabilityAnalysis",
    "GearSetStabilityAnalysis",
    "GearStabilityAnalysis",
    "GuideDxfModelStabilityAnalysis",
    "HypoidGearMeshStabilityAnalysis",
    "HypoidGearSetStabilityAnalysis",
    "HypoidGearStabilityAnalysis",
    "InterMountableComponentConnectionStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
    "MassDiscStabilityAnalysis",
    "MeasurementComponentStabilityAnalysis",
    "MountableComponentStabilityAnalysis",
    "OilSealStabilityAnalysis",
    "PartStabilityAnalysis",
    "PartToPartShearCouplingConnectionStabilityAnalysis",
    "PartToPartShearCouplingHalfStabilityAnalysis",
    "PartToPartShearCouplingStabilityAnalysis",
    "PlanetaryConnectionStabilityAnalysis",
    "PlanetaryGearSetStabilityAnalysis",
    "PlanetCarrierStabilityAnalysis",
    "PointLoadStabilityAnalysis",
    "PowerLoadStabilityAnalysis",
    "PulleyStabilityAnalysis",
    "RingPinsStabilityAnalysis",
    "RingPinsToDiscConnectionStabilityAnalysis",
    "RollingRingAssemblyStabilityAnalysis",
    "RollingRingConnectionStabilityAnalysis",
    "RollingRingStabilityAnalysis",
    "RootAssemblyStabilityAnalysis",
    "ShaftHubConnectionStabilityAnalysis",
    "ShaftStabilityAnalysis",
    "ShaftToMountableComponentConnectionStabilityAnalysis",
    "SpecialisedAssemblyStabilityAnalysis",
    "SpiralBevelGearMeshStabilityAnalysis",
    "SpiralBevelGearSetStabilityAnalysis",
    "SpiralBevelGearStabilityAnalysis",
    "SpringDamperConnectionStabilityAnalysis",
    "SpringDamperHalfStabilityAnalysis",
    "SpringDamperStabilityAnalysis",
    "StabilityAnalysis",
    "StabilityAnalysisDrawStyle",
    "StabilityAnalysisOptions",
    "StraightBevelDiffGearMeshStabilityAnalysis",
    "StraightBevelDiffGearSetStabilityAnalysis",
    "StraightBevelDiffGearStabilityAnalysis",
    "StraightBevelGearMeshStabilityAnalysis",
    "StraightBevelGearSetStabilityAnalysis",
    "StraightBevelGearStabilityAnalysis",
    "StraightBevelPlanetGearStabilityAnalysis",
    "StraightBevelSunGearStabilityAnalysis",
    "SynchroniserHalfStabilityAnalysis",
    "SynchroniserPartStabilityAnalysis",
    "SynchroniserSleeveStabilityAnalysis",
    "SynchroniserStabilityAnalysis",
    "TorqueConverterConnectionStabilityAnalysis",
    "TorqueConverterPumpStabilityAnalysis",
    "TorqueConverterStabilityAnalysis",
    "TorqueConverterTurbineStabilityAnalysis",
    "UnbalancedMassStabilityAnalysis",
    "VirtualComponentStabilityAnalysis",
    "WormGearMeshStabilityAnalysis",
    "WormGearSetStabilityAnalysis",
    "WormGearStabilityAnalysis",
    "ZerolBevelGearMeshStabilityAnalysis",
    "ZerolBevelGearSetStabilityAnalysis",
    "ZerolBevelGearStabilityAnalysis",
)
