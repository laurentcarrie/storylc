from dataclasses import dataclass, field
from enum import Enum, auto
from functools import reduce
from pathlib import Path
from typing import Any, Callable, List, Set


@dataclass(eq=True, frozen=True)
class Animation:
    name: str
    duration: int
    ips: int
    path: str


@dataclass(eq=True, frozen=True)
class Clear:
    pass


@dataclass(eq=True, frozen=True)
class Add:
    animation: Animation
    start: int
    ips: int


@dataclass(eq=True, frozen=True)
class WhatToDo:
    what: str


@dataclass(eq=True, frozen=True)
class Layer:
    name: str
    animations: List[str]

@dataclass(eq=True, frozen=True)
class Scene:
    name: str
    layers: List[Layer]
    @property
    def animations(self) -> Set[Animation]:
        return reduce(
            lambda a, b: a | b,
            map(lambda layer: set(layer.animations), self.layers),
            set(),
        )


@dataclass(eq=True, frozen=True)
class Movie:
    scenes: List[Scene]
    animations: List[Animation]
    root: Path = Path(".")
