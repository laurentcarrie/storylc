from collections.abc import Set
from dataclasses import dataclass
from functools import reduce
from typing import List, Tuple

import drawsvg  # type:ignore


@dataclass(eq=True, frozen=True)
class Circle:
    t: drawsvg.Circle

    def __post_init__(self):
        assert isinstance(self.t, drawsvg.Circle)


@dataclass(eq=True, frozen=True)
class Rectangle:
    t: drawsvg.Rectangle

    def __post_init__(self):
        assert isinstance(self.t, drawsvg.Rectangle)


@dataclass(eq=True, frozen=True)
class Group:
    t: drawsvg.Group

    def __post_init__(self):
        assert isinstance(self.t, drawsvg.Group)


@dataclass(eq=True, frozen=True)
class CircleMovement:
    circle: Circle
    moves: List[Tuple[int, int, int, int]]


@dataclass(eq=True, frozen=True)
class Scene:
    movements: Set[CircleMovement]
    duration: int


@dataclass(eq=True, frozen=True)
class Story:
    scenes: List[Scene]
    t: drawsvg.Drawing


def make_rectangle(x: int, y: int, width: int, height: int) -> Rectangle:
    return Rectangle(t=drawsvg.Rectangle(x=x, y=y, width=width, height=height))


def make_circle(cx: int, cy: int, r: int) -> Circle:
    return Circle(t=drawsvg.Circle(cx=cx, cy=cy, r=r))


def make_story(scenes: List[Scene]) -> Story:
    duration = reduce(lambda x, y: x + y, map(lambda scene: scene.duration, scenes), 0)
    d = drawsvg.Drawing(
        400,
        200,
        origin="center",
        animation_config=drawsvg.types.SyncedAnimationConfig(
            # Animation configuration
            duration=duration,  # Seconds
            show_playback_progress=True,
            show_playback_controls=True,
        ),
    )

    return Story(scenes=scenes, t=d)
