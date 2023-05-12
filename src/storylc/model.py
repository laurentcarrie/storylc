from collections.abc import Set
from dataclasses import dataclass
from functools import reduce
from typing import List, Tuple

import drawsvg  # type:ignore


@dataclass(eq=True, frozen=True)
class Circle:
    cx: int
    cy: int
    r: int
    fill: str


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
class CircleMove:
    moves: List[Tuple[int, Circle]]

    @property
    def duration(self):
        return reduce(lambda a, b: max(a, b), map(lambda x: x[0], self.moves))


@dataclass(eq=True, frozen=True)
class Scene:
    moves: Set[CircleMove]

    @property
    def duration(self):
        return reduce(lambda a, b: max(a, b), map(lambda m: m.duration, self.moves))


@dataclass(eq=True, frozen=True)
class Story:
    scenes: List[Scene]
    t: drawsvg.Drawing

    @property
    def duration(self) -> int:
        return reduce(lambda a, b: a + b, map(lambda s: s.duration, self.scenes), 0)


def make_rectangle(x: int, y: int, width: int, height: int) -> Rectangle:
    return Rectangle(t=drawsvg.Rectangle(x=x, y=y, width=width, height=height))


def make_circle(cx: int, cy: int, r: int) -> Circle:
    return Circle(cx=cx, cy=cy, r=r)


def make_move_circle(moves: List[Tuple[int, Circle]]) -> CircleMove:
    return CircleMove(moves=moves)


def make_scene(moves: Set[CircleMove]) -> Scene:
    return Scene(moves=moves)


def make_story(width: int, height: int, scenes: List[Scene]) -> Story:
    duration = reduce(lambda x, y: x + y, map(lambda scene: scene.duration, scenes), 0)
    d = drawsvg.Drawing(
        width,
        height,
        origin="center",
        animation_config=drawsvg.types.SyncedAnimationConfig(
            # Animation configuration
            duration=duration,  # Seconds
            show_playback_progress=True,
            show_playback_controls=True,
        ),
    )

    def add_circle_move(start: int, duration: int, cm: CircleMove) -> None:
        assert isinstance(duration, int)
        circle = drawsvg.Circle(cx=0, cy=0, r=0, fill="red")
        print(f"add cm {start} ; {cm}")
        circle.add_key_frame(0, cx=0, cy=0, r=0)
        circle.add_key_frame(start, cx=0, cy=0, r=0)
        list(
            map(
                lambda move: circle.add_key_frame(
                    start + move[0],
                    cx=move[1].cx,
                    cy=move[1].cy,
                    r=move[1].r,
                    fill=move[1].fill,
                ),
                cm.moves,
            )
        )
        circle.add_key_frame(start + duration, cx=0, cy=0, r=0)
        d.append(circle)

    def rec_add_scene(start: int, scenes: List[Scene]):
        print(f"add scene {start}")
        if len(scenes) == 0:
            return start
        scene = scenes[0]
        scenes = scenes[1:]
        list(map(lambda cm: add_circle_move(start, scene.duration, cm=cm), scene.moves))
        rec_add_scene(start + scene.duration, scenes)

    rec_add_scene(start=0, scenes=scenes)

    return Story(scenes=scenes, t=d)
