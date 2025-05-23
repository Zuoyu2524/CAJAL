import numpy as np
from _typeshed import Incomplete
from pandas import Float64Index as Float64Index, Index as Index
from pandas._libs import Timestamp as Timestamp, internals as libinternals, lib as lib, writers as writers
from pandas._libs.internals import BlockPlacement as BlockPlacement
from pandas._libs.tslibs import IncompatibleFrequency as IncompatibleFrequency
from pandas._typing import ArrayLike as ArrayLike, DtypeObj as DtypeObj, F as F, IgnoreRaise as IgnoreRaise, Shape as Shape, npt as npt
from pandas.core.array_algos.putmask import extract_bool_array as extract_bool_array, putmask_inplace as putmask_inplace, putmask_without_repeat as putmask_without_repeat, setitem_datetimelike_compat as setitem_datetimelike_compat, validate_putmask as validate_putmask
from pandas.core.array_algos.quantile import quantile_compat as quantile_compat
from pandas.core.array_algos.replace import compare_or_regex_search as compare_or_regex_search, replace_regex as replace_regex, should_use_regex as should_use_regex
from pandas.core.array_algos.transforms import shift as shift
from pandas.core.arrays import Categorical as Categorical, DatetimeArray as DatetimeArray, ExtensionArray as ExtensionArray, IntervalArray as IntervalArray, PandasArray as PandasArray, PeriodArray as PeriodArray, TimedeltaArray as TimedeltaArray
from pandas.core.arrays._mixins import NDArrayBackedExtensionArray as NDArrayBackedExtensionArray
from pandas.core.arrays.sparse import SparseDtype as SparseDtype
from pandas.core.base import PandasObject as PandasObject
from pandas.core.construction import ensure_wrapped_if_datetimelike as ensure_wrapped_if_datetimelike, extract_array as extract_array
from pandas.core.dtypes.astype import astype_array_safe as astype_array_safe
from pandas.core.dtypes.cast import LossySetitemError as LossySetitemError, can_hold_element as can_hold_element, find_result_type as find_result_type, maybe_downcast_to_dtype as maybe_downcast_to_dtype, np_can_hold_element as np_can_hold_element, soft_convert_objects as soft_convert_objects
from pandas.core.dtypes.common import ensure_platform_int as ensure_platform_int, is_1d_only_ea_dtype as is_1d_only_ea_dtype, is_1d_only_ea_obj as is_1d_only_ea_obj, is_dtype_equal as is_dtype_equal, is_interval_dtype as is_interval_dtype, is_list_like as is_list_like, is_sparse as is_sparse, is_string_dtype as is_string_dtype
from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype, ExtensionDtype as ExtensionDtype, PandasDtype as PandasDtype, PeriodDtype as PeriodDtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCIndex as ABCIndex, ABCPandasArray as ABCPandasArray, ABCSeries as ABCSeries
from pandas.core.dtypes.inference import is_inferred_bool_dtype as is_inferred_bool_dtype
from pandas.core.dtypes.missing import is_valid_na_for_dtype as is_valid_na_for_dtype, isna as isna, na_value_for_dtype as na_value_for_dtype
from pandas.core.indexers import check_setitem_lengths as check_setitem_lengths
from pandas.errors import AbstractMethodError as AbstractMethodError
from pandas.util._decorators import cache_readonly as cache_readonly
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util._validators import validate_bool_kwarg as validate_bool_kwarg
from typing import Any, Callable, Iterable, Sequence

def maybe_split(meth: F) -> F: ...

class Block(PandasObject):
    values: Union[np.ndarray, ExtensionArray]
    ndim: int
    __init__: Callable
    is_numeric: bool
    is_object: bool
    is_extension: bool
    def is_categorical(self) -> bool: ...
    @property
    def is_bool(self) -> bool: ...
    def external_values(self): ...
    def fill_value(self): ...
    @property
    def mgr_locs(self) -> BlockPlacement: ...
    @mgr_locs.setter
    def mgr_locs(self, new_mgr_locs: BlockPlacement) -> None: ...
    def make_block(self, values, placement: Incomplete | None = ...) -> Block: ...
    def make_block_same_class(self, values, placement: Union[BlockPlacement, None] = ...) -> Block: ...
    def __len__(self) -> int: ...
    def getitem_block(self, slicer: Union[slice, npt.NDArray[np.intp]]) -> Block: ...
    def getitem_block_columns(self, slicer: slice, new_mgr_locs: BlockPlacement) -> Block: ...
    def should_store(self, value: ArrayLike) -> bool: ...
    def apply(self, func, **kwargs) -> list[Block]: ...
    def reduce(self, func, ignore_failures: bool = ...) -> list[Block]: ...
    def split_and_operate(self, func, *args, **kwargs) -> list[Block]: ...
    def coerce_to_target_dtype(self, other) -> Block: ...
    def convert(self, copy: bool = ..., datetime: bool = ..., numeric: bool = ..., timedelta: bool = ...) -> list[Block]: ...
    def dtype(self) -> DtypeObj: ...
    def astype(self, dtype: DtypeObj, copy: bool = ..., errors: IgnoreRaise = ...) -> Block: ...
    def to_native_types(self, na_rep: str = ..., quoting: Incomplete | None = ..., **kwargs) -> Block: ...
    def copy(self, deep: bool = ...) -> Block: ...
    def replace(self, to_replace, value, inplace: bool = ..., mask: Union[npt.NDArray[np.bool_], None] = ...) -> list[Block]: ...
    def replace_list(self, src_list: Iterable[Any], dest_list: Sequence[Any], inplace: bool = ..., regex: bool = ...) -> list[Block]: ...
    @property
    def shape(self) -> Shape: ...
    def iget(self, i: Union[int, tuple[int, int], tuple[slice, int]]) -> np.ndarray: ...
    def set_inplace(self, locs, values: ArrayLike, copy: bool = ...) -> None: ...
    def take_nd(self, indexer: npt.NDArray[np.intp], axis: int, new_mgr_locs: Union[BlockPlacement, None] = ..., fill_value=...) -> Block: ...
    def setitem(self, indexer, value) -> Block: ...
    def putmask(self, mask, new) -> list[Block]: ...
    def where(self, other, cond, _downcast: str = ...) -> list[Block]: ...
    def fillna(self, value, limit: Union[int, None] = ..., inplace: bool = ..., downcast: Incomplete | None = ...) -> list[Block]: ...
    def interpolate(self, method: str = ..., axis: int = ..., index: Union[Index, None] = ..., inplace: bool = ..., limit: Union[int, None] = ..., limit_direction: str = ..., limit_area: Union[str, None] = ..., fill_value: Union[Any, None] = ..., downcast: Union[str, None] = ..., **kwargs) -> list[Block]: ...
    def diff(self, n: int, axis: int = ...) -> list[Block]: ...
    def shift(self, periods: int, axis: int = ..., fill_value: Any = ...) -> list[Block]: ...
    def quantile(self, qs: Float64Index, interpolation: str = ..., axis: int = ...) -> Block: ...
    def delete(self, loc) -> Block: ...
    @property
    def is_view(self) -> bool: ...
    @property
    def array_values(self) -> ExtensionArray: ...
    def get_values(self, dtype: Union[DtypeObj, None] = ...) -> np.ndarray: ...
    def values_for_json(self) -> np.ndarray: ...

class EABackedBlock(Block):
    values: ExtensionArray
    def setitem(self, indexer, value): ...
    def where(self, other, cond, _downcast: str = ...) -> list[Block]: ...
    def putmask(self, mask, new) -> list[Block]: ...
    def fillna(self, value, limit: Union[int, None] = ..., inplace: bool = ..., downcast: Incomplete | None = ...) -> list[Block]: ...
    def delete(self, loc) -> Block: ...
    def array_values(self) -> ExtensionArray: ...
    def get_values(self, dtype: Union[DtypeObj, None] = ...) -> np.ndarray: ...
    def values_for_json(self) -> np.ndarray: ...
    def interpolate(self, method: str = ..., axis: int = ..., inplace: bool = ..., limit: Incomplete | None = ..., fill_value: Incomplete | None = ..., **kwargs): ...

class ExtensionBlock(libinternals.Block, EABackedBlock):
    is_extension: bool
    values: ExtensionArray
    def shape(self) -> Shape: ...
    def iget(self, i: Union[int, tuple[int, int], tuple[slice, int]]): ...
    def set_inplace(self, locs, values: ArrayLike, copy: bool = ...) -> None: ...
    @property
    def is_view(self) -> bool: ...
    def is_numeric(self): ...
    def take_nd(self, indexer: npt.NDArray[np.intp], axis: int = ..., new_mgr_locs: Union[BlockPlacement, None] = ..., fill_value=...) -> Block: ...
    def getitem_block_index(self, slicer: slice) -> ExtensionBlock: ...
    def diff(self, n: int, axis: int = ...) -> list[Block]: ...
    def shift(self, periods: int, axis: int = ..., fill_value: Any = ...) -> list[Block]: ...

class NumpyBlock(libinternals.NumpyBlock, Block):
    values: np.ndarray
    @property
    def is_view(self) -> bool: ...
    @property
    def array_values(self) -> ExtensionArray: ...
    def get_values(self, dtype: Union[DtypeObj, None] = ...) -> np.ndarray: ...
    def values_for_json(self) -> np.ndarray: ...
    def delete(self, loc) -> Block: ...

class NumericBlock(NumpyBlock):
    is_numeric: bool

class NDArrayBackedExtensionBlock(libinternals.NDArrayBackedBlock, EABackedBlock):
    values: NDArrayBackedExtensionArray
    def is_extension(self) -> bool: ...
    @property
    def is_view(self) -> bool: ...
    def diff(self, n: int, axis: int = ...) -> list[Block]: ...
    def shift(self, periods: int, axis: int = ..., fill_value: Any = ...) -> list[Block]: ...

class DatetimeLikeBlock(NDArrayBackedExtensionBlock):
    is_numeric: bool
    values: Union[DatetimeArray, TimedeltaArray]
    def values_for_json(self) -> np.ndarray: ...

class DatetimeTZBlock(DatetimeLikeBlock):
    values: DatetimeArray
    is_extension: bool
    values_for_json: Incomplete

class ObjectBlock(NumpyBlock):
    is_object: bool
    def reduce(self, func, ignore_failures: bool = ...) -> list[Block]: ...
    def convert(self, copy: bool = ..., datetime: bool = ..., numeric: bool = ..., timedelta: bool = ...) -> list[Block]: ...

class CategoricalBlock(ExtensionBlock):
    @property
    def dtype(self) -> DtypeObj: ...

def maybe_coerce_values(values: ArrayLike) -> ArrayLike: ...
def get_block_type(dtype: DtypeObj): ...
def new_block_2d(values: ArrayLike, placement: BlockPlacement): ...
def new_block(values, placement, *, ndim: int) -> Block: ...
def check_ndim(values, placement: BlockPlacement, ndim: int) -> None: ...
def extract_pandas_array(values: Union[np.ndarray, ExtensionArray], dtype: Union[DtypeObj, None], ndim: int) -> tuple[Union[np.ndarray, ExtensionArray], Union[DtypeObj, None]]: ...
def extend_blocks(result, blocks: Incomplete | None = ...) -> list[Block]: ...
def ensure_block_shape(values: ArrayLike, ndim: int = ...) -> ArrayLike: ...
def to_native_types(values: ArrayLike, *, na_rep: str = ..., quoting: Incomplete | None = ..., float_format: Incomplete | None = ..., decimal: str = ..., **kwargs) -> np.ndarray: ...
def external_values(values: ArrayLike) -> ArrayLike: ...
