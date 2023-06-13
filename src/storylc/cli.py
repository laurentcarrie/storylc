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
from storylc.generate import generate
from storylc.model import Movie
from storylc.project_logs import a_logger, init_logs

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
        try:
            data = yaml.load(yml_path.read_text(), yaml.FullLoader)
        except Exception as e:
            a_logger.error(
                f"could not correctly load yaml file {yml_path.absolute()}, please check it"
            )
            raise e

        try:
            movie: Movie = from_dict(data_class=Movie, data=data)
        except Exception as e:
            a_logger.error(
                "could not convert yml data to a Movie object, please check fields"
            )
            raise e

        movie = Movie(
            root=yml_path.parent, scenes=movie.scenes, animations=movie.animations
        )
        a_logger.info(movie)
        generate(movie=movie, out=Path(out))
    except:  # noqa:E722
        traceback.print_exc()
        sys.exit(1)
