"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7002 import AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7003 import AbstractShaftAdvancedTimeSteppingAnalysisForModulation
    from ._7004 import AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation
    from ._7005 import (
        AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7006 import AdvancedTimeSteppingAnalysisForModulation
    from ._7007 import AtsamExcitationsOrOthers
    from ._7008 import AtsamNaturalFrequencyViewOption
    from ._7009 import AdvancedTimeSteppingAnalysisForModulationOptions
    from ._7010 import AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7011 import (
        AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7012 import (
        AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7013 import AssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7014 import ATSAMResultsVsLargeTimeStepSettings
    from ._7015 import BearingAdvancedTimeSteppingAnalysisForModulation
    from ._7016 import BeltConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7017 import BeltDriveAdvancedTimeSteppingAnalysisForModulation
    from ._7018 import BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
    from ._7019 import (
        BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7020 import BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7021 import (
        BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7022 import BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation
    from ._7023 import BevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7024 import BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7025 import BevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7026 import BoltAdvancedTimeSteppingAnalysisForModulation
    from ._7027 import BoltedJointAdvancedTimeSteppingAnalysisForModulation
    from ._7028 import ClutchAdvancedTimeSteppingAnalysisForModulation
    from ._7029 import ClutchConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7030 import ClutchHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7031 import CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7032 import ComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7033 import ConceptCouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7034 import (
        ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7035 import ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7036 import ConceptGearAdvancedTimeSteppingAnalysisForModulation
    from ._7037 import ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7038 import ConceptGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7039 import ConicalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7040 import ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7041 import ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7042 import ConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7043 import ConnectorAdvancedTimeSteppingAnalysisForModulation
    from ._7044 import CouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7045 import CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7046 import CouplingHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7047 import CVTAdvancedTimeSteppingAnalysisForModulation
    from ._7048 import CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7049 import CVTPulleyAdvancedTimeSteppingAnalysisForModulation
    from ._7050 import CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7051 import CycloidalDiscAdvancedTimeSteppingAnalysisForModulation
    from ._7052 import (
        CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7053 import (
        CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7054 import CylindricalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7055 import CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7056 import CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7057 import CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation
    from ._7058 import DatumAdvancedTimeSteppingAnalysisForModulation
    from ._7059 import ExternalCADModelAdvancedTimeSteppingAnalysisForModulation
    from ._7060 import FaceGearAdvancedTimeSteppingAnalysisForModulation
    from ._7061 import FaceGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7062 import FaceGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7063 import FEPartAdvancedTimeSteppingAnalysisForModulation
    from ._7064 import FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7065 import GearAdvancedTimeSteppingAnalysisForModulation
    from ._7066 import GearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7067 import GearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7068 import GuideDxfModelAdvancedTimeSteppingAnalysisForModulation
    from ._7069 import (
        HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7070 import HypoidGearAdvancedTimeSteppingAnalysisForModulation
    from ._7071 import HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7072 import HypoidGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7073 import (
        InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7074 import (
        KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7075 import (
        KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7076 import (
        KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7077 import (
        KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7078 import (
        KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7079 import (
        KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7080 import (
        KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7081 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7082 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7083 import MassDiscAdvancedTimeSteppingAnalysisForModulation
    from ._7084 import MeasurementComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7085 import MountableComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7086 import OilSealAdvancedTimeSteppingAnalysisForModulation
    from ._7087 import PartAdvancedTimeSteppingAnalysisForModulation
    from ._7088 import PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7089 import (
        PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7090 import (
        PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7091 import PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7092 import PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7093 import PlanetCarrierAdvancedTimeSteppingAnalysisForModulation
    from ._7094 import PointLoadAdvancedTimeSteppingAnalysisForModulation
    from ._7095 import PowerLoadAdvancedTimeSteppingAnalysisForModulation
    from ._7096 import PulleyAdvancedTimeSteppingAnalysisForModulation
    from ._7097 import RingPinsAdvancedTimeSteppingAnalysisForModulation
    from ._7098 import RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7099 import RollingRingAdvancedTimeSteppingAnalysisForModulation
    from ._7100 import RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7101 import RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7102 import RootAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7103 import ShaftAdvancedTimeSteppingAnalysisForModulation
    from ._7104 import ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7105 import (
        ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7106 import SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7107 import SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7108 import SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7109 import SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7110 import SpringDamperAdvancedTimeSteppingAnalysisForModulation
    from ._7111 import SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7112 import SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7113 import StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
    from ._7114 import (
        StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7115 import StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7116 import StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7117 import StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7118 import StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7119 import StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation
    from ._7120 import StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
    from ._7121 import SynchroniserAdvancedTimeSteppingAnalysisForModulation
    from ._7122 import SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7123 import SynchroniserPartAdvancedTimeSteppingAnalysisForModulation
    from ._7124 import SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation
    from ._7125 import TorqueConverterAdvancedTimeSteppingAnalysisForModulation
    from ._7126 import (
        TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7127 import TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation
    from ._7128 import TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation
    from ._7129 import UnbalancedMassAdvancedTimeSteppingAnalysisForModulation
    from ._7130 import VirtualComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7131 import WormGearAdvancedTimeSteppingAnalysisForModulation
    from ._7132 import WormGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7133 import WormGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7134 import ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7135 import ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7136 import ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
else:
    import_structure = {
        "_7002": ["AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7003": ["AbstractShaftAdvancedTimeSteppingAnalysisForModulation"],
        "_7004": ["AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation"],
        "_7005": [
            "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7006": ["AdvancedTimeSteppingAnalysisForModulation"],
        "_7007": ["AtsamExcitationsOrOthers"],
        "_7008": ["AtsamNaturalFrequencyViewOption"],
        "_7009": ["AdvancedTimeSteppingAnalysisForModulationOptions"],
        "_7010": ["AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7011": [
            "AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7012": ["AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7013": ["AssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7014": ["ATSAMResultsVsLargeTimeStepSettings"],
        "_7015": ["BearingAdvancedTimeSteppingAnalysisForModulation"],
        "_7016": ["BeltConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7017": ["BeltDriveAdvancedTimeSteppingAnalysisForModulation"],
        "_7018": ["BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7019": ["BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7020": ["BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7021": [
            "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7022": ["BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7023": ["BevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7024": ["BevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7025": ["BevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7026": ["BoltAdvancedTimeSteppingAnalysisForModulation"],
        "_7027": ["BoltedJointAdvancedTimeSteppingAnalysisForModulation"],
        "_7028": ["ClutchAdvancedTimeSteppingAnalysisForModulation"],
        "_7029": ["ClutchConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7030": ["ClutchHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7031": ["CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7032": ["ComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7033": ["ConceptCouplingAdvancedTimeSteppingAnalysisForModulation"],
        "_7034": ["ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7035": ["ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7036": ["ConceptGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7037": ["ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7038": ["ConceptGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7039": ["ConicalGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7040": ["ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7041": ["ConicalGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7042": ["ConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7043": ["ConnectorAdvancedTimeSteppingAnalysisForModulation"],
        "_7044": ["CouplingAdvancedTimeSteppingAnalysisForModulation"],
        "_7045": ["CouplingConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7046": ["CouplingHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7047": ["CVTAdvancedTimeSteppingAnalysisForModulation"],
        "_7048": ["CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7049": ["CVTPulleyAdvancedTimeSteppingAnalysisForModulation"],
        "_7050": ["CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7051": ["CycloidalDiscAdvancedTimeSteppingAnalysisForModulation"],
        "_7052": [
            "CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7053": [
            "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7054": ["CylindricalGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7055": ["CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7056": ["CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7057": ["CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7058": ["DatumAdvancedTimeSteppingAnalysisForModulation"],
        "_7059": ["ExternalCADModelAdvancedTimeSteppingAnalysisForModulation"],
        "_7060": ["FaceGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7061": ["FaceGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7062": ["FaceGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7063": ["FEPartAdvancedTimeSteppingAnalysisForModulation"],
        "_7064": ["FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7065": ["GearAdvancedTimeSteppingAnalysisForModulation"],
        "_7066": ["GearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7067": ["GearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7068": ["GuideDxfModelAdvancedTimeSteppingAnalysisForModulation"],
        "_7069": [
            "HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7070": ["HypoidGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7071": ["HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7072": ["HypoidGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7073": [
            "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7074": [
            "KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7075": [
            "KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7076": [
            "KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7077": [
            "KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7078": [
            "KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7079": [
            "KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7080": [
            "KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7081": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7082": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7083": ["MassDiscAdvancedTimeSteppingAnalysisForModulation"],
        "_7084": ["MeasurementComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7085": ["MountableComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7086": ["OilSealAdvancedTimeSteppingAnalysisForModulation"],
        "_7087": ["PartAdvancedTimeSteppingAnalysisForModulation"],
        "_7088": ["PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation"],
        "_7089": [
            "PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7090": [
            "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7091": ["PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7092": ["PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7093": ["PlanetCarrierAdvancedTimeSteppingAnalysisForModulation"],
        "_7094": ["PointLoadAdvancedTimeSteppingAnalysisForModulation"],
        "_7095": ["PowerLoadAdvancedTimeSteppingAnalysisForModulation"],
        "_7096": ["PulleyAdvancedTimeSteppingAnalysisForModulation"],
        "_7097": ["RingPinsAdvancedTimeSteppingAnalysisForModulation"],
        "_7098": ["RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7099": ["RollingRingAdvancedTimeSteppingAnalysisForModulation"],
        "_7100": ["RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7101": ["RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7102": ["RootAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7103": ["ShaftAdvancedTimeSteppingAnalysisForModulation"],
        "_7104": ["ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7105": [
            "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7106": ["SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7107": ["SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7108": ["SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7109": ["SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7110": ["SpringDamperAdvancedTimeSteppingAnalysisForModulation"],
        "_7111": ["SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7112": ["SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7113": ["StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7114": ["StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7115": ["StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7116": ["StraightBevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7117": ["StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7118": ["StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7119": ["StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7120": ["StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7121": ["SynchroniserAdvancedTimeSteppingAnalysisForModulation"],
        "_7122": ["SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7123": ["SynchroniserPartAdvancedTimeSteppingAnalysisForModulation"],
        "_7124": ["SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation"],
        "_7125": ["TorqueConverterAdvancedTimeSteppingAnalysisForModulation"],
        "_7126": ["TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7127": ["TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation"],
        "_7128": ["TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation"],
        "_7129": ["UnbalancedMassAdvancedTimeSteppingAnalysisForModulation"],
        "_7130": ["VirtualComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7131": ["WormGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7132": ["WormGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7133": ["WormGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7134": ["ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7135": ["ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7136": ["ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    "AdvancedTimeSteppingAnalysisForModulation",
    "AtsamExcitationsOrOthers",
    "AtsamNaturalFrequencyViewOption",
    "AdvancedTimeSteppingAnalysisForModulationOptions",
    "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "AssemblyAdvancedTimeSteppingAnalysisForModulation",
    "ATSAMResultsVsLargeTimeStepSettings",
    "BearingAdvancedTimeSteppingAnalysisForModulation",
    "BeltConnectionAdvancedTimeSteppingAnalysisForModulation",
    "BeltDriveAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "BoltAdvancedTimeSteppingAnalysisForModulation",
    "BoltedJointAdvancedTimeSteppingAnalysisForModulation",
    "ClutchAdvancedTimeSteppingAnalysisForModulation",
    "ClutchConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ClutchHalfAdvancedTimeSteppingAnalysisForModulation",
    "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ComponentAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "ConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ConnectorAdvancedTimeSteppingAnalysisForModulation",
    "CouplingAdvancedTimeSteppingAnalysisForModulation",
    "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
    "CVTAdvancedTimeSteppingAnalysisForModulation",
    "CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CVTPulleyAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",
    "DatumAdvancedTimeSteppingAnalysisForModulation",
    "ExternalCADModelAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearSetAdvancedTimeSteppingAnalysisForModulation",
    "FEPartAdvancedTimeSteppingAnalysisForModulation",
    "FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "GearAdvancedTimeSteppingAnalysisForModulation",
    "GearMeshAdvancedTimeSteppingAnalysisForModulation",
    "GearSetAdvancedTimeSteppingAnalysisForModulation",
    "GuideDxfModelAdvancedTimeSteppingAnalysisForModulation",
    "HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearSetAdvancedTimeSteppingAnalysisForModulation",
    "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "MassDiscAdvancedTimeSteppingAnalysisForModulation",
    "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation",
    "MountableComponentAdvancedTimeSteppingAnalysisForModulation",
    "OilSealAdvancedTimeSteppingAnalysisForModulation",
    "PartAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",
    "PlanetCarrierAdvancedTimeSteppingAnalysisForModulation",
    "PointLoadAdvancedTimeSteppingAnalysisForModulation",
    "PowerLoadAdvancedTimeSteppingAnalysisForModulation",
    "PulleyAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "RootAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "ShaftAdvancedTimeSteppingAnalysisForModulation",
    "ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation",
    "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
    "VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
    "WormGearAdvancedTimeSteppingAnalysisForModulation",
    "WormGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "WormGearSetAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
)
