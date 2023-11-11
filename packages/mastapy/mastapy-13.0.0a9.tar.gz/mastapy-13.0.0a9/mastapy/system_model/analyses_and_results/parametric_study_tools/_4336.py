"""CycloidalDiscCentralBearingConnectionParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4316
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CycloidalDiscCentralBearingConnectionParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2332


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionParametricStudyTool",)


Self = TypeVar("Self", bound="CycloidalDiscCentralBearingConnectionParametricStudyTool")


class CycloidalDiscCentralBearingConnectionParametricStudyTool(
    _4316.CoaxialConnectionParametricStudyTool
):
    """CycloidalDiscCentralBearingConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionParametricStudyTool",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionParametricStudyTool:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionParametricStudyTool to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionParametricStudyTool",
            parent: "CycloidalDiscCentralBearingConnectionParametricStudyTool",
        ):
            self._parent = parent

        @property
        def coaxial_connection_parametric_study_tool(
            self: "CycloidalDiscCentralBearingConnectionParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionParametricStudyTool",
        ):
            return self._parent._cast(_4316.CoaxialConnectionParametricStudyTool)

        @property
        def shaft_to_mountable_component_connection_parametric_study_tool(
            self: "CycloidalDiscCentralBearingConnectionParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4407,
            )

            return self._parent._cast(
                _4407.ShaftToMountableComponentConnectionParametricStudyTool
            )

        @property
        def abstract_shaft_to_mountable_component_connection_parametric_study_tool(
            self: "CycloidalDiscCentralBearingConnectionParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4295,
            )

            return self._parent._cast(
                _4295.AbstractShaftToMountableComponentConnectionParametricStudyTool
            )

        @property
        def connection_parametric_study_tool(
            self: "CycloidalDiscCentralBearingConnectionParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4327,
            )

            return self._parent._cast(_4327.ConnectionParametricStudyTool)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscCentralBearingConnectionParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscCentralBearingConnectionParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_parametric_study_tool(
            self: "CycloidalDiscCentralBearingConnectionParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionParametricStudyTool",
        ) -> "CycloidalDiscCentralBearingConnectionParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionParametricStudyTool",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2332.CycloidalDiscCentralBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscCentralBearingConnectionParametricStudyTool._Cast_CycloidalDiscCentralBearingConnectionParametricStudyTool":
        return self._Cast_CycloidalDiscCentralBearingConnectionParametricStudyTool(self)
