% Jan Holecek, Alexander Grahn
% 2022/01/25

prologues:=3;
outputtemplate := "%j_%c.mps";
outputformat := "mps";



input boxes ;

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


def gitremote=
    circleit.a(btex remote etex)
enddef;

i:=0;
beginfig(i);
    mygrid ;
    gitremote;
    circleit.a(btex Box 1 etex) ;
    drawshadowed(a) ;
endfig ;

i:=i+1;
beginfig(i);
    mygrid ;
    circleit.a(btex Box 1 etex) ;
    drawshadowed(a) ;
endfig ;

beginfig(2);
    mygrid ;
    circleit.a(btex Box 1 etex) ;
    circleit.b(btex Box 2 etex) ;
    b.s = a.n + (0,2cm) ;
    drawshadowed(a,b) ;
    drawarrow a.n -- b.s ;
endfig ;



end.
