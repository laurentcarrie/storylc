prologues:=3;
outputtemplate := "%j_%c.mps";
outputformat := "mps";



input boxes ;
input TEX ;
%input latexmp ;
input storylc/lib/slide



for i:=0 upto 10:
	beginfig(i);
		mygrid ;
		transform t ;
		t = identity shifted (0cm,3cm) scaled 1 ;
		gitremote(t,"blah",i) ;
	endfig ;
endfor;


end.
