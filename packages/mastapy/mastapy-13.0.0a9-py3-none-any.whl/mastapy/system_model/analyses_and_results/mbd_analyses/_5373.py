"""AbstractShaftMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5374
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "AbstractShaftMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2432


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftMultibodyDynamicsAnalysis")


class AbstractShaftMultibodyDynamicsAnalysis(
    _5374.AbstractShaftOrHousingMultibodyDynamicsAnalysis
):
    """AbstractShaftMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftMultibodyDynamicsAnalysis"
    )

    class _Cast_AbstractShaftMultibodyDynamicsAnalysis:
        """Special nested class for casting AbstractShaftMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftMultibodyDynamicsAnalysis._Cast_AbstractShaftMultibodyDynamicsAnalysis",
            parent: "AbstractShaftMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_multibody_dynamics_analysis(
            self: "AbstractShaftMultibodyDynamicsAnalysis._Cast_AbstractShaftMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5374.AbstractShaftOrHousingMultibodyDynamicsAnalysis
            )

        @property
        def component_multibody_dynamics_analysis(
            self: "AbstractShaftMultibodyDynamicsAnalysis._Cast_AbstractShaftMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400

            return self._parent._cast(_5400.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "AbstractShaftMultibodyDynamicsAnalysis._Cast_AbstractShaftMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "AbstractShaftMultibodyDynamicsAnalysis._Cast_AbstractShaftMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftMultibodyDynamicsAnalysis._Cast_AbstractShaftMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftMultibodyDynamicsAnalysis._Cast_AbstractShaftMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftMultibodyDynamicsAnalysis._Cast_AbstractShaftMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftMultibodyDynamicsAnalysis._Cast_AbstractShaftMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cycloidal_disc_multibody_dynamics_analysis(
            self: "AbstractShaftMultibodyDynamicsAnalysis._Cast_AbstractShaftMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5420

            return self._parent._cast(_5420.CycloidalDiscMultibodyDynamicsAnalysis)

        @property
        def shaft_multibody_dynamics_analysis(
            self: "AbstractShaftMultibodyDynamicsAnalysis._Cast_AbstractShaftMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5482

            return self._parent._cast(_5482.ShaftMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_multibody_dynamics_analysis(
            self: "AbstractShaftMultibodyDynamicsAnalysis._Cast_AbstractShaftMultibodyDynamicsAnalysis",
        ) -> "AbstractShaftMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftMultibodyDynamicsAnalysis._Cast_AbstractShaftMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2432.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

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
    ) -> "AbstractShaftMultibodyDynamicsAnalysis._Cast_AbstractShaftMultibodyDynamicsAnalysis":
        return self._Cast_AbstractShaftMultibodyDynamicsAnalysis(self)
