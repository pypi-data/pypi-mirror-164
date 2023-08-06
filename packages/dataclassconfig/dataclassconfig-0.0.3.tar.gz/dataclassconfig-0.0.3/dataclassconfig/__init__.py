import typing as tp
from dataclasses import dataclass
from pathlib import Path

import dacite
import yaml  # type: ignore

T = tp.TypeVar("T", bound="Config")


class Config:
    def __init_subclass__(cls):
        dataclass(cls)

    @classmethod
    def load(cls: tp.Type[T], source) -> T:
        """loads configuration state from file-like object

        Args:
            fp: file-like configuration object

        Returns:
            configuration state
        """
        data = source
        if isinstance(source, str):
            source = Path(source)
        if isinstance(source, Path):
            with open(source.expanduser(), "rb") as file:
                data = file.read()
        try:
            state = yaml.safe_load(data)
        except Exception:  # pylint: disable=broad-except
            data = data.read()
            state = yaml.safe_load(data)
        return cls.from_dict(state)

    @classmethod
    def from_dict(cls: tp.Type[T], state: tp.Dict[str, tp.Any]) -> T:
        """loads the configuration state from a dictionary

        Args:
            state (tp.Dict): dictionary containing configuration

        Returns:
            configuration state
        """
        return dacite.from_dict(
            data_class=cls,
            data=state,
            config=dacite.Config(cast=[Path]),
        )
