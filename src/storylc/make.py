import tempfile
import traceback
from functools import reduce
from pathlib import Path

from typing import Tuple


def write_makefile(makefile: Path, svgdata) -> bool:
    def _of_svg(line):
        outfile = line[0]
        delay = line[1]
        loop = line[2]
        deplist = " ".join(list(map(lambda n: n + ".svg", line[3])))
        yield f"{outfile}.gif: {deplist}\n"
        yield f"\trm -f $@\n"
        yield f"\tconvert -delay {delay} -loop {loop} -size 1024x1024 {deplist} $@\n\n"

        yield f"{outfile}.mp4 : {outfile}.gif\n"
        yield f"\trm -f $@\n"
        yield f"\tffmpeg -i {outfile}.gif -movflags faststart -pix_fmt yuv420p -vf \"scale=trunc(iw/2)*2:trunc(ih/2)*2\" $@\n\n"
        #          ffmpeg -i animated.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" video.mp4
        #yield f"\tffmpeg -i {outfile}.gif -pix_fmt yuv420p $@\n\n"

    def _header():
        yield ".PHONY: all clean\n\n"
        yield "all:all.mp4\n\n"

    data = []
    for line in _header():
        data += line

    for line in svgdata:
        for line2 in _of_svg(line):
            data += line2

    all_mp4 = reduce(lambda a, b: a + " " + b, list(map(lambda line: line[0] + ".mp4", svgdata)), "")
    Path("infile.txt").write_text(
        "\n".join(list(map(lambda line: f"file {line[0]}.mp4", svgdata)))
    )
    data += f"all.mp4 : {all_mp4}\n"
    data += f"\trm -f $@\n"
    data += f"\tffmpeg -f concat -safe 0 -i infile.txt -c copy $@\n\n"

    def mp_of_svg(svgfile) -> str:
        match s := svgfile.split("-"):
            case []:
                raise RuntimeError(f"bad svgfile : {svgfile}")
            case _:
                return s[0]

    svgfiles_noext = reduce(lambda a, b: a | b, list(map(lambda line: set(line[3]), svgdata)), set())
    mpfiles = set(map(lambda n: n.split("-")[0], svgfiles_noext))
    svgfiles = list(map(lambda n: n + ".svg", svgfiles_noext))
    print(mpfiles)

    for mpfile in mpfiles:
        svgfiles2 = reduce(lambda a, b: a + " " + b, filter(lambda n: mp_of_svg(n) == mpfile, svgfiles), "")
        print("XXXXXXXXXXXXXXXXXXX")
        data+=f"{svgfiles2} : {mpfile}.mp\n"
        data+=f"\trm -f {svgfiles2}\n"
        data+=f"\tmpost {mpfile}\n\n"

    print(svgfiles)
    print(mpfiles)
    giffiles = set(map(lambda line: line[0] + ".gif", svgdata))
    mp4files = set(map(lambda line: line[0] + ".mp4", svgdata))
    data+="clean:\n"
    data+=f"\trm -f {' '.join(svgfiles)}\n"
    data+=f"\trm -f {' '.join(giffiles)}\n"
    data+=f"\trm -f {' '.join(mp4files)}\n"
    data+=f"\trm -f all.mp4\n\n"



    if makefile.exists() and makefile.read_text() == data:
        return False


    makefile.write_text(''.join(data))

    return False
