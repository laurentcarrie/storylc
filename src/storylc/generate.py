from functools import reduce
from pathlib import Path

from jinja2 import Environment, PackageLoader, select_autoescape  # type:ignore
from storylc.model import Movie, Scene
from storylc.project_logs import a_logger

here = Path(__file__).absolute().parent


def get_old(outfile: Path):
    match outfile.exists():
        case True:
            return outfile.read_text()
        case False:
            return ""


def generate_omakeroot(movie: Movie, out: Path) -> bool:
    j_file: Path = here / "OMakeroot.jinja"
    outfile = out / "OMakeroot"
    env: Environment = Environment()
    template = env.from_string(source=j_file.read_text(), globals={})
    old_data = get_old(outfile)
    new_data = template.render(movie=movie, srcdir=str(movie.root.absolute()))
    if old_data == new_data:
        a_logger.info(f"{str(outfile.absolute())} was not regenerated")
        return True
    outfile.write_text(data=new_data)
    a_logger.info(f"{str(outfile.absolute())} was regenerated")
    return False

def generate_scene(movie:Movie,scene:Scene,out:Path):
    j_file: Path = here / "scene.mp.jinja"
    outfile = out / f"g_{scene.path}"
    env: Environment = Environment()
    template = env.from_string(source=j_file.read_text(), globals={})
    old_data = get_old(outfile)
    a_logger.info(movie.scenes)
    new_data = template.render(movie=movie, scene=scene)
    if old_data == new_data:
        a_logger.info(f"{str(outfile.absolute())} was not regenerated")
        return True
    outfile.write_text(data=new_data)
    a_logger.info(f"{str(outfile.absolute())} was regenerated")
    return False

def generate_omakefile(movie: Movie, out: Path) -> bool:
    j_file: Path = here / "OMakefile.jinja"
    outfile = out / "OMakefile"
    env: Environment = Environment()
    template = env.from_string(source=j_file.read_text(), globals={})
    old_data = get_old(outfile)
    a_logger.info(movie.scenes)
    new_data = template.render(movie=movie, scenes=movie.scenes)
    if old_data == new_data:
        a_logger.info(f"{str(outfile.absolute())} was not regenerated")
        return True
    outfile.write_text(data=new_data)
    a_logger.info(f"{str(outfile.absolute())} was regenerated")
    return False

def generate_master_tex(movie: Movie, out: Path) -> bool:
    j_file: Path = here / "master.tex.jinja"
    outfile = out / "master.tex"
    env: Environment = Environment()
    template = env.from_string(source=j_file.read_text(), globals={})
    old_data = get_old(outfile)
    a_logger.info(movie.scenes)
    def make_starts() :
        def rec_f(scenes,starts):
            if scenes==[]:
                return starts
            scene=scenes[0]
            scenes=scenes[1:]
            starts = starts + [ starts[-1]+scene.duration*scene.ips]
            return rec_f(scenes,starts)
        return rec_f(movie.scenes,[0])
    starts=make_starts()
    assert(len(starts)==len(movie.scenes)+1)
    new_data = template.render(zip=zip(movie.scenes,starts))

    if old_data == new_data:
        a_logger.info(f"{str(outfile.absolute())} was not regenerated")
        return True
    outfile.write_text(data=new_data)
    a_logger.info(f"{str(outfile.absolute())} was regenerated")
    return False

def generate_timeline(movie: Movie, out: Path) -> bool:
    j_file: Path = here / "timeline.jinja"
    outfile = out / "timeline.txt"
    env: Environment = Environment()
    template = env.from_string(source=j_file.read_text(), globals={})
    old_data = get_old(outfile)
    a_logger.info(movie.scenes)
    nb_points = reduce(lambda a,b:a+b,list(map(lambda scene:scene.duration*scene.ips,movie.scenes)),0)
    new_data = template.render(nb_points=nb_points)
    if old_data == new_data:
        a_logger.info(f"{str(outfile.absolute())} was not regenerated")
        return True
    outfile.write_text(data=new_data)
    a_logger.info(f"{str(outfile.absolute())} was regenerated")
    return False

def copy_mp(out:Path):
    from_paths = [
        "storylc/lib/slide.mp"
    ]
    def copy_one(source:str):
        source_path: Path=here.parent/source
        a_logger.info(f"copy {str(source_path.absolute())}")
        target_path:Path=out/source
        target_path.write_text(source_path.read_text())

    (out/"storylc/lib").mkdir(exist_ok=True,parents=True)
    list(map(lambda source:copy_one(source),from_paths))

def copy_src(movie:Movie,out:Path):
    def copy_one(scene:Scene):
        source_path:Path= movie.root/scene.path
        a_logger.info(f"copy {str(source_path.absolute())}")
        target_path:Path=out/"mounted"/scene.path
        target_path.write_text(source_path.read_text())

    (out/"mounted").mkdir(exist_ok=True,parents=True)
    list(map(lambda scene:copy_one(scene=scene),movie.scenes))



def generate(movie: Movie, out: Path):
    out.mkdir(exist_ok=True)
    generate_omakeroot(movie=movie, out=out)
    generate_omakefile(movie=movie, out=out)
    generate_master_tex(movie=movie, out=out)
    generate_timeline(movie=movie, out=out)
    list(map(lambda scene:generate_scene(movie=movie,scene=scene,out=out),movie.scenes))
    copy_mp(out)
    copy_src(movie=movie,out=out)
