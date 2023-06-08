outputformat := "svg";
%outputtemplate := "%j-%c.svg";
outputtemplate := "%j.svg";

color gray; gray := 0.6white;
pair p[];
p0 = (0,0); p1 = (2u,3u); p2 = (3u,2u);

def drawpoint(expr z, c) = draw z
withpen pencircle scaled 3 withcolor c;
enddef;


def run(expr t) =
v:=10cm ;

u := t * 1cm ;

pair O,A,B,C,D ;
O:=(0,0) ;
A:=(u,0) ;
B:=(0,u) ;
C:=(-u,0) ;
D:=(0,-u) ;

draw A .. B .. C .. D .. cycle ;
fill A -- B -- C -- D -- cycle withcolor green ;

%drawouterframe(0) ;


enddef;
