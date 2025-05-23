import numpy as np
from _typeshed import Incomplete
from pandas import DataFrame as DataFrame, Index as Index, Series as Series
from pandas._config import get_option as get_option
from pandas._libs import NaT as NaT, lib as lib
from pandas._libs.arrays import NDArrayBacked as NDArrayBacked
from pandas._libs.lib import NoDefault as NoDefault, no_default as no_default
from pandas._typing import ArrayLike as ArrayLike, AstypeArg as AstypeArg, Dtype as Dtype, NpDtype as NpDtype, Ordered as Ordered, Shape as Shape, npt as npt, type_t as type_t
from pandas.core import arraylike as arraylike, ops as ops
from pandas.core.accessor import PandasDelegate as PandasDelegate, delegate_names as delegate_names
from pandas.core.algorithms import factorize as factorize, take_nd as take_nd, unique1d as unique1d
from pandas.core.arrays._mixins import NDArrayBackedExtensionArray as NDArrayBackedExtensionArray, ravel_compat as ravel_compat
from pandas.core.base import ExtensionArray as ExtensionArray, NoNewAttributesMixin as NoNewAttributesMixin, PandasObject as PandasObject
from pandas.core.construction import extract_array as extract_array, sanitize_array as sanitize_array
from pandas.core.dtypes.cast import coerce_indexer_dtype as coerce_indexer_dtype
from pandas.core.dtypes.common import ensure_int64 as ensure_int64, ensure_platform_int as ensure_platform_int, is_categorical_dtype as is_categorical_dtype, is_datetime64_dtype as is_datetime64_dtype, is_dict_like as is_dict_like, is_dtype_equal as is_dtype_equal, is_extension_array_dtype as is_extension_array_dtype, is_hashable as is_hashable, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_scalar as is_scalar, is_timedelta64_dtype as is_timedelta64_dtype, needs_i8_conversion as needs_i8_conversion, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype, ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.generic import ABCIndex as ABCIndex, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import is_valid_na_for_dtype as is_valid_na_for_dtype, isna as isna, notna as notna
from pandas.core.ops.common import unpack_zerodim_and_defer as unpack_zerodim_and_defer
from pandas.core.sorting import nargsort as nargsort
from pandas.core.strings.object_array import ObjectStringArrayMixin as ObjectStringArrayMixin
from pandas.io.formats import console as console
from pandas.util._decorators import deprecate_kwarg as deprecate_kwarg, deprecate_nonkeyword_arguments as deprecate_nonkeyword_arguments
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util._validators import validate_bool_kwarg as validate_bool_kwarg
from typing import Literal, TypeVar, overload

CategoricalT = TypeVar('CategoricalT', bound='Categorical')

def contains(cat, key, container) -> bool: ...

class Categorical(NDArrayBackedExtensionArray, PandasObject, ObjectStringArrayMixin):
    __array_priority__: int
    def __init__(self, values, categories: Incomplete | None = ..., ordered: Incomplete | None = ..., dtype: Union[Dtype, None] = ..., fastpath: bool = ..., copy: bool = ...) -> None: ...
    @property
    def dtype(self) -> CategoricalDtype: ...
    @overload
    def astype(self, dtype: npt.DTypeLike, copy: bool = ...) -> np.ndarray: ...
    @overload
    def astype(self, dtype: ExtensionDtype, copy: bool = ...) -> ExtensionArray: ...
    @overload
    def astype(self, dtype: AstypeArg, copy: bool = ...) -> ArrayLike: ...
    def to_list(self): ...
    @classmethod
    def from_codes(cls, codes, categories: Incomplete | None = ..., ordered: Incomplete | None = ..., dtype: Union[Dtype, None] = ...) -> Categorical: ...
    @property
    def categories(self) -> Index: ...
    @categories.setter
    def categories(self, categories) -> None: ...
    @property
    def ordered(self) -> Ordered: ...
    @property
    def codes(self) -> np.ndarray: ...
    @overload
    def set_ordered(self, value, *, inplace: Union[NoDefault, Literal[False]] = ...) -> Categorical: ...
    @overload
    def set_ordered(self, value, *, inplace: Literal[True]) -> None: ...
    @overload
    def set_ordered(self, value, *, inplace: bool) -> Union[Categorical, None]: ...
    @overload
    def as_ordered(self, *, inplace: Union[NoDefault, Literal[False]] = ...) -> Categorical: ...
    @overload
    def as_ordered(self, *, inplace: Literal[True]) -> None: ...
    @overload
    def as_unordered(self, *, inplace: Union[NoDefault, Literal[False]] = ...) -> Categorical: ...
    @overload
    def as_unordered(self, *, inplace: Literal[True]) -> None: ...
    def set_categories(self, new_categories, ordered: Incomplete | None = ..., rename: bool = ..., inplace=...): ...
    @overload
    def rename_categories(self, new_categories, *, inplace: Union[Literal[False], NoDefault] = ...) -> Categorical: ...
    @overload
    def rename_categories(self, new_categories, *, inplace: Literal[True]) -> None: ...
    def reorder_categories(self, new_categories, ordered: Incomplete | None = ..., inplace=...): ...
    @overload
    def add_categories(self, new_categories, *, inplace: Union[Literal[False], NoDefault] = ...) -> Categorical: ...
    @overload
    def add_categories(self, new_categories, *, inplace: Literal[True]) -> None: ...
    def remove_categories(self, removals, inplace=...): ...
    @overload
    def remove_unused_categories(self, *, inplace: Union[Literal[False], NoDefault] = ...) -> Categorical: ...
    @overload
    def remove_unused_categories(self, *, inplace: Literal[True]) -> None: ...
    def map(self, mapper): ...
    __eq__: Incomplete
    __ne__: Incomplete
    __lt__: Incomplete
    __gt__: Incomplete
    __le__: Incomplete
    __ge__: Incomplete
    def __array__(self, dtype: Union[NpDtype, None] = ...) -> np.ndarray: ...
    def __array_ufunc__(self, ufunc: np.ufunc, method: str, *inputs, **kwargs): ...
    @property
    def nbytes(self) -> int: ...
    def memory_usage(self, deep: bool = ...) -> int: ...
    def isna(self) -> np.ndarray: ...
    isnull: Incomplete
    def notna(self) -> np.ndarray: ...
    notnull: Incomplete
    def value_counts(self, dropna: bool = ...) -> Series: ...
    def check_for_ordered(self, op) -> None: ...
    def argsort(self, ascending: bool = ..., kind: str = ..., **kwargs): ...
    @overload
    def sort_values(self, *, inplace: Literal[False] = ..., ascending: bool = ..., na_position: str = ...) -> Categorical: ...
    @overload
    def sort_values(self, *, inplace: Literal[True], ascending: bool = ..., na_position: str = ...) -> None: ...
    def to_dense(self) -> np.ndarray: ...
    def take_nd(self, indexer, allow_fill: bool = ..., fill_value: Incomplete | None = ...) -> Categorical: ...
    def __iter__(self): ...
    def __contains__(self, key) -> bool: ...
    def min(self, *, skipna: bool = ..., **kwargs): ...
    def max(self, *, skipna: bool = ..., **kwargs): ...
    def mode(self, dropna: bool = ...) -> Categorical: ...
    def unique(self): ...
    def equals(self, other: object) -> bool: ...
    def is_dtype_equal(self, other) -> bool: ...
    def describe(self) -> DataFrame: ...
    def isin(self, values) -> npt.NDArray[np.bool_]: ...
    @overload
    def replace(self, to_replace, value, *, inplace: Literal[False] = ...) -> Categorical: ...
    @overload
    def replace(self, to_replace, value, *, inplace: Literal[True]) -> None: ...

class CategoricalAccessor(PandasDelegate, PandasObject, NoNewAttributesMixin):
    def __init__(self, data) -> None: ...
    @property
    def codes(self) -> Series: ...

def recode_for_categories(codes: np.ndarray, old_categories, new_categories, copy: bool = ...) -> np.ndarray: ...
def factorize_from_iterable(values) -> tuple[np.ndarray, Index]: ...
def factorize_from_iterables(iterables) -> tuple[list[np.ndarray], list[Index]]: ...
