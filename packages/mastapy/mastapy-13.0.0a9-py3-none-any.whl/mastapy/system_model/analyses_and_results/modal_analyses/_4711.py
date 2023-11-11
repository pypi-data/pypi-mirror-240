"""ZerolBevelGearSetModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4586
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ZerolBevelGearSetModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2551
    from mastapy.system_model.analyses_and_results.static_loads import _6984
    from mastapy.system_model.analyses_and_results.system_deflections import _2837
    from mastapy.system_model.analyses_and_results.modal_analyses import _4710, _4709


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetModalAnalysis",)


Self = TypeVar("Self", bound="ZerolBevelGearSetModalAnalysis")


class ZerolBevelGearSetModalAnalysis(_4586.BevelGearSetModalAnalysis):
    """ZerolBevelGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearSetModalAnalysis")

    class _Cast_ZerolBevelGearSetModalAnalysis:
        """Special nested class for casting ZerolBevelGearSetModalAnalysis to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
            parent: "ZerolBevelGearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_modal_analysis(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ):
            return self._parent._cast(_4586.BevelGearSetModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4574

            return self._parent._cast(_4574.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4602

            return self._parent._cast(_4602.ConicalGearSetModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4633

            return self._parent._cast(_4633.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4678

            return self._parent._cast(_4678.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4568

            return self._parent._cast(_4568.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
        ) -> "ZerolBevelGearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelGearSetModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2551.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6984.ZerolBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase

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
    ) -> "_2837.ZerolBevelGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def zerol_bevel_gears_modal_analysis(
        self: Self,
    ) -> "List[_4710.ZerolBevelGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes_modal_analysis(
        self: Self,
    ) -> "List[_4709.ZerolBevelGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ZerolBevelGearMeshModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearSetModalAnalysis._Cast_ZerolBevelGearSetModalAnalysis":
        return self._Cast_ZerolBevelGearSetModalAnalysis(self)
