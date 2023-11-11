"""AGMAGleasonConicalGearModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4601
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "AGMAGleasonConicalGearModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2510
    from mastapy.system_model.analyses_and_results.system_deflections import _2688


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearModalAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearModalAnalysis")


class AGMAGleasonConicalGearModalAnalysis(_4601.ConicalGearModalAnalysis):
    """AGMAGleasonConicalGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearModalAnalysis")

    class _Cast_AGMAGleasonConicalGearModalAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearModalAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
            parent: "AGMAGleasonConicalGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ):
            return self._parent._cast(_4601.ConicalGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4632

            return self._parent._cast(_4632.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4654

            return self._parent._cast(_4654.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4580

            return self._parent._cast(_4580.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4582

            return self._parent._cast(_4582.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4583

            return self._parent._cast(_4583.BevelDifferentialSunGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4585

            return self._parent._cast(_4585.BevelGearModalAnalysis)

        @property
        def hypoid_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636

            return self._parent._cast(_4636.HypoidGearModalAnalysis)

        @property
        def spiral_bevel_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4680

            return self._parent._cast(_4680.SpiralBevelGearModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4686

            return self._parent._cast(_4686.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4689

            return self._parent._cast(_4689.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4691

            return self._parent._cast(_4691.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4692

            return self._parent._cast(_4692.StraightBevelSunGearModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4710

            return self._parent._cast(_4710.ZerolBevelGearModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
        ) -> "AGMAGleasonConicalGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2510.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2688.AGMAGleasonConicalGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSystemDeflection

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
    ) -> (
        "AGMAGleasonConicalGearModalAnalysis._Cast_AGMAGleasonConicalGearModalAnalysis"
    ):
        return self._Cast_AGMAGleasonConicalGearModalAnalysis(self)
