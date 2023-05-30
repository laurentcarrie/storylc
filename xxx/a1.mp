outputformat := "svg";
outputtemplate := "%j-%c.svg";

color gray; gray := 0.6white;
pair p[];
p0 = (0,0); p1 = (2u,3u); p2 = (3u,2u);

def drawpoint(expr z, c) = draw z
withpen pencircle scaled 3 withcolor c;
enddef;

v:=10cm ;
def drawouterframe(expr x) =
draw (v,v) -- (-v,v) -- (-v,-v) -- (v,-v) -- cycle ;
enddef;

beginfig(1);
u := 1.25cm;

pair O,A,B,C,D ;
O:=(0,0) ;
A:=(u,0) ;
B:=(0,u) ;
C:=(-u,0) ;
D:=(0,-u) ;

draw A .. B .. C .. D .. cycle ;
fill A -- B -- C -- D -- cycle withcolor green ;

drawouterframe(0) ;


endfig;


beginfig(2);
u := 2.25cm;

pair O,A,B,C,D ;
O:=(0,0) ;
A:=(u,0) ;
B:=(0,u) ;
C:=(-u,0) ;
D:=(0,-u) ;

draw  A .. B .. C .. D .. cycle ;
drawouterframe(0) ;

endfig;




beginfig(3);
u := 1.25cm;

pair O,A,B,C,D ;
O:=(u,0) ;
A:=(2*u,0) ;
B:=(u,u) ;
C:=(0,0) ;
D:=(u,-u) ;

draw A .. B .. C .. D .. cycle ;
fill A -- B -- C -- D -- cycle withcolor red ;


drawouterframe(0) ;

endfig;

end;