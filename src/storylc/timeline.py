from typing import Iterator, List, Tuple

from storylc.getters import animations_of_layer, get_animation
from storylc.model import Animation, AnimationTimeLine, Layer, Movie, Scene


def image_id_of_triplets(movie: Movie, scene: Scene) -> Iterator[Tuple[int, str, int]]:
    l_animations: List[List[Animation]] = list(
        map(lambda layer: animations_of_layer(movie=movie, layer=layer), scene.layers)
    )

    count = 0
    for la in l_animations:
        for anim in la:
            for i in range(anim.duration * anim.ips + 1):
                yield (count, anim.name, i)
                count += 1


def timeline_of_scene(movie: Movie, scene: Scene) -> List[str]:

    ips = 10  # 10 images per second

    def row_of_layer(i: int, layer: Layer) -> str:
        return ",".join(
            list(
                map(
                    lambda anim: str(i + anim.start),
                    animations_of_layer(movie=movie, layer=layer),
                )
            )
        )

    def row(i: int) -> str:
        return ";".join(list(map(lambda layer: row_of_layer(i, layer), scene.layers)))

    return list(map(row, range(scene.duration * ips)))
