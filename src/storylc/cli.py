import dataclasses
import importlib
import sys
import traceback
from pathlib import Path

import click
import pluto
import yaml
from dacite import from_dict  # type:ignore
from jinja2 import Environment, PackageLoader, select_autoescape  # type:ignore
from storylc.model import Movie
from storylc.project_logs import init_logs, a_logger
from storylc.generate import generate

here = Path(__file__).absolute().parent



@click.group()
def main():
    pass


@main.command("generate")
@click.option("--yml", type=str, required=True, help="yaml input file")
@click.option("--out", type=str, required=True, help="the directory where to generate")
def _generate(out: str, yml: str):
    try:
        Path("logs").mkdir(exist_ok=True)
        init_logs()
        yml_path = Path(yml)
        data = yaml.load(yml_path.read_text(), yaml.FullLoader)
        movie: Movie = from_dict(data_class=Movie, data=data)
        movie = Movie(root=yml_path.parent,scenes=movie.scenes)
        a_logger.info(movie)
        generate(movie=movie,out=Path(out))
    except:  # noqa:E722
        traceback.print_exc()
        sys.exit(1)
