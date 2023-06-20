from typing import List, Optional

from storylc.model import Animation, Layer, Movie


def get_animation(movie: Movie, name: str) -> Animation:
    anim: Optional[Animation] = None
    for anim in movie.animations:
        if anim.name == name:
            break
    else:
        raise RuntimeError(f"no such animation {name}")
    return anim


def animation_of_layer(movie: Movie, layer: Layer) -> Animation:
    return get_animation(movie=movie, name=layer.animation_name)
