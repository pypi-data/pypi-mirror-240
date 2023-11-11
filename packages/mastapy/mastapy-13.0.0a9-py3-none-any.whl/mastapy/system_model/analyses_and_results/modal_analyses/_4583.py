"""BevelDifferentialSunGearModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4580
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "BevelDifferentialSunGearModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2515
    from mastapy.system_model.analyses_and_results.system_deflections import _2702


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearModalAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearModalAnalysis")


class BevelDifferentialSunGearModalAnalysis(_4580.BevelDifferentialGearModalAnalysis):
    """BevelDifferentialSunGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearModalAnalysis"
    )

    class _Cast_BevelDifferentialSunGearModalAnalysis:
        """Special nested class for casting BevelDifferentialSunGearModalAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearModalAnalysis._Cast_BevelDifferentialSunGearModalAnalysis",
            parent: "BevelDifferentialSunGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_modal_analysis(
            self: "BevelDifferentialSunGearModalAnalysis._Cast_BevelDifferentialSunGearModalAnalysis",
        ):
            return self._parent._cast(_4580.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "BevelDifferentialSunGearModalAnalysis._Cast_BevelDifferentialSunGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4585

            return self._parent._cast(_4585.BevelGearModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "BevelDifferentialSunGearModalAnalysis._Cast_BevelDifferentialSunGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4573

            return self._parent._cast(_4573.AGMAGleasonConicalGearModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "BevelDifferentialSunGearModalAnalysis._Cast_BevelDifferentialSunGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4601

            return self._parent._cast(_4601.ConicalGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "BevelDifferentialSunGearModalAnalysis._Cast_BevelDifferentialSunGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4632

            return self._parent._cast(_4632.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "BevelDifferentialSunGearModalAnalysis._Cast_BevelDifferentialSunGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4654

            return self._parent._cast(_4654.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "BevelDifferentialSunGearModalAnalysis._Cast_BevelDifferentialSunGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "BevelDifferentialSunGearModalAnalysis._Cast_BevelDifferentialSunGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialSunGearModalAnalysis._Cast_BevelDifferentialSunGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialSunGearModalAnalysis._Cast_BevelDifferentialSunGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialSunGearModalAnalysis._Cast_BevelDifferentialSunGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialSunGearModalAnalysis._Cast_BevelDifferentialSunGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearModalAnalysis._Cast_BevelDifferentialSunGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "BevelDifferentialSunGearModalAnalysis._Cast_BevelDifferentialSunGearModalAnalysis",
        ) -> "BevelDifferentialSunGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearModalAnalysis._Cast_BevelDifferentialSunGearModalAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialSunGearModalAnalysis.TYPE"
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
    def system_deflection_results(
        self: Self,
    ) -> "_2702.BevelDifferentialSunGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialSunGearSystemDeflection

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
    ) -> "BevelDifferentialSunGearModalAnalysis._Cast_BevelDifferentialSunGearModalAnalysis":
        return self._Cast_BevelDifferentialSunGearModalAnalysis(self)
