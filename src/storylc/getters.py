from typing import List, Optional

from storylc.model import Animation, AnimationTimeLine, Layer, Movie


def get_animation(movie: Movie, name: str) -> Animation:
    anim: Optional[Animation] = None
    for anim in movie.animations:
        if anim.name == name:
            break
    else:
        raise RuntimeError(f"no such animation {name}")
    return anim


def animations_of_layer(movie: Movie, layer: Layer) -> List[Animation]:
    al: AnimationTimeLine  # noqa:F842
    return list(
        map(
            lambda al: get_animation(movie=movie, name=al.animation_name),
            layer.animations,
        )
    )
