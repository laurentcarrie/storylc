from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass(eq=True, frozen=True)
class Scene:
    path: Path
    name: str
    duration: int


@dataclass(eq=True, frozen=True)
class Movie:
    scenes: List[Scene]
