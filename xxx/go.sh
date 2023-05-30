#!/usr/bin/env sh

set -e
set -x
here=$(dirname $(realpath $0))

( cd $here && rm -f *.1 *.2 *.log *.aux )

(
  cd $here ;
  rm -f *.svg
  rm -f *.mp4
  rm -f *.gif
  mpost a1
  ls *.svg
  convert -delay 10 -loop 0 -size 1024x1024 \
    a1-1.svg a1-2.svg a1-1.svg \
    a1-1.svg a1-2.svg a1-1.svg \
    a1-1.svg a1-2.svg a1-1.svg \
    a1-1.svg a1-2.svg a1-1.svg \
    a1-1.svg a1-2.svg a1-1.svg \
    a1-1.svg a1-2.svg a1-1.svg \
    a1-1.svg a1-2.svg a1-1.svg \
    a1-1.svg a1-2.svg a1-1.svg \
    a1-1.svg a1-2.svg a1-1.svg \
    a1-1.svg a1-2.svg a1-1.svg \
    a1-1.svg a1-2.svg a1-1.svg \
    a1-1.svg a1-2.svg a1-1.svg \
    a1-1.svg a1-2.svg a1-1.svg \
    a1-1.svg a1-2.svg a1-1.svg \
    a1-1.svg a1-2.svg a1-1.svg \
    a1-1.svg a1-2.svg a1-1.svg \
    a1-1.svg a1-2.svg a1-1.svg \
    a1-1.svg a1-2.svg a1-1.svg \
    a1-1.svg a1-2.svg a1-1.svg \
    outfile-1.gif
  convert -delay 20 -loop 0 -size 1024x1024 a1-1.svg a1-2.svg a1-1.svg a1-3.svg outfile-2.gif
  convert -delay 20 -loop 0 -size 1024x1024 a1-1.svg a1-2.svg a1-1.svg a1-3.svg outfile-3.gif

  ffmpeg -i outfile-1.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" outfile-1.mp4
  ffmpeg -i outfile-2.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" outfile-2.mp4
  ffmpeg -i outfile-3.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" outfile-3.mp4

  ffmpeg -f concat -safe 0 -i filelist.txt -c copy outfile.mp4

  #ffmpeg -f gif -i outfile.gif outfile.mp4
)
