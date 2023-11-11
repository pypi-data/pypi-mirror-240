"""CouplingHalfSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2779
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CouplingHalfSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2581
    from mastapy.system_model.analyses_and_results.power_flows import _4067


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfSystemDeflection",)


Self = TypeVar("Self", bound="CouplingHalfSystemDeflection")


class CouplingHalfSystemDeflection(_2779.MountableComponentSystemDeflection):
    """CouplingHalfSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfSystemDeflection")

    class _Cast_CouplingHalfSystemDeflection:
        """Special nested class for casting CouplingHalfSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
            parent: "CouplingHalfSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ):
            return self._parent._cast(_2779.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_half_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2709,
            )

            return self._parent._cast(_2709.ClutchHalfSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.ConceptCouplingHalfSystemDeflection)

        @property
        def cvt_pulley_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.CVTPulleySystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(_2784.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def pulley_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(_2790.PulleySystemDeflection)

        @property
        def rolling_ring_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2796,
            )

            return self._parent._cast(_2796.RollingRingSystemDeflection)

        @property
        def spring_damper_half_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.SpringDamperHalfSystemDeflection)

        @property
        def synchroniser_half_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2818,
            )

            return self._parent._cast(_2818.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2819,
            )

            return self._parent._cast(_2819.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2820,
            )

            return self._parent._cast(_2820.SynchroniserSleeveSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2826,
            )

            return self._parent._cast(_2826.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2828,
            )

            return self._parent._cast(_2828.TorqueConverterTurbineSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
        ) -> "CouplingHalfSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2581.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4067.CouplingHalfPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.CouplingHalfPowerFlow

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
    ) -> "CouplingHalfSystemDeflection._Cast_CouplingHalfSystemDeflection":
        return self._Cast_CouplingHalfSystemDeflection(self)
