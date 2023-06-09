input boxes ;
input TEX ;
%input latexmp ;
input storylc/lib/slide ;


vardef scene(expr i,duration,ips)=
		mygrid ;
		%transform t ;
		%t = identity shifted (0cm,3cm) scaled 1 ;
		%gitremote(t,"blah",0) ;
		path a,b;
		pair o;
		a := fullcircle scaled 2cm ;
		fill a withcolor .2white ;
		o := dir(i*360/duration/ips) * 2cm ;
		b:= fullcircle scaled .5cm shifted o ;
		fill b withcolor .9white ;
		%label("x",o) ;

enddef ;

