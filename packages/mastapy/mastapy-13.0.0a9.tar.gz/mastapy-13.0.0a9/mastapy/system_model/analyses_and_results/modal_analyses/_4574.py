"""AGMAGleasonConicalGearSetModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4602
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "AGMAGleasonConicalGearSetModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2511
    from mastapy.system_model.analyses_and_results.system_deflections import _2687


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetModalAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetModalAnalysis")


class AGMAGleasonConicalGearSetModalAnalysis(_4602.ConicalGearSetModalAnalysis):
    """AGMAGleasonConicalGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetModalAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearSetModalAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetModalAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
            parent: "AGMAGleasonConicalGearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ):
            return self._parent._cast(_4602.ConicalGearSetModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4633

            return self._parent._cast(_4633.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4678

            return self._parent._cast(_4678.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4568

            return self._parent._cast(_4568.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4581

            return self._parent._cast(_4581.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4586

            return self._parent._cast(_4586.BevelGearSetModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4637

            return self._parent._cast(_4637.HypoidGearSetModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681

            return self._parent._cast(_4681.SpiralBevelGearSetModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4687

            return self._parent._cast(_4687.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.StraightBevelGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4711

            return self._parent._cast(_4711.ZerolBevelGearSetModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
        ) -> "AGMAGleasonConicalGearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearSetModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2511.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2687.AGMAGleasonConicalGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSetSystemDeflection

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
    ) -> "AGMAGleasonConicalGearSetModalAnalysis._Cast_AGMAGleasonConicalGearSetModalAnalysis":
        return self._Cast_AGMAGleasonConicalGearSetModalAnalysis(self)
