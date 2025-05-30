import numpy as np
from pandas._libs.tslibs import parsing as parsing
from pandas._typing import npt as npt
from pandas.util._exceptions import find_stack_level as find_stack_level

def parse_date_time(date_col, time_col) -> npt.NDArray[np.object_]: ...
def parse_date_fields(year_col, month_col, day_col) -> npt.NDArray[np.object_]: ...
def parse_all_fields(year_col, month_col, day_col, hour_col, minute_col, second_col) -> npt.NDArray[np.object_]: ...
def generic_parser(parse_func, *cols) -> np.ndarray: ...
