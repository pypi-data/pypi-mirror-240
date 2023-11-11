"""BevelDifferentialPlanetGearModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5125
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "BevelDifferentialPlanetGearModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2514


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearModalAnalysisAtASpeed")


class BevelDifferentialPlanetGearModalAnalysisAtASpeed(
    _5125.BevelDifferentialGearModalAnalysisAtASpeed
):
    """BevelDifferentialPlanetGearModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialPlanetGearModalAnalysisAtASpeed"
    )

    class _Cast_BevelDifferentialPlanetGearModalAnalysisAtASpeed:
        """Special nested class for casting BevelDifferentialPlanetGearModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearModalAnalysisAtASpeed",
            parent: "BevelDifferentialPlanetGearModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_modal_analysis_at_a_speed(
            self: "BevelDifferentialPlanetGearModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5125.BevelDifferentialGearModalAnalysisAtASpeed)

        @property
        def bevel_gear_modal_analysis_at_a_speed(
            self: "BevelDifferentialPlanetGearModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5130,
            )

            return self._parent._cast(_5130.BevelGearModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_speed(
            self: "BevelDifferentialPlanetGearModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5118,
            )

            return self._parent._cast(_5118.AGMAGleasonConicalGearModalAnalysisAtASpeed)

        @property
        def conical_gear_modal_analysis_at_a_speed(
            self: "BevelDifferentialPlanetGearModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5146,
            )

            return self._parent._cast(_5146.ConicalGearModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(
            self: "BevelDifferentialPlanetGearModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5172,
            )

            return self._parent._cast(_5172.GearModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "BevelDifferentialPlanetGearModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5191,
            )

            return self._parent._cast(_5191.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "BevelDifferentialPlanetGearModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5138,
            )

            return self._parent._cast(_5138.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "BevelDifferentialPlanetGearModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5193,
            )

            return self._parent._cast(_5193.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialPlanetGearModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialPlanetGearModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_speed(
            self: "BevelDifferentialPlanetGearModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearModalAnalysisAtASpeed",
        ) -> "BevelDifferentialPlanetGearModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearModalAnalysisAtASpeed",
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
        instance_to_wrap: "BevelDifferentialPlanetGearModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2514.BevelDifferentialPlanetGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialPlanetGearModalAnalysisAtASpeed._Cast_BevelDifferentialPlanetGearModalAnalysisAtASpeed":
        return self._Cast_BevelDifferentialPlanetGearModalAnalysisAtASpeed(self)
