"""CylindricalPlanetGearSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2744
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CylindricalPlanetGearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2524
    from mastapy.system_model.analyses_and_results.power_flows import _4080


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearSystemDeflection",)


Self = TypeVar("Self", bound="CylindricalPlanetGearSystemDeflection")


class CylindricalPlanetGearSystemDeflection(
    _2744.CylindricalGearSystemDeflectionWithLTCAResults
):
    """CylindricalPlanetGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearSystemDeflection"
    )

    class _Cast_CylindricalPlanetGearSystemDeflection:
        """Special nested class for casting CylindricalPlanetGearSystemDeflection to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
            parent: "CylindricalPlanetGearSystemDeflection",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ):
            return self._parent._cast(
                _2744.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_gear_system_deflection(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2742,
            )

            return self._parent._cast(_2742.CylindricalGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2779,
            )

            return self._parent._cast(_2779.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
        ) -> "CylindricalPlanetGearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection",
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
        self: Self, instance_to_wrap: "CylindricalPlanetGearSystemDeflection.TYPE"
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
    def power_flow_results(self: Self) -> "_4080.CylindricalPlanetGearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.CylindricalPlanetGearPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalPlanetGearSystemDeflection._Cast_CylindricalPlanetGearSystemDeflection":
        return self._Cast_CylindricalPlanetGearSystemDeflection(self)
