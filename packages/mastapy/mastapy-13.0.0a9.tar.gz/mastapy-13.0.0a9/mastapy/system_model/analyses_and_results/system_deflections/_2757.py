"""GearSetSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.analyses_and_results.system_deflections import _2803
from mastapy._internal.cast_exception import CastException

_GEAR_SET_IMPLEMENTATION_DETAIL = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearSetImplementationDetail"
)
_GEAR_SET_MODES = python_net_import("SMT.MastaAPI.Gears", "GearSetModes")
_TASK_PROGRESS = python_net_import("SMT.MastaAPIUtility", "TaskProgress")
_BOOLEAN = python_net_import("System", "Boolean")
_GEAR_SET_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "GearSetSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2529
    from mastapy.gears.rating import _361
    from mastapy.system_model.analyses_and_results.power_flows import _4091
    from mastapy.gears.analysis import _1229, _1226
    from mastapy.gears import _327
    from mastapy import _7555


__docformat__ = "restructuredtext en"
__all__ = ("GearSetSystemDeflection",)


Self = TypeVar("Self", bound="GearSetSystemDeflection")


class GearSetSystemDeflection(_2803.SpecialisedAssemblySystemDeflection):
    """GearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetSystemDeflection")

    class _Cast_GearSetSystemDeflection:
        """Special nested class for casting GearSetSystemDeflection to subclasses."""

        def __init__(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
            parent: "GearSetSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            return self._parent._cast(_2803.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2682,
            )

            return self._parent._cast(_2682.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2687,
            )

            return self._parent._cast(_2687.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2699,
            )

            return self._parent._cast(_2699.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2704,
            )

            return self._parent._cast(_2704.BevelGearSetSystemDeflection)

        @property
        def concept_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2718,
            )

            return self._parent._cast(_2718.ConceptGearSetSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2722,
            )

            return self._parent._cast(_2722.ConicalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2739,
            )

            return self._parent._cast(_2739.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2740,
            )

            return self._parent._cast(_2740.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2741,
            )

            return self._parent._cast(
                _2741.CylindricalGearSetSystemDeflectionWithLTCAResults
            )

        @property
        def face_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2752,
            )

            return self._parent._cast(_2752.FaceGearSetSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2761,
            )

            return self._parent._cast(_2761.HypoidGearSetSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2766,
            )

            return self._parent._cast(
                _2766.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2769,
            )

            return self._parent._cast(
                _2769.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2772,
            )

            return self._parent._cast(
                _2772.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(_2805.SpiralBevelGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2811,
            )

            return self._parent._cast(_2811.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.StraightBevelGearSetSystemDeflection)

        @property
        def worm_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2834,
            )

            return self._parent._cast(_2834.WormGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.ZerolBevelGearSetSystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "GearSetSystemDeflection":
            return self._parent

        def __getattr__(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2529.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_361.GearSetRating":
        """mastapy.gears.rating.GearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4091.GearSetPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.GearSetPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def analysis_for(
        self: Self,
        gear_set_imp_detail: "_1229.GearSetImplementationDetail",
        gear_set_mode: "_327.GearSetModes",
    ) -> "_1226.GearSetImplementationAnalysis":
        """mastapy.gears.analysis.GearSetImplementationAnalysis

        Args:
            gear_set_imp_detail (mastapy.gears.analysis.GearSetImplementationDetail)
            gear_set_mode (mastapy.gears.GearSetModes)
        """
        gear_set_mode = conversion.mp_to_pn_enum(
            gear_set_mode, "SMT.MastaAPI.Gears.GearSetModes"
        )
        method_result = self.wrapped.AnalysisFor(
            gear_set_imp_detail.wrapped if gear_set_imp_detail else None, gear_set_mode
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def implementation_detail_results_failed_for(
        self: Self,
        gear_set_imp_detail: "_1229.GearSetImplementationDetail",
        gear_set_mode: "_327.GearSetModes",
    ) -> "bool":
        """bool

        Args:
            gear_set_imp_detail (mastapy.gears.analysis.GearSetImplementationDetail)
            gear_set_mode (mastapy.gears.GearSetModes)
        """
        gear_set_mode = conversion.mp_to_pn_enum(
            gear_set_mode, "SMT.MastaAPI.Gears.GearSetModes"
        )
        method_result = self.wrapped.ImplementationDetailResultsFailedFor(
            gear_set_imp_detail.wrapped if gear_set_imp_detail else None, gear_set_mode
        )
        return method_result

    @enforce_parameter_types
    def perform_implementation_detail_analysis_with_progress(
        self: Self,
        imp_detail: "_1229.GearSetImplementationDetail",
        gear_set_mode: "_327.GearSetModes",
        progress: "_7555.TaskProgress",
        run_all_planetary_meshes: "bool" = True,
    ):
        """Method does not return.

        Args:
            imp_detail (mastapy.gears.analysis.GearSetImplementationDetail)
            gear_set_mode (mastapy.gears.GearSetModes)
            progress (mastapy.TaskProgress)
            run_all_planetary_meshes (bool, optional)
        """
        gear_set_mode = conversion.mp_to_pn_enum(
            gear_set_mode, "SMT.MastaAPI.Gears.GearSetModes"
        )
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        self.wrapped.PerformImplementationDetailAnalysis.Overloads[
            _GEAR_SET_IMPLEMENTATION_DETAIL, _GEAR_SET_MODES, _TASK_PROGRESS, _BOOLEAN
        ](
            imp_detail.wrapped if imp_detail else None,
            gear_set_mode,
            progress.wrapped if progress else None,
            run_all_planetary_meshes if run_all_planetary_meshes else False,
        )

    @enforce_parameter_types
    def perform_implementation_detail_analysis(
        self: Self,
        imp_detail: "_1229.GearSetImplementationDetail",
        gear_set_mode: "_327.GearSetModes",
        run_all_planetary_meshes: "bool" = True,
    ):
        """Method does not return.

        Args:
            imp_detail (mastapy.gears.analysis.GearSetImplementationDetail)
            gear_set_mode (mastapy.gears.GearSetModes)
            run_all_planetary_meshes (bool, optional)
        """
        gear_set_mode = conversion.mp_to_pn_enum(
            gear_set_mode, "SMT.MastaAPI.Gears.GearSetModes"
        )
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        self.wrapped.PerformImplementationDetailAnalysis.Overloads[
            _GEAR_SET_IMPLEMENTATION_DETAIL, _GEAR_SET_MODES, _BOOLEAN
        ](
            imp_detail.wrapped if imp_detail else None,
            gear_set_mode,
            run_all_planetary_meshes if run_all_planetary_meshes else False,
        )

    @property
    def cast_to(self: Self) -> "GearSetSystemDeflection._Cast_GearSetSystemDeflection":
        return self._Cast_GearSetSystemDeflection(self)
