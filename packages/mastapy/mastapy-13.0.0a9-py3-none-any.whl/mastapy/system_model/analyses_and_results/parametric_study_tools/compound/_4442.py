"""AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4474,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
        "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4295


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",)


Self = TypeVar(
    "Self",
    bound="AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",
)


class AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool(
    _4474.ConnectionCompoundParametricStudyTool
):
    """AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = (
        _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",
            parent: "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def connection_compound_parametric_study_tool(
            self: "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",
        ):
            return self._parent._cast(_4474.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_parametric_study_tool(
            self: "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4463,
            )

            return self._parent._cast(
                _4463.CoaxialConnectionCompoundParametricStudyTool
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_parametric_study_tool(
            self: "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4483,
            )

            return self._parent._cast(
                _4483.CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_parametric_study_tool(
            self: "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4485,
            )

            return self._parent._cast(
                _4485.CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool
            )

        @property
        def planetary_connection_compound_parametric_study_tool(
            self: "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(
                _4522.PlanetaryConnectionCompoundParametricStudyTool
            )

        @property
        def shaft_to_mountable_component_connection_compound_parametric_study_tool(
            self: "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4536,
            )

            return self._parent._cast(
                _4536.ShaftToMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_parametric_study_tool(
            self: "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",
        ) -> "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4295.AbstractShaftToMountableComponentConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.AbstractShaftToMountableComponentConnectionParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4295.AbstractShaftToMountableComponentConnectionParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.AbstractShaftToMountableComponentConnectionParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool._Cast_AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool":
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool(
            self
        )
