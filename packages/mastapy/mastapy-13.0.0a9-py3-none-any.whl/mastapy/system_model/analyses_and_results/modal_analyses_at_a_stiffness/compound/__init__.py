"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4984 import AbstractAssemblyCompoundModalAnalysisAtAStiffness
    from ._4985 import AbstractShaftCompoundModalAnalysisAtAStiffness
    from ._4986 import AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness
    from ._4987 import (
        AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._4988 import AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
    from ._4989 import AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness
    from ._4990 import AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
    from ._4991 import AssemblyCompoundModalAnalysisAtAStiffness
    from ._4992 import BearingCompoundModalAnalysisAtAStiffness
    from ._4993 import BeltConnectionCompoundModalAnalysisAtAStiffness
    from ._4994 import BeltDriveCompoundModalAnalysisAtAStiffness
    from ._4995 import BevelDifferentialGearCompoundModalAnalysisAtAStiffness
    from ._4996 import BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness
    from ._4997 import BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness
    from ._4998 import BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness
    from ._4999 import BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness
    from ._5000 import BevelGearCompoundModalAnalysisAtAStiffness
    from ._5001 import BevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5002 import BevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5003 import BoltCompoundModalAnalysisAtAStiffness
    from ._5004 import BoltedJointCompoundModalAnalysisAtAStiffness
    from ._5005 import ClutchCompoundModalAnalysisAtAStiffness
    from ._5006 import ClutchConnectionCompoundModalAnalysisAtAStiffness
    from ._5007 import ClutchHalfCompoundModalAnalysisAtAStiffness
    from ._5008 import CoaxialConnectionCompoundModalAnalysisAtAStiffness
    from ._5009 import ComponentCompoundModalAnalysisAtAStiffness
    from ._5010 import ConceptCouplingCompoundModalAnalysisAtAStiffness
    from ._5011 import ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness
    from ._5012 import ConceptCouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5013 import ConceptGearCompoundModalAnalysisAtAStiffness
    from ._5014 import ConceptGearMeshCompoundModalAnalysisAtAStiffness
    from ._5015 import ConceptGearSetCompoundModalAnalysisAtAStiffness
    from ._5016 import ConicalGearCompoundModalAnalysisAtAStiffness
    from ._5017 import ConicalGearMeshCompoundModalAnalysisAtAStiffness
    from ._5018 import ConicalGearSetCompoundModalAnalysisAtAStiffness
    from ._5019 import ConnectionCompoundModalAnalysisAtAStiffness
    from ._5020 import ConnectorCompoundModalAnalysisAtAStiffness
    from ._5021 import CouplingCompoundModalAnalysisAtAStiffness
    from ._5022 import CouplingConnectionCompoundModalAnalysisAtAStiffness
    from ._5023 import CouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5024 import CVTBeltConnectionCompoundModalAnalysisAtAStiffness
    from ._5025 import CVTCompoundModalAnalysisAtAStiffness
    from ._5026 import CVTPulleyCompoundModalAnalysisAtAStiffness
    from ._5027 import CycloidalAssemblyCompoundModalAnalysisAtAStiffness
    from ._5028 import (
        CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5029 import CycloidalDiscCompoundModalAnalysisAtAStiffness
    from ._5030 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5031 import CylindricalGearCompoundModalAnalysisAtAStiffness
    from ._5032 import CylindricalGearMeshCompoundModalAnalysisAtAStiffness
    from ._5033 import CylindricalGearSetCompoundModalAnalysisAtAStiffness
    from ._5034 import CylindricalPlanetGearCompoundModalAnalysisAtAStiffness
    from ._5035 import DatumCompoundModalAnalysisAtAStiffness
    from ._5036 import ExternalCADModelCompoundModalAnalysisAtAStiffness
    from ._5037 import FaceGearCompoundModalAnalysisAtAStiffness
    from ._5038 import FaceGearMeshCompoundModalAnalysisAtAStiffness
    from ._5039 import FaceGearSetCompoundModalAnalysisAtAStiffness
    from ._5040 import FEPartCompoundModalAnalysisAtAStiffness
    from ._5041 import FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness
    from ._5042 import GearCompoundModalAnalysisAtAStiffness
    from ._5043 import GearMeshCompoundModalAnalysisAtAStiffness
    from ._5044 import GearSetCompoundModalAnalysisAtAStiffness
    from ._5045 import GuideDxfModelCompoundModalAnalysisAtAStiffness
    from ._5046 import HypoidGearCompoundModalAnalysisAtAStiffness
    from ._5047 import HypoidGearMeshCompoundModalAnalysisAtAStiffness
    from ._5048 import HypoidGearSetCompoundModalAnalysisAtAStiffness
    from ._5049 import (
        InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5050 import (
        KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness,
    )
    from ._5051 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness,
    )
    from ._5052 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness,
    )
    from ._5053 import (
        KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness,
    )
    from ._5054 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness,
    )
    from ._5055 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness,
    )
    from ._5056 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness,
    )
    from ._5057 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness,
    )
    from ._5058 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness,
    )
    from ._5059 import MassDiscCompoundModalAnalysisAtAStiffness
    from ._5060 import MeasurementComponentCompoundModalAnalysisAtAStiffness
    from ._5061 import MountableComponentCompoundModalAnalysisAtAStiffness
    from ._5062 import OilSealCompoundModalAnalysisAtAStiffness
    from ._5063 import PartCompoundModalAnalysisAtAStiffness
    from ._5064 import PartToPartShearCouplingCompoundModalAnalysisAtAStiffness
    from ._5065 import (
        PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5066 import PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5067 import PlanetaryConnectionCompoundModalAnalysisAtAStiffness
    from ._5068 import PlanetaryGearSetCompoundModalAnalysisAtAStiffness
    from ._5069 import PlanetCarrierCompoundModalAnalysisAtAStiffness
    from ._5070 import PointLoadCompoundModalAnalysisAtAStiffness
    from ._5071 import PowerLoadCompoundModalAnalysisAtAStiffness
    from ._5072 import PulleyCompoundModalAnalysisAtAStiffness
    from ._5073 import RingPinsCompoundModalAnalysisAtAStiffness
    from ._5074 import RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness
    from ._5075 import RollingRingAssemblyCompoundModalAnalysisAtAStiffness
    from ._5076 import RollingRingCompoundModalAnalysisAtAStiffness
    from ._5077 import RollingRingConnectionCompoundModalAnalysisAtAStiffness
    from ._5078 import RootAssemblyCompoundModalAnalysisAtAStiffness
    from ._5079 import ShaftCompoundModalAnalysisAtAStiffness
    from ._5080 import ShaftHubConnectionCompoundModalAnalysisAtAStiffness
    from ._5081 import (
        ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5082 import SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
    from ._5083 import SpiralBevelGearCompoundModalAnalysisAtAStiffness
    from ._5084 import SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5085 import SpiralBevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5086 import SpringDamperCompoundModalAnalysisAtAStiffness
    from ._5087 import SpringDamperConnectionCompoundModalAnalysisAtAStiffness
    from ._5088 import SpringDamperHalfCompoundModalAnalysisAtAStiffness
    from ._5089 import StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
    from ._5090 import StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness
    from ._5091 import StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness
    from ._5092 import StraightBevelGearCompoundModalAnalysisAtAStiffness
    from ._5093 import StraightBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5094 import StraightBevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5095 import StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
    from ._5096 import StraightBevelSunGearCompoundModalAnalysisAtAStiffness
    from ._5097 import SynchroniserCompoundModalAnalysisAtAStiffness
    from ._5098 import SynchroniserHalfCompoundModalAnalysisAtAStiffness
    from ._5099 import SynchroniserPartCompoundModalAnalysisAtAStiffness
    from ._5100 import SynchroniserSleeveCompoundModalAnalysisAtAStiffness
    from ._5101 import TorqueConverterCompoundModalAnalysisAtAStiffness
    from ._5102 import TorqueConverterConnectionCompoundModalAnalysisAtAStiffness
    from ._5103 import TorqueConverterPumpCompoundModalAnalysisAtAStiffness
    from ._5104 import TorqueConverterTurbineCompoundModalAnalysisAtAStiffness
    from ._5105 import UnbalancedMassCompoundModalAnalysisAtAStiffness
    from ._5106 import VirtualComponentCompoundModalAnalysisAtAStiffness
    from ._5107 import WormGearCompoundModalAnalysisAtAStiffness
    from ._5108 import WormGearMeshCompoundModalAnalysisAtAStiffness
    from ._5109 import WormGearSetCompoundModalAnalysisAtAStiffness
    from ._5110 import ZerolBevelGearCompoundModalAnalysisAtAStiffness
    from ._5111 import ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5112 import ZerolBevelGearSetCompoundModalAnalysisAtAStiffness
else:
    import_structure = {
        "_4984": ["AbstractAssemblyCompoundModalAnalysisAtAStiffness"],
        "_4985": ["AbstractShaftCompoundModalAnalysisAtAStiffness"],
        "_4986": ["AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness"],
        "_4987": [
            "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_4988": ["AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness"],
        "_4989": ["AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness"],
        "_4990": ["AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness"],
        "_4991": ["AssemblyCompoundModalAnalysisAtAStiffness"],
        "_4992": ["BearingCompoundModalAnalysisAtAStiffness"],
        "_4993": ["BeltConnectionCompoundModalAnalysisAtAStiffness"],
        "_4994": ["BeltDriveCompoundModalAnalysisAtAStiffness"],
        "_4995": ["BevelDifferentialGearCompoundModalAnalysisAtAStiffness"],
        "_4996": ["BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness"],
        "_4997": ["BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness"],
        "_4998": ["BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness"],
        "_4999": ["BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness"],
        "_5000": ["BevelGearCompoundModalAnalysisAtAStiffness"],
        "_5001": ["BevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5002": ["BevelGearSetCompoundModalAnalysisAtAStiffness"],
        "_5003": ["BoltCompoundModalAnalysisAtAStiffness"],
        "_5004": ["BoltedJointCompoundModalAnalysisAtAStiffness"],
        "_5005": ["ClutchCompoundModalAnalysisAtAStiffness"],
        "_5006": ["ClutchConnectionCompoundModalAnalysisAtAStiffness"],
        "_5007": ["ClutchHalfCompoundModalAnalysisAtAStiffness"],
        "_5008": ["CoaxialConnectionCompoundModalAnalysisAtAStiffness"],
        "_5009": ["ComponentCompoundModalAnalysisAtAStiffness"],
        "_5010": ["ConceptCouplingCompoundModalAnalysisAtAStiffness"],
        "_5011": ["ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5012": ["ConceptCouplingHalfCompoundModalAnalysisAtAStiffness"],
        "_5013": ["ConceptGearCompoundModalAnalysisAtAStiffness"],
        "_5014": ["ConceptGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5015": ["ConceptGearSetCompoundModalAnalysisAtAStiffness"],
        "_5016": ["ConicalGearCompoundModalAnalysisAtAStiffness"],
        "_5017": ["ConicalGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5018": ["ConicalGearSetCompoundModalAnalysisAtAStiffness"],
        "_5019": ["ConnectionCompoundModalAnalysisAtAStiffness"],
        "_5020": ["ConnectorCompoundModalAnalysisAtAStiffness"],
        "_5021": ["CouplingCompoundModalAnalysisAtAStiffness"],
        "_5022": ["CouplingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5023": ["CouplingHalfCompoundModalAnalysisAtAStiffness"],
        "_5024": ["CVTBeltConnectionCompoundModalAnalysisAtAStiffness"],
        "_5025": ["CVTCompoundModalAnalysisAtAStiffness"],
        "_5026": ["CVTPulleyCompoundModalAnalysisAtAStiffness"],
        "_5027": ["CycloidalAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5028": [
            "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5029": ["CycloidalDiscCompoundModalAnalysisAtAStiffness"],
        "_5030": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5031": ["CylindricalGearCompoundModalAnalysisAtAStiffness"],
        "_5032": ["CylindricalGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5033": ["CylindricalGearSetCompoundModalAnalysisAtAStiffness"],
        "_5034": ["CylindricalPlanetGearCompoundModalAnalysisAtAStiffness"],
        "_5035": ["DatumCompoundModalAnalysisAtAStiffness"],
        "_5036": ["ExternalCADModelCompoundModalAnalysisAtAStiffness"],
        "_5037": ["FaceGearCompoundModalAnalysisAtAStiffness"],
        "_5038": ["FaceGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5039": ["FaceGearSetCompoundModalAnalysisAtAStiffness"],
        "_5040": ["FEPartCompoundModalAnalysisAtAStiffness"],
        "_5041": ["FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5042": ["GearCompoundModalAnalysisAtAStiffness"],
        "_5043": ["GearMeshCompoundModalAnalysisAtAStiffness"],
        "_5044": ["GearSetCompoundModalAnalysisAtAStiffness"],
        "_5045": ["GuideDxfModelCompoundModalAnalysisAtAStiffness"],
        "_5046": ["HypoidGearCompoundModalAnalysisAtAStiffness"],
        "_5047": ["HypoidGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5048": ["HypoidGearSetCompoundModalAnalysisAtAStiffness"],
        "_5049": ["InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness"],
        "_5050": [
            "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness"
        ],
        "_5051": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness"
        ],
        "_5052": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness"
        ],
        "_5053": [
            "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness"
        ],
        "_5054": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness"
        ],
        "_5055": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness"
        ],
        "_5056": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness"
        ],
        "_5057": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness"
        ],
        "_5058": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness"
        ],
        "_5059": ["MassDiscCompoundModalAnalysisAtAStiffness"],
        "_5060": ["MeasurementComponentCompoundModalAnalysisAtAStiffness"],
        "_5061": ["MountableComponentCompoundModalAnalysisAtAStiffness"],
        "_5062": ["OilSealCompoundModalAnalysisAtAStiffness"],
        "_5063": ["PartCompoundModalAnalysisAtAStiffness"],
        "_5064": ["PartToPartShearCouplingCompoundModalAnalysisAtAStiffness"],
        "_5065": ["PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5066": ["PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness"],
        "_5067": ["PlanetaryConnectionCompoundModalAnalysisAtAStiffness"],
        "_5068": ["PlanetaryGearSetCompoundModalAnalysisAtAStiffness"],
        "_5069": ["PlanetCarrierCompoundModalAnalysisAtAStiffness"],
        "_5070": ["PointLoadCompoundModalAnalysisAtAStiffness"],
        "_5071": ["PowerLoadCompoundModalAnalysisAtAStiffness"],
        "_5072": ["PulleyCompoundModalAnalysisAtAStiffness"],
        "_5073": ["RingPinsCompoundModalAnalysisAtAStiffness"],
        "_5074": ["RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness"],
        "_5075": ["RollingRingAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5076": ["RollingRingCompoundModalAnalysisAtAStiffness"],
        "_5077": ["RollingRingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5078": ["RootAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5079": ["ShaftCompoundModalAnalysisAtAStiffness"],
        "_5080": ["ShaftHubConnectionCompoundModalAnalysisAtAStiffness"],
        "_5081": [
            "ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5082": ["SpecialisedAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5083": ["SpiralBevelGearCompoundModalAnalysisAtAStiffness"],
        "_5084": ["SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5085": ["SpiralBevelGearSetCompoundModalAnalysisAtAStiffness"],
        "_5086": ["SpringDamperCompoundModalAnalysisAtAStiffness"],
        "_5087": ["SpringDamperConnectionCompoundModalAnalysisAtAStiffness"],
        "_5088": ["SpringDamperHalfCompoundModalAnalysisAtAStiffness"],
        "_5089": ["StraightBevelDiffGearCompoundModalAnalysisAtAStiffness"],
        "_5090": ["StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5091": ["StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness"],
        "_5092": ["StraightBevelGearCompoundModalAnalysisAtAStiffness"],
        "_5093": ["StraightBevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5094": ["StraightBevelGearSetCompoundModalAnalysisAtAStiffness"],
        "_5095": ["StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness"],
        "_5096": ["StraightBevelSunGearCompoundModalAnalysisAtAStiffness"],
        "_5097": ["SynchroniserCompoundModalAnalysisAtAStiffness"],
        "_5098": ["SynchroniserHalfCompoundModalAnalysisAtAStiffness"],
        "_5099": ["SynchroniserPartCompoundModalAnalysisAtAStiffness"],
        "_5100": ["SynchroniserSleeveCompoundModalAnalysisAtAStiffness"],
        "_5101": ["TorqueConverterCompoundModalAnalysisAtAStiffness"],
        "_5102": ["TorqueConverterConnectionCompoundModalAnalysisAtAStiffness"],
        "_5103": ["TorqueConverterPumpCompoundModalAnalysisAtAStiffness"],
        "_5104": ["TorqueConverterTurbineCompoundModalAnalysisAtAStiffness"],
        "_5105": ["UnbalancedMassCompoundModalAnalysisAtAStiffness"],
        "_5106": ["VirtualComponentCompoundModalAnalysisAtAStiffness"],
        "_5107": ["WormGearCompoundModalAnalysisAtAStiffness"],
        "_5108": ["WormGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5109": ["WormGearSetCompoundModalAnalysisAtAStiffness"],
        "_5110": ["ZerolBevelGearCompoundModalAnalysisAtAStiffness"],
        "_5111": ["ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5112": ["ZerolBevelGearSetCompoundModalAnalysisAtAStiffness"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundModalAnalysisAtAStiffness",
    "AbstractShaftCompoundModalAnalysisAtAStiffness",
    "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness",
    "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
    "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
    "AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness",
    "AssemblyCompoundModalAnalysisAtAStiffness",
    "BearingCompoundModalAnalysisAtAStiffness",
    "BeltConnectionCompoundModalAnalysisAtAStiffness",
    "BeltDriveCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialGearCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness",
    "BevelGearCompoundModalAnalysisAtAStiffness",
    "BevelGearMeshCompoundModalAnalysisAtAStiffness",
    "BevelGearSetCompoundModalAnalysisAtAStiffness",
    "BoltCompoundModalAnalysisAtAStiffness",
    "BoltedJointCompoundModalAnalysisAtAStiffness",
    "ClutchCompoundModalAnalysisAtAStiffness",
    "ClutchConnectionCompoundModalAnalysisAtAStiffness",
    "ClutchHalfCompoundModalAnalysisAtAStiffness",
    "CoaxialConnectionCompoundModalAnalysisAtAStiffness",
    "ComponentCompoundModalAnalysisAtAStiffness",
    "ConceptCouplingCompoundModalAnalysisAtAStiffness",
    "ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness",
    "ConceptCouplingHalfCompoundModalAnalysisAtAStiffness",
    "ConceptGearCompoundModalAnalysisAtAStiffness",
    "ConceptGearMeshCompoundModalAnalysisAtAStiffness",
    "ConceptGearSetCompoundModalAnalysisAtAStiffness",
    "ConicalGearCompoundModalAnalysisAtAStiffness",
    "ConicalGearMeshCompoundModalAnalysisAtAStiffness",
    "ConicalGearSetCompoundModalAnalysisAtAStiffness",
    "ConnectionCompoundModalAnalysisAtAStiffness",
    "ConnectorCompoundModalAnalysisAtAStiffness",
    "CouplingCompoundModalAnalysisAtAStiffness",
    "CouplingConnectionCompoundModalAnalysisAtAStiffness",
    "CouplingHalfCompoundModalAnalysisAtAStiffness",
    "CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
    "CVTCompoundModalAnalysisAtAStiffness",
    "CVTPulleyCompoundModalAnalysisAtAStiffness",
    "CycloidalAssemblyCompoundModalAnalysisAtAStiffness",
    "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
    "CycloidalDiscCompoundModalAnalysisAtAStiffness",
    "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness",
    "CylindricalGearCompoundModalAnalysisAtAStiffness",
    "CylindricalGearMeshCompoundModalAnalysisAtAStiffness",
    "CylindricalGearSetCompoundModalAnalysisAtAStiffness",
    "CylindricalPlanetGearCompoundModalAnalysisAtAStiffness",
    "DatumCompoundModalAnalysisAtAStiffness",
    "ExternalCADModelCompoundModalAnalysisAtAStiffness",
    "FaceGearCompoundModalAnalysisAtAStiffness",
    "FaceGearMeshCompoundModalAnalysisAtAStiffness",
    "FaceGearSetCompoundModalAnalysisAtAStiffness",
    "FEPartCompoundModalAnalysisAtAStiffness",
    "FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness",
    "GearCompoundModalAnalysisAtAStiffness",
    "GearMeshCompoundModalAnalysisAtAStiffness",
    "GearSetCompoundModalAnalysisAtAStiffness",
    "GuideDxfModelCompoundModalAnalysisAtAStiffness",
    "HypoidGearCompoundModalAnalysisAtAStiffness",
    "HypoidGearMeshCompoundModalAnalysisAtAStiffness",
    "HypoidGearSetCompoundModalAnalysisAtAStiffness",
    "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness",
    "MassDiscCompoundModalAnalysisAtAStiffness",
    "MeasurementComponentCompoundModalAnalysisAtAStiffness",
    "MountableComponentCompoundModalAnalysisAtAStiffness",
    "OilSealCompoundModalAnalysisAtAStiffness",
    "PartCompoundModalAnalysisAtAStiffness",
    "PartToPartShearCouplingCompoundModalAnalysisAtAStiffness",
    "PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness",
    "PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness",
    "PlanetaryConnectionCompoundModalAnalysisAtAStiffness",
    "PlanetaryGearSetCompoundModalAnalysisAtAStiffness",
    "PlanetCarrierCompoundModalAnalysisAtAStiffness",
    "PointLoadCompoundModalAnalysisAtAStiffness",
    "PowerLoadCompoundModalAnalysisAtAStiffness",
    "PulleyCompoundModalAnalysisAtAStiffness",
    "RingPinsCompoundModalAnalysisAtAStiffness",
    "RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness",
    "RollingRingAssemblyCompoundModalAnalysisAtAStiffness",
    "RollingRingCompoundModalAnalysisAtAStiffness",
    "RollingRingConnectionCompoundModalAnalysisAtAStiffness",
    "RootAssemblyCompoundModalAnalysisAtAStiffness",
    "ShaftCompoundModalAnalysisAtAStiffness",
    "ShaftHubConnectionCompoundModalAnalysisAtAStiffness",
    "ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
    "SpiralBevelGearCompoundModalAnalysisAtAStiffness",
    "SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "SpiralBevelGearSetCompoundModalAnalysisAtAStiffness",
    "SpringDamperCompoundModalAnalysisAtAStiffness",
    "SpringDamperConnectionCompoundModalAnalysisAtAStiffness",
    "SpringDamperHalfCompoundModalAnalysisAtAStiffness",
    "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
    "StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness",
    "StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness",
    "StraightBevelGearCompoundModalAnalysisAtAStiffness",
    "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "StraightBevelGearSetCompoundModalAnalysisAtAStiffness",
    "StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness",
    "StraightBevelSunGearCompoundModalAnalysisAtAStiffness",
    "SynchroniserCompoundModalAnalysisAtAStiffness",
    "SynchroniserHalfCompoundModalAnalysisAtAStiffness",
    "SynchroniserPartCompoundModalAnalysisAtAStiffness",
    "SynchroniserSleeveCompoundModalAnalysisAtAStiffness",
    "TorqueConverterCompoundModalAnalysisAtAStiffness",
    "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
    "TorqueConverterPumpCompoundModalAnalysisAtAStiffness",
    "TorqueConverterTurbineCompoundModalAnalysisAtAStiffness",
    "UnbalancedMassCompoundModalAnalysisAtAStiffness",
    "VirtualComponentCompoundModalAnalysisAtAStiffness",
    "WormGearCompoundModalAnalysisAtAStiffness",
    "WormGearMeshCompoundModalAnalysisAtAStiffness",
    "WormGearSetCompoundModalAnalysisAtAStiffness",
    "ZerolBevelGearCompoundModalAnalysisAtAStiffness",
    "ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
)
