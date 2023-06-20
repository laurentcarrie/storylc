from pathlib import Path

from jinja2 import Environment, PackageLoader, select_autoescape  # type:ignore
from typing import List

from storylc.model import Movie, Scene, Animation, AnimationTimeLine, Layer
from storylc.project_logs import a_logger

here = Path(__file__).absolute().parent

def get_old(outfile: Path) -> str: ...
def generate_omakeroot(movie: Movie, out: Path) -> bool: ...
def generate_omakefile(movie: Movie, out: Path) -> bool: ...
def generate(movie: Movie, out: Path): ...
def copy_src(movie: Movie, out: Path): ...
def copy_mp(out: Path): ...
def generate_omakefile_scene(movie: Movie, scene: Scene, out: Path) -> bool: ...
def generate_master_tex(movie: Movie, out: Path) -> bool: ...
def generate_omakefile_mps(movie: Movie, out: Path) -> bool: ...
def make_starts(animations: List[Animation]) -> List[int]: ...
def fix_start(movie) -> Movie: ...
def generate_timeline_animation(animation: Animation, out: Path) -> bool: ...
def generate_animation(movie: Movie, animation: Animation, out: Path): ...
def generate_omakefile_animation(animation: Animation, out: Path) -> bool: ...
def generate_for_animation(movie: Movie, animation: Animation, out: Path) -> None: ...
def generate_animation_tex(animation: Animation, out: Path) -> None: ...
def generate_for_scene(movie: Movie, scene: Scene, out: Path) -> None: ...
def generate_scene_tex(movie: Movie, scene: Scene, out: Path) -> bool: ...
def generate_timeline_scene(movie: Movie, scene: Scene, out: Path) -> bool: ...

# def make_layer_timelines(movie: Movie, layer: Layer) -> str: ...
# def interpol(al: AnimationTimeLine, t: float) -> float: ...
# def check_interpol(al: AnimationTimeLine) -> None: ...
