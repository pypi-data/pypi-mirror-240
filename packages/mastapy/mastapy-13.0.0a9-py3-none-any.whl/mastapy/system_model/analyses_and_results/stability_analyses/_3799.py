"""CouplingStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3860
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "CouplingStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2580


__docformat__ = "restructuredtext en"
__all__ = ("CouplingStabilityAnalysis",)


Self = TypeVar("Self", bound="CouplingStabilityAnalysis")


class CouplingStabilityAnalysis(_3860.SpecialisedAssemblyStabilityAnalysis):
    """CouplingStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingStabilityAnalysis")

    class _Cast_CouplingStabilityAnalysis:
        """Special nested class for casting CouplingStabilityAnalysis to subclasses."""

        def __init__(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
            parent: "CouplingStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            return self._parent._cast(_3860.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3760,
            )

            return self._parent._cast(_3760.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3783,
            )

            return self._parent._cast(_3783.ClutchStabilityAnalysis)

        @property
        def concept_coupling_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.ConceptCouplingStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.PartToPartShearCouplingStabilityAnalysis)

        @property
        def spring_damper_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3866,
            )

            return self._parent._cast(_3866.SpringDamperStabilityAnalysis)

        @property
        def torque_converter_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3884,
            )

            return self._parent._cast(_3884.TorqueConverterStabilityAnalysis)

        @property
        def coupling_stability_analysis(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis",
        ) -> "CouplingStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2580.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingStabilityAnalysis._Cast_CouplingStabilityAnalysis":
        return self._Cast_CouplingStabilityAnalysis(self)
