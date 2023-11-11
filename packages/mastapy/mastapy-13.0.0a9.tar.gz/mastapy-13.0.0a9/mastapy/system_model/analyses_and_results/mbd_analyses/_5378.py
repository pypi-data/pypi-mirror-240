"""AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5409
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2511


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis")


class AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis(
    _5409.ConicalGearSetMultibodyDynamicsAnalysis
):
    """AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
            parent: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5409.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436

            return self._parent._cast(_5436.GearSetMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5485

            return self._parent._cast(
                _5485.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5372

            return self._parent._cast(_5372.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5387

            return self._parent._cast(
                _5387.BevelDifferentialGearSetMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_set_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5392

            return self._parent._cast(_5392.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5440

            return self._parent._cast(_5440.HypoidGearSetMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.SpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_set_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5494

            return self._parent._cast(
                _5494.StraightBevelDiffGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5497

            return self._parent._cast(
                _5497.StraightBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_set_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5518

            return self._parent._cast(_5518.ZerolBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2511.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis":
        return self._Cast_AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis(self)
