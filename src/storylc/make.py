import tempfile
import traceback
from functools import reduce
from pathlib import Path
from typing import List, Tuple
from jinja2 import Environment, PackageLoader, select_autoescape  # type:ignore

from storylc.model import Movie, Scene


def write_makefile(makefile: Path, movie: Movie) -> bool:
    def _cinematique(scene:Scene):
        data=""
        for i in range(10):
            outfile = scene.path.parent/f"{scene.name}-{i}.mp"
            def get_old():
                match outfile.exists():
                    case True:
                        return outfile.read_text()
                    case False:
                        return ""

            env: Environment = Environment()
            template = env.from_string(source=scene.path.read_text(), globals={})
            old_data = get_old()
            new_data = template.render(t=i)
            data+=f"{scene.name}-{i}.svg : {scene.name}-{i}.mp\n"
            data+=f"\tmpost {scene.name}-{i}\n\n"
            if old_data != new_data:
                outfile.write_text(data=new_data)
        return data

    def _of_svg(scene: Scene):
        deplist = " ".join(
            list(map(lambda i: f"{scene.name}-{i}.svg", range(scene.duration)))
        )
        yield f"{scene.name}.gif: {deplist}\n"
        yield "\trm -f $@\n"
        yield f"\tconvert -delay 1 -loop 1 -size 1024x1024 {deplist} $@\n\n"

        yield f"{scene.name}.mp4 : {scene.name}.gif\n"
        yield "\trm -f $@\n"
        yield f'\tffmpeg -i {scene.name}.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" $@\n\n'
        #          ffmpeg -i animated.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" video.mp4
        # yield f"\tffmpeg -i {outfile}.gif -pix_fmt yuv420p $@\n\n"

    def _header():
        yield ".PHONY: all clean\n\n"
        yield "all:all.mp4\n\n"

    data = []
    for line in _header():
        data += line

    for scene in movie.scenes:
        data+=_cinematique(scene)
        for line2 in _of_svg(scene):
            data += line2


    all_mp4 = reduce(
        lambda a, b: a + " " + b,
        list(map(lambda scene: scene.name + ".mp4", movie.scenes)),
        "",
    )
    (makefile.parent / "infile.txt").write_text(
        "\n".join(list(map(lambda scene: f"file {scene.name}.mp4", movie.scenes)))
    )
    data += f"all.mp4 : {all_mp4}\n"
    data += "\trm -f $@\n"
    data += "\tffmpeg -f concat -safe 0 -i infile.txt -c copy $@\n\n"

    def mp_of_svg(svgfile) -> str:
        match s := svgfile.split("-"):
            case []:
                raise RuntimeError(f"bad svgfile : {svgfile}")
            case _:
                return s[0]

    # svgfiles_noext = reduce(
    #     lambda a, b: a | b, list(map(lambda line: set(line[3]), svgdata)), set()
    # )
    svgfiles_noext: List[str] = []
    mpfiles = set(map(lambda n: n.split("-")[0], svgfiles_noext))
    svgfiles = list(map(lambda n: n + ".svg", svgfiles_noext))
    print(mpfiles)

    for mpfile in mpfiles:
        svgfiles2 = reduce(
            lambda a, b: a + b + " ",
            filter(lambda n: mp_of_svg(n) == mpfile, svgfiles),
            "",
        )
        print("XXXXXXXXXXXXXXXXXXX")
        data += f"{svgfiles2} : {mpfile}.mp\n"
        data += f"\trm -f {svgfiles2}\n"
        data += f"\tmpost {mpfile}\n\n"

    print(svgfiles)
    print(mpfiles)
    # giffiles = set(map(lambda scene: line[0] + ".gif", svgdata))
    giffiles: List[str] = []
    # mp4files = set(map(lambda line: line[0] + ".mp4", svgdata))
    mp4files: List[str] = []
    data += "clean:\n"
    data += f"\trm -f {' '.join(svgfiles)}\n"
    data += f"\trm -f {' '.join(giffiles)}\n"
    data += f"\trm -f {' '.join(mp4files)}\n"
    data += "\trm -f all.mp4\n\n"

    if makefile.exists() and makefile.read_text() == data:
        return False

    makefile.write_text("".join(data))

    return False
