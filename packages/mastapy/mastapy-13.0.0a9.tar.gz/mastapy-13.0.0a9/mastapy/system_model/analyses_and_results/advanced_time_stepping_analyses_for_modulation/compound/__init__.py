"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7137 import AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7138 import AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7139 import (
        AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7140 import (
        AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7141 import (
        AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7142 import (
        AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7143 import (
        AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7144 import AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7145 import BearingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7146 import BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7147 import BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7148 import (
        BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7149 import (
        BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7150 import (
        BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7151 import (
        BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7152 import (
        BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7153 import BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7154 import BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7155 import BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7156 import BoltCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7157 import BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7158 import ClutchCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7159 import ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7160 import ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7161 import (
        CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7162 import ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7163 import ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7164 import (
        ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7165 import (
        ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7166 import ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7167 import ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7168 import ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7169 import ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7170 import ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7171 import ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7172 import ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7173 import ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7174 import CouplingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7175 import (
        CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7176 import CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7177 import (
        CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7178 import CVTCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7179 import CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7180 import (
        CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7181 import (
        CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7182 import CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7183 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7184 import CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7185 import (
        CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7186 import (
        CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7187 import (
        CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7188 import DatumCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7189 import ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7190 import FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7191 import FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7192 import FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7193 import FEPartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7194 import (
        FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7195 import GearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7196 import GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7197 import GearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7198 import GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7199 import HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7200 import HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7201 import HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7202 import (
        InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7203 import (
        KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7204 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7205 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7206 import (
        KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7207 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7208 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7209 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7210 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7211 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7212 import MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7213 import (
        MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7214 import (
        MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7215 import OilSealCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7216 import PartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7217 import (
        PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7218 import (
        PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7219 import (
        PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7220 import (
        PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7221 import PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7222 import PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7223 import PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7224 import PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7225 import PulleyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7226 import RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7227 import (
        RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7228 import (
        RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7229 import RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7230 import (
        RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7231 import RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7232 import ShaftCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7233 import (
        ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7234 import (
        ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7235 import (
        SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7236 import SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7237 import (
        SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7238 import (
        SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7239 import SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7240 import (
        SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7241 import SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7242 import (
        StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7243 import (
        StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7244 import (
        StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7245 import (
        StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7246 import (
        StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7247 import (
        StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7248 import (
        StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7249 import (
        StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7250 import SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7251 import SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7252 import SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7253 import (
        SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7254 import TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7255 import (
        TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7256 import (
        TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7257 import (
        TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7258 import UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7259 import VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7260 import WormGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7261 import WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7262 import WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7263 import ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7264 import (
        ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7265 import (
        ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
else:
    import_structure = {
        "_7137": ["AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7138": ["AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7139": [
            "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7140": [
            "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7141": [
            "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7142": [
            "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7143": [
            "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7144": ["AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7145": ["BearingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7146": ["BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7147": ["BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7148": [
            "BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7149": [
            "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7150": [
            "BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7151": [
            "BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7152": [
            "BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7153": ["BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7154": ["BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7155": ["BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7156": ["BoltCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7157": ["BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7158": ["ClutchCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7159": ["ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7160": ["ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7161": ["CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7162": ["ComponentCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7163": ["ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7164": [
            "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7165": [
            "ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7166": ["ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7167": ["ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7168": ["ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7169": ["ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7170": ["ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7171": ["ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7172": ["ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7173": ["ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7174": ["CouplingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7175": [
            "CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7176": ["CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7177": ["CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7178": ["CVTCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7179": ["CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7180": ["CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7181": [
            "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7182": ["CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7183": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7184": ["CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7185": [
            "CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7186": [
            "CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7187": [
            "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7188": ["DatumCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7189": ["ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7190": ["FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7191": ["FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7192": ["FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7193": ["FEPartCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7194": [
            "FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7195": ["GearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7196": ["GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7197": ["GearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7198": ["GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7199": ["HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7200": ["HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7201": ["HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7202": [
            "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7203": [
            "KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7204": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7205": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7206": [
            "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7207": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7208": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7209": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7210": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7211": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7212": ["MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7213": [
            "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7214": [
            "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7215": ["OilSealCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7216": ["PartCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7217": [
            "PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7218": [
            "PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7219": [
            "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7220": [
            "PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7221": ["PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7222": ["PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7223": ["PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7224": ["PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7225": ["PulleyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7226": ["RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7227": [
            "RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7228": [
            "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7229": ["RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7230": [
            "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7231": ["RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7232": ["ShaftCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7233": [
            "ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7234": [
            "ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7235": [
            "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7236": ["SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7237": [
            "SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7238": [
            "SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7239": ["SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7240": [
            "SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7241": ["SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7242": [
            "StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7243": [
            "StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7244": [
            "StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7245": ["StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7246": [
            "StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7247": [
            "StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7248": [
            "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7249": [
            "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7250": ["SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7251": ["SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7252": ["SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7253": [
            "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7254": ["TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7255": [
            "TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7256": [
            "TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7257": [
            "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7258": ["UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7259": ["VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7260": ["WormGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7261": ["WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7262": ["WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7263": ["ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7264": [
            "ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7265": ["ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BearingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BoltCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ClutchCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CVTCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "DatumCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FEPartCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation",
    "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "OilSealCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation",
    "UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation",
    "VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "WormGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
)
