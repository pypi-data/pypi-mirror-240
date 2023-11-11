"""BevelDifferentialSunGearModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4865,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "BevelDifferentialSunGearModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2515


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearModalAnalysisAtAStiffness")


class BevelDifferentialSunGearModalAnalysisAtAStiffness(
    _4865.BevelDifferentialGearModalAnalysisAtAStiffness
):
    """BevelDifferentialSunGearModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness"
    )

    class _Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness:
        """Special nested class for casting BevelDifferentialSunGearModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
            parent: "BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _4865.BevelDifferentialGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4870,
            )

            return self._parent._cast(_4870.BevelGearModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4858,
            )

            return self._parent._cast(
                _4858.AGMAGleasonConicalGearModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4886,
            )

            return self._parent._cast(_4886.ConicalGearModalAnalysisAtAStiffness)

        @property
        def gear_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4913,
            )

            return self._parent._cast(_4913.GearModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4932,
            )

            return self._parent._cast(_4932.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4878,
            )

            return self._parent._cast(_4878.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4934,
            )

            return self._parent._cast(_4934.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_stiffness(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
        ) -> "BevelDifferentialSunGearModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness",
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
        instance_to_wrap: "BevelDifferentialSunGearModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2515.BevelDifferentialSunGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialSunGear

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
    ) -> "BevelDifferentialSunGearModalAnalysisAtAStiffness._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness":
        return self._Cast_BevelDifferentialSunGearModalAnalysisAtAStiffness(self)
