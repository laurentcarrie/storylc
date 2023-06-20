input boxes ;
input TEX ;
%input latexmp ;
input storylclib/slide ;



vardef main(expr i,duration,ips)=
		mygrida(i) ;
		%transform t ;
		%t = identity shifted (0cm,3cm) scaled 1 ;
		%gitremote(t,"blah",0) ;
		path a,b;
		pair o;
		a := fullcircle scaled 2cm ;
		fill a withcolor .2white ;
		j:=i/duration/ips ;
		o := dir(-j*360) * 2cm ;
		%o := dir(45) * 2cm ;
		b:= fullcircle scaled .5cm shifted o ;
		k:=i / duration / ips ;
		t:=i/ips ;
		fill b withcolor (0,0,1) ;
enddef ;
