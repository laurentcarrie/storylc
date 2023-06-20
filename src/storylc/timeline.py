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

    # first int : the mps number
    # second str : the name of the animation
    # third int : the frame number in the anim
    triplets: List[Tuple[int, str, int]] = list(
        image_id_of_triplets(movie=movie, scene=scene)
    )

    def layer_of_anim_and_row(row: int, anim_name: str) -> str:
        now: List[Tuple[int, str, int]] = list(
            filter(lambda x: x[2] == row and x[1] == anim_name, triplets)
        )
        assert len(now) == 1
        return str(now[0][0])

    ips = 20

    def one_row(i: int) -> str:
        layer: Layer  # noqa:F842
        return ";".join(
            list(
                map(
                    lambda layer: layer_of_anim_and_row(
                        row=i, anim_name=layer.animations[0].animation_name
                    ),
                    scene.layers,
                )
            )
        )

    return list(map(one_row, range(scene.duration * ips)))
