from typing import Iterator, List, Tuple

from storylc.getters import get_animation
from storylc.model import Animation, Layer, Movie, Scene


def image_id_of_triplets(movie: Movie, scene: Scene) -> Iterator[Tuple[int, str, int]]:
    count = 0
    for layer in scene.layers:
        for i in range(layer.animation.duration * layer.animation.ips):
            yield (count, layer.animation.name, i)
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
        return f"{now[0][0]}"

    ips = 20

    def one_row(i: int) -> str:
        layer: Layer  # noqa:F842
        return ";".join(
            list(
                map(
                    lambda layer: layer_of_anim_and_row(
                        row=i, anim_name=layer.animation.name
                    ),
                    scene.layers,
                )
            )
        )

    return list(map(one_row, range(scene.duration * ips)))
