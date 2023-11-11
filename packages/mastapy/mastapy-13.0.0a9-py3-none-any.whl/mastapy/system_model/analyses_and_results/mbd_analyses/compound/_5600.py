"""MassDiscCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5647
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "MassDiscCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2459
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5455


__docformat__ = "restructuredtext en"
__all__ = ("MassDiscCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="MassDiscCompoundMultibodyDynamicsAnalysis")


class MassDiscCompoundMultibodyDynamicsAnalysis(
    _5647.VirtualComponentCompoundMultibodyDynamicsAnalysis
):
    """MassDiscCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MassDiscCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_MassDiscCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting MassDiscCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "MassDiscCompoundMultibodyDynamicsAnalysis._Cast_MassDiscCompoundMultibodyDynamicsAnalysis",
            parent: "MassDiscCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_multibody_dynamics_analysis(
            self: "MassDiscCompoundMultibodyDynamicsAnalysis._Cast_MassDiscCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5647.VirtualComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "MassDiscCompoundMultibodyDynamicsAnalysis._Cast_MassDiscCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5602,
            )

            return self._parent._cast(
                _5602.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "MassDiscCompoundMultibodyDynamicsAnalysis._Cast_MassDiscCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5550,
            )

            return self._parent._cast(_5550.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "MassDiscCompoundMultibodyDynamicsAnalysis._Cast_MassDiscCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5604,
            )

            return self._parent._cast(_5604.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "MassDiscCompoundMultibodyDynamicsAnalysis._Cast_MassDiscCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MassDiscCompoundMultibodyDynamicsAnalysis._Cast_MassDiscCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MassDiscCompoundMultibodyDynamicsAnalysis._Cast_MassDiscCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def mass_disc_compound_multibody_dynamics_analysis(
            self: "MassDiscCompoundMultibodyDynamicsAnalysis._Cast_MassDiscCompoundMultibodyDynamicsAnalysis",
        ) -> "MassDiscCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "MassDiscCompoundMultibodyDynamicsAnalysis._Cast_MassDiscCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "MassDiscCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2459.MassDisc":
        """mastapy.system_model.part_model.MassDisc

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
    ) -> "List[_5455.MassDiscMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.MassDiscMultibodyDynamicsAnalysis]

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
    def planetaries(self: Self) -> "List[MassDiscCompoundMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.compound.MassDiscCompoundMultibodyDynamicsAnalysis]

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
    ) -> "List[_5455.MassDiscMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.MassDiscMultibodyDynamicsAnalysis]

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
    ) -> "MassDiscCompoundMultibodyDynamicsAnalysis._Cast_MassDiscCompoundMultibodyDynamicsAnalysis":
        return self._Cast_MassDiscCompoundMultibodyDynamicsAnalysis(self)
