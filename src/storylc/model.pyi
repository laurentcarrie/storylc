from dataclasses import dataclass
from pathlib import Path
from typing import Any, List

class Scene:
    __match_args__: Any
    path: Path
    name: str
    duration: int

    def __init__(self, path: Path, name: str, duration: int) -> None: ...

class Movie:
    __match_args__: Any
    scenes: List[Scene]
    def __init__(self, scenes: List[Scene]) -> None: ...
