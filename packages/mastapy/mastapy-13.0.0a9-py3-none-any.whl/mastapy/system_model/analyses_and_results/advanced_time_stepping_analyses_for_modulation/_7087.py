"""PartAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7544
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "PartAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7006,
    )
    from mastapy.system_model.part_model import _2465
    from mastapy.system_model.analyses_and_results.system_deflections import _2782


__docformat__ = "restructuredtext en"
__all__ = ("PartAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="PartAdvancedTimeSteppingAnalysisForModulation")


class PartAdvancedTimeSteppingAnalysisForModulation(_7544.PartStaticLoadAnalysisCase):
    """PartAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _PART_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_PartAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting PartAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
            parent: "PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7002,
            )

            return self._parent._cast(
                _7002.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7003,
            )

            return self._parent._cast(
                _7003.AbstractShaftAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_or_housing_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7004,
            )

            return self._parent._cast(
                _7004.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7010,
            )

            return self._parent._cast(
                _7010.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7012,
            )

            return self._parent._cast(
                _7012.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7013,
            )

            return self._parent._cast(
                _7013.AssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bearing_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7015,
            )

            return self._parent._cast(
                _7015.BearingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_drive_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7017,
            )

            return self._parent._cast(
                _7017.BeltDriveAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7018,
            )

            return self._parent._cast(
                _7018.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7020,
            )

            return self._parent._cast(
                _7020.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7021,
            )

            return self._parent._cast(
                _7021.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7022,
            )

            return self._parent._cast(
                _7022.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7023,
            )

            return self._parent._cast(
                _7023.BevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7025,
            )

            return self._parent._cast(
                _7025.BevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolt_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7026,
            )

            return self._parent._cast(
                _7026.BoltAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolted_joint_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7027,
            )

            return self._parent._cast(
                _7027.BoltedJointAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7028,
            )

            return self._parent._cast(
                _7028.ClutchAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7030,
            )

            return self._parent._cast(
                _7030.ClutchHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7032,
            )

            return self._parent._cast(
                _7032.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7033,
            )

            return self._parent._cast(
                _7033.ConceptCouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7035,
            )

            return self._parent._cast(
                _7035.ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7036,
            )

            return self._parent._cast(
                _7036.ConceptGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7038,
            )

            return self._parent._cast(
                _7038.ConceptGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7039,
            )

            return self._parent._cast(
                _7039.ConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7041,
            )

            return self._parent._cast(
                _7041.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connector_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7043,
            )

            return self._parent._cast(
                _7043.ConnectorAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7044,
            )

            return self._parent._cast(
                _7044.CouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7046,
            )

            return self._parent._cast(
                _7046.CouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7047,
            )

            return self._parent._cast(
                _7047.CVTAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_pulley_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7049,
            )

            return self._parent._cast(
                _7049.CVTPulleyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7050,
            )

            return self._parent._cast(
                _7050.CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7051,
            )

            return self._parent._cast(
                _7051.CycloidalDiscAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7054,
            )

            return self._parent._cast(
                _7054.CylindricalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7056,
            )

            return self._parent._cast(
                _7056.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7057,
            )

            return self._parent._cast(
                _7057.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def datum_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7058,
            )

            return self._parent._cast(
                _7058.DatumAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def external_cad_model_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7059,
            )

            return self._parent._cast(
                _7059.ExternalCADModelAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7060,
            )

            return self._parent._cast(
                _7060.FaceGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7062,
            )

            return self._parent._cast(
                _7062.FaceGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def fe_part_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7063,
            )

            return self._parent._cast(
                _7063.FEPartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def flexible_pin_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7064,
            )

            return self._parent._cast(
                _7064.FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7065,
            )

            return self._parent._cast(
                _7065.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7067,
            )

            return self._parent._cast(
                _7067.GearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def guide_dxf_model_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7068,
            )

            return self._parent._cast(
                _7068.GuideDxfModelAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7070,
            )

            return self._parent._cast(
                _7070.HypoidGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7072,
            )

            return self._parent._cast(
                _7072.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7074,
            )

            return self._parent._cast(
                _7074.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7076,
            )

            return self._parent._cast(
                _7076.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7077,
            )

            return self._parent._cast(
                _7077.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7079,
            )

            return self._parent._cast(
                _7079.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7080,
            )

            return self._parent._cast(
                _7080.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7082,
            )

            return self._parent._cast(
                _7082.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mass_disc_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7083,
            )

            return self._parent._cast(
                _7083.MassDiscAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def measurement_component_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7084,
            )

            return self._parent._cast(
                _7084.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7085,
            )

            return self._parent._cast(
                _7085.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def oil_seal_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7086,
            )

            return self._parent._cast(
                _7086.OilSealAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7088,
            )

            return self._parent._cast(
                _7088.PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7090,
            )

            return self._parent._cast(
                _7090.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7092,
            )

            return self._parent._cast(
                _7092.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planet_carrier_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7093,
            )

            return self._parent._cast(
                _7093.PlanetCarrierAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def point_load_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7094,
            )

            return self._parent._cast(
                _7094.PointLoadAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def power_load_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7095,
            )

            return self._parent._cast(
                _7095.PowerLoadAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def pulley_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7096,
            )

            return self._parent._cast(
                _7096.PulleyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7097,
            )

            return self._parent._cast(
                _7097.RingPinsAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7099,
            )

            return self._parent._cast(
                _7099.RollingRingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7100,
            )

            return self._parent._cast(
                _7100.RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def root_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7102,
            )

            return self._parent._cast(
                _7102.RootAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7103,
            )

            return self._parent._cast(
                _7103.ShaftAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_hub_connection_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7104,
            )

            return self._parent._cast(
                _7104.ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7106,
            )

            return self._parent._cast(
                _7106.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7107,
            )

            return self._parent._cast(
                _7107.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7109,
            )

            return self._parent._cast(
                _7109.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7110,
            )

            return self._parent._cast(
                _7110.SpringDamperAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7112,
            )

            return self._parent._cast(
                _7112.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7113,
            )

            return self._parent._cast(
                _7113.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7115,
            )

            return self._parent._cast(
                _7115.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7116,
            )

            return self._parent._cast(
                _7116.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7118,
            )

            return self._parent._cast(
                _7118.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7119,
            )

            return self._parent._cast(
                _7119.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7120,
            )

            return self._parent._cast(
                _7120.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7121,
            )

            return self._parent._cast(
                _7121.SynchroniserAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7122,
            )

            return self._parent._cast(
                _7122.SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_part_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7123,
            )

            return self._parent._cast(
                _7123.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_sleeve_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7124,
            )

            return self._parent._cast(
                _7124.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7125,
            )

            return self._parent._cast(
                _7125.TorqueConverterAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_pump_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7127,
            )

            return self._parent._cast(
                _7127.TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_turbine_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7128,
            )

            return self._parent._cast(
                _7128.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def unbalanced_mass_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7129,
            )

            return self._parent._cast(
                _7129.UnbalancedMassAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def virtual_component_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7130,
            )

            return self._parent._cast(
                _7130.VirtualComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7131,
            )

            return self._parent._cast(
                _7131.WormGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7133,
            )

            return self._parent._cast(
                _7133.WormGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7134,
            )

            return self._parent._cast(
                _7134.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7136,
            )

            return self._parent._cast(
                _7136.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
        ) -> "PartAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self,
        instance_to_wrap: "PartAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "_7006.AdvancedTimeSteppingAnalysisForModulation":
        """mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AdvancedTimeSteppingAnalysisForModulation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_design(self: Self) -> "_2465.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2782.PartSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PartSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_PartAdvancedTimeSteppingAnalysisForModulation(self)
