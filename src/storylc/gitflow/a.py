from pathlib import Path

import yaml
from storylc.model import Movie, Scene


def main():
    s = Path("x.yml")
    m = Movie(scenes=[Scene(name="xx", duration=42, path="ua path")])

    s.write_text(yaml.dump(m))


if __name__ == "__main__":
    main()
