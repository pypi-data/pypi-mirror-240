"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5113 import AbstractAssemblyModalAnalysisAtASpeed
    from ._5114 import AbstractShaftModalAnalysisAtASpeed
    from ._5115 import AbstractShaftOrHousingModalAnalysisAtASpeed
    from ._5116 import AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed
    from ._5117 import AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
    from ._5118 import AGMAGleasonConicalGearModalAnalysisAtASpeed
    from ._5119 import AGMAGleasonConicalGearSetModalAnalysisAtASpeed
    from ._5120 import AssemblyModalAnalysisAtASpeed
    from ._5121 import BearingModalAnalysisAtASpeed
    from ._5122 import BeltConnectionModalAnalysisAtASpeed
    from ._5123 import BeltDriveModalAnalysisAtASpeed
    from ._5124 import BevelDifferentialGearMeshModalAnalysisAtASpeed
    from ._5125 import BevelDifferentialGearModalAnalysisAtASpeed
    from ._5126 import BevelDifferentialGearSetModalAnalysisAtASpeed
    from ._5127 import BevelDifferentialPlanetGearModalAnalysisAtASpeed
    from ._5128 import BevelDifferentialSunGearModalAnalysisAtASpeed
    from ._5129 import BevelGearMeshModalAnalysisAtASpeed
    from ._5130 import BevelGearModalAnalysisAtASpeed
    from ._5131 import BevelGearSetModalAnalysisAtASpeed
    from ._5132 import BoltedJointModalAnalysisAtASpeed
    from ._5133 import BoltModalAnalysisAtASpeed
    from ._5134 import ClutchConnectionModalAnalysisAtASpeed
    from ._5135 import ClutchHalfModalAnalysisAtASpeed
    from ._5136 import ClutchModalAnalysisAtASpeed
    from ._5137 import CoaxialConnectionModalAnalysisAtASpeed
    from ._5138 import ComponentModalAnalysisAtASpeed
    from ._5139 import ConceptCouplingConnectionModalAnalysisAtASpeed
    from ._5140 import ConceptCouplingHalfModalAnalysisAtASpeed
    from ._5141 import ConceptCouplingModalAnalysisAtASpeed
    from ._5142 import ConceptGearMeshModalAnalysisAtASpeed
    from ._5143 import ConceptGearModalAnalysisAtASpeed
    from ._5144 import ConceptGearSetModalAnalysisAtASpeed
    from ._5145 import ConicalGearMeshModalAnalysisAtASpeed
    from ._5146 import ConicalGearModalAnalysisAtASpeed
    from ._5147 import ConicalGearSetModalAnalysisAtASpeed
    from ._5148 import ConnectionModalAnalysisAtASpeed
    from ._5149 import ConnectorModalAnalysisAtASpeed
    from ._5150 import CouplingConnectionModalAnalysisAtASpeed
    from ._5151 import CouplingHalfModalAnalysisAtASpeed
    from ._5152 import CouplingModalAnalysisAtASpeed
    from ._5153 import CVTBeltConnectionModalAnalysisAtASpeed
    from ._5154 import CVTModalAnalysisAtASpeed
    from ._5155 import CVTPulleyModalAnalysisAtASpeed
    from ._5156 import CycloidalAssemblyModalAnalysisAtASpeed
    from ._5157 import CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed
    from ._5158 import CycloidalDiscModalAnalysisAtASpeed
    from ._5159 import CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed
    from ._5160 import CylindricalGearMeshModalAnalysisAtASpeed
    from ._5161 import CylindricalGearModalAnalysisAtASpeed
    from ._5162 import CylindricalGearSetModalAnalysisAtASpeed
    from ._5163 import CylindricalPlanetGearModalAnalysisAtASpeed
    from ._5164 import DatumModalAnalysisAtASpeed
    from ._5165 import ExternalCADModelModalAnalysisAtASpeed
    from ._5166 import FaceGearMeshModalAnalysisAtASpeed
    from ._5167 import FaceGearModalAnalysisAtASpeed
    from ._5168 import FaceGearSetModalAnalysisAtASpeed
    from ._5169 import FEPartModalAnalysisAtASpeed
    from ._5170 import FlexiblePinAssemblyModalAnalysisAtASpeed
    from ._5171 import GearMeshModalAnalysisAtASpeed
    from ._5172 import GearModalAnalysisAtASpeed
    from ._5173 import GearSetModalAnalysisAtASpeed
    from ._5174 import GuideDxfModelModalAnalysisAtASpeed
    from ._5175 import HypoidGearMeshModalAnalysisAtASpeed
    from ._5176 import HypoidGearModalAnalysisAtASpeed
    from ._5177 import HypoidGearSetModalAnalysisAtASpeed
    from ._5178 import InterMountableComponentConnectionModalAnalysisAtASpeed
    from ._5179 import KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
    from ._5180 import KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed
    from ._5181 import KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed
    from ._5182 import KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed
    from ._5183 import KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed
    from ._5184 import KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed
    from ._5185 import KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed
    from ._5186 import KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed
    from ._5187 import KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed
    from ._5188 import MassDiscModalAnalysisAtASpeed
    from ._5189 import MeasurementComponentModalAnalysisAtASpeed
    from ._5190 import ModalAnalysisAtASpeed
    from ._5191 import MountableComponentModalAnalysisAtASpeed
    from ._5192 import OilSealModalAnalysisAtASpeed
    from ._5193 import PartModalAnalysisAtASpeed
    from ._5194 import PartToPartShearCouplingConnectionModalAnalysisAtASpeed
    from ._5195 import PartToPartShearCouplingHalfModalAnalysisAtASpeed
    from ._5196 import PartToPartShearCouplingModalAnalysisAtASpeed
    from ._5197 import PlanetaryConnectionModalAnalysisAtASpeed
    from ._5198 import PlanetaryGearSetModalAnalysisAtASpeed
    from ._5199 import PlanetCarrierModalAnalysisAtASpeed
    from ._5200 import PointLoadModalAnalysisAtASpeed
    from ._5201 import PowerLoadModalAnalysisAtASpeed
    from ._5202 import PulleyModalAnalysisAtASpeed
    from ._5203 import RingPinsModalAnalysisAtASpeed
    from ._5204 import RingPinsToDiscConnectionModalAnalysisAtASpeed
    from ._5205 import RollingRingAssemblyModalAnalysisAtASpeed
    from ._5206 import RollingRingConnectionModalAnalysisAtASpeed
    from ._5207 import RollingRingModalAnalysisAtASpeed
    from ._5208 import RootAssemblyModalAnalysisAtASpeed
    from ._5209 import ShaftHubConnectionModalAnalysisAtASpeed
    from ._5210 import ShaftModalAnalysisAtASpeed
    from ._5211 import ShaftToMountableComponentConnectionModalAnalysisAtASpeed
    from ._5212 import SpecialisedAssemblyModalAnalysisAtASpeed
    from ._5213 import SpiralBevelGearMeshModalAnalysisAtASpeed
    from ._5214 import SpiralBevelGearModalAnalysisAtASpeed
    from ._5215 import SpiralBevelGearSetModalAnalysisAtASpeed
    from ._5216 import SpringDamperConnectionModalAnalysisAtASpeed
    from ._5217 import SpringDamperHalfModalAnalysisAtASpeed
    from ._5218 import SpringDamperModalAnalysisAtASpeed
    from ._5219 import StraightBevelDiffGearMeshModalAnalysisAtASpeed
    from ._5220 import StraightBevelDiffGearModalAnalysisAtASpeed
    from ._5221 import StraightBevelDiffGearSetModalAnalysisAtASpeed
    from ._5222 import StraightBevelGearMeshModalAnalysisAtASpeed
    from ._5223 import StraightBevelGearModalAnalysisAtASpeed
    from ._5224 import StraightBevelGearSetModalAnalysisAtASpeed
    from ._5225 import StraightBevelPlanetGearModalAnalysisAtASpeed
    from ._5226 import StraightBevelSunGearModalAnalysisAtASpeed
    from ._5227 import SynchroniserHalfModalAnalysisAtASpeed
    from ._5228 import SynchroniserModalAnalysisAtASpeed
    from ._5229 import SynchroniserPartModalAnalysisAtASpeed
    from ._5230 import SynchroniserSleeveModalAnalysisAtASpeed
    from ._5231 import TorqueConverterConnectionModalAnalysisAtASpeed
    from ._5232 import TorqueConverterModalAnalysisAtASpeed
    from ._5233 import TorqueConverterPumpModalAnalysisAtASpeed
    from ._5234 import TorqueConverterTurbineModalAnalysisAtASpeed
    from ._5235 import UnbalancedMassModalAnalysisAtASpeed
    from ._5236 import VirtualComponentModalAnalysisAtASpeed
    from ._5237 import WormGearMeshModalAnalysisAtASpeed
    from ._5238 import WormGearModalAnalysisAtASpeed
    from ._5239 import WormGearSetModalAnalysisAtASpeed
    from ._5240 import ZerolBevelGearMeshModalAnalysisAtASpeed
    from ._5241 import ZerolBevelGearModalAnalysisAtASpeed
    from ._5242 import ZerolBevelGearSetModalAnalysisAtASpeed
else:
    import_structure = {
        "_5113": ["AbstractAssemblyModalAnalysisAtASpeed"],
        "_5114": ["AbstractShaftModalAnalysisAtASpeed"],
        "_5115": ["AbstractShaftOrHousingModalAnalysisAtASpeed"],
        "_5116": ["AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed"],
        "_5117": ["AGMAGleasonConicalGearMeshModalAnalysisAtASpeed"],
        "_5118": ["AGMAGleasonConicalGearModalAnalysisAtASpeed"],
        "_5119": ["AGMAGleasonConicalGearSetModalAnalysisAtASpeed"],
        "_5120": ["AssemblyModalAnalysisAtASpeed"],
        "_5121": ["BearingModalAnalysisAtASpeed"],
        "_5122": ["BeltConnectionModalAnalysisAtASpeed"],
        "_5123": ["BeltDriveModalAnalysisAtASpeed"],
        "_5124": ["BevelDifferentialGearMeshModalAnalysisAtASpeed"],
        "_5125": ["BevelDifferentialGearModalAnalysisAtASpeed"],
        "_5126": ["BevelDifferentialGearSetModalAnalysisAtASpeed"],
        "_5127": ["BevelDifferentialPlanetGearModalAnalysisAtASpeed"],
        "_5128": ["BevelDifferentialSunGearModalAnalysisAtASpeed"],
        "_5129": ["BevelGearMeshModalAnalysisAtASpeed"],
        "_5130": ["BevelGearModalAnalysisAtASpeed"],
        "_5131": ["BevelGearSetModalAnalysisAtASpeed"],
        "_5132": ["BoltedJointModalAnalysisAtASpeed"],
        "_5133": ["BoltModalAnalysisAtASpeed"],
        "_5134": ["ClutchConnectionModalAnalysisAtASpeed"],
        "_5135": ["ClutchHalfModalAnalysisAtASpeed"],
        "_5136": ["ClutchModalAnalysisAtASpeed"],
        "_5137": ["CoaxialConnectionModalAnalysisAtASpeed"],
        "_5138": ["ComponentModalAnalysisAtASpeed"],
        "_5139": ["ConceptCouplingConnectionModalAnalysisAtASpeed"],
        "_5140": ["ConceptCouplingHalfModalAnalysisAtASpeed"],
        "_5141": ["ConceptCouplingModalAnalysisAtASpeed"],
        "_5142": ["ConceptGearMeshModalAnalysisAtASpeed"],
        "_5143": ["ConceptGearModalAnalysisAtASpeed"],
        "_5144": ["ConceptGearSetModalAnalysisAtASpeed"],
        "_5145": ["ConicalGearMeshModalAnalysisAtASpeed"],
        "_5146": ["ConicalGearModalAnalysisAtASpeed"],
        "_5147": ["ConicalGearSetModalAnalysisAtASpeed"],
        "_5148": ["ConnectionModalAnalysisAtASpeed"],
        "_5149": ["ConnectorModalAnalysisAtASpeed"],
        "_5150": ["CouplingConnectionModalAnalysisAtASpeed"],
        "_5151": ["CouplingHalfModalAnalysisAtASpeed"],
        "_5152": ["CouplingModalAnalysisAtASpeed"],
        "_5153": ["CVTBeltConnectionModalAnalysisAtASpeed"],
        "_5154": ["CVTModalAnalysisAtASpeed"],
        "_5155": ["CVTPulleyModalAnalysisAtASpeed"],
        "_5156": ["CycloidalAssemblyModalAnalysisAtASpeed"],
        "_5157": ["CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed"],
        "_5158": ["CycloidalDiscModalAnalysisAtASpeed"],
        "_5159": ["CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed"],
        "_5160": ["CylindricalGearMeshModalAnalysisAtASpeed"],
        "_5161": ["CylindricalGearModalAnalysisAtASpeed"],
        "_5162": ["CylindricalGearSetModalAnalysisAtASpeed"],
        "_5163": ["CylindricalPlanetGearModalAnalysisAtASpeed"],
        "_5164": ["DatumModalAnalysisAtASpeed"],
        "_5165": ["ExternalCADModelModalAnalysisAtASpeed"],
        "_5166": ["FaceGearMeshModalAnalysisAtASpeed"],
        "_5167": ["FaceGearModalAnalysisAtASpeed"],
        "_5168": ["FaceGearSetModalAnalysisAtASpeed"],
        "_5169": ["FEPartModalAnalysisAtASpeed"],
        "_5170": ["FlexiblePinAssemblyModalAnalysisAtASpeed"],
        "_5171": ["GearMeshModalAnalysisAtASpeed"],
        "_5172": ["GearModalAnalysisAtASpeed"],
        "_5173": ["GearSetModalAnalysisAtASpeed"],
        "_5174": ["GuideDxfModelModalAnalysisAtASpeed"],
        "_5175": ["HypoidGearMeshModalAnalysisAtASpeed"],
        "_5176": ["HypoidGearModalAnalysisAtASpeed"],
        "_5177": ["HypoidGearSetModalAnalysisAtASpeed"],
        "_5178": ["InterMountableComponentConnectionModalAnalysisAtASpeed"],
        "_5179": ["KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed"],
        "_5180": ["KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed"],
        "_5181": ["KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed"],
        "_5182": ["KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed"],
        "_5183": ["KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed"],
        "_5184": ["KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed"],
        "_5185": ["KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed"],
        "_5186": ["KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed"],
        "_5187": ["KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed"],
        "_5188": ["MassDiscModalAnalysisAtASpeed"],
        "_5189": ["MeasurementComponentModalAnalysisAtASpeed"],
        "_5190": ["ModalAnalysisAtASpeed"],
        "_5191": ["MountableComponentModalAnalysisAtASpeed"],
        "_5192": ["OilSealModalAnalysisAtASpeed"],
        "_5193": ["PartModalAnalysisAtASpeed"],
        "_5194": ["PartToPartShearCouplingConnectionModalAnalysisAtASpeed"],
        "_5195": ["PartToPartShearCouplingHalfModalAnalysisAtASpeed"],
        "_5196": ["PartToPartShearCouplingModalAnalysisAtASpeed"],
        "_5197": ["PlanetaryConnectionModalAnalysisAtASpeed"],
        "_5198": ["PlanetaryGearSetModalAnalysisAtASpeed"],
        "_5199": ["PlanetCarrierModalAnalysisAtASpeed"],
        "_5200": ["PointLoadModalAnalysisAtASpeed"],
        "_5201": ["PowerLoadModalAnalysisAtASpeed"],
        "_5202": ["PulleyModalAnalysisAtASpeed"],
        "_5203": ["RingPinsModalAnalysisAtASpeed"],
        "_5204": ["RingPinsToDiscConnectionModalAnalysisAtASpeed"],
        "_5205": ["RollingRingAssemblyModalAnalysisAtASpeed"],
        "_5206": ["RollingRingConnectionModalAnalysisAtASpeed"],
        "_5207": ["RollingRingModalAnalysisAtASpeed"],
        "_5208": ["RootAssemblyModalAnalysisAtASpeed"],
        "_5209": ["ShaftHubConnectionModalAnalysisAtASpeed"],
        "_5210": ["ShaftModalAnalysisAtASpeed"],
        "_5211": ["ShaftToMountableComponentConnectionModalAnalysisAtASpeed"],
        "_5212": ["SpecialisedAssemblyModalAnalysisAtASpeed"],
        "_5213": ["SpiralBevelGearMeshModalAnalysisAtASpeed"],
        "_5214": ["SpiralBevelGearModalAnalysisAtASpeed"],
        "_5215": ["SpiralBevelGearSetModalAnalysisAtASpeed"],
        "_5216": ["SpringDamperConnectionModalAnalysisAtASpeed"],
        "_5217": ["SpringDamperHalfModalAnalysisAtASpeed"],
        "_5218": ["SpringDamperModalAnalysisAtASpeed"],
        "_5219": ["StraightBevelDiffGearMeshModalAnalysisAtASpeed"],
        "_5220": ["StraightBevelDiffGearModalAnalysisAtASpeed"],
        "_5221": ["StraightBevelDiffGearSetModalAnalysisAtASpeed"],
        "_5222": ["StraightBevelGearMeshModalAnalysisAtASpeed"],
        "_5223": ["StraightBevelGearModalAnalysisAtASpeed"],
        "_5224": ["StraightBevelGearSetModalAnalysisAtASpeed"],
        "_5225": ["StraightBevelPlanetGearModalAnalysisAtASpeed"],
        "_5226": ["StraightBevelSunGearModalAnalysisAtASpeed"],
        "_5227": ["SynchroniserHalfModalAnalysisAtASpeed"],
        "_5228": ["SynchroniserModalAnalysisAtASpeed"],
        "_5229": ["SynchroniserPartModalAnalysisAtASpeed"],
        "_5230": ["SynchroniserSleeveModalAnalysisAtASpeed"],
        "_5231": ["TorqueConverterConnectionModalAnalysisAtASpeed"],
        "_5232": ["TorqueConverterModalAnalysisAtASpeed"],
        "_5233": ["TorqueConverterPumpModalAnalysisAtASpeed"],
        "_5234": ["TorqueConverterTurbineModalAnalysisAtASpeed"],
        "_5235": ["UnbalancedMassModalAnalysisAtASpeed"],
        "_5236": ["VirtualComponentModalAnalysisAtASpeed"],
        "_5237": ["WormGearMeshModalAnalysisAtASpeed"],
        "_5238": ["WormGearModalAnalysisAtASpeed"],
        "_5239": ["WormGearSetModalAnalysisAtASpeed"],
        "_5240": ["ZerolBevelGearMeshModalAnalysisAtASpeed"],
        "_5241": ["ZerolBevelGearModalAnalysisAtASpeed"],
        "_5242": ["ZerolBevelGearSetModalAnalysisAtASpeed"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyModalAnalysisAtASpeed",
    "AbstractShaftModalAnalysisAtASpeed",
    "AbstractShaftOrHousingModalAnalysisAtASpeed",
    "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
    "AssemblyModalAnalysisAtASpeed",
    "BearingModalAnalysisAtASpeed",
    "BeltConnectionModalAnalysisAtASpeed",
    "BeltDriveModalAnalysisAtASpeed",
    "BevelDifferentialGearMeshModalAnalysisAtASpeed",
    "BevelDifferentialGearModalAnalysisAtASpeed",
    "BevelDifferentialGearSetModalAnalysisAtASpeed",
    "BevelDifferentialPlanetGearModalAnalysisAtASpeed",
    "BevelDifferentialSunGearModalAnalysisAtASpeed",
    "BevelGearMeshModalAnalysisAtASpeed",
    "BevelGearModalAnalysisAtASpeed",
    "BevelGearSetModalAnalysisAtASpeed",
    "BoltedJointModalAnalysisAtASpeed",
    "BoltModalAnalysisAtASpeed",
    "ClutchConnectionModalAnalysisAtASpeed",
    "ClutchHalfModalAnalysisAtASpeed",
    "ClutchModalAnalysisAtASpeed",
    "CoaxialConnectionModalAnalysisAtASpeed",
    "ComponentModalAnalysisAtASpeed",
    "ConceptCouplingConnectionModalAnalysisAtASpeed",
    "ConceptCouplingHalfModalAnalysisAtASpeed",
    "ConceptCouplingModalAnalysisAtASpeed",
    "ConceptGearMeshModalAnalysisAtASpeed",
    "ConceptGearModalAnalysisAtASpeed",
    "ConceptGearSetModalAnalysisAtASpeed",
    "ConicalGearMeshModalAnalysisAtASpeed",
    "ConicalGearModalAnalysisAtASpeed",
    "ConicalGearSetModalAnalysisAtASpeed",
    "ConnectionModalAnalysisAtASpeed",
    "ConnectorModalAnalysisAtASpeed",
    "CouplingConnectionModalAnalysisAtASpeed",
    "CouplingHalfModalAnalysisAtASpeed",
    "CouplingModalAnalysisAtASpeed",
    "CVTBeltConnectionModalAnalysisAtASpeed",
    "CVTModalAnalysisAtASpeed",
    "CVTPulleyModalAnalysisAtASpeed",
    "CycloidalAssemblyModalAnalysisAtASpeed",
    "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed",
    "CycloidalDiscModalAnalysisAtASpeed",
    "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed",
    "CylindricalGearMeshModalAnalysisAtASpeed",
    "CylindricalGearModalAnalysisAtASpeed",
    "CylindricalGearSetModalAnalysisAtASpeed",
    "CylindricalPlanetGearModalAnalysisAtASpeed",
    "DatumModalAnalysisAtASpeed",
    "ExternalCADModelModalAnalysisAtASpeed",
    "FaceGearMeshModalAnalysisAtASpeed",
    "FaceGearModalAnalysisAtASpeed",
    "FaceGearSetModalAnalysisAtASpeed",
    "FEPartModalAnalysisAtASpeed",
    "FlexiblePinAssemblyModalAnalysisAtASpeed",
    "GearMeshModalAnalysisAtASpeed",
    "GearModalAnalysisAtASpeed",
    "GearSetModalAnalysisAtASpeed",
    "GuideDxfModelModalAnalysisAtASpeed",
    "HypoidGearMeshModalAnalysisAtASpeed",
    "HypoidGearModalAnalysisAtASpeed",
    "HypoidGearSetModalAnalysisAtASpeed",
    "InterMountableComponentConnectionModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
    "MassDiscModalAnalysisAtASpeed",
    "MeasurementComponentModalAnalysisAtASpeed",
    "ModalAnalysisAtASpeed",
    "MountableComponentModalAnalysisAtASpeed",
    "OilSealModalAnalysisAtASpeed",
    "PartModalAnalysisAtASpeed",
    "PartToPartShearCouplingConnectionModalAnalysisAtASpeed",
    "PartToPartShearCouplingHalfModalAnalysisAtASpeed",
    "PartToPartShearCouplingModalAnalysisAtASpeed",
    "PlanetaryConnectionModalAnalysisAtASpeed",
    "PlanetaryGearSetModalAnalysisAtASpeed",
    "PlanetCarrierModalAnalysisAtASpeed",
    "PointLoadModalAnalysisAtASpeed",
    "PowerLoadModalAnalysisAtASpeed",
    "PulleyModalAnalysisAtASpeed",
    "RingPinsModalAnalysisAtASpeed",
    "RingPinsToDiscConnectionModalAnalysisAtASpeed",
    "RollingRingAssemblyModalAnalysisAtASpeed",
    "RollingRingConnectionModalAnalysisAtASpeed",
    "RollingRingModalAnalysisAtASpeed",
    "RootAssemblyModalAnalysisAtASpeed",
    "ShaftHubConnectionModalAnalysisAtASpeed",
    "ShaftModalAnalysisAtASpeed",
    "ShaftToMountableComponentConnectionModalAnalysisAtASpeed",
    "SpecialisedAssemblyModalAnalysisAtASpeed",
    "SpiralBevelGearMeshModalAnalysisAtASpeed",
    "SpiralBevelGearModalAnalysisAtASpeed",
    "SpiralBevelGearSetModalAnalysisAtASpeed",
    "SpringDamperConnectionModalAnalysisAtASpeed",
    "SpringDamperHalfModalAnalysisAtASpeed",
    "SpringDamperModalAnalysisAtASpeed",
    "StraightBevelDiffGearMeshModalAnalysisAtASpeed",
    "StraightBevelDiffGearModalAnalysisAtASpeed",
    "StraightBevelDiffGearSetModalAnalysisAtASpeed",
    "StraightBevelGearMeshModalAnalysisAtASpeed",
    "StraightBevelGearModalAnalysisAtASpeed",
    "StraightBevelGearSetModalAnalysisAtASpeed",
    "StraightBevelPlanetGearModalAnalysisAtASpeed",
    "StraightBevelSunGearModalAnalysisAtASpeed",
    "SynchroniserHalfModalAnalysisAtASpeed",
    "SynchroniserModalAnalysisAtASpeed",
    "SynchroniserPartModalAnalysisAtASpeed",
    "SynchroniserSleeveModalAnalysisAtASpeed",
    "TorqueConverterConnectionModalAnalysisAtASpeed",
    "TorqueConverterModalAnalysisAtASpeed",
    "TorqueConverterPumpModalAnalysisAtASpeed",
    "TorqueConverterTurbineModalAnalysisAtASpeed",
    "UnbalancedMassModalAnalysisAtASpeed",
    "VirtualComponentModalAnalysisAtASpeed",
    "WormGearMeshModalAnalysisAtASpeed",
    "WormGearModalAnalysisAtASpeed",
    "WormGearSetModalAnalysisAtASpeed",
    "ZerolBevelGearMeshModalAnalysisAtASpeed",
    "ZerolBevelGearModalAnalysisAtASpeed",
    "ZerolBevelGearSetModalAnalysisAtASpeed",
)
