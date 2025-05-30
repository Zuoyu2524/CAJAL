import numpy as np
from _typeshed import Incomplete
from pandas import Float64Index as Float64Index
from pandas._libs import NaT as NaT, lib as lib
from pandas._typing import ArrayLike as ArrayLike, DtypeObj as DtypeObj, npt as npt
from pandas.core.array_algos.quantile import quantile_compat as quantile_compat
from pandas.core.array_algos.take import take_1d as take_1d
from pandas.core.arrays import DatetimeArray as DatetimeArray, ExtensionArray as ExtensionArray, PandasArray as PandasArray, TimedeltaArray as TimedeltaArray
from pandas.core.arrays.sparse import SparseDtype as SparseDtype
from pandas.core.construction import ensure_wrapped_if_datetimelike as ensure_wrapped_if_datetimelike, extract_array as extract_array, sanitize_array as sanitize_array
from pandas.core.dtypes.astype import astype_array_safe as astype_array_safe
from pandas.core.dtypes.cast import ensure_dtype_can_hold_na as ensure_dtype_can_hold_na, infer_dtype_from_scalar as infer_dtype_from_scalar, soft_convert_objects as soft_convert_objects
from pandas.core.dtypes.common import ensure_platform_int as ensure_platform_int, is_datetime64_ns_dtype as is_datetime64_ns_dtype, is_dtype_equal as is_dtype_equal, is_extension_array_dtype as is_extension_array_dtype, is_integer as is_integer, is_numeric_dtype as is_numeric_dtype, is_object_dtype as is_object_dtype, is_timedelta64_ns_dtype as is_timedelta64_ns_dtype
from pandas.core.dtypes.dtypes import ExtensionDtype as ExtensionDtype, PandasDtype as PandasDtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.dtypes.inference import is_inferred_bool_dtype as is_inferred_bool_dtype
from pandas.core.dtypes.missing import array_equals as array_equals, isna as isna, na_value_for_dtype as na_value_for_dtype
from pandas.core.indexers import maybe_convert_indices as maybe_convert_indices, validate_indices as validate_indices
from pandas.core.indexes.api import Index as Index, ensure_index as ensure_index
from pandas.core.internals.base import DataManager as DataManager, SingleDataManager as SingleDataManager, interleaved_dtype as interleaved_dtype
from pandas.core.internals.blocks import ensure_block_shape as ensure_block_shape, external_values as external_values, extract_pandas_array as extract_pandas_array, maybe_coerce_values as maybe_coerce_values, new_block as new_block, to_native_types as to_native_types
from pandas.util._validators import validate_bool_kwarg as validate_bool_kwarg
from typing import Any, Callable, Hashable, Literal, TypeVar

T = TypeVar('T', bound='BaseArrayManager')

class BaseArrayManager(DataManager):
    arrays: list[Union[np.ndarray, ExtensionArray]]
    def __init__(self, arrays: list[Union[np.ndarray, ExtensionArray]], axes: list[Index], verify_integrity: bool = ...) -> None: ...
    def make_empty(self, axes: Incomplete | None = ...) -> T: ...
    @property
    def items(self) -> Index: ...
    @property
    def axes(self) -> list[Index]: ...
    @property
    def shape_proper(self) -> tuple[int, ...]: ...
    def set_axis(self, axis: int, new_labels: Index) -> None: ...
    def get_dtypes(self) -> np.ndarray: ...
    def apply(self, f, align_keys: Union[list[str], None] = ..., ignore_failures: bool = ..., **kwargs) -> T: ...
    def apply_with_block(self, f, align_keys: Incomplete | None = ..., swap_axis: bool = ..., **kwargs) -> T: ...
    def where(self, other, cond, align: bool) -> T: ...
    def setitem(self, indexer, value) -> T: ...
    def putmask(self, mask, new, align: bool = ...) -> T: ...
    def diff(self, n: int, axis: int) -> T: ...
    def interpolate(self, **kwargs) -> T: ...
    def shift(self, periods: int, axis: int, fill_value) -> T: ...
    def fillna(self, value, limit, inplace: bool, downcast) -> T: ...
    def astype(self, dtype, copy: bool = ..., errors: str = ...) -> T: ...
    def convert(self, copy: bool = ..., datetime: bool = ..., numeric: bool = ..., timedelta: bool = ...) -> T: ...
    def replace_regex(self, **kwargs) -> T: ...
    def replace(self, to_replace, value, inplace: bool) -> T: ...
    def replace_list(self, src_list: list[Any], dest_list: list[Any], inplace: bool = ..., regex: bool = ...) -> T: ...
    def to_native_types(self, **kwargs) -> T: ...
    @property
    def is_mixed_type(self) -> bool: ...
    @property
    def is_numeric_mixed_type(self) -> bool: ...
    @property
    def any_extension_types(self) -> bool: ...
    @property
    def is_view(self) -> bool: ...
    @property
    def is_single_block(self) -> bool: ...
    def get_bool_data(self, copy: bool = ...) -> T: ...
    def get_numeric_data(self, copy: bool = ...) -> T: ...
    def copy(self, deep: bool = ...) -> T: ...
    def reindex_indexer(self, new_axis, indexer, axis: int, fill_value: Incomplete | None = ..., allow_dups: bool = ..., copy: bool = ..., only_slice: bool = ..., use_na_proxy: bool = ...) -> T: ...
    def take(self, indexer, axis: int = ..., verify: bool = ..., convert_indices: bool = ...) -> T: ...

class ArrayManager(BaseArrayManager):
    @property
    def ndim(self) -> Literal[2]: ...
    arrays: Incomplete
    def __init__(self, arrays: list[Union[np.ndarray, ExtensionArray]], axes: list[Index], verify_integrity: bool = ...) -> None: ...
    def fast_xs(self, loc: int) -> SingleArrayManager: ...
    def get_slice(self, slobj: slice, axis: int = ...) -> ArrayManager: ...
    def iget(self, i: int) -> SingleArrayManager: ...
    def iget_values(self, i: int) -> ArrayLike: ...
    @property
    def column_arrays(self) -> list[ArrayLike]: ...
    def iset(self, loc: Union[int, slice, np.ndarray], value: ArrayLike, inplace: bool = ...) -> None: ...
    def column_setitem(self, loc: int, idx: Union[int, slice, np.ndarray], value) -> None: ...
    def insert(self, loc: int, item: Hashable, value: ArrayLike) -> None: ...
    def idelete(self, indexer) -> ArrayManager: ...
    def grouped_reduce(self, func: Callable, ignore_failures: bool = ...) -> T: ...
    def reduce(self, func: Callable, ignore_failures: bool = ...) -> tuple[T, np.ndarray]: ...
    def operate_blockwise(self, other: ArrayManager, array_op) -> ArrayManager: ...
    def quantile(self, *, qs: Float64Index, axis: int = ..., transposed: bool = ..., interpolation: str = ...) -> ArrayManager: ...
    def unstack(self, unstacker, fill_value) -> ArrayManager: ...
    def as_array(self, dtype: Incomplete | None = ..., copy: bool = ..., na_value: object = ...) -> np.ndarray: ...

class SingleArrayManager(BaseArrayManager, SingleDataManager):
    arrays: list[Union[np.ndarray, ExtensionArray]]
    @property
    def ndim(self) -> Literal[1]: ...
    def __init__(self, arrays: list[Union[np.ndarray, ExtensionArray]], axes: list[Index], verify_integrity: bool = ...) -> None: ...
    def make_empty(self, axes: Incomplete | None = ...) -> SingleArrayManager: ...
    @classmethod
    def from_array(cls, array, index) -> SingleArrayManager: ...
    @property
    def axes(self): ...
    @property
    def index(self) -> Index: ...
    @property
    def dtype(self): ...
    def external_values(self): ...
    def internal_values(self): ...
    def array_values(self): ...
    @property
    def is_single_block(self) -> bool: ...
    def fast_xs(self, loc: int) -> SingleArrayManager: ...
    def get_slice(self, slobj: slice, axis: int = ...) -> SingleArrayManager: ...
    def getitem_mgr(self, indexer) -> SingleArrayManager: ...
    def apply(self, func, **kwargs): ...
    def setitem(self, indexer, value) -> SingleArrayManager: ...
    def idelete(self, indexer) -> SingleArrayManager: ...
    def set_values(self, values: ArrayLike) -> None: ...
    def to_2d_mgr(self, columns: Index) -> ArrayManager: ...

class NullArrayProxy:
    ndim: int
    n: Incomplete
    def __init__(self, n: int) -> None: ...
    @property
    def shape(self) -> tuple[int]: ...
    def to_array(self, dtype: DtypeObj) -> ArrayLike: ...
