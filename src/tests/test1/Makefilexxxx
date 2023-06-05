.PHONY: all clean

all:all.mp4

scene-1-0.svg : scene-1-0.mp
	mpost scene-1-0

scene-1-1.svg : scene-1-1.mp
	mpost scene-1-1

scene-1-2.svg : scene-1-2.mp
	mpost scene-1-2

scene-1-3.svg : scene-1-3.mp
	mpost scene-1-3

scene-1-4.svg : scene-1-4.mp
	mpost scene-1-4

scene-1-5.svg : scene-1-5.mp
	mpost scene-1-5

scene-1-6.svg : scene-1-6.mp
	mpost scene-1-6

scene-1-7.svg : scene-1-7.mp
	mpost scene-1-7

scene-1-8.svg : scene-1-8.mp
	mpost scene-1-8

scene-1-9.svg : scene-1-9.mp
	mpost scene-1-9

scene-1.gif: scene-1-0.svg scene-1-1.svg scene-1-2.svg scene-1-3.svg scene-1-4.svg scene-1-5.svg scene-1-6.svg scene-1-7.svg scene-1-8.svg scene-1-9.svg
	rm -f $@
	convert -delay 1 -loop 1 -size 1024x1024 scene-1-0.svg scene-1-1.svg scene-1-2.svg scene-1-3.svg scene-1-4.svg scene-1-5.svg scene-1-6.svg scene-1-7.svg scene-1-8.svg scene-1-9.svg $@

scene-1.mp4 : scene-1.gif
	rm -f $@
	ffmpeg -i scene-1.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" $@

all.mp4 :  scene-1.mp4
	rm -f $@
	ffmpeg -f concat -safe 0 -i infile.txt -c copy $@

clean:
	rm -f 
	rm -f 
	rm -f 
	rm -f all.mp4

