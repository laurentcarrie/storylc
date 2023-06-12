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
		j:=i/duration/ips ;
		o := dir(j*360) * 2cm ;
		%o := dir(45) * 2cm ;
		b:= fullcircle scaled .5cm shifted o ;
		k:=i / duration / ips ;
		fill b withcolor (k,1-k,0) ;
		%label("x",o) ;
		label(decimal j,origin) ;
		label(decimal i,(-5cm,0)) ;

enddef ;
