"""PlanetaryGearSetMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5424
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "PlanetaryGearSetMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="PlanetaryGearSetMultibodyDynamicsAnalysis")


class PlanetaryGearSetMultibodyDynamicsAnalysis(
    _5424.CylindricalGearSetMultibodyDynamicsAnalysis
):
    """PlanetaryGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetMultibodyDynamicsAnalysis"
    )

    class _Cast_PlanetaryGearSetMultibodyDynamicsAnalysis:
        """Special nested class for casting PlanetaryGearSetMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
            parent: "PlanetaryGearSetMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_multibody_dynamics_analysis(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5424.CylindricalGearSetMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436

            return self._parent._cast(_5436.GearSetMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5485

            return self._parent._cast(
                _5485.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5372

            return self._parent._cast(_5372.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def planetary_gear_set_multibody_dynamics_analysis(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
        ) -> "PlanetaryGearSetMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2539.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

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
    ) -> "PlanetaryGearSetMultibodyDynamicsAnalysis._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis":
        return self._Cast_PlanetaryGearSetMultibodyDynamicsAnalysis(self)
