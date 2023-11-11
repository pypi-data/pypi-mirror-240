"""BevelGearSetModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4574
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "BevelGearSetModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2517
    from mastapy.system_model.analyses_and_results.system_deflections import _2704


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetModalAnalysis",)


Self = TypeVar("Self", bound="BevelGearSetModalAnalysis")


class BevelGearSetModalAnalysis(_4574.AGMAGleasonConicalGearSetModalAnalysis):
    """BevelGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetModalAnalysis")

    class _Cast_BevelGearSetModalAnalysis:
        """Special nested class for casting BevelGearSetModalAnalysis to subclasses."""

        def __init__(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
            parent: "BevelGearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ):
            return self._parent._cast(_4574.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4602

            return self._parent._cast(_4602.ConicalGearSetModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4633

            return self._parent._cast(_4633.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4678

            return self._parent._cast(_4678.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4568

            return self._parent._cast(_4568.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4581

            return self._parent._cast(_4581.BevelDifferentialGearSetModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681

            return self._parent._cast(_4681.SpiralBevelGearSetModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4687

            return self._parent._cast(_4687.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.StraightBevelGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4711

            return self._parent._cast(_4711.ZerolBevelGearSetModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis",
        ) -> "BevelGearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearSetModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2517.BevelGearSet":
        """mastapy.system_model.part_model.gears.BevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2704.BevelGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelGearSetSystemDeflection

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
    ) -> "BevelGearSetModalAnalysis._Cast_BevelGearSetModalAnalysis":
        return self._Cast_BevelGearSetModalAnalysis(self)
