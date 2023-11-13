"""
lstcalendar.LSTInterval
"""

from enum import Enum, auto


class LSTIntervalType(Enum):
    ALL_DAY = auto()
    NIGHT = auto()
    OBSERVATION_WINDOW = auto()
    SUNRISE_SUNSET = auto()
    SUNSET_SUNRISE = auto()
