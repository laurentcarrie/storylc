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
    start: int = -1

    # end exclusive
    @property
    def end(self) -> int:
        return self.start + self.duration * self.ips


@dataclass(eq=True, frozen=True)
class Layer:
    name: str
    animation: Animation


@dataclass(eq=True, frozen=True)
class Scene:
    name: str
    duration: int
    layers: List[Layer]

    @property
    def animations(self) -> Set[Animation]:
        return set(map(lambda layer: layer.animation, self.layers))


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
                lambda animation: animation.end - animation.start,
                self.animations,
            ),
            0,
        )
