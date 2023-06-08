from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, List


@dataclass(eq=True, frozen=True)
class Scene:
    name: str
    duration: int
    ips: int
    path: str


@dataclass(eq=True, frozen=True)
class Movie:
    scenes: List[Scene]
    root: Path = Path(".")
