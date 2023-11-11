"""KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5447
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2535
    from mastapy.system_model.analyses_and_results.static_loads import _6912


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis"
)


class KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis(
    _5447.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis
):
    """KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
            parent: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5447.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5408

            return self._parent._cast(_5408.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5435

            return self._parent._cast(_5435.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5460

            return self._parent._cast(_5460.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400

            return self._parent._cast(_5400.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
        ) -> "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2535.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(
        self: Self,
    ) -> "_6912.KlingelnbergCycloPalloidHypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis(
            self
        )
