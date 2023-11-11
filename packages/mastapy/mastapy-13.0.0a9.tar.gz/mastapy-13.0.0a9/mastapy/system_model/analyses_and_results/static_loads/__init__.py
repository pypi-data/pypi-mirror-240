"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6800 import LoadCase
    from ._6801 import StaticLoadCase
    from ._6802 import TimeSeriesLoadCase
    from ._6803 import AbstractAssemblyLoadCase
    from ._6804 import AbstractShaftLoadCase
    from ._6805 import AbstractShaftOrHousingLoadCase
    from ._6806 import AbstractShaftToMountableComponentConnectionLoadCase
    from ._6807 import AdditionalAccelerationOptions
    from ._6808 import AdvancedTimeSteppingAnalysisForModulationStaticLoadCase
    from ._6809 import AdvancedTimeSteppingAnalysisForModulationType
    from ._6810 import AGMAGleasonConicalGearLoadCase
    from ._6811 import AGMAGleasonConicalGearMeshLoadCase
    from ._6812 import AGMAGleasonConicalGearSetLoadCase
    from ._6813 import AllRingPinsManufacturingError
    from ._6814 import AnalysisType
    from ._6815 import AssemblyLoadCase
    from ._6816 import BearingLoadCase
    from ._6817 import BeltConnectionLoadCase
    from ._6818 import BeltDriveLoadCase
    from ._6819 import BevelDifferentialGearLoadCase
    from ._6820 import BevelDifferentialGearMeshLoadCase
    from ._6821 import BevelDifferentialGearSetLoadCase
    from ._6822 import BevelDifferentialPlanetGearLoadCase
    from ._6823 import BevelDifferentialSunGearLoadCase
    from ._6824 import BevelGearLoadCase
    from ._6825 import BevelGearMeshLoadCase
    from ._6826 import BevelGearSetLoadCase
    from ._6827 import BoltedJointLoadCase
    from ._6828 import BoltLoadCase
    from ._6829 import ClutchConnectionLoadCase
    from ._6830 import ClutchHalfLoadCase
    from ._6831 import ClutchLoadCase
    from ._6832 import CMSElementFaceGroupWithSelectionOption
    from ._6833 import CoaxialConnectionLoadCase
    from ._6834 import ComponentLoadCase
    from ._6835 import ConceptCouplingConnectionLoadCase
    from ._6836 import ConceptCouplingHalfLoadCase
    from ._6837 import ConceptCouplingLoadCase
    from ._6838 import ConceptGearLoadCase
    from ._6839 import ConceptGearMeshLoadCase
    from ._6840 import ConceptGearSetLoadCase
    from ._6841 import ConicalGearLoadCase
    from ._6842 import ConicalGearManufactureError
    from ._6843 import ConicalGearMeshLoadCase
    from ._6844 import ConicalGearSetHarmonicLoadData
    from ._6845 import ConicalGearSetLoadCase
    from ._6846 import ConnectionLoadCase
    from ._6847 import ConnectorLoadCase
    from ._6848 import CouplingConnectionLoadCase
    from ._6849 import CouplingHalfLoadCase
    from ._6850 import CouplingLoadCase
    from ._6851 import CVTBeltConnectionLoadCase
    from ._6852 import CVTLoadCase
    from ._6853 import CVTPulleyLoadCase
    from ._6854 import CycloidalAssemblyLoadCase
    from ._6855 import CycloidalDiscCentralBearingConnectionLoadCase
    from ._6856 import CycloidalDiscLoadCase
    from ._6857 import CycloidalDiscPlanetaryBearingConnectionLoadCase
    from ._6858 import CylindricalGearLoadCase
    from ._6859 import CylindricalGearManufactureError
    from ._6860 import CylindricalGearMeshLoadCase
    from ._6861 import CylindricalGearSetHarmonicLoadData
    from ._6862 import CylindricalGearSetLoadCase
    from ._6863 import CylindricalPlanetGearLoadCase
    from ._6864 import DataFromMotorPackagePerMeanTorque
    from ._6865 import DataFromMotorPackagePerSpeed
    from ._6866 import DatumLoadCase
    from ._6867 import ElectricMachineDataImportType
    from ._6868 import ElectricMachineHarmonicLoadData
    from ._6869 import ElectricMachineHarmonicLoadDataFromExcel
    from ._6870 import ElectricMachineHarmonicLoadDataFromFlux
    from ._6871 import ElectricMachineHarmonicLoadDataFromJMAG
    from ._6872 import ElectricMachineHarmonicLoadDataFromMASTA
    from ._6873 import ElectricMachineHarmonicLoadDataFromMotorCAD
    from ._6874 import ElectricMachineHarmonicLoadDataFromMotorPackages
    from ._6875 import ElectricMachineHarmonicLoadExcelImportOptions
    from ._6876 import ElectricMachineHarmonicLoadFluxImportOptions
    from ._6877 import ElectricMachineHarmonicLoadImportOptionsBase
    from ._6878 import ElectricMachineHarmonicLoadJMAGImportOptions
    from ._6879 import ElectricMachineHarmonicLoadMotorCADImportOptions
    from ._6880 import ExternalCADModelLoadCase
    from ._6881 import FaceGearLoadCase
    from ._6882 import FaceGearMeshLoadCase
    from ._6883 import FaceGearSetLoadCase
    from ._6884 import FEPartLoadCase
    from ._6885 import FlexiblePinAssemblyLoadCase
    from ._6886 import ForceAndTorqueScalingFactor
    from ._6887 import GearLoadCase
    from ._6888 import GearManufactureError
    from ._6889 import GearMeshLoadCase
    from ._6890 import GearMeshTEOrderType
    from ._6891 import GearSetHarmonicLoadData
    from ._6892 import GearSetLoadCase
    from ._6893 import GuideDxfModelLoadCase
    from ._6894 import HarmonicExcitationType
    from ._6895 import HarmonicLoadDataCSVImport
    from ._6896 import HarmonicLoadDataExcelImport
    from ._6897 import HarmonicLoadDataFluxImport
    from ._6898 import HarmonicLoadDataImportBase
    from ._6899 import HarmonicLoadDataImportFromMotorPackages
    from ._6900 import HarmonicLoadDataJMAGImport
    from ._6901 import HarmonicLoadDataMotorCADImport
    from ._6902 import HypoidGearLoadCase
    from ._6903 import HypoidGearMeshLoadCase
    from ._6904 import HypoidGearSetLoadCase
    from ._6905 import ImportType
    from ._6906 import InformationAtRingPinToDiscContactPointFromGeometry
    from ._6907 import InnerDiameterReference
    from ._6908 import InterMountableComponentConnectionLoadCase
    from ._6909 import KlingelnbergCycloPalloidConicalGearLoadCase
    from ._6910 import KlingelnbergCycloPalloidConicalGearMeshLoadCase
    from ._6911 import KlingelnbergCycloPalloidConicalGearSetLoadCase
    from ._6912 import KlingelnbergCycloPalloidHypoidGearLoadCase
    from ._6913 import KlingelnbergCycloPalloidHypoidGearMeshLoadCase
    from ._6914 import KlingelnbergCycloPalloidHypoidGearSetLoadCase
    from ._6915 import KlingelnbergCycloPalloidSpiralBevelGearLoadCase
    from ._6916 import KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
    from ._6917 import KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
    from ._6918 import MassDiscLoadCase
    from ._6919 import MeasurementComponentLoadCase
    from ._6920 import MeshStiffnessSource
    from ._6921 import MountableComponentLoadCase
    from ._6922 import NamedSpeed
    from ._6923 import OilSealLoadCase
    from ._6924 import ParametricStudyType
    from ._6925 import PartLoadCase
    from ._6926 import PartToPartShearCouplingConnectionLoadCase
    from ._6927 import PartToPartShearCouplingHalfLoadCase
    from ._6928 import PartToPartShearCouplingLoadCase
    from ._6929 import PlanetaryConnectionLoadCase
    from ._6930 import PlanetaryGearSetLoadCase
    from ._6931 import PlanetarySocketManufactureError
    from ._6932 import PlanetCarrierLoadCase
    from ._6933 import PlanetManufactureError
    from ._6934 import PointLoadHarmonicLoadData
    from ._6935 import PointLoadLoadCase
    from ._6936 import PowerLoadLoadCase
    from ._6937 import PulleyLoadCase
    from ._6938 import ResetMicroGeometryOptions
    from ._6939 import RingPinManufacturingError
    from ._6940 import RingPinsLoadCase
    from ._6941 import RingPinsToDiscConnectionLoadCase
    from ._6942 import RollingRingAssemblyLoadCase
    from ._6943 import RollingRingConnectionLoadCase
    from ._6944 import RollingRingLoadCase
    from ._6945 import RootAssemblyLoadCase
    from ._6946 import ShaftHubConnectionLoadCase
    from ._6947 import ShaftLoadCase
    from ._6948 import ShaftToMountableComponentConnectionLoadCase
    from ._6949 import SpecialisedAssemblyLoadCase
    from ._6950 import SpiralBevelGearLoadCase
    from ._6951 import SpiralBevelGearMeshLoadCase
    from ._6952 import SpiralBevelGearSetLoadCase
    from ._6953 import SpringDamperConnectionLoadCase
    from ._6954 import SpringDamperHalfLoadCase
    from ._6955 import SpringDamperLoadCase
    from ._6956 import StraightBevelDiffGearLoadCase
    from ._6957 import StraightBevelDiffGearMeshLoadCase
    from ._6958 import StraightBevelDiffGearSetLoadCase
    from ._6959 import StraightBevelGearLoadCase
    from ._6960 import StraightBevelGearMeshLoadCase
    from ._6961 import StraightBevelGearSetLoadCase
    from ._6962 import StraightBevelPlanetGearLoadCase
    from ._6963 import StraightBevelSunGearLoadCase
    from ._6964 import SynchroniserHalfLoadCase
    from ._6965 import SynchroniserLoadCase
    from ._6966 import SynchroniserPartLoadCase
    from ._6967 import SynchroniserSleeveLoadCase
    from ._6968 import TEExcitationType
    from ._6969 import TorqueConverterConnectionLoadCase
    from ._6970 import TorqueConverterLoadCase
    from ._6971 import TorqueConverterPumpLoadCase
    from ._6972 import TorqueConverterTurbineLoadCase
    from ._6973 import TorqueRippleInputType
    from ._6974 import TorqueSpecificationForSystemDeflection
    from ._6975 import TransmissionEfficiencySettings
    from ._6976 import UnbalancedMassHarmonicLoadData
    from ._6977 import UnbalancedMassLoadCase
    from ._6978 import VirtualComponentLoadCase
    from ._6979 import WormGearLoadCase
    from ._6980 import WormGearMeshLoadCase
    from ._6981 import WormGearSetLoadCase
    from ._6982 import ZerolBevelGearLoadCase
    from ._6983 import ZerolBevelGearMeshLoadCase
    from ._6984 import ZerolBevelGearSetLoadCase
else:
    import_structure = {
        "_6800": ["LoadCase"],
        "_6801": ["StaticLoadCase"],
        "_6802": ["TimeSeriesLoadCase"],
        "_6803": ["AbstractAssemblyLoadCase"],
        "_6804": ["AbstractShaftLoadCase"],
        "_6805": ["AbstractShaftOrHousingLoadCase"],
        "_6806": ["AbstractShaftToMountableComponentConnectionLoadCase"],
        "_6807": ["AdditionalAccelerationOptions"],
        "_6808": ["AdvancedTimeSteppingAnalysisForModulationStaticLoadCase"],
        "_6809": ["AdvancedTimeSteppingAnalysisForModulationType"],
        "_6810": ["AGMAGleasonConicalGearLoadCase"],
        "_6811": ["AGMAGleasonConicalGearMeshLoadCase"],
        "_6812": ["AGMAGleasonConicalGearSetLoadCase"],
        "_6813": ["AllRingPinsManufacturingError"],
        "_6814": ["AnalysisType"],
        "_6815": ["AssemblyLoadCase"],
        "_6816": ["BearingLoadCase"],
        "_6817": ["BeltConnectionLoadCase"],
        "_6818": ["BeltDriveLoadCase"],
        "_6819": ["BevelDifferentialGearLoadCase"],
        "_6820": ["BevelDifferentialGearMeshLoadCase"],
        "_6821": ["BevelDifferentialGearSetLoadCase"],
        "_6822": ["BevelDifferentialPlanetGearLoadCase"],
        "_6823": ["BevelDifferentialSunGearLoadCase"],
        "_6824": ["BevelGearLoadCase"],
        "_6825": ["BevelGearMeshLoadCase"],
        "_6826": ["BevelGearSetLoadCase"],
        "_6827": ["BoltedJointLoadCase"],
        "_6828": ["BoltLoadCase"],
        "_6829": ["ClutchConnectionLoadCase"],
        "_6830": ["ClutchHalfLoadCase"],
        "_6831": ["ClutchLoadCase"],
        "_6832": ["CMSElementFaceGroupWithSelectionOption"],
        "_6833": ["CoaxialConnectionLoadCase"],
        "_6834": ["ComponentLoadCase"],
        "_6835": ["ConceptCouplingConnectionLoadCase"],
        "_6836": ["ConceptCouplingHalfLoadCase"],
        "_6837": ["ConceptCouplingLoadCase"],
        "_6838": ["ConceptGearLoadCase"],
        "_6839": ["ConceptGearMeshLoadCase"],
        "_6840": ["ConceptGearSetLoadCase"],
        "_6841": ["ConicalGearLoadCase"],
        "_6842": ["ConicalGearManufactureError"],
        "_6843": ["ConicalGearMeshLoadCase"],
        "_6844": ["ConicalGearSetHarmonicLoadData"],
        "_6845": ["ConicalGearSetLoadCase"],
        "_6846": ["ConnectionLoadCase"],
        "_6847": ["ConnectorLoadCase"],
        "_6848": ["CouplingConnectionLoadCase"],
        "_6849": ["CouplingHalfLoadCase"],
        "_6850": ["CouplingLoadCase"],
        "_6851": ["CVTBeltConnectionLoadCase"],
        "_6852": ["CVTLoadCase"],
        "_6853": ["CVTPulleyLoadCase"],
        "_6854": ["CycloidalAssemblyLoadCase"],
        "_6855": ["CycloidalDiscCentralBearingConnectionLoadCase"],
        "_6856": ["CycloidalDiscLoadCase"],
        "_6857": ["CycloidalDiscPlanetaryBearingConnectionLoadCase"],
        "_6858": ["CylindricalGearLoadCase"],
        "_6859": ["CylindricalGearManufactureError"],
        "_6860": ["CylindricalGearMeshLoadCase"],
        "_6861": ["CylindricalGearSetHarmonicLoadData"],
        "_6862": ["CylindricalGearSetLoadCase"],
        "_6863": ["CylindricalPlanetGearLoadCase"],
        "_6864": ["DataFromMotorPackagePerMeanTorque"],
        "_6865": ["DataFromMotorPackagePerSpeed"],
        "_6866": ["DatumLoadCase"],
        "_6867": ["ElectricMachineDataImportType"],
        "_6868": ["ElectricMachineHarmonicLoadData"],
        "_6869": ["ElectricMachineHarmonicLoadDataFromExcel"],
        "_6870": ["ElectricMachineHarmonicLoadDataFromFlux"],
        "_6871": ["ElectricMachineHarmonicLoadDataFromJMAG"],
        "_6872": ["ElectricMachineHarmonicLoadDataFromMASTA"],
        "_6873": ["ElectricMachineHarmonicLoadDataFromMotorCAD"],
        "_6874": ["ElectricMachineHarmonicLoadDataFromMotorPackages"],
        "_6875": ["ElectricMachineHarmonicLoadExcelImportOptions"],
        "_6876": ["ElectricMachineHarmonicLoadFluxImportOptions"],
        "_6877": ["ElectricMachineHarmonicLoadImportOptionsBase"],
        "_6878": ["ElectricMachineHarmonicLoadJMAGImportOptions"],
        "_6879": ["ElectricMachineHarmonicLoadMotorCADImportOptions"],
        "_6880": ["ExternalCADModelLoadCase"],
        "_6881": ["FaceGearLoadCase"],
        "_6882": ["FaceGearMeshLoadCase"],
        "_6883": ["FaceGearSetLoadCase"],
        "_6884": ["FEPartLoadCase"],
        "_6885": ["FlexiblePinAssemblyLoadCase"],
        "_6886": ["ForceAndTorqueScalingFactor"],
        "_6887": ["GearLoadCase"],
        "_6888": ["GearManufactureError"],
        "_6889": ["GearMeshLoadCase"],
        "_6890": ["GearMeshTEOrderType"],
        "_6891": ["GearSetHarmonicLoadData"],
        "_6892": ["GearSetLoadCase"],
        "_6893": ["GuideDxfModelLoadCase"],
        "_6894": ["HarmonicExcitationType"],
        "_6895": ["HarmonicLoadDataCSVImport"],
        "_6896": ["HarmonicLoadDataExcelImport"],
        "_6897": ["HarmonicLoadDataFluxImport"],
        "_6898": ["HarmonicLoadDataImportBase"],
        "_6899": ["HarmonicLoadDataImportFromMotorPackages"],
        "_6900": ["HarmonicLoadDataJMAGImport"],
        "_6901": ["HarmonicLoadDataMotorCADImport"],
        "_6902": ["HypoidGearLoadCase"],
        "_6903": ["HypoidGearMeshLoadCase"],
        "_6904": ["HypoidGearSetLoadCase"],
        "_6905": ["ImportType"],
        "_6906": ["InformationAtRingPinToDiscContactPointFromGeometry"],
        "_6907": ["InnerDiameterReference"],
        "_6908": ["InterMountableComponentConnectionLoadCase"],
        "_6909": ["KlingelnbergCycloPalloidConicalGearLoadCase"],
        "_6910": ["KlingelnbergCycloPalloidConicalGearMeshLoadCase"],
        "_6911": ["KlingelnbergCycloPalloidConicalGearSetLoadCase"],
        "_6912": ["KlingelnbergCycloPalloidHypoidGearLoadCase"],
        "_6913": ["KlingelnbergCycloPalloidHypoidGearMeshLoadCase"],
        "_6914": ["KlingelnbergCycloPalloidHypoidGearSetLoadCase"],
        "_6915": ["KlingelnbergCycloPalloidSpiralBevelGearLoadCase"],
        "_6916": ["KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase"],
        "_6917": ["KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase"],
        "_6918": ["MassDiscLoadCase"],
        "_6919": ["MeasurementComponentLoadCase"],
        "_6920": ["MeshStiffnessSource"],
        "_6921": ["MountableComponentLoadCase"],
        "_6922": ["NamedSpeed"],
        "_6923": ["OilSealLoadCase"],
        "_6924": ["ParametricStudyType"],
        "_6925": ["PartLoadCase"],
        "_6926": ["PartToPartShearCouplingConnectionLoadCase"],
        "_6927": ["PartToPartShearCouplingHalfLoadCase"],
        "_6928": ["PartToPartShearCouplingLoadCase"],
        "_6929": ["PlanetaryConnectionLoadCase"],
        "_6930": ["PlanetaryGearSetLoadCase"],
        "_6931": ["PlanetarySocketManufactureError"],
        "_6932": ["PlanetCarrierLoadCase"],
        "_6933": ["PlanetManufactureError"],
        "_6934": ["PointLoadHarmonicLoadData"],
        "_6935": ["PointLoadLoadCase"],
        "_6936": ["PowerLoadLoadCase"],
        "_6937": ["PulleyLoadCase"],
        "_6938": ["ResetMicroGeometryOptions"],
        "_6939": ["RingPinManufacturingError"],
        "_6940": ["RingPinsLoadCase"],
        "_6941": ["RingPinsToDiscConnectionLoadCase"],
        "_6942": ["RollingRingAssemblyLoadCase"],
        "_6943": ["RollingRingConnectionLoadCase"],
        "_6944": ["RollingRingLoadCase"],
        "_6945": ["RootAssemblyLoadCase"],
        "_6946": ["ShaftHubConnectionLoadCase"],
        "_6947": ["ShaftLoadCase"],
        "_6948": ["ShaftToMountableComponentConnectionLoadCase"],
        "_6949": ["SpecialisedAssemblyLoadCase"],
        "_6950": ["SpiralBevelGearLoadCase"],
        "_6951": ["SpiralBevelGearMeshLoadCase"],
        "_6952": ["SpiralBevelGearSetLoadCase"],
        "_6953": ["SpringDamperConnectionLoadCase"],
        "_6954": ["SpringDamperHalfLoadCase"],
        "_6955": ["SpringDamperLoadCase"],
        "_6956": ["StraightBevelDiffGearLoadCase"],
        "_6957": ["StraightBevelDiffGearMeshLoadCase"],
        "_6958": ["StraightBevelDiffGearSetLoadCase"],
        "_6959": ["StraightBevelGearLoadCase"],
        "_6960": ["StraightBevelGearMeshLoadCase"],
        "_6961": ["StraightBevelGearSetLoadCase"],
        "_6962": ["StraightBevelPlanetGearLoadCase"],
        "_6963": ["StraightBevelSunGearLoadCase"],
        "_6964": ["SynchroniserHalfLoadCase"],
        "_6965": ["SynchroniserLoadCase"],
        "_6966": ["SynchroniserPartLoadCase"],
        "_6967": ["SynchroniserSleeveLoadCase"],
        "_6968": ["TEExcitationType"],
        "_6969": ["TorqueConverterConnectionLoadCase"],
        "_6970": ["TorqueConverterLoadCase"],
        "_6971": ["TorqueConverterPumpLoadCase"],
        "_6972": ["TorqueConverterTurbineLoadCase"],
        "_6973": ["TorqueRippleInputType"],
        "_6974": ["TorqueSpecificationForSystemDeflection"],
        "_6975": ["TransmissionEfficiencySettings"],
        "_6976": ["UnbalancedMassHarmonicLoadData"],
        "_6977": ["UnbalancedMassLoadCase"],
        "_6978": ["VirtualComponentLoadCase"],
        "_6979": ["WormGearLoadCase"],
        "_6980": ["WormGearMeshLoadCase"],
        "_6981": ["WormGearSetLoadCase"],
        "_6982": ["ZerolBevelGearLoadCase"],
        "_6983": ["ZerolBevelGearMeshLoadCase"],
        "_6984": ["ZerolBevelGearSetLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "LoadCase",
    "StaticLoadCase",
    "TimeSeriesLoadCase",
    "AbstractAssemblyLoadCase",
    "AbstractShaftLoadCase",
    "AbstractShaftOrHousingLoadCase",
    "AbstractShaftToMountableComponentConnectionLoadCase",
    "AdditionalAccelerationOptions",
    "AdvancedTimeSteppingAnalysisForModulationStaticLoadCase",
    "AdvancedTimeSteppingAnalysisForModulationType",
    "AGMAGleasonConicalGearLoadCase",
    "AGMAGleasonConicalGearMeshLoadCase",
    "AGMAGleasonConicalGearSetLoadCase",
    "AllRingPinsManufacturingError",
    "AnalysisType",
    "AssemblyLoadCase",
    "BearingLoadCase",
    "BeltConnectionLoadCase",
    "BeltDriveLoadCase",
    "BevelDifferentialGearLoadCase",
    "BevelDifferentialGearMeshLoadCase",
    "BevelDifferentialGearSetLoadCase",
    "BevelDifferentialPlanetGearLoadCase",
    "BevelDifferentialSunGearLoadCase",
    "BevelGearLoadCase",
    "BevelGearMeshLoadCase",
    "BevelGearSetLoadCase",
    "BoltedJointLoadCase",
    "BoltLoadCase",
    "ClutchConnectionLoadCase",
    "ClutchHalfLoadCase",
    "ClutchLoadCase",
    "CMSElementFaceGroupWithSelectionOption",
    "CoaxialConnectionLoadCase",
    "ComponentLoadCase",
    "ConceptCouplingConnectionLoadCase",
    "ConceptCouplingHalfLoadCase",
    "ConceptCouplingLoadCase",
    "ConceptGearLoadCase",
    "ConceptGearMeshLoadCase",
    "ConceptGearSetLoadCase",
    "ConicalGearLoadCase",
    "ConicalGearManufactureError",
    "ConicalGearMeshLoadCase",
    "ConicalGearSetHarmonicLoadData",
    "ConicalGearSetLoadCase",
    "ConnectionLoadCase",
    "ConnectorLoadCase",
    "CouplingConnectionLoadCase",
    "CouplingHalfLoadCase",
    "CouplingLoadCase",
    "CVTBeltConnectionLoadCase",
    "CVTLoadCase",
    "CVTPulleyLoadCase",
    "CycloidalAssemblyLoadCase",
    "CycloidalDiscCentralBearingConnectionLoadCase",
    "CycloidalDiscLoadCase",
    "CycloidalDiscPlanetaryBearingConnectionLoadCase",
    "CylindricalGearLoadCase",
    "CylindricalGearManufactureError",
    "CylindricalGearMeshLoadCase",
    "CylindricalGearSetHarmonicLoadData",
    "CylindricalGearSetLoadCase",
    "CylindricalPlanetGearLoadCase",
    "DataFromMotorPackagePerMeanTorque",
    "DataFromMotorPackagePerSpeed",
    "DatumLoadCase",
    "ElectricMachineDataImportType",
    "ElectricMachineHarmonicLoadData",
    "ElectricMachineHarmonicLoadDataFromExcel",
    "ElectricMachineHarmonicLoadDataFromFlux",
    "ElectricMachineHarmonicLoadDataFromJMAG",
    "ElectricMachineHarmonicLoadDataFromMASTA",
    "ElectricMachineHarmonicLoadDataFromMotorCAD",
    "ElectricMachineHarmonicLoadDataFromMotorPackages",
    "ElectricMachineHarmonicLoadExcelImportOptions",
    "ElectricMachineHarmonicLoadFluxImportOptions",
    "ElectricMachineHarmonicLoadImportOptionsBase",
    "ElectricMachineHarmonicLoadJMAGImportOptions",
    "ElectricMachineHarmonicLoadMotorCADImportOptions",
    "ExternalCADModelLoadCase",
    "FaceGearLoadCase",
    "FaceGearMeshLoadCase",
    "FaceGearSetLoadCase",
    "FEPartLoadCase",
    "FlexiblePinAssemblyLoadCase",
    "ForceAndTorqueScalingFactor",
    "GearLoadCase",
    "GearManufactureError",
    "GearMeshLoadCase",
    "GearMeshTEOrderType",
    "GearSetHarmonicLoadData",
    "GearSetLoadCase",
    "GuideDxfModelLoadCase",
    "HarmonicExcitationType",
    "HarmonicLoadDataCSVImport",
    "HarmonicLoadDataExcelImport",
    "HarmonicLoadDataFluxImport",
    "HarmonicLoadDataImportBase",
    "HarmonicLoadDataImportFromMotorPackages",
    "HarmonicLoadDataJMAGImport",
    "HarmonicLoadDataMotorCADImport",
    "HypoidGearLoadCase",
    "HypoidGearMeshLoadCase",
    "HypoidGearSetLoadCase",
    "ImportType",
    "InformationAtRingPinToDiscContactPointFromGeometry",
    "InnerDiameterReference",
    "InterMountableComponentConnectionLoadCase",
    "KlingelnbergCycloPalloidConicalGearLoadCase",
    "KlingelnbergCycloPalloidConicalGearMeshLoadCase",
    "KlingelnbergCycloPalloidConicalGearSetLoadCase",
    "KlingelnbergCycloPalloidHypoidGearLoadCase",
    "KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
    "KlingelnbergCycloPalloidHypoidGearSetLoadCase",
    "KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase",
    "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
    "MassDiscLoadCase",
    "MeasurementComponentLoadCase",
    "MeshStiffnessSource",
    "MountableComponentLoadCase",
    "NamedSpeed",
    "OilSealLoadCase",
    "ParametricStudyType",
    "PartLoadCase",
    "PartToPartShearCouplingConnectionLoadCase",
    "PartToPartShearCouplingHalfLoadCase",
    "PartToPartShearCouplingLoadCase",
    "PlanetaryConnectionLoadCase",
    "PlanetaryGearSetLoadCase",
    "PlanetarySocketManufactureError",
    "PlanetCarrierLoadCase",
    "PlanetManufactureError",
    "PointLoadHarmonicLoadData",
    "PointLoadLoadCase",
    "PowerLoadLoadCase",
    "PulleyLoadCase",
    "ResetMicroGeometryOptions",
    "RingPinManufacturingError",
    "RingPinsLoadCase",
    "RingPinsToDiscConnectionLoadCase",
    "RollingRingAssemblyLoadCase",
    "RollingRingConnectionLoadCase",
    "RollingRingLoadCase",
    "RootAssemblyLoadCase",
    "ShaftHubConnectionLoadCase",
    "ShaftLoadCase",
    "ShaftToMountableComponentConnectionLoadCase",
    "SpecialisedAssemblyLoadCase",
    "SpiralBevelGearLoadCase",
    "SpiralBevelGearMeshLoadCase",
    "SpiralBevelGearSetLoadCase",
    "SpringDamperConnectionLoadCase",
    "SpringDamperHalfLoadCase",
    "SpringDamperLoadCase",
    "StraightBevelDiffGearLoadCase",
    "StraightBevelDiffGearMeshLoadCase",
    "StraightBevelDiffGearSetLoadCase",
    "StraightBevelGearLoadCase",
    "StraightBevelGearMeshLoadCase",
    "StraightBevelGearSetLoadCase",
    "StraightBevelPlanetGearLoadCase",
    "StraightBevelSunGearLoadCase",
    "SynchroniserHalfLoadCase",
    "SynchroniserLoadCase",
    "SynchroniserPartLoadCase",
    "SynchroniserSleeveLoadCase",
    "TEExcitationType",
    "TorqueConverterConnectionLoadCase",
    "TorqueConverterLoadCase",
    "TorqueConverterPumpLoadCase",
    "TorqueConverterTurbineLoadCase",
    "TorqueRippleInputType",
    "TorqueSpecificationForSystemDeflection",
    "TransmissionEfficiencySettings",
    "UnbalancedMassHarmonicLoadData",
    "UnbalancedMassLoadCase",
    "VirtualComponentLoadCase",
    "WormGearLoadCase",
    "WormGearMeshLoadCase",
    "WormGearSetLoadCase",
    "ZerolBevelGearLoadCase",
    "ZerolBevelGearMeshLoadCase",
    "ZerolBevelGearSetLoadCase",
)
