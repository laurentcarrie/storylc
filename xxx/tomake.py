import traceback
from functools import reduce
from pathlib import Path

from typing import Tuple

def main(svgdata) -> bool:
    makefile = Path("Makefile")
    old_data = makefile.read_text() if makefile.exists() else ""

    def _of_svg(line):
        outfile = line[0]
        delay=line[1]
        loop=line[2]
        deplist = " ".join(list(map(lambda n:n+".svg",line[3])))
        yield f"{outfile}.gif: {deplist}\n"
        yield f"\trm -f $@\n"
        yield f"\tconvert -delay {delay} -loop {loop} -size 1024x1024 {deplist} $@\n\n"

        yield f"{outfile}.mp4 : {outfile}.gif\n"
        yield f"\trm -f $@\n"
        yield f"\tffmpeg -i {outfile}.gif -movflags faststart -pix_fmt yuv420p -vf \"scale=trunc(iw/2)*2:trunc(ih/2)*2\" $@\n\n"


    with makefile.open('w') as fout:
        fout.write(".PHONY: all clean\n\n")
        fout.write("all:all.mp4\n\n")
        for line in svgdata:
            for data in _of_svg(line):
                fout.write(data)

        all_mp4=reduce(lambda a,b:a+" "+b,list(map(lambda line:line[0]+".mp4",svgdata)),"")
        Path("infile.txt").write_text(
            "\n".join(list(map(lambda line:f"file {line[0]}.mp4",svgdata)))
        )
        fout.write(f"all.mp4 : {all_mp4}\n")
        fout.write(f"\trm -f $@\n")
        fout.write(f"\tffmpeg -f concat -safe 0 -i infile.txt -c copy $@\n\n")


        def mp_of_svg(svgfile) -> str:
            match s:=svgfile.split("-") :
                case [] : raise RuntimeError(f"bad svgfile : {svgfile}")
                case _: return s[0]

        svgfiles_noext=reduce(lambda a,b:a|b,list(map(lambda line:set(line[3]),svgdata)),set())
        mpfiles=set(map(lambda n:n.split("-")[0],svgfiles_noext))
        svgfiles=list(map(lambda n:n+".svg",svgfiles_noext))
        print(mpfiles)

        for mpfile in mpfiles:
            svgfiles2 = reduce(lambda a,b:a+" "+b,filter(lambda n:mp_of_svg(n)==mpfile,svgfiles),"")
            print("XXXXXXXXXXXXXXXXXXX")
            fout.write(f"{svgfiles2} : {mpfile}.mp\n")
            fout.write(f"\trm -f {svgfiles2}\n")
            fout.write(f"\tmpost {mpfile}\n\n")

        print(svgfiles)
        print(mpfiles)
        giffiles=set(map(lambda line:line[0]+".gif",svgdata))
        mp4files=set(map(lambda line:line[0]+".mp4",svgdata))
        fout.write("clean:\n")
        fout.write(f"\trm -f {' '.join(svgfiles)}\n")
        fout.write(f"\trm -f {' '.join(giffiles)}\n")
        fout.write(f"\trm -f {' '.join(mp4files)}\n")
        fout.write(f"\trm -f all.mp4\n\n")

    new_data=makefile.read_text()

    return old_data == new_data


if __name__ == "__main__":
    try:
        changed = main()
        if changed:
            exit(1)
    except:
        traceback.print_exc()

