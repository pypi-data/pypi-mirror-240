"""CouplingHalfHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5782
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "CouplingHalfHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2581
    from mastapy.system_model.analyses_and_results.system_deflections import _2727


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfHarmonicAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfHarmonicAnalysis")


class CouplingHalfHarmonicAnalysis(_5782.MountableComponentHarmonicAnalysis):
    """CouplingHalfHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfHarmonicAnalysis")

    class _Cast_CouplingHalfHarmonicAnalysis:
        """Special nested class for casting CouplingHalfHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
            parent: "CouplingHalfHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ):
            return self._parent._cast(_5782.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5701,
            )

            return self._parent._cast(_5701.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5697,
            )

            return self._parent._cast(_5697.ClutchHalfHarmonicAnalysis)

        @property
        def concept_coupling_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5703,
            )

            return self._parent._cast(_5703.ConceptCouplingHalfHarmonicAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5718,
            )

            return self._parent._cast(_5718.CVTPulleyHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5786,
            )

            return self._parent._cast(_5786.PartToPartShearCouplingHalfHarmonicAnalysis)

        @property
        def pulley_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5794,
            )

            return self._parent._cast(_5794.PulleyHarmonicAnalysis)

        @property
        def rolling_ring_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5800,
            )

            return self._parent._cast(_5800.RollingRingHarmonicAnalysis)

        @property
        def spring_damper_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5812,
            )

            return self._parent._cast(_5812.SpringDamperHalfHarmonicAnalysis)

        @property
        def synchroniser_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5823,
            )

            return self._parent._cast(_5823.SynchroniserHalfHarmonicAnalysis)

        @property
        def synchroniser_part_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5825,
            )

            return self._parent._cast(_5825.SynchroniserPartHarmonicAnalysis)

        @property
        def synchroniser_sleeve_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5826,
            )

            return self._parent._cast(_5826.SynchroniserSleeveHarmonicAnalysis)

        @property
        def torque_converter_pump_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5829,
            )

            return self._parent._cast(_5829.TorqueConverterPumpHarmonicAnalysis)

        @property
        def torque_converter_turbine_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5830,
            )

            return self._parent._cast(_5830.TorqueConverterTurbineHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "CouplingHalfHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfHarmonicAnalysis.TYPE"):
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
    ) -> "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis":
        return self._Cast_CouplingHalfHarmonicAnalysis(self)
