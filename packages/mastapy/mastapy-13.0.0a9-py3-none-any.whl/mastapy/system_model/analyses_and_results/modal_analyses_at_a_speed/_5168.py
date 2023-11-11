"""FaceGearSetModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5173
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "FaceGearSetModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2526
    from mastapy.system_model.analyses_and_results.static_loads import _6883
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5167,
        _5166,
    )


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="FaceGearSetModalAnalysisAtASpeed")


class FaceGearSetModalAnalysisAtASpeed(_5173.GearSetModalAnalysisAtASpeed):
    """FaceGearSetModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetModalAnalysisAtASpeed")

    class _Cast_FaceGearSetModalAnalysisAtASpeed:
        """Special nested class for casting FaceGearSetModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "FaceGearSetModalAnalysisAtASpeed._Cast_FaceGearSetModalAnalysisAtASpeed",
            parent: "FaceGearSetModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_set_modal_analysis_at_a_speed(
            self: "FaceGearSetModalAnalysisAtASpeed._Cast_FaceGearSetModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5173.GearSetModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "FaceGearSetModalAnalysisAtASpeed._Cast_FaceGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5212,
            )

            return self._parent._cast(_5212.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "FaceGearSetModalAnalysisAtASpeed._Cast_FaceGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5113,
            )

            return self._parent._cast(_5113.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "FaceGearSetModalAnalysisAtASpeed._Cast_FaceGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5193,
            )

            return self._parent._cast(_5193.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearSetModalAnalysisAtASpeed._Cast_FaceGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearSetModalAnalysisAtASpeed._Cast_FaceGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearSetModalAnalysisAtASpeed._Cast_FaceGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearSetModalAnalysisAtASpeed._Cast_FaceGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSetModalAnalysisAtASpeed._Cast_FaceGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def face_gear_set_modal_analysis_at_a_speed(
            self: "FaceGearSetModalAnalysisAtASpeed._Cast_FaceGearSetModalAnalysisAtASpeed",
        ) -> "FaceGearSetModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "FaceGearSetModalAnalysisAtASpeed._Cast_FaceGearSetModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSetModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2526.FaceGearSet":
        """mastapy.system_model.part_model.gears.FaceGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6883.FaceGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def face_gears_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5167.FaceGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.FaceGearModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearsModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5166.FaceGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.FaceGearMeshModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshesModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearSetModalAnalysisAtASpeed._Cast_FaceGearSetModalAnalysisAtASpeed":
        return self._Cast_FaceGearSetModalAnalysisAtASpeed(self)
