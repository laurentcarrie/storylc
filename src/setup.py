import os
from datetime import datetime
from pathlib import Path
from typing import List

from setuptools import find_packages, setup  # type: ignore

entry_points: List[str] = [
    "story-lc=storylc.cli:main",
]


def get_requires() -> List[str]:
    return (here / "requirements.txt").read_text().split("\n")


here = Path(__file__).parent.absolute()
rootdir = here.parent

version = os.getenv("wheel_version", None)
print(f"...................... version {version}")

if version is None:
    print("no version provided, it should come from the environment")
    version = "0.0.0"

branch = os.getenv("branch", os.getenv("USER", "what-no-user"))
product_name = "storylc"

setup(
    name=product_name,
    version=version,
    packages=find_packages(exclude=["tests"]),
    entry_points={"console_scripts": entry_points},
    install_requires=get_requires(),
    extras_require={},
    package_dir={"pluto": "pluto"},
    package_data={
        "pluto": [
            "logging.yml",
            "py.typed",
            "*.pyi",
            "**/*.pyi",
            "run.sh",
            "**/*.jinja",
            "airflow/.env",
            "airflow/configs/nginx.conf",
        ]
    },
    description=(rootdir / "README.md").read_text(),
    long_description=(rootdir / "README.md").read_text(),
)
