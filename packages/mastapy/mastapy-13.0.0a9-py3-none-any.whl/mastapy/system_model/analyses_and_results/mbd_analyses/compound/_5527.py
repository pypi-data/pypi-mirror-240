"""AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5550
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5374


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis")


class AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis(
    _5550.ComponentCompoundMultibodyDynamicsAnalysis
):
    """AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
            parent: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5550.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5604,
            )

            return self._parent._cast(_5604.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_multibody_dynamics_analysis(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5526,
            )

            return self._parent._cast(
                _5526.AbstractShaftCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_compound_multibody_dynamics_analysis(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5570,
            )

            return self._parent._cast(
                _5570.CycloidalDiscCompoundMultibodyDynamicsAnalysis
            )

        @property
        def fe_part_compound_multibody_dynamics_analysis(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5581,
            )

            return self._parent._cast(_5581.FEPartCompoundMultibodyDynamicsAnalysis)

        @property
        def shaft_compound_multibody_dynamics_analysis(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5620,
            )

            return self._parent._cast(_5620.ShaftCompoundMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_or_housing_compound_multibody_dynamics_analysis(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
        ) -> "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis",
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
        self: Self,
        instance_to_wrap: "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5374.AbstractShaftOrHousingMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AbstractShaftOrHousingMultibodyDynamicsAnalysis]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5374.AbstractShaftOrHousingMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AbstractShaftOrHousingMultibodyDynamicsAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis":
        return self._Cast_AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis(self)
