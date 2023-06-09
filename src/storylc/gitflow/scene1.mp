input boxes ;
input TEX ;
%input latexmp ;
%input storylc/lib/slide


vardef scene(expr i)=
		%mygrid ;
		%transform t ;
		%t = identity shifted (0cm,3cm) scaled 1 ;
		%gitremote(t,"blah",0) ;
		path a;
		a = fullcircle scaled 2cm ;
		fill a withcolor .7white ;
		draw origin -- (i*1cm,i*3cm) ;
enddef ;

