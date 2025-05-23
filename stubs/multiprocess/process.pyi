from _typeshed import Incomplete

def current_process(): ...
def active_children(): ...
def parent_process(): ...

class BaseProcess:
    def __init__(self, group: Incomplete | None = ..., target: Incomplete | None = ..., name: Incomplete | None = ..., args=..., kwargs=..., *, daemon: Incomplete | None = ...) -> None: ...
    def run(self) -> None: ...
    def start(self) -> None: ...
    def terminate(self) -> None: ...
    def kill(self) -> None: ...
    def join(self, timeout: Incomplete | None = ...) -> None: ...
    def is_alive(self): ...
    def close(self) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def daemon(self): ...
    @daemon.setter
    def daemon(self, daemonic) -> None: ...
    @property
    def authkey(self): ...
    @authkey.setter
    def authkey(self, authkey) -> None: ...
    @property
    def exitcode(self): ...
    @property
    def ident(self): ...
    pid: Incomplete
    @property
    def sentinel(self): ...

class AuthenticationString(bytes):
    def __reduce__(self): ...

class _ParentProcess(BaseProcess):
    def __init__(self, name, pid, sentinel) -> None: ...
    def is_alive(self): ...
    @property
    def ident(self): ...
    def join(self, timeout: Incomplete | None = ...) -> None: ...
    pid: Incomplete

class _MainProcess(BaseProcess):
    def __init__(self) -> None: ...
    def close(self) -> None: ...
