from functools import reduce
from pathlib import Path
from typing import List

from jinja2 import Environment, PackageLoader, select_autoescape  # type:ignore
from storylc.model import Animation, Movie, Scene
from storylc.project_logs import a_logger

here = Path(__file__).absolute().parent


def get_old(outfile: Path):
    match outfile.exists():
        case True:
            return outfile.read_text()
        case False:
            return ""


def animation_of_name(movie:Movie,name:str) -> Animation:
    for a in movie.animations:
        if a.name == name:
            return a
    raise RuntimeError(f"no such animation : '{name}'")

def make_starts(movie: Movie) -> List[int]:
    def rec_f(animations: List[Animation], starts: List[int]) -> List[int]:
        if animations == []:
            return starts
        animation = animations[0]
        animations = animations[1:]
        starts = starts + [starts[-1] + animation.duration * animation.ips + 1]
        return rec_f(animations, starts)

    return rec_f(movie.animations, [0])


def generate_omakeroot(movie: Movie, out: Path) -> bool:
    j_file: Path = here / "jinja/OMakeroot.jinja"
    outfile = out / "OMakeroot"
    env: Environment = Environment()
    template = env.from_string(source=j_file.read_text(), globals={})
    old_data = get_old(outfile)
    new_data = template.render(
        libdir=str(here.absolute()), movie=movie, srcdir=str(movie.root.absolute())
    )
    if old_data == new_data:
        a_logger.info(f"{str(outfile.absolute())} was not regenerated")
        return True
    outfile.write_text(data=new_data)
    a_logger.info(f"{str(outfile.absolute())} was regenerated")
    return False


def generate_animation(movie: Movie, animation: Animation, out: Path):
    j_file: Path = here / "jinja/animation.mp.jinja"
    outfile = out / f"tmp-animation-{animation.name}/animation.mp"
    (outfile.parent).mkdir(exist_ok=True)
    env: Environment = Environment()
    template = env.from_string(source=j_file.read_text(), globals={})
    old_data = get_old(outfile)
    new_data = template.render(movie=movie, animation=animation)
    if old_data == new_data:
        a_logger.info(f"{str(outfile.absolute())} was not regenerated")
        return True
    outfile.write_text(data=new_data)
    a_logger.info(f"{str(outfile.absolute())} was regenerated")
    return False


def generate_omakefile(movie: Movie, out: Path) -> bool:
    a_logger.info("generate master OMakefile")
    j_file: Path = here / "jinja/OMakefile.jinja"
    outfile = out / "OMakefile"
    env: Environment = Environment()
    template = env.from_string(source=j_file.read_text(), globals={})
    old_data = get_old(outfile)
    a_logger.info(movie.scenes)
    starts = make_starts(movie)
    # nb_images = starts[-1]
    new_data = template.render(
        movie=movie,
        scenes=movie.scenes,
        zip=zip(movie.scenes, starts),
        # nb_images=nb_images,
    )
    if old_data == new_data:
        a_logger.info(f"{str(outfile.absolute())} was not regenerated")
        return True
    outfile.write_text(data=new_data)
    a_logger.info(f"{str(outfile.absolute())} was regenerated")
    return False


def generate_omakefile_scene(movie: Movie, scene: Scene, out: Path) -> bool:
    a_logger.info(f"generate omakefile for scene {scene.name}")
    j_file: Path = here / "jinja/OMakefile_scene.jinja"
    outfile = out / f"tmp-scene-{scene.name}/OMakefile"
    (outfile.parent).mkdir(exist_ok=True)
    env: Environment = Environment()
    template = env.from_string(source=j_file.read_text(), globals={})
    old_data = get_old(outfile)
    new_data = template.render(movie=movie, scene=scene)
    if old_data == new_data:
        a_logger.info(f"{str(outfile.absolute())} was not regenerated")
        return True
    outfile.write_text(data=new_data)
    a_logger.info(f"{str(outfile.absolute())} was regenerated")
    return False


def generate_omakefile_animation(animation: Animation, out: Path) -> bool:
    a_logger.info(f"generate omakefile for animation {animation.name}")
    j_file: Path = here / "jinja/OMakefile_animation.jinja"
    outfile = out / f"tmp-animation-{animation.name}/OMakefile"
    (outfile.parent).mkdir(exist_ok=True)
    env: Environment = Environment()
    template = env.from_string(source=j_file.read_text(), globals={})
    old_data = get_old(outfile)
    new_data = template.render(libdir=str(here.absolute()), animation=animation)
    if old_data == new_data:
        a_logger.info(f"{str(outfile.absolute())} was not regenerated")
        return True
    outfile.write_text(data=new_data)
    a_logger.info(f"{str(outfile.absolute())} was regenerated")
    return False


def generate_animation_tex(animation: Animation, out: Path) -> bool:
    a_logger.info(f"generate master.tex for animation {animation.name}")
    j_file: Path = here / "jinja/animation.tex.jinja"
    outfile = out / f"tmp-animation-{animation.name}/animation.tex"
    (outfile.parent).mkdir(exist_ok=True)
    env: Environment = Environment()
    template = env.from_string(source=j_file.read_text(), globals={})
    old_data = get_old(outfile)
    new_data = template.render(libdir=str(here.absolute()), animation=animation)
    if old_data == new_data:
        a_logger.info(f"{str(outfile.absolute())} was not regenerated")
        return True
    outfile.write_text(data=new_data)
    a_logger.info(f"{str(outfile.absolute())} was regenerated")
    return False


def generate_scene_tex(scene: Scene, out: Path) -> bool:
    a_logger.info(f"generate master.tex for scene {scene.name}")
    j_file: Path = here / "jinja/scene.tex.jinja"
    outfile = out / f"tmp-scene-{scene.name}/scene.tex"
    (outfile.parent).mkdir(exist_ok=True)
    env: Environment = Environment()
    template = env.from_string(source=j_file.read_text(), globals={})
    old_data = get_old(outfile)
    new_data = template.render(libdir=str(here.absolute()), scene=scene)
    if old_data == new_data:
        a_logger.info(f"{str(outfile.absolute())} was not regenerated")
        return True
    outfile.write_text(data=new_data)
    a_logger.info(f"{str(outfile.absolute())} was regenerated")
    return False


def generate_omakefile_mps(movie: Movie, out: Path) -> bool:
    a_logger.info("generate omakefile mps")
    j_file: Path = here / "jinja/OMakefile_mps.jinja"
    outfile = out / "mps/OMakefile"
    (outfile.parent).mkdir(exist_ok=True, parents=True)
    env: Environment = Environment()
    template = env.from_string(source=j_file.read_text(), globals={})
    old_data = get_old(outfile)
    starts = make_starts(movie)
    new_data = template.render(movie=movie, zip=zip(movie.animations, starts))
    if old_data == new_data:
        a_logger.info(f"{str(outfile.absolute())} was not regenerated")
        return True
    outfile.write_text(data=new_data)
    a_logger.info(f"{str(outfile.absolute())} was regenerated")
    return False


def generate_master_tex(movie: Movie, out: Path) -> bool:
    a_logger.info("generate master.tex")
    j_file: Path = here / "jinja/master.tex.jinja"
    outfile = out / "master.tex"
    env: Environment = Environment()
    template = env.from_string(source=j_file.read_text(), globals={})
    old_data = get_old(outfile)
    a_logger.info(movie.scenes)

    starts = make_starts(movie)
    a_logger.info(starts)
    # assert len(starts) == len(movie.scenes) + 1
    new_data = template.render(zip=zip(movie.scenes, starts))

    if old_data == new_data:
        a_logger.info(f"{str(outfile.absolute())} was not regenerated")
        return True
    outfile.write_text(data=new_data)
    a_logger.info(f"{str(outfile.absolute())} was regenerated")
    return False


def generate_timeline_animation(animation: Animation, out: Path) -> bool:
    j_file: Path = here / "jinja/timeline_animation.jinja"
    outfile = out / f"tmp-animation-{animation.name}/timeline.txt"
    env: Environment = Environment()
    template = env.from_string(source=j_file.read_text(), globals={})
    old_data = get_old(outfile)
    new_data = template.render(animation=animation)
    if old_data == new_data:
        a_logger.info(f"{str(outfile.absolute())} was not regenerated")
        return True
    outfile.write_text(data=new_data)
    a_logger.info(f"{str(outfile.absolute())} was regenerated")
    return False


def generate_timeline_scene(scene: Scene, out: Path) -> bool:
    j_file: Path = here / "jinja/timeline_scene.jinja"
    outfile = out / f"tmp-scene-{scene.name}/timeline.txt"
    env: Environment = Environment()
    template = env.from_string(source=j_file.read_text(), globals={})
    old_data = get_old(outfile)
    # animations:List[Animation] = list(map(lambda a:animation_of_name(a.name),
    #                                       scene.animations))
    new_data = template.render(scene=scene,zip=zip(scene.animations,[]))
    if old_data == new_data:
        a_logger.info(f"{str(outfile.absolute())} was not regenerated")
        return True
    outfile.write_text(data=new_data)
    a_logger.info(f"{str(outfile.absolute())} was regenerated")
    return False


def copy_mp(out: Path):
    from_paths = ["storylc/lib/slide.mp"]

    def copy_one(source: str):
        source_path: Path = here.parent / source
        a_logger.info(f"copy {str(source_path.absolute())}")
        target_path: Path = out / source
        target_path.write_text(source_path.read_text())

    (out / "storylc/lib").mkdir(exist_ok=True, parents=True)
    list(map(lambda source: copy_one(source), from_paths))


def copy_src(movie: Movie, out: Path):
    def copy_for_one_sandbox(sandbox: Path):
        def copy_one(animation: Animation):
            source_path: Path = movie.root / animation.path
            a_logger.info(f"copy {str(source_path.absolute())}")
            target_path: Path = sandbox / animation.path
            target_path.write_text(source_path.read_text())

        sandbox.mkdir(exist_ok=True, parents=True)
        list(map(lambda animation: copy_one(animation=animation), movie.animations))

    list(
        map(
            lambda animation: copy_for_one_sandbox(
                sandbox=out / ("tmp-animation-" + animation.name) / "mounted"
            ),
            movie.animations,
        )
    )


def generate_for_animation(movie: Movie, animation: Animation, out: Path) -> None:
    generate_omakefile_animation(animation=animation, out=out)
    generate_animation_tex(animation=animation, out=out)
    generate_animation(movie=movie, animation=animation, out=out)
    generate_timeline_animation(animation=animation, out=out)


def generate_for_scene(movie: Movie, scene: Scene, out: Path) -> None:
    generate_omakefile_scene(movie=movie, scene=scene, out=out)
    generate_scene_tex(scene=scene, out=out)
    # generate_animation_tex(animation=animation, out=out)
    # generate_animation(movie=movie, animation=animation, out=out)
    generate_timeline_scene(scene=scene, out=out)


def generate(movie: Movie, out: Path):
    out.mkdir(exist_ok=True)
    generate_omakeroot(movie=movie, out=out)
    generate_omakefile(movie=movie, out=out)
    list(
        map(
            lambda animation: generate_for_animation(
                movie=movie, animation=animation, out=out
            ),
            movie.animations,
        )
    )
    list(
        map(
            lambda scene: generate_for_scene(movie=movie, scene=scene, out=out),
            movie.scenes,
        )
    )
    generate_omakefile_mps(movie=movie, out=out)
    # generate_master_tex(movie=movie, out=out)
    # generate_timeline(movie=movie, out=out)
    # list(
    #     map(
    #         lambda animation: generate_animation(
    #             movie=movie, animation=animation, out=out
    #         ),
    #         movie.animations,
    #     )
    # )
    # list(
    #     map(
    #         lambda scene: generate_omakefile_scene(scene=scene, out=out),
    #         movie.scenes,
    #     )
    # )
    # copy_mp(out)
    copy_src(movie=movie, out=out)
