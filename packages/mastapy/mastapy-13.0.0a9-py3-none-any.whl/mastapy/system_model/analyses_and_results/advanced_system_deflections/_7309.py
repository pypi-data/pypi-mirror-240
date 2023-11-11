"""CouplingHalfAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7349
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "CouplingHalfAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2581


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CouplingHalfAdvancedSystemDeflection")


class CouplingHalfAdvancedSystemDeflection(
    _7349.MountableComponentAdvancedSystemDeflection
):
    """CouplingHalfAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfAdvancedSystemDeflection")

    class _Cast_CouplingHalfAdvancedSystemDeflection:
        """Special nested class for casting CouplingHalfAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
            parent: "CouplingHalfAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7349.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7294,
            )

            return self._parent._cast(_7294.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(_7351.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_half_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7292,
            )

            return self._parent._cast(_7292.ClutchHalfAdvancedSystemDeflection)

        @property
        def concept_coupling_half_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7297,
            )

            return self._parent._cast(_7297.ConceptCouplingHalfAdvancedSystemDeflection)

        @property
        def cvt_pulley_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7312,
            )

            return self._parent._cast(_7312.CVTPulleyAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(
                _7354.PartToPartShearCouplingHalfAdvancedSystemDeflection
            )

        @property
        def pulley_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7360,
            )

            return self._parent._cast(_7360.PulleyAdvancedSystemDeflection)

        @property
        def rolling_ring_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(_7363.RollingRingAdvancedSystemDeflection)

        @property
        def spring_damper_half_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7376,
            )

            return self._parent._cast(_7376.SpringDamperHalfAdvancedSystemDeflection)

        @property
        def synchroniser_half_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7386,
            )

            return self._parent._cast(_7386.SynchroniserHalfAdvancedSystemDeflection)

        @property
        def synchroniser_part_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7387,
            )

            return self._parent._cast(_7387.SynchroniserPartAdvancedSystemDeflection)

        @property
        def synchroniser_sleeve_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7388,
            )

            return self._parent._cast(_7388.SynchroniserSleeveAdvancedSystemDeflection)

        @property
        def torque_converter_pump_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7391,
            )

            return self._parent._cast(_7391.TorqueConverterPumpAdvancedSystemDeflection)

        @property
        def torque_converter_turbine_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7392,
            )

            return self._parent._cast(
                _7392.TorqueConverterTurbineAdvancedSystemDeflection
            )

        @property
        def coupling_half_advanced_system_deflection(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
        ) -> "CouplingHalfAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "CouplingHalfAdvancedSystemDeflection.TYPE"
    ):
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
    def cast_to(
        self: Self,
    ) -> "CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection":
        return self._Cast_CouplingHalfAdvancedSystemDeflection(self)
