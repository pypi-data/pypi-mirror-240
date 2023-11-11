"""DatumMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5400
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "DatumMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2445
    from mastapy.system_model.analyses_and_results.static_loads import _6866


__docformat__ = "restructuredtext en"
__all__ = ("DatumMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="DatumMultibodyDynamicsAnalysis")


class DatumMultibodyDynamicsAnalysis(_5400.ComponentMultibodyDynamicsAnalysis):
    """DatumMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _DATUM_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DatumMultibodyDynamicsAnalysis")

    class _Cast_DatumMultibodyDynamicsAnalysis:
        """Special nested class for casting DatumMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "DatumMultibodyDynamicsAnalysis._Cast_DatumMultibodyDynamicsAnalysis",
            parent: "DatumMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def component_multibody_dynamics_analysis(
            self: "DatumMultibodyDynamicsAnalysis._Cast_DatumMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5400.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "DatumMultibodyDynamicsAnalysis._Cast_DatumMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "DatumMultibodyDynamicsAnalysis._Cast_DatumMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "DatumMultibodyDynamicsAnalysis._Cast_DatumMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "DatumMultibodyDynamicsAnalysis._Cast_DatumMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "DatumMultibodyDynamicsAnalysis._Cast_DatumMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "DatumMultibodyDynamicsAnalysis._Cast_DatumMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def datum_multibody_dynamics_analysis(
            self: "DatumMultibodyDynamicsAnalysis._Cast_DatumMultibodyDynamicsAnalysis",
        ) -> "DatumMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "DatumMultibodyDynamicsAnalysis._Cast_DatumMultibodyDynamicsAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DatumMultibodyDynamicsAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2445.Datum":
        """mastapy.system_model.part_model.Datum

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6866.DatumLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "DatumMultibodyDynamicsAnalysis._Cast_DatumMultibodyDynamicsAnalysis":
        return self._Cast_DatumMultibodyDynamicsAnalysis(self)
