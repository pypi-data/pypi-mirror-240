"""SpiralBevelGearCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5541
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "SpiralBevelGearCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2540
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5487


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearCompoundMultibodyDynamicsAnalysis")


class SpiralBevelGearCompoundMultibodyDynamicsAnalysis(
    _5541.BevelGearCompoundMultibodyDynamicsAnalysis
):
    """SpiralBevelGearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_SpiralBevelGearCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting SpiralBevelGearCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearCompoundMultibodyDynamicsAnalysis",
            parent: "SpiralBevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(
            self: "SpiralBevelGearCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5541.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
            self: "SpiralBevelGearCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5529,
            )

            return self._parent._cast(
                _5529.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_compound_multibody_dynamics_analysis(
            self: "SpiralBevelGearCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5557,
            )

            return self._parent._cast(
                _5557.ConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "SpiralBevelGearCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5583,
            )

            return self._parent._cast(_5583.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "SpiralBevelGearCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5602,
            )

            return self._parent._cast(
                _5602.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "SpiralBevelGearCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5550,
            )

            return self._parent._cast(_5550.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "SpiralBevelGearCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5604,
            )

            return self._parent._cast(_5604.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "SpiralBevelGearCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "SpiralBevelGearCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearCompoundMultibodyDynamicsAnalysis",
        ) -> "SpiralBevelGearCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "SpiralBevelGearCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2540.SpiralBevelGear":
        """mastapy.system_model.part_model.gears.SpiralBevelGear

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
    ) -> "List[_5487.SpiralBevelGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.SpiralBevelGearMultibodyDynamicsAnalysis]

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
    ) -> "List[_5487.SpiralBevelGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.SpiralBevelGearMultibodyDynamicsAnalysis]

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
    ) -> "SpiralBevelGearCompoundMultibodyDynamicsAnalysis._Cast_SpiralBevelGearCompoundMultibodyDynamicsAnalysis":
        return self._Cast_SpiralBevelGearCompoundMultibodyDynamicsAnalysis(self)
