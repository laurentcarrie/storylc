input boxes ;
input TEX ;
%input latexmp ;
input storylclib/slide ;



vardef main(expr i,duration,ips)=

	k:=i / duration / ips ;
	t:=i/ips ;

	mygrida(i) ;
	path a,b;
	pair o;
	pair c ;

	transform tr ;

	c := (0,k * 4cm *k) ;

	tr = identity scaled  (.1 * k + 1-k) shifted c;


	%o := dir(-k*360) * 2cm ;
	o := dir(-k*360) * 2cm transformed tr ;

	%a := fullcircle scaled 2cm ;
	a := fullcircle scaled 2cm transformed tr ;
	fill a withcolor .2white ;
	%b:= fullcircle scaled .5cm shifted o ;
	b:= fullcircle scaled .5cm shifted o transformed tr  ;
	fill b withcolor (0,0,1) ;

enddef ;
