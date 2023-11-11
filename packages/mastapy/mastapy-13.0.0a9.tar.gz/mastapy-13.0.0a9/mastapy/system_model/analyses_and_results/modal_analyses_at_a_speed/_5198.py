"""PlanetaryGearSetModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5162
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "PlanetaryGearSetModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="PlanetaryGearSetModalAnalysisAtASpeed")


class PlanetaryGearSetModalAnalysisAtASpeed(
    _5162.CylindricalGearSetModalAnalysisAtASpeed
):
    """PlanetaryGearSetModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetModalAnalysisAtASpeed"
    )

    class _Cast_PlanetaryGearSetModalAnalysisAtASpeed:
        """Special nested class for casting PlanetaryGearSetModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
            parent: "PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5162.CylindricalGearSetModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5173,
            )

            return self._parent._cast(_5173.GearSetModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5212,
            )

            return self._parent._cast(_5212.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5113,
            )

            return self._parent._cast(_5113.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5193,
            )

            return self._parent._cast(_5193.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def planetary_gear_set_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ) -> "PlanetaryGearSetModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2539.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed":
        return self._Cast_PlanetaryGearSetModalAnalysisAtASpeed(self)
