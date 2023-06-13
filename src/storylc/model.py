from dataclasses import dataclass, field
from enum import Enum, auto
from functools import reduce
from pathlib import Path
from typing import Any, Callable, Iterator, List, Set, Tuple


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
class AnimationTimeLine:
    animation_name: str
    timeline: List[float]


@dataclass(eq=True, frozen=True)
class Layer:
    name: str
    animations: List[AnimationTimeLine]


@dataclass(eq=True, frozen=True)
class Scene:
    name: str
    layers: List[Layer]

    @property
    def animations(self) -> Set[str]:
        seed: List[AnimationTimeLine] = []
        llanimations: List[AnimationTimeLine] = reduce(
            list.__add__, list(map(lambda layer: layer.animations, self.layers)), seed
        )
        return set(map(lambda atl: atl.animation_name, llanimations))


@dataclass(eq=True, frozen=True)
class Movie:
    scenes: List[Scene]
    animations: List[Animation]
    root: Path = Path(".")

    @property
    def nb_images(self) -> int:
        return reduce(
            lambda a, b: a + b,
            map(
                lambda animation: animation.duration * animation.ips + 1,
                self.animations,
            ),
            0,
        )
