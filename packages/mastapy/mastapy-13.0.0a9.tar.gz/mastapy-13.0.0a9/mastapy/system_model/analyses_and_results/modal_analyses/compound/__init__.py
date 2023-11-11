"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4724 import AbstractAssemblyCompoundModalAnalysis
    from ._4725 import AbstractShaftCompoundModalAnalysis
    from ._4726 import AbstractShaftOrHousingCompoundModalAnalysis
    from ._4727 import AbstractShaftToMountableComponentConnectionCompoundModalAnalysis
    from ._4728 import AGMAGleasonConicalGearCompoundModalAnalysis
    from ._4729 import AGMAGleasonConicalGearMeshCompoundModalAnalysis
    from ._4730 import AGMAGleasonConicalGearSetCompoundModalAnalysis
    from ._4731 import AssemblyCompoundModalAnalysis
    from ._4732 import BearingCompoundModalAnalysis
    from ._4733 import BeltConnectionCompoundModalAnalysis
    from ._4734 import BeltDriveCompoundModalAnalysis
    from ._4735 import BevelDifferentialGearCompoundModalAnalysis
    from ._4736 import BevelDifferentialGearMeshCompoundModalAnalysis
    from ._4737 import BevelDifferentialGearSetCompoundModalAnalysis
    from ._4738 import BevelDifferentialPlanetGearCompoundModalAnalysis
    from ._4739 import BevelDifferentialSunGearCompoundModalAnalysis
    from ._4740 import BevelGearCompoundModalAnalysis
    from ._4741 import BevelGearMeshCompoundModalAnalysis
    from ._4742 import BevelGearSetCompoundModalAnalysis
    from ._4743 import BoltCompoundModalAnalysis
    from ._4744 import BoltedJointCompoundModalAnalysis
    from ._4745 import ClutchCompoundModalAnalysis
    from ._4746 import ClutchConnectionCompoundModalAnalysis
    from ._4747 import ClutchHalfCompoundModalAnalysis
    from ._4748 import CoaxialConnectionCompoundModalAnalysis
    from ._4749 import ComponentCompoundModalAnalysis
    from ._4750 import ConceptCouplingCompoundModalAnalysis
    from ._4751 import ConceptCouplingConnectionCompoundModalAnalysis
    from ._4752 import ConceptCouplingHalfCompoundModalAnalysis
    from ._4753 import ConceptGearCompoundModalAnalysis
    from ._4754 import ConceptGearMeshCompoundModalAnalysis
    from ._4755 import ConceptGearSetCompoundModalAnalysis
    from ._4756 import ConicalGearCompoundModalAnalysis
    from ._4757 import ConicalGearMeshCompoundModalAnalysis
    from ._4758 import ConicalGearSetCompoundModalAnalysis
    from ._4759 import ConnectionCompoundModalAnalysis
    from ._4760 import ConnectorCompoundModalAnalysis
    from ._4761 import CouplingCompoundModalAnalysis
    from ._4762 import CouplingConnectionCompoundModalAnalysis
    from ._4763 import CouplingHalfCompoundModalAnalysis
    from ._4764 import CVTBeltConnectionCompoundModalAnalysis
    from ._4765 import CVTCompoundModalAnalysis
    from ._4766 import CVTPulleyCompoundModalAnalysis
    from ._4767 import CycloidalAssemblyCompoundModalAnalysis
    from ._4768 import CycloidalDiscCentralBearingConnectionCompoundModalAnalysis
    from ._4769 import CycloidalDiscCompoundModalAnalysis
    from ._4770 import CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis
    from ._4771 import CylindricalGearCompoundModalAnalysis
    from ._4772 import CylindricalGearMeshCompoundModalAnalysis
    from ._4773 import CylindricalGearSetCompoundModalAnalysis
    from ._4774 import CylindricalPlanetGearCompoundModalAnalysis
    from ._4775 import DatumCompoundModalAnalysis
    from ._4776 import ExternalCADModelCompoundModalAnalysis
    from ._4777 import FaceGearCompoundModalAnalysis
    from ._4778 import FaceGearMeshCompoundModalAnalysis
    from ._4779 import FaceGearSetCompoundModalAnalysis
    from ._4780 import FEPartCompoundModalAnalysis
    from ._4781 import FlexiblePinAssemblyCompoundModalAnalysis
    from ._4782 import GearCompoundModalAnalysis
    from ._4783 import GearMeshCompoundModalAnalysis
    from ._4784 import GearSetCompoundModalAnalysis
    from ._4785 import GuideDxfModelCompoundModalAnalysis
    from ._4786 import HypoidGearCompoundModalAnalysis
    from ._4787 import HypoidGearMeshCompoundModalAnalysis
    from ._4788 import HypoidGearSetCompoundModalAnalysis
    from ._4789 import InterMountableComponentConnectionCompoundModalAnalysis
    from ._4790 import KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
    from ._4791 import KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis
    from ._4792 import KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
    from ._4793 import KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
    from ._4794 import KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis
    from ._4795 import KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
    from ._4796 import KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
    from ._4797 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis
    from ._4798 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
    from ._4799 import MassDiscCompoundModalAnalysis
    from ._4800 import MeasurementComponentCompoundModalAnalysis
    from ._4801 import MountableComponentCompoundModalAnalysis
    from ._4802 import OilSealCompoundModalAnalysis
    from ._4803 import PartCompoundModalAnalysis
    from ._4804 import PartToPartShearCouplingCompoundModalAnalysis
    from ._4805 import PartToPartShearCouplingConnectionCompoundModalAnalysis
    from ._4806 import PartToPartShearCouplingHalfCompoundModalAnalysis
    from ._4807 import PlanetaryConnectionCompoundModalAnalysis
    from ._4808 import PlanetaryGearSetCompoundModalAnalysis
    from ._4809 import PlanetCarrierCompoundModalAnalysis
    from ._4810 import PointLoadCompoundModalAnalysis
    from ._4811 import PowerLoadCompoundModalAnalysis
    from ._4812 import PulleyCompoundModalAnalysis
    from ._4813 import RingPinsCompoundModalAnalysis
    from ._4814 import RingPinsToDiscConnectionCompoundModalAnalysis
    from ._4815 import RollingRingAssemblyCompoundModalAnalysis
    from ._4816 import RollingRingCompoundModalAnalysis
    from ._4817 import RollingRingConnectionCompoundModalAnalysis
    from ._4818 import RootAssemblyCompoundModalAnalysis
    from ._4819 import ShaftCompoundModalAnalysis
    from ._4820 import ShaftHubConnectionCompoundModalAnalysis
    from ._4821 import ShaftToMountableComponentConnectionCompoundModalAnalysis
    from ._4822 import SpecialisedAssemblyCompoundModalAnalysis
    from ._4823 import SpiralBevelGearCompoundModalAnalysis
    from ._4824 import SpiralBevelGearMeshCompoundModalAnalysis
    from ._4825 import SpiralBevelGearSetCompoundModalAnalysis
    from ._4826 import SpringDamperCompoundModalAnalysis
    from ._4827 import SpringDamperConnectionCompoundModalAnalysis
    from ._4828 import SpringDamperHalfCompoundModalAnalysis
    from ._4829 import StraightBevelDiffGearCompoundModalAnalysis
    from ._4830 import StraightBevelDiffGearMeshCompoundModalAnalysis
    from ._4831 import StraightBevelDiffGearSetCompoundModalAnalysis
    from ._4832 import StraightBevelGearCompoundModalAnalysis
    from ._4833 import StraightBevelGearMeshCompoundModalAnalysis
    from ._4834 import StraightBevelGearSetCompoundModalAnalysis
    from ._4835 import StraightBevelPlanetGearCompoundModalAnalysis
    from ._4836 import StraightBevelSunGearCompoundModalAnalysis
    from ._4837 import SynchroniserCompoundModalAnalysis
    from ._4838 import SynchroniserHalfCompoundModalAnalysis
    from ._4839 import SynchroniserPartCompoundModalAnalysis
    from ._4840 import SynchroniserSleeveCompoundModalAnalysis
    from ._4841 import TorqueConverterCompoundModalAnalysis
    from ._4842 import TorqueConverterConnectionCompoundModalAnalysis
    from ._4843 import TorqueConverterPumpCompoundModalAnalysis
    from ._4844 import TorqueConverterTurbineCompoundModalAnalysis
    from ._4845 import UnbalancedMassCompoundModalAnalysis
    from ._4846 import VirtualComponentCompoundModalAnalysis
    from ._4847 import WormGearCompoundModalAnalysis
    from ._4848 import WormGearMeshCompoundModalAnalysis
    from ._4849 import WormGearSetCompoundModalAnalysis
    from ._4850 import ZerolBevelGearCompoundModalAnalysis
    from ._4851 import ZerolBevelGearMeshCompoundModalAnalysis
    from ._4852 import ZerolBevelGearSetCompoundModalAnalysis
else:
    import_structure = {
        "_4724": ["AbstractAssemblyCompoundModalAnalysis"],
        "_4725": ["AbstractShaftCompoundModalAnalysis"],
        "_4726": ["AbstractShaftOrHousingCompoundModalAnalysis"],
        "_4727": ["AbstractShaftToMountableComponentConnectionCompoundModalAnalysis"],
        "_4728": ["AGMAGleasonConicalGearCompoundModalAnalysis"],
        "_4729": ["AGMAGleasonConicalGearMeshCompoundModalAnalysis"],
        "_4730": ["AGMAGleasonConicalGearSetCompoundModalAnalysis"],
        "_4731": ["AssemblyCompoundModalAnalysis"],
        "_4732": ["BearingCompoundModalAnalysis"],
        "_4733": ["BeltConnectionCompoundModalAnalysis"],
        "_4734": ["BeltDriveCompoundModalAnalysis"],
        "_4735": ["BevelDifferentialGearCompoundModalAnalysis"],
        "_4736": ["BevelDifferentialGearMeshCompoundModalAnalysis"],
        "_4737": ["BevelDifferentialGearSetCompoundModalAnalysis"],
        "_4738": ["BevelDifferentialPlanetGearCompoundModalAnalysis"],
        "_4739": ["BevelDifferentialSunGearCompoundModalAnalysis"],
        "_4740": ["BevelGearCompoundModalAnalysis"],
        "_4741": ["BevelGearMeshCompoundModalAnalysis"],
        "_4742": ["BevelGearSetCompoundModalAnalysis"],
        "_4743": ["BoltCompoundModalAnalysis"],
        "_4744": ["BoltedJointCompoundModalAnalysis"],
        "_4745": ["ClutchCompoundModalAnalysis"],
        "_4746": ["ClutchConnectionCompoundModalAnalysis"],
        "_4747": ["ClutchHalfCompoundModalAnalysis"],
        "_4748": ["CoaxialConnectionCompoundModalAnalysis"],
        "_4749": ["ComponentCompoundModalAnalysis"],
        "_4750": ["ConceptCouplingCompoundModalAnalysis"],
        "_4751": ["ConceptCouplingConnectionCompoundModalAnalysis"],
        "_4752": ["ConceptCouplingHalfCompoundModalAnalysis"],
        "_4753": ["ConceptGearCompoundModalAnalysis"],
        "_4754": ["ConceptGearMeshCompoundModalAnalysis"],
        "_4755": ["ConceptGearSetCompoundModalAnalysis"],
        "_4756": ["ConicalGearCompoundModalAnalysis"],
        "_4757": ["ConicalGearMeshCompoundModalAnalysis"],
        "_4758": ["ConicalGearSetCompoundModalAnalysis"],
        "_4759": ["ConnectionCompoundModalAnalysis"],
        "_4760": ["ConnectorCompoundModalAnalysis"],
        "_4761": ["CouplingCompoundModalAnalysis"],
        "_4762": ["CouplingConnectionCompoundModalAnalysis"],
        "_4763": ["CouplingHalfCompoundModalAnalysis"],
        "_4764": ["CVTBeltConnectionCompoundModalAnalysis"],
        "_4765": ["CVTCompoundModalAnalysis"],
        "_4766": ["CVTPulleyCompoundModalAnalysis"],
        "_4767": ["CycloidalAssemblyCompoundModalAnalysis"],
        "_4768": ["CycloidalDiscCentralBearingConnectionCompoundModalAnalysis"],
        "_4769": ["CycloidalDiscCompoundModalAnalysis"],
        "_4770": ["CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis"],
        "_4771": ["CylindricalGearCompoundModalAnalysis"],
        "_4772": ["CylindricalGearMeshCompoundModalAnalysis"],
        "_4773": ["CylindricalGearSetCompoundModalAnalysis"],
        "_4774": ["CylindricalPlanetGearCompoundModalAnalysis"],
        "_4775": ["DatumCompoundModalAnalysis"],
        "_4776": ["ExternalCADModelCompoundModalAnalysis"],
        "_4777": ["FaceGearCompoundModalAnalysis"],
        "_4778": ["FaceGearMeshCompoundModalAnalysis"],
        "_4779": ["FaceGearSetCompoundModalAnalysis"],
        "_4780": ["FEPartCompoundModalAnalysis"],
        "_4781": ["FlexiblePinAssemblyCompoundModalAnalysis"],
        "_4782": ["GearCompoundModalAnalysis"],
        "_4783": ["GearMeshCompoundModalAnalysis"],
        "_4784": ["GearSetCompoundModalAnalysis"],
        "_4785": ["GuideDxfModelCompoundModalAnalysis"],
        "_4786": ["HypoidGearCompoundModalAnalysis"],
        "_4787": ["HypoidGearMeshCompoundModalAnalysis"],
        "_4788": ["HypoidGearSetCompoundModalAnalysis"],
        "_4789": ["InterMountableComponentConnectionCompoundModalAnalysis"],
        "_4790": ["KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis"],
        "_4791": ["KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis"],
        "_4792": ["KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis"],
        "_4793": ["KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis"],
        "_4794": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis"],
        "_4795": ["KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis"],
        "_4796": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis"],
        "_4797": ["KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis"],
        "_4798": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis"],
        "_4799": ["MassDiscCompoundModalAnalysis"],
        "_4800": ["MeasurementComponentCompoundModalAnalysis"],
        "_4801": ["MountableComponentCompoundModalAnalysis"],
        "_4802": ["OilSealCompoundModalAnalysis"],
        "_4803": ["PartCompoundModalAnalysis"],
        "_4804": ["PartToPartShearCouplingCompoundModalAnalysis"],
        "_4805": ["PartToPartShearCouplingConnectionCompoundModalAnalysis"],
        "_4806": ["PartToPartShearCouplingHalfCompoundModalAnalysis"],
        "_4807": ["PlanetaryConnectionCompoundModalAnalysis"],
        "_4808": ["PlanetaryGearSetCompoundModalAnalysis"],
        "_4809": ["PlanetCarrierCompoundModalAnalysis"],
        "_4810": ["PointLoadCompoundModalAnalysis"],
        "_4811": ["PowerLoadCompoundModalAnalysis"],
        "_4812": ["PulleyCompoundModalAnalysis"],
        "_4813": ["RingPinsCompoundModalAnalysis"],
        "_4814": ["RingPinsToDiscConnectionCompoundModalAnalysis"],
        "_4815": ["RollingRingAssemblyCompoundModalAnalysis"],
        "_4816": ["RollingRingCompoundModalAnalysis"],
        "_4817": ["RollingRingConnectionCompoundModalAnalysis"],
        "_4818": ["RootAssemblyCompoundModalAnalysis"],
        "_4819": ["ShaftCompoundModalAnalysis"],
        "_4820": ["ShaftHubConnectionCompoundModalAnalysis"],
        "_4821": ["ShaftToMountableComponentConnectionCompoundModalAnalysis"],
        "_4822": ["SpecialisedAssemblyCompoundModalAnalysis"],
        "_4823": ["SpiralBevelGearCompoundModalAnalysis"],
        "_4824": ["SpiralBevelGearMeshCompoundModalAnalysis"],
        "_4825": ["SpiralBevelGearSetCompoundModalAnalysis"],
        "_4826": ["SpringDamperCompoundModalAnalysis"],
        "_4827": ["SpringDamperConnectionCompoundModalAnalysis"],
        "_4828": ["SpringDamperHalfCompoundModalAnalysis"],
        "_4829": ["StraightBevelDiffGearCompoundModalAnalysis"],
        "_4830": ["StraightBevelDiffGearMeshCompoundModalAnalysis"],
        "_4831": ["StraightBevelDiffGearSetCompoundModalAnalysis"],
        "_4832": ["StraightBevelGearCompoundModalAnalysis"],
        "_4833": ["StraightBevelGearMeshCompoundModalAnalysis"],
        "_4834": ["StraightBevelGearSetCompoundModalAnalysis"],
        "_4835": ["StraightBevelPlanetGearCompoundModalAnalysis"],
        "_4836": ["StraightBevelSunGearCompoundModalAnalysis"],
        "_4837": ["SynchroniserCompoundModalAnalysis"],
        "_4838": ["SynchroniserHalfCompoundModalAnalysis"],
        "_4839": ["SynchroniserPartCompoundModalAnalysis"],
        "_4840": ["SynchroniserSleeveCompoundModalAnalysis"],
        "_4841": ["TorqueConverterCompoundModalAnalysis"],
        "_4842": ["TorqueConverterConnectionCompoundModalAnalysis"],
        "_4843": ["TorqueConverterPumpCompoundModalAnalysis"],
        "_4844": ["TorqueConverterTurbineCompoundModalAnalysis"],
        "_4845": ["UnbalancedMassCompoundModalAnalysis"],
        "_4846": ["VirtualComponentCompoundModalAnalysis"],
        "_4847": ["WormGearCompoundModalAnalysis"],
        "_4848": ["WormGearMeshCompoundModalAnalysis"],
        "_4849": ["WormGearSetCompoundModalAnalysis"],
        "_4850": ["ZerolBevelGearCompoundModalAnalysis"],
        "_4851": ["ZerolBevelGearMeshCompoundModalAnalysis"],
        "_4852": ["ZerolBevelGearSetCompoundModalAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundModalAnalysis",
    "AbstractShaftCompoundModalAnalysis",
    "AbstractShaftOrHousingCompoundModalAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
    "AGMAGleasonConicalGearCompoundModalAnalysis",
    "AGMAGleasonConicalGearMeshCompoundModalAnalysis",
    "AGMAGleasonConicalGearSetCompoundModalAnalysis",
    "AssemblyCompoundModalAnalysis",
    "BearingCompoundModalAnalysis",
    "BeltConnectionCompoundModalAnalysis",
    "BeltDriveCompoundModalAnalysis",
    "BevelDifferentialGearCompoundModalAnalysis",
    "BevelDifferentialGearMeshCompoundModalAnalysis",
    "BevelDifferentialGearSetCompoundModalAnalysis",
    "BevelDifferentialPlanetGearCompoundModalAnalysis",
    "BevelDifferentialSunGearCompoundModalAnalysis",
    "BevelGearCompoundModalAnalysis",
    "BevelGearMeshCompoundModalAnalysis",
    "BevelGearSetCompoundModalAnalysis",
    "BoltCompoundModalAnalysis",
    "BoltedJointCompoundModalAnalysis",
    "ClutchCompoundModalAnalysis",
    "ClutchConnectionCompoundModalAnalysis",
    "ClutchHalfCompoundModalAnalysis",
    "CoaxialConnectionCompoundModalAnalysis",
    "ComponentCompoundModalAnalysis",
    "ConceptCouplingCompoundModalAnalysis",
    "ConceptCouplingConnectionCompoundModalAnalysis",
    "ConceptCouplingHalfCompoundModalAnalysis",
    "ConceptGearCompoundModalAnalysis",
    "ConceptGearMeshCompoundModalAnalysis",
    "ConceptGearSetCompoundModalAnalysis",
    "ConicalGearCompoundModalAnalysis",
    "ConicalGearMeshCompoundModalAnalysis",
    "ConicalGearSetCompoundModalAnalysis",
    "ConnectionCompoundModalAnalysis",
    "ConnectorCompoundModalAnalysis",
    "CouplingCompoundModalAnalysis",
    "CouplingConnectionCompoundModalAnalysis",
    "CouplingHalfCompoundModalAnalysis",
    "CVTBeltConnectionCompoundModalAnalysis",
    "CVTCompoundModalAnalysis",
    "CVTPulleyCompoundModalAnalysis",
    "CycloidalAssemblyCompoundModalAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundModalAnalysis",
    "CycloidalDiscCompoundModalAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis",
    "CylindricalGearCompoundModalAnalysis",
    "CylindricalGearMeshCompoundModalAnalysis",
    "CylindricalGearSetCompoundModalAnalysis",
    "CylindricalPlanetGearCompoundModalAnalysis",
    "DatumCompoundModalAnalysis",
    "ExternalCADModelCompoundModalAnalysis",
    "FaceGearCompoundModalAnalysis",
    "FaceGearMeshCompoundModalAnalysis",
    "FaceGearSetCompoundModalAnalysis",
    "FEPartCompoundModalAnalysis",
    "FlexiblePinAssemblyCompoundModalAnalysis",
    "GearCompoundModalAnalysis",
    "GearMeshCompoundModalAnalysis",
    "GearSetCompoundModalAnalysis",
    "GuideDxfModelCompoundModalAnalysis",
    "HypoidGearCompoundModalAnalysis",
    "HypoidGearMeshCompoundModalAnalysis",
    "HypoidGearSetCompoundModalAnalysis",
    "InterMountableComponentConnectionCompoundModalAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis",
    "MassDiscCompoundModalAnalysis",
    "MeasurementComponentCompoundModalAnalysis",
    "MountableComponentCompoundModalAnalysis",
    "OilSealCompoundModalAnalysis",
    "PartCompoundModalAnalysis",
    "PartToPartShearCouplingCompoundModalAnalysis",
    "PartToPartShearCouplingConnectionCompoundModalAnalysis",
    "PartToPartShearCouplingHalfCompoundModalAnalysis",
    "PlanetaryConnectionCompoundModalAnalysis",
    "PlanetaryGearSetCompoundModalAnalysis",
    "PlanetCarrierCompoundModalAnalysis",
    "PointLoadCompoundModalAnalysis",
    "PowerLoadCompoundModalAnalysis",
    "PulleyCompoundModalAnalysis",
    "RingPinsCompoundModalAnalysis",
    "RingPinsToDiscConnectionCompoundModalAnalysis",
    "RollingRingAssemblyCompoundModalAnalysis",
    "RollingRingCompoundModalAnalysis",
    "RollingRingConnectionCompoundModalAnalysis",
    "RootAssemblyCompoundModalAnalysis",
    "ShaftCompoundModalAnalysis",
    "ShaftHubConnectionCompoundModalAnalysis",
    "ShaftToMountableComponentConnectionCompoundModalAnalysis",
    "SpecialisedAssemblyCompoundModalAnalysis",
    "SpiralBevelGearCompoundModalAnalysis",
    "SpiralBevelGearMeshCompoundModalAnalysis",
    "SpiralBevelGearSetCompoundModalAnalysis",
    "SpringDamperCompoundModalAnalysis",
    "SpringDamperConnectionCompoundModalAnalysis",
    "SpringDamperHalfCompoundModalAnalysis",
    "StraightBevelDiffGearCompoundModalAnalysis",
    "StraightBevelDiffGearMeshCompoundModalAnalysis",
    "StraightBevelDiffGearSetCompoundModalAnalysis",
    "StraightBevelGearCompoundModalAnalysis",
    "StraightBevelGearMeshCompoundModalAnalysis",
    "StraightBevelGearSetCompoundModalAnalysis",
    "StraightBevelPlanetGearCompoundModalAnalysis",
    "StraightBevelSunGearCompoundModalAnalysis",
    "SynchroniserCompoundModalAnalysis",
    "SynchroniserHalfCompoundModalAnalysis",
    "SynchroniserPartCompoundModalAnalysis",
    "SynchroniserSleeveCompoundModalAnalysis",
    "TorqueConverterCompoundModalAnalysis",
    "TorqueConverterConnectionCompoundModalAnalysis",
    "TorqueConverterPumpCompoundModalAnalysis",
    "TorqueConverterTurbineCompoundModalAnalysis",
    "UnbalancedMassCompoundModalAnalysis",
    "VirtualComponentCompoundModalAnalysis",
    "WormGearCompoundModalAnalysis",
    "WormGearMeshCompoundModalAnalysis",
    "WormGearSetCompoundModalAnalysis",
    "ZerolBevelGearCompoundModalAnalysis",
    "ZerolBevelGearMeshCompoundModalAnalysis",
    "ZerolBevelGearSetCompoundModalAnalysis",
)
