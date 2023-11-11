"""CouplingConnectionSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2764
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CouplingConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2343
    from mastapy.system_model.analyses_and_results.power_flows import _4066


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionSystemDeflection",)


Self = TypeVar("Self", bound="CouplingConnectionSystemDeflection")


class CouplingConnectionSystemDeflection(
    _2764.InterMountableComponentConnectionSystemDeflection
):
    """CouplingConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingConnectionSystemDeflection")

    class _Cast_CouplingConnectionSystemDeflection:
        """Special nested class for casting CouplingConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
            parent: "CouplingConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            return self._parent._cast(
                _2764.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2708,
            )

            return self._parent._cast(_2708.ClutchConnectionSystemDeflection)

        @property
        def concept_coupling_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2714,
            )

            return self._parent._cast(_2714.ConceptCouplingConnectionSystemDeflection)

        @property
        def part_to_part_shear_coupling_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2783,
            )

            return self._parent._cast(
                _2783.PartToPartShearCouplingConnectionSystemDeflection
            )

        @property
        def spring_damper_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2807,
            )

            return self._parent._cast(_2807.SpringDamperConnectionSystemDeflection)

        @property
        def torque_converter_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2825,
            )

            return self._parent._cast(_2825.TorqueConverterConnectionSystemDeflection)

        @property
        def coupling_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ) -> "CouplingConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
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
        self: Self, instance_to_wrap: "CouplingConnectionSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2343.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4066.CouplingConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.CouplingConnectionPowerFlow

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
    ) -> "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection":
        return self._Cast_CouplingConnectionSystemDeflection(self)
