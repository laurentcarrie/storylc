#!/usr/bin/env sh

set -e
set -x

perl svgpath2ps.pl test.svg > single.ps
ps2pdf single.ps > multi.ps 2>&1 # also writes `single.pdf' which we do not use further
ps2pdf multi.ps # creates `multi.pdf' we animate in the next step
pdflatex animatepath.tex
pdflatex animatepath.tex
