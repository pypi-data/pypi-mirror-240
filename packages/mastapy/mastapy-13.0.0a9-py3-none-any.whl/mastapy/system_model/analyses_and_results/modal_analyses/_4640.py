"""KlingelnbergCycloPalloidConicalGearModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4601
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "KlingelnbergCycloPalloidConicalGearModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.system_deflections import _2767


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearModalAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearModalAnalysis")


class KlingelnbergCycloPalloidConicalGearModalAnalysis(_4601.ConicalGearModalAnalysis):
    """KlingelnbergCycloPalloidConicalGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearModalAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ):
            return self._parent._cast(_4601.ConicalGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4632

            return self._parent._cast(_4632.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4654

            return self._parent._cast(_4654.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4643

            return self._parent._cast(
                _4643.KlingelnbergCycloPalloidHypoidGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646

            return self._parent._cast(
                _4646.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2533.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

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
    ) -> "_2767.KlingelnbergCycloPalloidConicalGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearSystemDeflection

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
    ) -> "KlingelnbergCycloPalloidConicalGearModalAnalysis._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysis(self)
