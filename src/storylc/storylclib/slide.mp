
input boxes ;
input TEX ;

verbatimtex
\documentclass{article}
%\usepackage{lmodern}
  \usepackage[tt=false]{libertine}
  \usepackage[libertine]{newtxmath}
\usepackage{amsmath}
\begin{document}
etex



vardef drawshadowed(text t) =
	fixsize(t) ;
	forsuffixes s=t :
		fill bpath.s shifted (1pt,-1pt) ;
		unfill bpath.s ;
		drawboxed(s) ;
	endfor
enddef ;

def mygrida(expr t)=
	u:=.2cm ;
	margin:=4cm ;
	draw (-margin,-margin) -- (-margin,margin) -- (margin,margin) -- (margin,-margin)  withcolor white	;
	 label(decimal t,(-margin,-margin)/2) ;
	%draw textext("cycle " & decimal t) shifted (-margin,-margin)/2  ;
enddef ;


def mygrid=
	u:=.2cm ;
	margin:=4cm ;
	for y=(-margin) step u until margin:
		draw (-margin,y) -- (margin,y) withcolor 0.8white ;
	endfor;
	for x=(-margin) step u until margin:
		draw (x,-margin) -- (x,margin) withcolor 0.8white;
	endfor;
enddef ;


vardef gitremote(expr  t,name,nbnodes)=
	width:=2cm ;
	height:=15cm ;
	pair A,B,C,D ;
	A=(0,0) transformed t ;
	B=(width,0) transformed t ;
	C=(width,height) transformed t ;
	D-A=C-B ;

	draw A -- B -- C -- D -- cycle ;
	dotlabel.bot(btex remote repository etex,.5[A,B]) ;
	label.bot(btex name etex,.5[A,B]) ;
	pair X,Y,XH,XB ;
	XB = .5[A,B] ;
	XH = .5[D,C] ;
	%dotlabel.bot(btex XB etex,XB) ;
	%dotlabel.bot(btex XH etex,XH) ;

	ustep:=1cm ;
	r:=.4cm * xxpart t ;
	path p[] ;
	pair a[] ;
	y := ustep ;
	pair I,J ;
	for i=1 step 1 until nbnodes :
		%forever : exitunless ypart I < ypart XH ;
		%for i:=ustep step ustep until maxu-ustep :
		I := XB shifted (0,i*ustep) ;
		J := XB shifted (0,(i+1)*ustep) ;
		p1 := fullcircle scaled r shifted I  ;
		draw p1 ;
		p2 := fullcircle scaled r shifted J  ;
		%draw p2 ;
		a1 := I shifted (0,r/2) ;
		%dotlabel.lft(btex a1 etex,a1)  ;
		%dotlabel.lft(btex X etex,X)  ;
		%dotlabel.lft(btex Y etex,Y)  ;
		label.rt(btex \small{commit} etex,I shifted(r/2,0)) ;

		a2 := J shifted (0,-r/2) ;
		drawarrow a1 -- a2 ;
		%drawarrow X -- Y ;

	endfor ;

	J := XB shifted (0,(nbnodes+1)*ustep) ;
	p2 := fullcircle scaled r shifted J  ;
	draw p2 ;
	label.rt(btex \small{HEAD} etex,J shifted(r/2,0)) ;

enddef ;


%for i:=0 upto 10:
%	beginfig(i);
%		mygrid ;
%		transform t ;
%		t = identity shifted (0cm,3cm) scaled 1 ;
%		gitremote(t,"blah",i) ;
%		circleit.a(btex Box 1 etex) ;
%		drawshadowed(a) ;
%	endfig ;
%endfor;
