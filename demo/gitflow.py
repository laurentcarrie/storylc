import traceback
from functools import reduce
from pathlib import Path

svgdata = [
    ("out1", 20,100,[
        "a1-1", "a1-3",
        "a1-1", "a1-3",
        "a1-1", "a1-3",
        "a1-1", "a1-3",
        "a1-1", "a1-3",
        "a1-1", "a1-3",
        "a1-1", "a1-3",
        "a1-1", "a1-3",
        "a1-1", "a1-3",
        "a1-1", "a1-3",
        "a1-1", "a1-3",
        "a1-1", "a1-3",
        "a1-1", "a1-3",
        "a1-1", "a1-3",
        "a1-1", "a1-3",
        "a1-1", "a1-3",

        "a1-1", "a1-3",
        "a1-1", "a1-3",


        "a1-1", "a1-3",
        "a1-1", "a1-3",
        "a1-1", "a1-3",
        "a1-1", "a1-3",
        "a1-1", "a1-3",
    ]),
    ("out2", 20,1,["a1-2", "a1-2", ]),
    ("out3", 20,1,[ "a1-3"])
]

from storylc.make import write_makefile

def main():
    here=Path(__file__).parent.absolute()
    makefile = here / "Makefile"
    write_makefile(makefile,svgdata)


if __name__=="__main__":
    main()