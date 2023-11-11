"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2616 import CompoundAnalysis
    from ._2617 import SingleAnalysis
    from ._2618 import AdvancedSystemDeflectionAnalysis
    from ._2619 import AdvancedSystemDeflectionSubAnalysis
    from ._2620 import AdvancedTimeSteppingAnalysisForModulation
    from ._2621 import CompoundParametricStudyToolAnalysis
    from ._2622 import CriticalSpeedAnalysis
    from ._2623 import DynamicAnalysis
    from ._2624 import DynamicModelAtAStiffnessAnalysis
    from ._2625 import DynamicModelForHarmonicAnalysis
    from ._2626 import DynamicModelForModalAnalysis
    from ._2627 import DynamicModelForStabilityAnalysis
    from ._2628 import DynamicModelForSteadyStateSynchronousResponseAnalysis
    from ._2629 import HarmonicAnalysis
    from ._2630 import HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
    from ._2631 import HarmonicAnalysisOfSingleExcitationAnalysis
    from ._2632 import ModalAnalysis
    from ._2633 import ModalAnalysisAtASpeed
    from ._2634 import ModalAnalysisAtAStiffness
    from ._2635 import ModalAnalysisForHarmonicAnalysis
    from ._2636 import MultibodyDynamicsAnalysis
    from ._2637 import ParametricStudyToolAnalysis
    from ._2638 import PowerFlowAnalysis
    from ._2639 import StabilityAnalysis
    from ._2640 import SteadyStateSynchronousResponseAnalysis
    from ._2641 import SteadyStateSynchronousResponseAtASpeedAnalysis
    from ._2642 import SteadyStateSynchronousResponseOnAShaftAnalysis
    from ._2643 import SystemDeflectionAnalysis
    from ._2644 import TorsionalSystemDeflectionAnalysis
    from ._2645 import AnalysisCaseVariable
    from ._2646 import ConnectionAnalysis
    from ._2647 import Context
    from ._2648 import DesignEntityAnalysis
    from ._2649 import DesignEntityGroupAnalysis
    from ._2650 import DesignEntitySingleContextAnalysis
    from ._2654 import PartAnalysis
    from ._2655 import CompoundAdvancedSystemDeflectionAnalysis
    from ._2656 import CompoundAdvancedSystemDeflectionSubAnalysis
    from ._2657 import CompoundAdvancedTimeSteppingAnalysisForModulation
    from ._2658 import CompoundCriticalSpeedAnalysis
    from ._2659 import CompoundDynamicAnalysis
    from ._2660 import CompoundDynamicModelAtAStiffnessAnalysis
    from ._2661 import CompoundDynamicModelForHarmonicAnalysis
    from ._2662 import CompoundDynamicModelForModalAnalysis
    from ._2663 import CompoundDynamicModelForStabilityAnalysis
    from ._2664 import CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis
    from ._2665 import CompoundHarmonicAnalysis
    from ._2666 import (
        CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._2667 import CompoundHarmonicAnalysisOfSingleExcitationAnalysis
    from ._2668 import CompoundModalAnalysis
    from ._2669 import CompoundModalAnalysisAtASpeed
    from ._2670 import CompoundModalAnalysisAtAStiffness
    from ._2671 import CompoundModalAnalysisForHarmonicAnalysis
    from ._2672 import CompoundMultibodyDynamicsAnalysis
    from ._2673 import CompoundPowerFlowAnalysis
    from ._2674 import CompoundStabilityAnalysis
    from ._2675 import CompoundSteadyStateSynchronousResponseAnalysis
    from ._2676 import CompoundSteadyStateSynchronousResponseAtASpeedAnalysis
    from ._2677 import CompoundSteadyStateSynchronousResponseOnAShaftAnalysis
    from ._2678 import CompoundSystemDeflectionAnalysis
    from ._2679 import CompoundTorsionalSystemDeflectionAnalysis
    from ._2680 import TESetUpForDynamicAnalysisOptions
    from ._2681 import TimeOptions
else:
    import_structure = {
        "_2616": ["CompoundAnalysis"],
        "_2617": ["SingleAnalysis"],
        "_2618": ["AdvancedSystemDeflectionAnalysis"],
        "_2619": ["AdvancedSystemDeflectionSubAnalysis"],
        "_2620": ["AdvancedTimeSteppingAnalysisForModulation"],
        "_2621": ["CompoundParametricStudyToolAnalysis"],
        "_2622": ["CriticalSpeedAnalysis"],
        "_2623": ["DynamicAnalysis"],
        "_2624": ["DynamicModelAtAStiffnessAnalysis"],
        "_2625": ["DynamicModelForHarmonicAnalysis"],
        "_2626": ["DynamicModelForModalAnalysis"],
        "_2627": ["DynamicModelForStabilityAnalysis"],
        "_2628": ["DynamicModelForSteadyStateSynchronousResponseAnalysis"],
        "_2629": ["HarmonicAnalysis"],
        "_2630": ["HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"],
        "_2631": ["HarmonicAnalysisOfSingleExcitationAnalysis"],
        "_2632": ["ModalAnalysis"],
        "_2633": ["ModalAnalysisAtASpeed"],
        "_2634": ["ModalAnalysisAtAStiffness"],
        "_2635": ["ModalAnalysisForHarmonicAnalysis"],
        "_2636": ["MultibodyDynamicsAnalysis"],
        "_2637": ["ParametricStudyToolAnalysis"],
        "_2638": ["PowerFlowAnalysis"],
        "_2639": ["StabilityAnalysis"],
        "_2640": ["SteadyStateSynchronousResponseAnalysis"],
        "_2641": ["SteadyStateSynchronousResponseAtASpeedAnalysis"],
        "_2642": ["SteadyStateSynchronousResponseOnAShaftAnalysis"],
        "_2643": ["SystemDeflectionAnalysis"],
        "_2644": ["TorsionalSystemDeflectionAnalysis"],
        "_2645": ["AnalysisCaseVariable"],
        "_2646": ["ConnectionAnalysis"],
        "_2647": ["Context"],
        "_2648": ["DesignEntityAnalysis"],
        "_2649": ["DesignEntityGroupAnalysis"],
        "_2650": ["DesignEntitySingleContextAnalysis"],
        "_2654": ["PartAnalysis"],
        "_2655": ["CompoundAdvancedSystemDeflectionAnalysis"],
        "_2656": ["CompoundAdvancedSystemDeflectionSubAnalysis"],
        "_2657": ["CompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_2658": ["CompoundCriticalSpeedAnalysis"],
        "_2659": ["CompoundDynamicAnalysis"],
        "_2660": ["CompoundDynamicModelAtAStiffnessAnalysis"],
        "_2661": ["CompoundDynamicModelForHarmonicAnalysis"],
        "_2662": ["CompoundDynamicModelForModalAnalysis"],
        "_2663": ["CompoundDynamicModelForStabilityAnalysis"],
        "_2664": ["CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis"],
        "_2665": ["CompoundHarmonicAnalysis"],
        "_2666": [
            "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_2667": ["CompoundHarmonicAnalysisOfSingleExcitationAnalysis"],
        "_2668": ["CompoundModalAnalysis"],
        "_2669": ["CompoundModalAnalysisAtASpeed"],
        "_2670": ["CompoundModalAnalysisAtAStiffness"],
        "_2671": ["CompoundModalAnalysisForHarmonicAnalysis"],
        "_2672": ["CompoundMultibodyDynamicsAnalysis"],
        "_2673": ["CompoundPowerFlowAnalysis"],
        "_2674": ["CompoundStabilityAnalysis"],
        "_2675": ["CompoundSteadyStateSynchronousResponseAnalysis"],
        "_2676": ["CompoundSteadyStateSynchronousResponseAtASpeedAnalysis"],
        "_2677": ["CompoundSteadyStateSynchronousResponseOnAShaftAnalysis"],
        "_2678": ["CompoundSystemDeflectionAnalysis"],
        "_2679": ["CompoundTorsionalSystemDeflectionAnalysis"],
        "_2680": ["TESetUpForDynamicAnalysisOptions"],
        "_2681": ["TimeOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CompoundAnalysis",
    "SingleAnalysis",
    "AdvancedSystemDeflectionAnalysis",
    "AdvancedSystemDeflectionSubAnalysis",
    "AdvancedTimeSteppingAnalysisForModulation",
    "CompoundParametricStudyToolAnalysis",
    "CriticalSpeedAnalysis",
    "DynamicAnalysis",
    "DynamicModelAtAStiffnessAnalysis",
    "DynamicModelForHarmonicAnalysis",
    "DynamicModelForModalAnalysis",
    "DynamicModelForStabilityAnalysis",
    "DynamicModelForSteadyStateSynchronousResponseAnalysis",
    "HarmonicAnalysis",
    "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    "HarmonicAnalysisOfSingleExcitationAnalysis",
    "ModalAnalysis",
    "ModalAnalysisAtASpeed",
    "ModalAnalysisAtAStiffness",
    "ModalAnalysisForHarmonicAnalysis",
    "MultibodyDynamicsAnalysis",
    "ParametricStudyToolAnalysis",
    "PowerFlowAnalysis",
    "StabilityAnalysis",
    "SteadyStateSynchronousResponseAnalysis",
    "SteadyStateSynchronousResponseAtASpeedAnalysis",
    "SteadyStateSynchronousResponseOnAShaftAnalysis",
    "SystemDeflectionAnalysis",
    "TorsionalSystemDeflectionAnalysis",
    "AnalysisCaseVariable",
    "ConnectionAnalysis",
    "Context",
    "DesignEntityAnalysis",
    "DesignEntityGroupAnalysis",
    "DesignEntitySingleContextAnalysis",
    "PartAnalysis",
    "CompoundAdvancedSystemDeflectionAnalysis",
    "CompoundAdvancedSystemDeflectionSubAnalysis",
    "CompoundAdvancedTimeSteppingAnalysisForModulation",
    "CompoundCriticalSpeedAnalysis",
    "CompoundDynamicAnalysis",
    "CompoundDynamicModelAtAStiffnessAnalysis",
    "CompoundDynamicModelForHarmonicAnalysis",
    "CompoundDynamicModelForModalAnalysis",
    "CompoundDynamicModelForStabilityAnalysis",
    "CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis",
    "CompoundHarmonicAnalysis",
    "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    "CompoundHarmonicAnalysisOfSingleExcitationAnalysis",
    "CompoundModalAnalysis",
    "CompoundModalAnalysisAtASpeed",
    "CompoundModalAnalysisAtAStiffness",
    "CompoundModalAnalysisForHarmonicAnalysis",
    "CompoundMultibodyDynamicsAnalysis",
    "CompoundPowerFlowAnalysis",
    "CompoundStabilityAnalysis",
    "CompoundSteadyStateSynchronousResponseAnalysis",
    "CompoundSteadyStateSynchronousResponseAtASpeedAnalysis",
    "CompoundSteadyStateSynchronousResponseOnAShaftAnalysis",
    "CompoundSystemDeflectionAnalysis",
    "CompoundTorsionalSystemDeflectionAnalysis",
    "TESetUpForDynamicAnalysisOptions",
    "TimeOptions",
)
