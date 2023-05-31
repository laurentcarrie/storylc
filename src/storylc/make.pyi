import tempfile
import traceback
from functools import reduce
from pathlib import Path
from typing import Tuple

from storylc.model import Movie, Scene

def write_makefile(makefile: Path, movie: Movie) -> bool: ...
