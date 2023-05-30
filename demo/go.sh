#!/usr/bin/env sh

set -e
set -x

here=$(dirname $(realpath $0))

old_makefile=$(cat $here/Makefile)

ret=$(python $here/gitflow.py)

new_makefile=$(cat $here/Makefile)

if test "x$old_makefile" != "x$new_makefile" ; then
  make -C $here clean
fi




make -C $here

mplayer all.mp4



