"""StraightBevelDiffGearSetMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5392
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "StraightBevelDiffGearSetMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.static_loads import _6958
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5493, _5492


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetMultibodyDynamicsAnalysis")


class StraightBevelDiffGearSetMultibodyDynamicsAnalysis(
    _5392.BevelGearSetMultibodyDynamicsAnalysis
):
    """StraightBevelDiffGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearSetMultibodyDynamicsAnalysis"
    )

    class _Cast_StraightBevelDiffGearSetMultibodyDynamicsAnalysis:
        """Special nested class for casting StraightBevelDiffGearSetMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetMultibodyDynamicsAnalysis",
            parent: "StraightBevelDiffGearSetMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5392.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5378

            return self._parent._cast(
                _5378.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5409

            return self._parent._cast(_5409.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436

            return self._parent._cast(_5436.GearSetMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5485

            return self._parent._cast(
                _5485.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5372

            return self._parent._cast(_5372.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "StraightBevelDiffGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_multibody_dynamics_analysis(
            self: "StraightBevelDiffGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetMultibodyDynamicsAnalysis",
        ) -> "StraightBevelDiffGearSetMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "StraightBevelDiffGearSetMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2543.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6958.StraightBevelDiffGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(
        self: Self,
    ) -> "List[_5493.StraightBevelDiffGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.StraightBevelDiffGearMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_gears_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5493.StraightBevelDiffGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.StraightBevelDiffGearMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5492.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetMultibodyDynamicsAnalysis._Cast_StraightBevelDiffGearSetMultibodyDynamicsAnalysis":
        return self._Cast_StraightBevelDiffGearSetMultibodyDynamicsAnalysis(self)
