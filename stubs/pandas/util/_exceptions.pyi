from typing import Iterator

def rewrite_exception(old_name: str, new_name: str) -> Iterator[None]: ...
def find_stack_level() -> int: ...
def rewrite_warning(target_message: str, target_category: type[Warning], new_message: str, new_category: Union[type[Warning], None] = ...) -> Iterator[None]: ...
