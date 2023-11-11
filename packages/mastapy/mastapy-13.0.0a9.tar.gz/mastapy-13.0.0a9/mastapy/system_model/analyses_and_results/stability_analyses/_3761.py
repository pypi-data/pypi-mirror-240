"""AbstractShaftOrHousingStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3785
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "AbstractShaftOrHousingStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2433


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingStabilityAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingStabilityAnalysis")


class AbstractShaftOrHousingStabilityAnalysis(_3785.ComponentStabilityAnalysis):
    """AbstractShaftOrHousingStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingStabilityAnalysis"
    )

    class _Cast_AbstractShaftOrHousingStabilityAnalysis:
        """Special nested class for casting AbstractShaftOrHousingStabilityAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
            parent: "AbstractShaftOrHousingStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def component_stability_analysis(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ):
            return self._parent._cast(_3785.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_shaft_stability_analysis(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3762,
            )

            return self._parent._cast(_3762.AbstractShaftStabilityAnalysis)

        @property
        def cycloidal_disc_stability_analysis(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3807,
            )

            return self._parent._cast(_3807.CycloidalDiscStabilityAnalysis)

        @property
        def fe_part_stability_analysis(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3818,
            )

            return self._parent._cast(_3818.FEPartStabilityAnalysis)

        @property
        def shaft_stability_analysis(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3858,
            )

            return self._parent._cast(_3858.ShaftStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_stability_analysis(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
        ) -> "AbstractShaftOrHousingStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftOrHousingStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2433.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

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
    ) -> "AbstractShaftOrHousingStabilityAnalysis._Cast_AbstractShaftOrHousingStabilityAnalysis":
        return self._Cast_AbstractShaftOrHousingStabilityAnalysis(self)
