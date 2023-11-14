"""
lstpressure.lstcalendar
"""
from __future__ import annotations  # Not required from python 3.11 onwards
from datetime import datetime
from intervaltree import Interval
from .LSTIntervalType import LSTIntervalType
from ..lstcalendar import Sun, LSTCalendarDate
from ..observation import Observation
from typing import Union, Optional
from ..utils import normalize_yyyymmdd_to_datetime


def normalize_interval(start, end, days=1):
    if end < start:
        end += 24
    end += 24 * (days - 1)
    return (start, end)


class LSTInterval:
    """
    A wrapper around the intervaltree Interval class
    for easer access in the context of lst-pressure
    """

    def __init__(
        self,
        start: float,
        end: float,
        start_utc: Union[datetime, float],
        end_utc: Union[datetime, float],
        parent: Optional[Union[LSTCalendarDate, Observation]] = None,
        dt: Optional[datetime] = None,
        type: Optional[LSTIntervalType] = None,
        sun: Optional[Sun] = None,
        tomorrow_sun: Optional[Sun] = None,
    ) -> None:
        self._type = type if type else None
        self._dt = normalize_yyyymmdd_to_datetime(dt) if dt else None
        self._sun = sun if sun else None
        self._tomorrow_sun = tomorrow_sun if tomorrow_sun else None
        self._parent = parent if parent else None
        self._interval = Interval(start, end, self)
        self._start_utc = start_utc
        self._end_utc = end_utc

    @property
    def parent(self):
        return self._parent

    @property
    def interval(self):
        return self._interval

    @property
    def start(self):
        return self._interval[0]

    @property
    def start_utc(self):
        return self._start_utc

    @property
    def end(self):
        return self._interval[1]

    @property
    def end_utc(self):
        return self._end_utc

    @property
    def type(self):
        return self._type

    @property
    def dt(self):
        return self._dt

    @property
    def sun(self):
        return self._sun

    @property
    def tomorrow_sun(self):
        return self._tomorrow_sun
