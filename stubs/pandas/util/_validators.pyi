import numpy as np
from pandas.core.dtypes.common import is_bool as is_bool, is_integer as is_integer
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Any, Iterable, Sequence, TypeVar, overload

BoolishT = TypeVar('BoolishT', bool, int)
BoolishNoneT = TypeVar('BoolishNoneT', bool, int, None)

def validate_args(fname, args, max_fname_arg_count, compat_args) -> None: ...
def validate_kwargs(fname, kwargs, compat_args) -> None: ...
def validate_args_and_kwargs(fname, args, kwargs, max_fname_arg_count, compat_args) -> None: ...
def validate_bool_kwarg(value: BoolishNoneT, arg_name, none_allowed: bool = ..., int_allowed: bool = ...) -> BoolishNoneT: ...
def validate_axis_style_args(data, args, kwargs, arg_name, method_name) -> dict[str, Any]: ...
def validate_fillna_kwargs(value, method, validate_scalar_dict_value: bool = ...): ...
def validate_percentile(q: Union[float, Iterable[float]]) -> np.ndarray: ...
@overload
def validate_ascending(ascending: BoolishT) -> BoolishT: ...
@overload
def validate_ascending(ascending: Sequence[BoolishT]) -> list[BoolishT]: ...
def validate_endpoints(closed: Union[str, None]) -> tuple[bool, bool]: ...
def validate_inclusive(inclusive: Union[str, None]) -> tuple[bool, bool]: ...
def validate_insert_loc(loc: int, length: int) -> int: ...
