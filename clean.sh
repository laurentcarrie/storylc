#!/bin/sh

set -e
set -x

clean() {
  find . -wholename "$1" | while read f; do
    echo $f
    rm -rf $f
  done
}

rm -rf src/build
rm -rf src/dist
clean build
clean lib
clean "*egg-info"
clean "*whl"
clean ".pytest_cache"
clean "dist"
clean ".mypy_cache"
clean "__pycache__"
clean "*.pyc"
clean "*tmp*"
clean "*.log"
