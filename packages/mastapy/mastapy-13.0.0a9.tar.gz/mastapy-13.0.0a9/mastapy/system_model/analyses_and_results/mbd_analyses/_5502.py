"""SynchroniserPartMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5413
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "SynchroniserPartMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2602


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SynchroniserPartMultibodyDynamicsAnalysis")


class SynchroniserPartMultibodyDynamicsAnalysis(
    _5413.CouplingHalfMultibodyDynamicsAnalysis
):
    """SynchroniserPartMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartMultibodyDynamicsAnalysis"
    )

    class _Cast_SynchroniserPartMultibodyDynamicsAnalysis:
        """Special nested class for casting SynchroniserPartMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
            parent: "SynchroniserPartMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5413.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5460

            return self._parent._cast(_5460.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400

            return self._parent._cast(_5400.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def synchroniser_half_multibody_dynamics_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5500

            return self._parent._cast(_5500.SynchroniserHalfMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_multibody_dynamics_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5503

            return self._parent._cast(_5503.SynchroniserSleeveMultibodyDynamicsAnalysis)

        @property
        def synchroniser_part_multibody_dynamics_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "SynchroniserPartMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserPartMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2602.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

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
    ) -> "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis":
        return self._Cast_SynchroniserPartMultibodyDynamicsAnalysis(self)
