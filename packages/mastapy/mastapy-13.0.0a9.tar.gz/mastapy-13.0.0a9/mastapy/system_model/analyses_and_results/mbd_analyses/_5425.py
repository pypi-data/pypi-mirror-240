"""CylindricalPlanetGearMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5423
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "CylindricalPlanetGearMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2524


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CylindricalPlanetGearMultibodyDynamicsAnalysis")


class CylindricalPlanetGearMultibodyDynamicsAnalysis(
    _5423.CylindricalGearMultibodyDynamicsAnalysis
):
    """CylindricalPlanetGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis"
    )

    class _Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis:
        """Special nested class for casting CylindricalPlanetGearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
            parent: "CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_multibody_dynamics_analysis(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5423.CylindricalGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5435

            return self._parent._cast(_5435.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5460

            return self._parent._cast(_5460.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400

            return self._parent._cast(_5400.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_multibody_dynamics_analysis(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
        ) -> "CylindricalPlanetGearMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "CylindricalPlanetGearMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2524.CylindricalPlanetGear":
        """mastapy.system_model.part_model.gears.CylindricalPlanetGear

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
    ) -> "CylindricalPlanetGearMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis":
        return self._Cast_CylindricalPlanetGearMultibodyDynamicsAnalysis(self)
