input boxes ;
input TEX ;
%input latexmp ;
input storylclib/slide ;



vardef main(expr i,duration,ips)=
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
		t:=i/ips ;
		fill b withcolor (k,1-k,0) ;
enddef ;

vardef main_b(expr i,duration,ips)=
		k:=i / duration / ips ;
		t:=i/ips ;
        label("i=" & decimal i & "", (-5cm, 0));
        label("k=" & decimal k & "", (-5cm, -.3cm));
        label("t=" & decimal t & " s", (-5cm, -.6cm));
enddef ;
