
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

vardef produce_label(expr i) =
  "label(" & "btex $P_{" & "89" & "}$ etex, (3cm,3cm)) ;"
enddef;






def cartouche(expr i,duration,ips)=
	u:=.2cm ;
	margin:=4cm ;
	% label(btex $P_{"&decimal i&"}$ etex,(3cm,3cm)) ;
	% label(btex & decimal(i) & etex ,(3cm,3cm)) ;
    %label(TEX("$"&decimal(round(5*i))&"$"),(3cm,3cm));enddef ;
    %write produce_label(43) to "DynamicTeXLabels.tmp";
    %write EOF to "DynamicTeXLabels.tmp";
    %input DynamicTeXLabels.tmp;
    label("i=" & decimal i , (3cm,3cm)) ;
enddef ;

