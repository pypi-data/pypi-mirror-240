"""KlingelnbergCycloPalloidConicalGearSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2723
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "KlingelnbergCycloPalloidConicalGearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533
    from mastapy.system_model.analyses_and_results.power_flows import _4098


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSystemDeflection",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearSystemDeflection")


class KlingelnbergCycloPalloidConicalGearSystemDeflection(
    _2723.ConicalGearSystemDeflection
):
    """KlingelnbergCycloPalloidConicalGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
            parent: "KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ):
            return self._parent._cast(_2723.ConicalGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2779,
            )

            return self._parent._cast(_2779.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2770,
            )

            return self._parent._cast(
                _2770.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2773,
            )

            return self._parent._cast(
                _2773.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ) -> "KlingelnbergCycloPalloidConicalGearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2533.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(
        self: Self,
    ) -> "_4098.KlingelnbergCycloPalloidConicalGearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidConicalGearPowerFlow

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
    ) -> "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection(self)
