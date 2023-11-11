"""FEPartCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5527
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "FEPartCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2450
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5431


__docformat__ = "restructuredtext en"
__all__ = ("FEPartCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="FEPartCompoundMultibodyDynamicsAnalysis")


class FEPartCompoundMultibodyDynamicsAnalysis(
    _5527.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis
):
    """FEPartCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _FE_PART_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FEPartCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_FEPartCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting FEPartCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "FEPartCompoundMultibodyDynamicsAnalysis._Cast_FEPartCompoundMultibodyDynamicsAnalysis",
            parent: "FEPartCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_multibody_dynamics_analysis(
            self: "FEPartCompoundMultibodyDynamicsAnalysis._Cast_FEPartCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5527.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "FEPartCompoundMultibodyDynamicsAnalysis._Cast_FEPartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5550,
            )

            return self._parent._cast(_5550.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "FEPartCompoundMultibodyDynamicsAnalysis._Cast_FEPartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5604,
            )

            return self._parent._cast(_5604.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "FEPartCompoundMultibodyDynamicsAnalysis._Cast_FEPartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FEPartCompoundMultibodyDynamicsAnalysis._Cast_FEPartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartCompoundMultibodyDynamicsAnalysis._Cast_FEPartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def fe_part_compound_multibody_dynamics_analysis(
            self: "FEPartCompoundMultibodyDynamicsAnalysis._Cast_FEPartCompoundMultibodyDynamicsAnalysis",
        ) -> "FEPartCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "FEPartCompoundMultibodyDynamicsAnalysis._Cast_FEPartCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "FEPartCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2450.FEPart":
        """mastapy.system_model.part_model.FEPart

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
    ) -> "List[_5431.FEPartMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.FEPartMultibodyDynamicsAnalysis]

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
    def planetaries(self: Self) -> "List[FEPartCompoundMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.compound.FEPartCompoundMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5431.FEPartMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.FEPartMultibodyDynamicsAnalysis]

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
    ) -> "FEPartCompoundMultibodyDynamicsAnalysis._Cast_FEPartCompoundMultibodyDynamicsAnalysis":
        return self._Cast_FEPartCompoundMultibodyDynamicsAnalysis(self)
