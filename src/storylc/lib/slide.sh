#!/usr/bin/env sh

set -e
set -x

here=$(dirname $(realpath $0))

( cd $here && mpost slide )
( cd $here && pdflatex slide && pdflatex slide )

