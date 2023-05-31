import sys

from storylc.model import Movie,Scene
from pathlib import Path
def generate_one(out:Path,name:str,t:float) -> None:
    with out.open(mode='w') as fout :
        fout.write(f"""
    outputformat := "svg";
    % outputtemplate := "%j-%c.svg";
    outputtemplate := "%j.svg";

    input {name} ;
    run({t})

    endfig;

    end;
""")

def generate(name:str,duration:int) :
    nbpoints=10
    for i in range(nbpoints):
        generate_one(out=Path(f"{name}-{i}.mp"),name=name,t=float(i)/float(nbpoints-1))

if __name__=="__main__":
    name=sys.argv[1]
    duration=sys.argv[2]
    generate(name=name,duration=duration)

