from dataclasses import dataclass
from pathlib import Path
from typing import Any, List, Set, Tuple

class Animation:
    __match_args__: Any
    name: str
    duration: int
    ips: int
    path: str
    start: int = -1

    def __init__(
        self, name: str, duration: int, ips: int, path: str, start: int = -1
    ) -> None: ...
    @property
    def end(self) -> int: ...

class Layer:
    __match_args__: Any
    name: str
    animation_name: str
    def __init__(self, name: str, animation_name: str) -> None: ...

class Scene:
    __match_args__: Any
    name: str
    duration: int
    layers: List[Layer]
    def __init__(self, name: str, duration: int, layers: List[Layer]) -> None: ...

class Movie:
    __match_args__: Any
    scenes: List[Scene]
    animations: List[Animation]
    root: Path = Path(".")
    def __init__(
        self, scenes: List[Scene], animations: List[Animation], root: Path = Path(".")
    ) -> None: ...
    @property
    def nb_images(self) -> int: ...
