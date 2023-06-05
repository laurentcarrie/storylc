import sys
import traceback

from storylc.model import Movie,Scene
from pathlib import Path

nbpoints = 10


def generate_one(out:Path,name:str,t:float) -> None:
    print(f"generating {str(out.absolute())}")
    with out.open(mode='w') as fout :
        fout.write(f"""
outputformat := "svg";
% outputtemplate := "%j-%c.svg";
outputtemplate := "%j.svg";

beginfig(1);       
input {name} ;
run({t}) ;

endfig;

end;
""")




def generate(name:str,ips:int,duration:int) :
    for i in range(ips*duration):
        generate_one(out=Path(f"{name}-{i}.mp"),name=name,t=float(i)/float(ips*duration-1))

def make_svg_list(name:str,ips:int,duration:int):
    return " ".join(list(map(lambda i: f"{name}-{i}.svg",range(ips*duration))))

def make_mp_list(name:str,ips:int,duration:int):
    return " ".join(list(map(lambda i: f"{name}-{i}.mp",range(ips*duration))))


if __name__=="__main__":
    try:
        what=sys.argv[1]
        name=sys.argv[2]
        ips=int(sys.argv[3])
        duration=int(sys.argv[4])
        match what:
            case 'G' : generate(name=name,duration=duration,ips=ips)
            case 'L-svg' : print(make_svg_list(name=name,ips=ips,duration=duration))
            case 'L-mp' : print(make_mp_list(name=name,ips=ips,duration=duration))
            case _ : raise RuntimeError(f"no such case : {what}")
    except:#noqa:E722
        traceback.print_exc()
        sys.exit(1)

