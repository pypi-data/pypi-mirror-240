"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4568 import AbstractAssemblyModalAnalysis
    from ._4569 import AbstractShaftModalAnalysis
    from ._4570 import AbstractShaftOrHousingModalAnalysis
    from ._4571 import AbstractShaftToMountableComponentConnectionModalAnalysis
    from ._4572 import AGMAGleasonConicalGearMeshModalAnalysis
    from ._4573 import AGMAGleasonConicalGearModalAnalysis
    from ._4574 import AGMAGleasonConicalGearSetModalAnalysis
    from ._4575 import AssemblyModalAnalysis
    from ._4576 import BearingModalAnalysis
    from ._4577 import BeltConnectionModalAnalysis
    from ._4578 import BeltDriveModalAnalysis
    from ._4579 import BevelDifferentialGearMeshModalAnalysis
    from ._4580 import BevelDifferentialGearModalAnalysis
    from ._4581 import BevelDifferentialGearSetModalAnalysis
    from ._4582 import BevelDifferentialPlanetGearModalAnalysis
    from ._4583 import BevelDifferentialSunGearModalAnalysis
    from ._4584 import BevelGearMeshModalAnalysis
    from ._4585 import BevelGearModalAnalysis
    from ._4586 import BevelGearSetModalAnalysis
    from ._4587 import BoltedJointModalAnalysis
    from ._4588 import BoltModalAnalysis
    from ._4589 import ClutchConnectionModalAnalysis
    from ._4590 import ClutchHalfModalAnalysis
    from ._4591 import ClutchModalAnalysis
    from ._4592 import CoaxialConnectionModalAnalysis
    from ._4593 import ComponentModalAnalysis
    from ._4594 import ConceptCouplingConnectionModalAnalysis
    from ._4595 import ConceptCouplingHalfModalAnalysis
    from ._4596 import ConceptCouplingModalAnalysis
    from ._4597 import ConceptGearMeshModalAnalysis
    from ._4598 import ConceptGearModalAnalysis
    from ._4599 import ConceptGearSetModalAnalysis
    from ._4600 import ConicalGearMeshModalAnalysis
    from ._4601 import ConicalGearModalAnalysis
    from ._4602 import ConicalGearSetModalAnalysis
    from ._4603 import ConnectionModalAnalysis
    from ._4604 import ConnectorModalAnalysis
    from ._4605 import CoordinateSystemForWhine
    from ._4606 import CouplingConnectionModalAnalysis
    from ._4607 import CouplingHalfModalAnalysis
    from ._4608 import CouplingModalAnalysis
    from ._4609 import CVTBeltConnectionModalAnalysis
    from ._4610 import CVTModalAnalysis
    from ._4611 import CVTPulleyModalAnalysis
    from ._4612 import CycloidalAssemblyModalAnalysis
    from ._4613 import CycloidalDiscCentralBearingConnectionModalAnalysis
    from ._4614 import CycloidalDiscModalAnalysis
    from ._4615 import CycloidalDiscPlanetaryBearingConnectionModalAnalysis
    from ._4616 import CylindricalGearMeshModalAnalysis
    from ._4617 import CylindricalGearModalAnalysis
    from ._4618 import CylindricalGearSetModalAnalysis
    from ._4619 import CylindricalPlanetGearModalAnalysis
    from ._4620 import DatumModalAnalysis
    from ._4621 import DynamicModelForModalAnalysis
    from ._4622 import DynamicsResponse3DChartType
    from ._4623 import DynamicsResponseType
    from ._4624 import ExternalCADModelModalAnalysis
    from ._4625 import FaceGearMeshModalAnalysis
    from ._4626 import FaceGearModalAnalysis
    from ._4627 import FaceGearSetModalAnalysis
    from ._4628 import FEPartModalAnalysis
    from ._4629 import FlexiblePinAssemblyModalAnalysis
    from ._4630 import FrequencyResponseAnalysisOptions
    from ._4631 import GearMeshModalAnalysis
    from ._4632 import GearModalAnalysis
    from ._4633 import GearSetModalAnalysis
    from ._4634 import GuideDxfModelModalAnalysis
    from ._4635 import HypoidGearMeshModalAnalysis
    from ._4636 import HypoidGearModalAnalysis
    from ._4637 import HypoidGearSetModalAnalysis
    from ._4638 import InterMountableComponentConnectionModalAnalysis
    from ._4639 import KlingelnbergCycloPalloidConicalGearMeshModalAnalysis
    from ._4640 import KlingelnbergCycloPalloidConicalGearModalAnalysis
    from ._4641 import KlingelnbergCycloPalloidConicalGearSetModalAnalysis
    from ._4642 import KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis
    from ._4643 import KlingelnbergCycloPalloidHypoidGearModalAnalysis
    from ._4644 import KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
    from ._4645 import KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis
    from ._4646 import KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
    from ._4647 import KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
    from ._4648 import MassDiscModalAnalysis
    from ._4649 import MeasurementComponentModalAnalysis
    from ._4650 import ModalAnalysis
    from ._4651 import ModalAnalysisBarModelFEExportOptions
    from ._4652 import ModalAnalysisDrawStyle
    from ._4653 import ModalAnalysisOptions
    from ._4654 import MountableComponentModalAnalysis
    from ._4655 import MultipleExcitationsSpeedRangeOption
    from ._4656 import OilSealModalAnalysis
    from ._4657 import OrderCutsChartSettings
    from ._4658 import PartModalAnalysis
    from ._4659 import PartToPartShearCouplingConnectionModalAnalysis
    from ._4660 import PartToPartShearCouplingHalfModalAnalysis
    from ._4661 import PartToPartShearCouplingModalAnalysis
    from ._4662 import PlanetaryConnectionModalAnalysis
    from ._4663 import PlanetaryGearSetModalAnalysis
    from ._4664 import PlanetCarrierModalAnalysis
    from ._4665 import PointLoadModalAnalysis
    from ._4666 import PowerLoadModalAnalysis
    from ._4667 import PulleyModalAnalysis
    from ._4668 import RingPinsModalAnalysis
    from ._4669 import RingPinsToDiscConnectionModalAnalysis
    from ._4670 import RollingRingAssemblyModalAnalysis
    from ._4671 import RollingRingConnectionModalAnalysis
    from ._4672 import RollingRingModalAnalysis
    from ._4673 import RootAssemblyModalAnalysis
    from ._4674 import ShaftHubConnectionModalAnalysis
    from ._4675 import ShaftModalAnalysis
    from ._4676 import ShaftModalAnalysisMode
    from ._4677 import ShaftToMountableComponentConnectionModalAnalysis
    from ._4678 import SpecialisedAssemblyModalAnalysis
    from ._4679 import SpiralBevelGearMeshModalAnalysis
    from ._4680 import SpiralBevelGearModalAnalysis
    from ._4681 import SpiralBevelGearSetModalAnalysis
    from ._4682 import SpringDamperConnectionModalAnalysis
    from ._4683 import SpringDamperHalfModalAnalysis
    from ._4684 import SpringDamperModalAnalysis
    from ._4685 import StraightBevelDiffGearMeshModalAnalysis
    from ._4686 import StraightBevelDiffGearModalAnalysis
    from ._4687 import StraightBevelDiffGearSetModalAnalysis
    from ._4688 import StraightBevelGearMeshModalAnalysis
    from ._4689 import StraightBevelGearModalAnalysis
    from ._4690 import StraightBevelGearSetModalAnalysis
    from ._4691 import StraightBevelPlanetGearModalAnalysis
    from ._4692 import StraightBevelSunGearModalAnalysis
    from ._4693 import SynchroniserHalfModalAnalysis
    from ._4694 import SynchroniserModalAnalysis
    from ._4695 import SynchroniserPartModalAnalysis
    from ._4696 import SynchroniserSleeveModalAnalysis
    from ._4697 import TorqueConverterConnectionModalAnalysis
    from ._4698 import TorqueConverterModalAnalysis
    from ._4699 import TorqueConverterPumpModalAnalysis
    from ._4700 import TorqueConverterTurbineModalAnalysis
    from ._4701 import UnbalancedMassModalAnalysis
    from ._4702 import VirtualComponentModalAnalysis
    from ._4703 import WaterfallChartSettings
    from ._4704 import WhineWaterfallExportOption
    from ._4705 import WhineWaterfallSettings
    from ._4706 import WormGearMeshModalAnalysis
    from ._4707 import WormGearModalAnalysis
    from ._4708 import WormGearSetModalAnalysis
    from ._4709 import ZerolBevelGearMeshModalAnalysis
    from ._4710 import ZerolBevelGearModalAnalysis
    from ._4711 import ZerolBevelGearSetModalAnalysis
else:
    import_structure = {
        "_4568": ["AbstractAssemblyModalAnalysis"],
        "_4569": ["AbstractShaftModalAnalysis"],
        "_4570": ["AbstractShaftOrHousingModalAnalysis"],
        "_4571": ["AbstractShaftToMountableComponentConnectionModalAnalysis"],
        "_4572": ["AGMAGleasonConicalGearMeshModalAnalysis"],
        "_4573": ["AGMAGleasonConicalGearModalAnalysis"],
        "_4574": ["AGMAGleasonConicalGearSetModalAnalysis"],
        "_4575": ["AssemblyModalAnalysis"],
        "_4576": ["BearingModalAnalysis"],
        "_4577": ["BeltConnectionModalAnalysis"],
        "_4578": ["BeltDriveModalAnalysis"],
        "_4579": ["BevelDifferentialGearMeshModalAnalysis"],
        "_4580": ["BevelDifferentialGearModalAnalysis"],
        "_4581": ["BevelDifferentialGearSetModalAnalysis"],
        "_4582": ["BevelDifferentialPlanetGearModalAnalysis"],
        "_4583": ["BevelDifferentialSunGearModalAnalysis"],
        "_4584": ["BevelGearMeshModalAnalysis"],
        "_4585": ["BevelGearModalAnalysis"],
        "_4586": ["BevelGearSetModalAnalysis"],
        "_4587": ["BoltedJointModalAnalysis"],
        "_4588": ["BoltModalAnalysis"],
        "_4589": ["ClutchConnectionModalAnalysis"],
        "_4590": ["ClutchHalfModalAnalysis"],
        "_4591": ["ClutchModalAnalysis"],
        "_4592": ["CoaxialConnectionModalAnalysis"],
        "_4593": ["ComponentModalAnalysis"],
        "_4594": ["ConceptCouplingConnectionModalAnalysis"],
        "_4595": ["ConceptCouplingHalfModalAnalysis"],
        "_4596": ["ConceptCouplingModalAnalysis"],
        "_4597": ["ConceptGearMeshModalAnalysis"],
        "_4598": ["ConceptGearModalAnalysis"],
        "_4599": ["ConceptGearSetModalAnalysis"],
        "_4600": ["ConicalGearMeshModalAnalysis"],
        "_4601": ["ConicalGearModalAnalysis"],
        "_4602": ["ConicalGearSetModalAnalysis"],
        "_4603": ["ConnectionModalAnalysis"],
        "_4604": ["ConnectorModalAnalysis"],
        "_4605": ["CoordinateSystemForWhine"],
        "_4606": ["CouplingConnectionModalAnalysis"],
        "_4607": ["CouplingHalfModalAnalysis"],
        "_4608": ["CouplingModalAnalysis"],
        "_4609": ["CVTBeltConnectionModalAnalysis"],
        "_4610": ["CVTModalAnalysis"],
        "_4611": ["CVTPulleyModalAnalysis"],
        "_4612": ["CycloidalAssemblyModalAnalysis"],
        "_4613": ["CycloidalDiscCentralBearingConnectionModalAnalysis"],
        "_4614": ["CycloidalDiscModalAnalysis"],
        "_4615": ["CycloidalDiscPlanetaryBearingConnectionModalAnalysis"],
        "_4616": ["CylindricalGearMeshModalAnalysis"],
        "_4617": ["CylindricalGearModalAnalysis"],
        "_4618": ["CylindricalGearSetModalAnalysis"],
        "_4619": ["CylindricalPlanetGearModalAnalysis"],
        "_4620": ["DatumModalAnalysis"],
        "_4621": ["DynamicModelForModalAnalysis"],
        "_4622": ["DynamicsResponse3DChartType"],
        "_4623": ["DynamicsResponseType"],
        "_4624": ["ExternalCADModelModalAnalysis"],
        "_4625": ["FaceGearMeshModalAnalysis"],
        "_4626": ["FaceGearModalAnalysis"],
        "_4627": ["FaceGearSetModalAnalysis"],
        "_4628": ["FEPartModalAnalysis"],
        "_4629": ["FlexiblePinAssemblyModalAnalysis"],
        "_4630": ["FrequencyResponseAnalysisOptions"],
        "_4631": ["GearMeshModalAnalysis"],
        "_4632": ["GearModalAnalysis"],
        "_4633": ["GearSetModalAnalysis"],
        "_4634": ["GuideDxfModelModalAnalysis"],
        "_4635": ["HypoidGearMeshModalAnalysis"],
        "_4636": ["HypoidGearModalAnalysis"],
        "_4637": ["HypoidGearSetModalAnalysis"],
        "_4638": ["InterMountableComponentConnectionModalAnalysis"],
        "_4639": ["KlingelnbergCycloPalloidConicalGearMeshModalAnalysis"],
        "_4640": ["KlingelnbergCycloPalloidConicalGearModalAnalysis"],
        "_4641": ["KlingelnbergCycloPalloidConicalGearSetModalAnalysis"],
        "_4642": ["KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis"],
        "_4643": ["KlingelnbergCycloPalloidHypoidGearModalAnalysis"],
        "_4644": ["KlingelnbergCycloPalloidHypoidGearSetModalAnalysis"],
        "_4645": ["KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis"],
        "_4646": ["KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis"],
        "_4647": ["KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis"],
        "_4648": ["MassDiscModalAnalysis"],
        "_4649": ["MeasurementComponentModalAnalysis"],
        "_4650": ["ModalAnalysis"],
        "_4651": ["ModalAnalysisBarModelFEExportOptions"],
        "_4652": ["ModalAnalysisDrawStyle"],
        "_4653": ["ModalAnalysisOptions"],
        "_4654": ["MountableComponentModalAnalysis"],
        "_4655": ["MultipleExcitationsSpeedRangeOption"],
        "_4656": ["OilSealModalAnalysis"],
        "_4657": ["OrderCutsChartSettings"],
        "_4658": ["PartModalAnalysis"],
        "_4659": ["PartToPartShearCouplingConnectionModalAnalysis"],
        "_4660": ["PartToPartShearCouplingHalfModalAnalysis"],
        "_4661": ["PartToPartShearCouplingModalAnalysis"],
        "_4662": ["PlanetaryConnectionModalAnalysis"],
        "_4663": ["PlanetaryGearSetModalAnalysis"],
        "_4664": ["PlanetCarrierModalAnalysis"],
        "_4665": ["PointLoadModalAnalysis"],
        "_4666": ["PowerLoadModalAnalysis"],
        "_4667": ["PulleyModalAnalysis"],
        "_4668": ["RingPinsModalAnalysis"],
        "_4669": ["RingPinsToDiscConnectionModalAnalysis"],
        "_4670": ["RollingRingAssemblyModalAnalysis"],
        "_4671": ["RollingRingConnectionModalAnalysis"],
        "_4672": ["RollingRingModalAnalysis"],
        "_4673": ["RootAssemblyModalAnalysis"],
        "_4674": ["ShaftHubConnectionModalAnalysis"],
        "_4675": ["ShaftModalAnalysis"],
        "_4676": ["ShaftModalAnalysisMode"],
        "_4677": ["ShaftToMountableComponentConnectionModalAnalysis"],
        "_4678": ["SpecialisedAssemblyModalAnalysis"],
        "_4679": ["SpiralBevelGearMeshModalAnalysis"],
        "_4680": ["SpiralBevelGearModalAnalysis"],
        "_4681": ["SpiralBevelGearSetModalAnalysis"],
        "_4682": ["SpringDamperConnectionModalAnalysis"],
        "_4683": ["SpringDamperHalfModalAnalysis"],
        "_4684": ["SpringDamperModalAnalysis"],
        "_4685": ["StraightBevelDiffGearMeshModalAnalysis"],
        "_4686": ["StraightBevelDiffGearModalAnalysis"],
        "_4687": ["StraightBevelDiffGearSetModalAnalysis"],
        "_4688": ["StraightBevelGearMeshModalAnalysis"],
        "_4689": ["StraightBevelGearModalAnalysis"],
        "_4690": ["StraightBevelGearSetModalAnalysis"],
        "_4691": ["StraightBevelPlanetGearModalAnalysis"],
        "_4692": ["StraightBevelSunGearModalAnalysis"],
        "_4693": ["SynchroniserHalfModalAnalysis"],
        "_4694": ["SynchroniserModalAnalysis"],
        "_4695": ["SynchroniserPartModalAnalysis"],
        "_4696": ["SynchroniserSleeveModalAnalysis"],
        "_4697": ["TorqueConverterConnectionModalAnalysis"],
        "_4698": ["TorqueConverterModalAnalysis"],
        "_4699": ["TorqueConverterPumpModalAnalysis"],
        "_4700": ["TorqueConverterTurbineModalAnalysis"],
        "_4701": ["UnbalancedMassModalAnalysis"],
        "_4702": ["VirtualComponentModalAnalysis"],
        "_4703": ["WaterfallChartSettings"],
        "_4704": ["WhineWaterfallExportOption"],
        "_4705": ["WhineWaterfallSettings"],
        "_4706": ["WormGearMeshModalAnalysis"],
        "_4707": ["WormGearModalAnalysis"],
        "_4708": ["WormGearSetModalAnalysis"],
        "_4709": ["ZerolBevelGearMeshModalAnalysis"],
        "_4710": ["ZerolBevelGearModalAnalysis"],
        "_4711": ["ZerolBevelGearSetModalAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyModalAnalysis",
    "AbstractShaftModalAnalysis",
    "AbstractShaftOrHousingModalAnalysis",
    "AbstractShaftToMountableComponentConnectionModalAnalysis",
    "AGMAGleasonConicalGearMeshModalAnalysis",
    "AGMAGleasonConicalGearModalAnalysis",
    "AGMAGleasonConicalGearSetModalAnalysis",
    "AssemblyModalAnalysis",
    "BearingModalAnalysis",
    "BeltConnectionModalAnalysis",
    "BeltDriveModalAnalysis",
    "BevelDifferentialGearMeshModalAnalysis",
    "BevelDifferentialGearModalAnalysis",
    "BevelDifferentialGearSetModalAnalysis",
    "BevelDifferentialPlanetGearModalAnalysis",
    "BevelDifferentialSunGearModalAnalysis",
    "BevelGearMeshModalAnalysis",
    "BevelGearModalAnalysis",
    "BevelGearSetModalAnalysis",
    "BoltedJointModalAnalysis",
    "BoltModalAnalysis",
    "ClutchConnectionModalAnalysis",
    "ClutchHalfModalAnalysis",
    "ClutchModalAnalysis",
    "CoaxialConnectionModalAnalysis",
    "ComponentModalAnalysis",
    "ConceptCouplingConnectionModalAnalysis",
    "ConceptCouplingHalfModalAnalysis",
    "ConceptCouplingModalAnalysis",
    "ConceptGearMeshModalAnalysis",
    "ConceptGearModalAnalysis",
    "ConceptGearSetModalAnalysis",
    "ConicalGearMeshModalAnalysis",
    "ConicalGearModalAnalysis",
    "ConicalGearSetModalAnalysis",
    "ConnectionModalAnalysis",
    "ConnectorModalAnalysis",
    "CoordinateSystemForWhine",
    "CouplingConnectionModalAnalysis",
    "CouplingHalfModalAnalysis",
    "CouplingModalAnalysis",
    "CVTBeltConnectionModalAnalysis",
    "CVTModalAnalysis",
    "CVTPulleyModalAnalysis",
    "CycloidalAssemblyModalAnalysis",
    "CycloidalDiscCentralBearingConnectionModalAnalysis",
    "CycloidalDiscModalAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionModalAnalysis",
    "CylindricalGearMeshModalAnalysis",
    "CylindricalGearModalAnalysis",
    "CylindricalGearSetModalAnalysis",
    "CylindricalPlanetGearModalAnalysis",
    "DatumModalAnalysis",
    "DynamicModelForModalAnalysis",
    "DynamicsResponse3DChartType",
    "DynamicsResponseType",
    "ExternalCADModelModalAnalysis",
    "FaceGearMeshModalAnalysis",
    "FaceGearModalAnalysis",
    "FaceGearSetModalAnalysis",
    "FEPartModalAnalysis",
    "FlexiblePinAssemblyModalAnalysis",
    "FrequencyResponseAnalysisOptions",
    "GearMeshModalAnalysis",
    "GearModalAnalysis",
    "GearSetModalAnalysis",
    "GuideDxfModelModalAnalysis",
    "HypoidGearMeshModalAnalysis",
    "HypoidGearModalAnalysis",
    "HypoidGearSetModalAnalysis",
    "InterMountableComponentConnectionModalAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshModalAnalysis",
    "KlingelnbergCycloPalloidConicalGearModalAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetModalAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis",
    "KlingelnbergCycloPalloidHypoidGearModalAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetModalAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis",
    "MassDiscModalAnalysis",
    "MeasurementComponentModalAnalysis",
    "ModalAnalysis",
    "ModalAnalysisBarModelFEExportOptions",
    "ModalAnalysisDrawStyle",
    "ModalAnalysisOptions",
    "MountableComponentModalAnalysis",
    "MultipleExcitationsSpeedRangeOption",
    "OilSealModalAnalysis",
    "OrderCutsChartSettings",
    "PartModalAnalysis",
    "PartToPartShearCouplingConnectionModalAnalysis",
    "PartToPartShearCouplingHalfModalAnalysis",
    "PartToPartShearCouplingModalAnalysis",
    "PlanetaryConnectionModalAnalysis",
    "PlanetaryGearSetModalAnalysis",
    "PlanetCarrierModalAnalysis",
    "PointLoadModalAnalysis",
    "PowerLoadModalAnalysis",
    "PulleyModalAnalysis",
    "RingPinsModalAnalysis",
    "RingPinsToDiscConnectionModalAnalysis",
    "RollingRingAssemblyModalAnalysis",
    "RollingRingConnectionModalAnalysis",
    "RollingRingModalAnalysis",
    "RootAssemblyModalAnalysis",
    "ShaftHubConnectionModalAnalysis",
    "ShaftModalAnalysis",
    "ShaftModalAnalysisMode",
    "ShaftToMountableComponentConnectionModalAnalysis",
    "SpecialisedAssemblyModalAnalysis",
    "SpiralBevelGearMeshModalAnalysis",
    "SpiralBevelGearModalAnalysis",
    "SpiralBevelGearSetModalAnalysis",
    "SpringDamperConnectionModalAnalysis",
    "SpringDamperHalfModalAnalysis",
    "SpringDamperModalAnalysis",
    "StraightBevelDiffGearMeshModalAnalysis",
    "StraightBevelDiffGearModalAnalysis",
    "StraightBevelDiffGearSetModalAnalysis",
    "StraightBevelGearMeshModalAnalysis",
    "StraightBevelGearModalAnalysis",
    "StraightBevelGearSetModalAnalysis",
    "StraightBevelPlanetGearModalAnalysis",
    "StraightBevelSunGearModalAnalysis",
    "SynchroniserHalfModalAnalysis",
    "SynchroniserModalAnalysis",
    "SynchroniserPartModalAnalysis",
    "SynchroniserSleeveModalAnalysis",
    "TorqueConverterConnectionModalAnalysis",
    "TorqueConverterModalAnalysis",
    "TorqueConverterPumpModalAnalysis",
    "TorqueConverterTurbineModalAnalysis",
    "UnbalancedMassModalAnalysis",
    "VirtualComponentModalAnalysis",
    "WaterfallChartSettings",
    "WhineWaterfallExportOption",
    "WhineWaterfallSettings",
    "WormGearMeshModalAnalysis",
    "WormGearModalAnalysis",
    "WormGearSetModalAnalysis",
    "ZerolBevelGearMeshModalAnalysis",
    "ZerolBevelGearModalAnalysis",
    "ZerolBevelGearSetModalAnalysis",
)
