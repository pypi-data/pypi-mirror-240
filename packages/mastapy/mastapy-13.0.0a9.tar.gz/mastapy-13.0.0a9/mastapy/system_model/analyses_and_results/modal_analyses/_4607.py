"""CouplingHalfModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4654
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "CouplingHalfModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2581
    from mastapy.system_model.analyses_and_results.system_deflections import _2727


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfModalAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfModalAnalysis")


class CouplingHalfModalAnalysis(_4654.MountableComponentModalAnalysis):
    """CouplingHalfModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfModalAnalysis")

    class _Cast_CouplingHalfModalAnalysis:
        """Special nested class for casting CouplingHalfModalAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
            parent: "CouplingHalfModalAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ):
            return self._parent._cast(_4654.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_half_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4590

            return self._parent._cast(_4590.ClutchHalfModalAnalysis)

        @property
        def concept_coupling_half_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595

            return self._parent._cast(_4595.ConceptCouplingHalfModalAnalysis)

        @property
        def cvt_pulley_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4611

            return self._parent._cast(_4611.CVTPulleyModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660

            return self._parent._cast(_4660.PartToPartShearCouplingHalfModalAnalysis)

        @property
        def pulley_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4667

            return self._parent._cast(_4667.PulleyModalAnalysis)

        @property
        def rolling_ring_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4672

            return self._parent._cast(_4672.RollingRingModalAnalysis)

        @property
        def spring_damper_half_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4683

            return self._parent._cast(_4683.SpringDamperHalfModalAnalysis)

        @property
        def synchroniser_half_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4693

            return self._parent._cast(_4693.SynchroniserHalfModalAnalysis)

        @property
        def synchroniser_part_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4695

            return self._parent._cast(_4695.SynchroniserPartModalAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4696

            return self._parent._cast(_4696.SynchroniserSleeveModalAnalysis)

        @property
        def torque_converter_pump_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4699

            return self._parent._cast(_4699.TorqueConverterPumpModalAnalysis)

        @property
        def torque_converter_turbine_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4700

            return self._parent._cast(_4700.TorqueConverterTurbineModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "CouplingHalfModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2581.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2727.CouplingHalfSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CouplingHalfSystemDeflection

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
    ) -> "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis":
        return self._Cast_CouplingHalfModalAnalysis(self)
