from _typeshed import Incomplete

def reset_plugins() -> None: ...
def find_available_plugins(loaded: bool = ...): ...

available_plugins: Incomplete

def call_plugin(kind, *args, **kwargs): ...
def use_plugin(name, kind: Incomplete | None = ...) -> None: ...
def plugin_info(plugin): ...
def plugin_order(): ...
