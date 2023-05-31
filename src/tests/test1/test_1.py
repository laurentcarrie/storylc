from pathlib import Path

from storylc.make import write_makefile
from storylc.model import Movie, Scene

here = Path(__file__).absolute().parent


def test_1() -> None:
    import traceback
    from functools import reduce
    from pathlib import Path

    movie = Movie(scenes=[Scene(name="scene-1", path=here / "a.mp", duration=10)])
    makefile = here / "Makefile"
    write_makefile(makefile=makefile, movie=movie)
