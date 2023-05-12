from typing import Any, Set, List, Tuple, Sequence

import drawsvg  # type:ignore

class Circle:
    __match_args__: Any
    t: drawsvg.Circle
    def __init__(self, t) -> None: ...
    def __post_init__(self) -> None: ...

class CircleMovement:
    __match_args__: Any
    circle: Circle
    moves: Sequence[Tuple[int, int, int, int]]
    def __init__(self, circle, moves) -> None: ...

class Rectangle:
    __match_args__: Any
    t: drawsvg.Rectangle
    def __init__(self, t) -> None: ...
    def __post_init__(self) -> None: ...

class Group:
    __match_args__: Any
    t: drawsvg.Group
    def __init__(self, t) -> None: ...
    def __post_init__(self) -> None: ...

class Scene:
    __match_args__: Any
    movements: Set[CircleMovement]
    duration: int
    def __init__(self, movements: Set[CircleMovement], duration: int) -> None: ...

class Story:
    __match_args__: Any
    scenes: List[Scene]
    t: drawsvg.Drawing
    def __init__(self, scenes: List[Scene], t: drawsvg.Drawing) -> None: ...

def make_rectangle(x: int, y: int, width: int, height: int) -> Rectangle: ...
def make_circle(cx: int, cy: int, r: int) -> Circle: ...
def make_story(scenes: List[Scene]) -> Story: ...
