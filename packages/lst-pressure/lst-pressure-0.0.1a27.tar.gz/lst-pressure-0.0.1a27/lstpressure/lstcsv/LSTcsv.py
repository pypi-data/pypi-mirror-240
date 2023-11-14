from __future__ import annotations
import pandas as pd
from pandas import DataFrame
from datetime import datetime
from typing import Optional, Union, List, Callable
from ..observation import Observation
from ..observable import Observable
from .helpers import calculate_observations, calculate_observables
from collections import defaultdict

now = datetime.now().strftime("%Y%m%d")


class LSTcsv:
    """
    Wrap the LSTCalendar/Observation API for use with SARAO OPT
    CSV downloads
    """

    def __init__(
        self,
        input_data: Union[DataFrame, str, List[List[str]]],
        input_filter: Optional[Callable[[List[List[str]]], bool]] = lambda _: True,
        observation_filter: Optional[Callable[[List[Observation]], bool]] = lambda _: True,
        calendar_start: Optional[Union[str, datetime]] = now,
        calendar_end: Optional[Union[str, datetime]] = None,
    ) -> None:
        self._input_data = input_data
        self._calendar_start = calendar_start
        self._calendar_end = calendar_end or calendar_start
        self._observation_filter = observation_filter

        # Process input based on its type
        if isinstance(input_data, str):
            # Input is a file path, read CSV and filter rows
            df = pd.read_csv(input_data)
        elif isinstance(input_data, list):
            # Input is a list of lists, the first list is treated as header
            header, *data = input_data
            df = pd.DataFrame(data, columns=header)
        elif isinstance(input_data, DataFrame):
            # Input is already a DataFrame, make a copy
            df = input_data.copy()
        else:
            raise TypeError(
                "Input must be a path to a CSV file, a DataFrame, or a list of lists (rows)."
            )

        # Apply the filter to the DataFrame
        self._df = df[df.apply(input_filter, axis=1)]

    @property
    def df(self) -> DataFrame:
        return self._df

    @property
    def input(self) -> Union[str, List[list[str]]]:
        return self._input

    @property
    def calendar_start(self) -> Union[str, datetime]:
        return self._calendar_start

    @property
    def calendar_end(self):
        return self._calendar_end

    @property
    def observation_filter(self) -> Callable[[List[Observation]], bool]:
        return self._observation_filter

    @property
    def observations(self) -> List[Observation]:
        """
        NOTE changing self.dataFrame after initiation could result in stale data
        """
        return calculate_observations(self)

    @property
    def observables(self) -> List[Observable]:
        return calculate_observables(self.calendar_start, self.calendar_end, self.observations)

    def write_to_csv(self, output: str) -> None:
        data = [o.to_tuple() for o in self.observables]

        # Use a defaultdict to group data by date
        grouped_data = defaultdict(list)
        for record in data:
            (
                id,
                date,
                constraint,
                lst_start,
                lst_end,
                utc_start,
                utc_end,
                duration,
                proposal_id,
            ) = record
            grouped_data[date].append(
                [id, constraint, duration, lst_start, lst_end, utc_start, utc_end, proposal_id]
            )

        # Create a list of dictionaries to construct the DataFrame
        data_list = [
            {
                "date": date,
                "id": id,
                "proposal_id": proposal_id,
                "constraint": constraint,
                "duration": duration,
                "lst_start": lst_start,
                "lst_end": lst_end,
                "utc_start": utc_start,
                "utc_end": utc_end,
            }
            for date, id_value in grouped_data.items()
            for id, constraint, duration, lst_start, lst_end, utc_start, utc_end, proposal_id in id_value
        ]

        # Construct the DataFrame
        df = pd.DataFrame(data_list)

        # Write dataFrame to CSV
        df.to_csv(output, sep=",", quotechar='"', quoting=1, index=False, encoding="utf-8")
