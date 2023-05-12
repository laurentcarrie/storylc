#!/usr/bin/env sh

here=$(dirname $(realpath $0))
version_file="$here/VERSION.bumped"
current=$(cat $version_file)

date +%Y.%m.%d > $version_file

new=$(cat $version_file)

if test "x$new" == "x$current" ; then
  exit 0
else
  exit 1
fi
