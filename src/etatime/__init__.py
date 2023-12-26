"""A library for tracking, computing, and formatting time estimates."""

__version__ = "2.7.10"

from . import eta, time, completion, constants, validate

from .eta import Eta, EtaCalculator, eta_calculator, eta_bar
from .time import (
    SplitTime, TimeString,
    split_seconds, day_of_month_suffix, day_of_month_string, timezone_name
)
from .completion import progress_char, Completion
from .constants import EtaDefaults, TimeDefaults, CompletionDefaults
from .validate import ValidationError, Validate

# TODO: Finish adding docstrings and function annotations
# TODO: Add doctest strings
# TODO: Investigate not validating parameters, see what breaks and how (we have annotations)
# TODO: Add comprehensive unit tests
# TODO: Investigate if inlining instance attributes helps with speed
