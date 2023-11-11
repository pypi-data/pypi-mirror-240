"""StraightBevelDiffGearSetModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4586
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "StraightBevelDiffGearSetModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.static_loads import _6958
    from mastapy.system_model.analyses_and_results.system_deflections import _2811
    from mastapy.system_model.analyses_and_results.modal_analyses import _4686, _4685


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetModalAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetModalAnalysis")


class StraightBevelDiffGearSetModalAnalysis(_4586.BevelGearSetModalAnalysis):
    """StraightBevelDiffGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearSetModalAnalysis"
    )

    class _Cast_StraightBevelDiffGearSetModalAnalysis:
        """Special nested class for casting StraightBevelDiffGearSetModalAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
            parent: "StraightBevelDiffGearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_modal_analysis(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            return self._parent._cast(_4586.BevelGearSetModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4574

            return self._parent._cast(_4574.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4602

            return self._parent._cast(_4602.ConicalGearSetModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4633

            return self._parent._cast(_4633.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4678

            return self._parent._cast(_4678.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4568

            return self._parent._cast(_4568.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
        ) -> "StraightBevelDiffGearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearSetModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2543.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6958.StraightBevelDiffGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2811.StraightBevelDiffGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gears_modal_analysis(
        self: Self,
    ) -> "List[_4686.StraightBevelDiffGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_modal_analysis(
        self: Self,
    ) -> "List[_4685.StraightBevelDiffGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearMeshModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetModalAnalysis._Cast_StraightBevelDiffGearSetModalAnalysis":
        return self._Cast_StraightBevelDiffGearSetModalAnalysis(self)
