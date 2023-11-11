"""AGMAGleasonConicalGearMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5408
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2510


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMultibodyDynamicsAnalysis")


class AGMAGleasonConicalGearMultibodyDynamicsAnalysis(
    _5408.ConicalGearMultibodyDynamicsAnalysis
):
    """AGMAGleasonConicalGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
            parent: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5408.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5435

            return self._parent._cast(_5435.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5460

            return self._parent._cast(_5460.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400

            return self._parent._cast(_5400.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5386

            return self._parent._cast(
                _5386.BevelDifferentialGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5388

            return self._parent._cast(
                _5388.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5389

            return self._parent._cast(
                _5389.BevelDifferentialSunGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5391

            return self._parent._cast(_5391.BevelGearMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439

            return self._parent._cast(_5439.HypoidGearMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5487

            return self._parent._cast(_5487.SpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5493

            return self._parent._cast(
                _5493.StraightBevelDiffGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5496

            return self._parent._cast(_5496.StraightBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_planet_gear_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5498

            return self._parent._cast(
                _5498.StraightBevelPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5499

            return self._parent._cast(
                _5499.StraightBevelSunGearMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5517

            return self._parent._cast(_5517.ZerolBevelGearMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
        ) -> "AGMAGleasonConicalGearMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2510.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

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
    ) -> "AGMAGleasonConicalGearMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis":
        return self._Cast_AGMAGleasonConicalGearMultibodyDynamicsAnalysis(self)
