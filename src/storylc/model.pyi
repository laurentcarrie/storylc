from dataclasses import dataclass
from pathlib import Path
from typing import Any, List, Set, Tuple

class Clear:
    __match_args__: Any
    def __init__(self) -> None: ...

class Add:
    __match_args__: Any
    animation: "Animation"
    start: int
    ips: int
    def __init__(self, animation: "Animation", start: int, ips: int) -> None: ...

class WhatToDo:
    __match_args__: Any
    what: str
    def __init__(self, what: str) -> None: ...

@dataclass(eq=True, frozen=True)
class AnimationTimeLine:
    __match_args__: Any
    animation_name: str
    timeline: List[float]
    def __init__(self, animation_name: str, timeline: List[float]) -> None: ...

class Animation:
    __match_args__: Any
    name: str
    duration: int
    ips: int
    path: str

    def __init__(self, name: str, duration: int, ips: int, path: str) -> None: ...

class Layer:
    __match_args__: Any
    name: str
    animations: List[str]
    def __init__(self, name: str, animations: List[AnimationTimeLine]) -> None: ...

class Scene:
    __match_args__: Any
    name: str
    layers: List[Layer]
    def __init__(self, name: str, layers: List[Layer]) -> None: ...
    @property
    def animations(self) -> Set[Animation]: ...

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
