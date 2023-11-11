"""CouplingHalfStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3839
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CouplingHalfStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2581


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfStabilityAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfStabilityAnalysis")


class CouplingHalfStabilityAnalysis(_3839.MountableComponentStabilityAnalysis):
    """CouplingHalfStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfStabilityAnalysis")

    class _Cast_CouplingHalfStabilityAnalysis:
        """Special nested class for casting CouplingHalfStabilityAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
            parent: "CouplingHalfStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            return self._parent._cast(_3839.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3785,
            )

            return self._parent._cast(_3785.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_half_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3782,
            )

            return self._parent._cast(_3782.ClutchHalfStabilityAnalysis)

        @property
        def concept_coupling_half_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3787,
            )

            return self._parent._cast(_3787.ConceptCouplingHalfStabilityAnalysis)

        @property
        def cvt_pulley_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3802,
            )

            return self._parent._cast(_3802.CVTPulleyStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3843,
            )

            return self._parent._cast(
                _3843.PartToPartShearCouplingHalfStabilityAnalysis
            )

        @property
        def pulley_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3850,
            )

            return self._parent._cast(_3850.PulleyStabilityAnalysis)

        @property
        def rolling_ring_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3855,
            )

            return self._parent._cast(_3855.RollingRingStabilityAnalysis)

        @property
        def spring_damper_half_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.SpringDamperHalfStabilityAnalysis)

        @property
        def synchroniser_half_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3878,
            )

            return self._parent._cast(_3878.SynchroniserHalfStabilityAnalysis)

        @property
        def synchroniser_part_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3879,
            )

            return self._parent._cast(_3879.SynchroniserPartStabilityAnalysis)

        @property
        def synchroniser_sleeve_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3880,
            )

            return self._parent._cast(_3880.SynchroniserSleeveStabilityAnalysis)

        @property
        def torque_converter_pump_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3883,
            )

            return self._parent._cast(_3883.TorqueConverterPumpStabilityAnalysis)

        @property
        def torque_converter_turbine_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3885,
            )

            return self._parent._cast(_3885.TorqueConverterTurbineStabilityAnalysis)

        @property
        def coupling_half_stability_analysis(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
        ) -> "CouplingHalfStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfStabilityAnalysis.TYPE"):
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
    def cast_to(
        self: Self,
    ) -> "CouplingHalfStabilityAnalysis._Cast_CouplingHalfStabilityAnalysis":
        return self._Cast_CouplingHalfStabilityAnalysis(self)
