"""BoltedJointMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5485
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "BoltedJointMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2440
    from mastapy.system_model.analyses_and_results.static_loads import _6827


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="BoltedJointMultibodyDynamicsAnalysis")


class BoltedJointMultibodyDynamicsAnalysis(
    _5485.SpecialisedAssemblyMultibodyDynamicsAnalysis
):
    """BoltedJointMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltedJointMultibodyDynamicsAnalysis")

    class _Cast_BoltedJointMultibodyDynamicsAnalysis:
        """Special nested class for casting BoltedJointMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BoltedJointMultibodyDynamicsAnalysis._Cast_BoltedJointMultibodyDynamicsAnalysis",
            parent: "BoltedJointMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "BoltedJointMultibodyDynamicsAnalysis._Cast_BoltedJointMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5485.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "BoltedJointMultibodyDynamicsAnalysis._Cast_BoltedJointMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5372

            return self._parent._cast(_5372.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "BoltedJointMultibodyDynamicsAnalysis._Cast_BoltedJointMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "BoltedJointMultibodyDynamicsAnalysis._Cast_BoltedJointMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BoltedJointMultibodyDynamicsAnalysis._Cast_BoltedJointMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BoltedJointMultibodyDynamicsAnalysis._Cast_BoltedJointMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltedJointMultibodyDynamicsAnalysis._Cast_BoltedJointMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointMultibodyDynamicsAnalysis._Cast_BoltedJointMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bolted_joint_multibody_dynamics_analysis(
            self: "BoltedJointMultibodyDynamicsAnalysis._Cast_BoltedJointMultibodyDynamicsAnalysis",
        ) -> "BoltedJointMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BoltedJointMultibodyDynamicsAnalysis._Cast_BoltedJointMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "BoltedJointMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2440.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6827.BoltedJointLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BoltedJointMultibodyDynamicsAnalysis._Cast_BoltedJointMultibodyDynamicsAnalysis":
        return self._Cast_BoltedJointMultibodyDynamicsAnalysis(self)
