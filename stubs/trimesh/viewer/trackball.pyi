from .. import transformations as transformations
from _typeshed import Incomplete

class Trackball:
    STATE_ROTATE: int
    STATE_PAN: int
    STATE_ROLL: int
    STATE_ZOOM: int
    def __init__(self, pose, size, scale, target=...) -> None: ...
    @property
    def pose(self): ...
    def set_state(self, state) -> None: ...
    def resize(self, size) -> None: ...
    def down(self, point) -> None: ...
    def drag(self, point) -> None: ...
    def scroll(self, clicks) -> None: ...
    def rotate(self, azimuth, axis: Incomplete | None = ...) -> None: ...
