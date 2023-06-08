from dataclasses import dataclass
from pathlib import Path
from typing import Any, List

class Scene:
    __match_args__: Any
    name: str
    duration: int
    ips: int
    path: str

    def __init__(self, name: str, duration: int, ips: int, path: str) -> None: ...

class Movie:
    __match_args__: Any
    scenes: List[Scene]
    root: Path = Path(".")
    def __init__(self, scenes: List[Scene], root: Path = Path(".")) -> None: ...
