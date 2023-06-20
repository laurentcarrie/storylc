from typing import Iterator, List, Tuple

from storylc.getters import get_animation
from storylc.model import Animation, Layer, Movie, Scene

def image_id_of_triplets(
    movie: Movie, scene: Scene
) -> Iterator[Tuple[int, str, int]]: ...
def timeline_of_scene(movie: Movie, scene: Scene) -> List[str]: ...
