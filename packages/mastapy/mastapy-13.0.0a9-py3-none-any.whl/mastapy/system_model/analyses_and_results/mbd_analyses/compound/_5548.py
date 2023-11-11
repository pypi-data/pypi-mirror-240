"""ClutchHalfCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5564
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "ClutchHalfCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2576
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5396


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHalfCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ClutchHalfCompoundMultibodyDynamicsAnalysis")


class ClutchHalfCompoundMultibodyDynamicsAnalysis(
    _5564.CouplingHalfCompoundMultibodyDynamicsAnalysis
):
    """ClutchHalfCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ClutchHalfCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_ClutchHalfCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting ClutchHalfCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ClutchHalfCompoundMultibodyDynamicsAnalysis._Cast_ClutchHalfCompoundMultibodyDynamicsAnalysis",
            parent: "ClutchHalfCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_multibody_dynamics_analysis(
            self: "ClutchHalfCompoundMultibodyDynamicsAnalysis._Cast_ClutchHalfCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5564.CouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "ClutchHalfCompoundMultibodyDynamicsAnalysis._Cast_ClutchHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5602,
            )

            return self._parent._cast(
                _5602.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "ClutchHalfCompoundMultibodyDynamicsAnalysis._Cast_ClutchHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5550,
            )

            return self._parent._cast(_5550.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "ClutchHalfCompoundMultibodyDynamicsAnalysis._Cast_ClutchHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5604,
            )

            return self._parent._cast(_5604.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "ClutchHalfCompoundMultibodyDynamicsAnalysis._Cast_ClutchHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ClutchHalfCompoundMultibodyDynamicsAnalysis._Cast_ClutchHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchHalfCompoundMultibodyDynamicsAnalysis._Cast_ClutchHalfCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_half_compound_multibody_dynamics_analysis(
            self: "ClutchHalfCompoundMultibodyDynamicsAnalysis._Cast_ClutchHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "ClutchHalfCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ClutchHalfCompoundMultibodyDynamicsAnalysis._Cast_ClutchHalfCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ClutchHalfCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2576.ClutchHalf":
        """mastapy.system_model.part_model.couplings.ClutchHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5396.ClutchHalfMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ClutchHalfMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5396.ClutchHalfMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ClutchHalfMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ClutchHalfCompoundMultibodyDynamicsAnalysis._Cast_ClutchHalfCompoundMultibodyDynamicsAnalysis":
        return self._Cast_ClutchHalfCompoundMultibodyDynamicsAnalysis(self)
