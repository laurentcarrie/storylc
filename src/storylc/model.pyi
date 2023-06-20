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
    # timeline_x: List[float]
    # timeline_y: List[float]
    def __init__(self, animation_name: str) -> None: ...

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
    animations: List[AnimationTimeLine]
    def __init__(self, name: str, animations: List[AnimationTimeLine]) -> None: ...

class Scene:
    __match_args__: Any
    name: str
    duration: int
    layers: List[Layer]
    def __init__(self, name: str, duration: int, layers: List[Layer]) -> None: ...
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
