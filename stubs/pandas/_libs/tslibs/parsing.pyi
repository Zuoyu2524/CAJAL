from typing import Any, ClassVar

import _thread
import collections
import datetime
import dateutil.parser._parser
import dateutil.tz._common
import dateutil.tz.tz
import pandas._config.config
import weakref
DEFAULTPARSER: dateutil.parser._parser.parser
PARSING_WARNING_MSG: str
_DATEUTIL_LEXER_SPLIT: method
_DEFAULT_DATETIME: datetime.datetime
du_parse: function
find_stack_level: function
get_option: pandas._config.config.CallableDynamicDoc

class DateParseError(ValueError): ...

class _dateutil_tzlocal(dateutil.tz._common._tzinfo):
    __init__: ClassVar[function] = ...
    _isdst: ClassVar[function] = ...
    _naive_is_dst: ClassVar[function] = ...
    dst: ClassVar[function] = ...
    is_ambiguous: ClassVar[function] = ...
    tzname: ClassVar[function] = ...
    utcoffset: ClassVar[function] = ...
    __eq__: ClassVar[function] = ...
    __hash__: ClassVar[None] = ...
    __ne__: ClassVar[function] = ...
    def __reduce__(self) -> Any: ...

class _dateutil_tzstr(dateutil.tz.tz.tzrange):
    __init__: ClassVar[function] = ...
    _TzStrFactory__cache_lock: ClassVar[_thread.lock] = ...
    _TzStrFactory__instances: ClassVar[weakref.WeakValueDictionary] = ...
    _TzStrFactory__strong_cache: ClassVar[collections.OrderedDict] = ...
    _TzStrFactory__strong_cache_size: ClassVar[int] = ...
    _delta: ClassVar[function] = ...

class _dateutil_tzutc(datetime.tzinfo):
    _TzSingleton__instance: ClassVar[dateutil.tz.tz.tzutc] = ...
    dst: ClassVar[function] = ...
    fromutc: ClassVar[function] = ...
    is_ambiguous: ClassVar[function] = ...
    tzname: ClassVar[function] = ...
    utcoffset: ClassVar[function] = ...
    __eq__: ClassVar[function] = ...
    __hash__: ClassVar[None] = ...
    __ne__: ClassVar[function] = ...
    def __reduce__(self) -> Any: ...

class _timelex:
    def __init__(self, *args, **kwargs) -> None: ...
    def get_tokens(self, *args, **kwargs) -> Any: ...
    @classmethod
    def split(cls, *args, **kwargs) -> Any: ...

class relativedelta:
    __init__: ClassVar[function] = ...
    _fix: ClassVar[function] = ...
    _set_months: ClassVar[function] = ...
    normalized: ClassVar[function] = ...
    __abs__: ClassVar[function] = ...
    __add__: ClassVar[function] = ...
    __bool__: ClassVar[function] = ...
    __div__: ClassVar[function] = ...
    __eq__: ClassVar[function] = ...
    __hash__: ClassVar[function] = ...
    __mul__: ClassVar[function] = ...
    __ne__: ClassVar[function] = ...
    __neg__: ClassVar[function] = ...
    __nonzero__: ClassVar[function] = ...
    __radd__: ClassVar[function] = ...
    __rmul__: ClassVar[function] = ...
    __rsub__: ClassVar[function] = ...
    __sub__: ClassVar[function] = ...
    __truediv__: ClassVar[function] = ...
    weeks: Any

class tzoffset(datetime.tzinfo):
    __init__: ClassVar[function] = ...
    _TzOffsetFactory__instances: ClassVar[weakref.WeakValueDictionary] = ...
    _TzOffsetFactory__strong_cache: ClassVar[collections.OrderedDict] = ...
    _TzOffsetFactory__strong_cache_size: ClassVar[int] = ...
    _cache_lock: ClassVar[_thread.lock] = ...
    dst: ClassVar[function] = ...
    fromutc: ClassVar[function] = ...
    is_ambiguous: ClassVar[function] = ...
    tzname: ClassVar[function] = ...
    utcoffset: ClassVar[function] = ...
    __eq__: ClassVar[function] = ...
    __hash__: ClassVar[None] = ...
    __ne__: ClassVar[function] = ...
    def __reduce__(self) -> Any: ...

def __pyx_unpickle_Enum(*args, **kwargs) -> Any: ...
def _does_string_look_like_datetime(*args, **kwargs) -> Any: ...
def concat_date_cols(*args, **kwargs) -> Any: ...
def format_is_iso(*args, **kwargs) -> Any: ...
def get_rule_month(*args, **kwargs) -> Any: ...
def guess_datetime_format(*args, **kwargs) -> Any: ...
def parse_datetime_string(*args, **kwargs) -> Any: ...
def parse_time_string(*args, **kwargs) -> Any: ...
def quarter_to_myear(*args, **kwargs) -> Any: ...
def try_parse_date_and_time(*args, **kwargs) -> Any: ...
def try_parse_dates(*args, **kwargs) -> Any: ...
def try_parse_datetime_components(*args, **kwargs) -> Any: ...
def try_parse_year_month_day(*args, **kwargs) -> Any: ...
