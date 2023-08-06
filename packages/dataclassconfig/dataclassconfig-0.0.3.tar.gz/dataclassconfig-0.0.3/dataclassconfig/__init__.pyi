import typing as tp
from typing import Any

T: Any

class Config:
    def __init_subclass__(cls) -> None: ...
    @classmethod
    def load(cls, source) -> T: ...
    @classmethod
    def from_dict(cls, state: tp.Dict[str, tp.Any]) -> T: ...
