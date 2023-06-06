% Jan Holecek, Alexander Grahn
% 2022/01/25

prologues:=3;
outputtemplate := "%j_%c.mps";
outputformat := "mps";



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


vardef gitremote(expr  t)=
    u:=.2cm ;
    width:=2cm ;
    height:=5cm ;
    pair A,B,C,D ;
    A=(0,0) transformed t ;
    B=(width,0) transformed t ;;
    C=(width,height) transformed t ;;
    D-A=C-B ;

    draw A -- B -- C -- D -- cycle ;
    dotlabel.bot(btex remote repository etex,.5[A,B]) ;
    pair X,XH,XB ;
    XB = .5[A,B] ;
    XH = .5[D,C] ;
    %dotlabel.bot(btex XB etex,XB) ;
    %dotlabel.bot(btex XH etex,XH) ;

    ustep:=.1 ;
    minu:=ustep ;
    maxu:=1 ;
    r:=.2cm ;
    for i:=ustep step ustep until maxu :
        u:=i*.05cm ;
        X := i[XB,XH] ;
        draw fullcircle scaled r shifted X  ;
    endfor ;

    pair XA,XB,Y ;
    path PX,PY ;
    for i:=ustep step ustep until maxu :
        u:=i*.05cm ;
        %j:=i+ustep ;
        X := i[XB,XH] ;
        draw origin -- X ;
        %PX := fullcircle scaled r shifted X ;
        %draw  fullcircle scaled r shifted X ;
        %Y := j[XB,XH] ;
        %PB:=fullcircle scaled r shifted Y  ;
    endfor ;

enddef ;


i:=0;
beginfig(i);
    mygrid ;
    transform t ;
    t = identity shifted (0cm,3cm) ;
    gitremote(t) ;
    circleit.a(btex Box 1 etex) ;
    drawshadowed(a) ;
endfig ;

i:=i+1;
beginfig(i);
    mygrid ;
    circleit.a(btex Box 1 etex) ;
    drawshadowed(a) ;
    transform t ;
    t = identity rotated 45 scaled .1 ;
    gitremote(t) ;
endfig ;

beginfig(2);
    mygrid ;
    circleit.a(btex Box 1 etex) ;
    circleit.b(btex Box 2 etex) ;
    b.s = a.n + (0,2cm) ;
    drawshadowed(a,b) ;
    drawarrow a.n -- b.s ;
endfig ;


hppp := 0.25;
vppp := 0.25;
uu:=0.5cm;
vardef fun (expr x)=
  (x**2)*uu/10
enddef;

beginfig(3)
  for i:=0 upto 10:
    draw (0,i*u)--(10u,i*u);
    draw (i*u,0)--(i*u,10u);
    %label.bot(TEX("$x_{"& decimal(i) &"}$"),(i*u,0));
    %label.bot(btex hello etex);
  endfor;
  draw (0,0) for i:=1 upto 10: ..(i*u,fun(i)) endfor;
endfig;

end.
