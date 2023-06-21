
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

% this function is from http://www.ursoswald.ch/metapost/tutorial/DynamicTeXLabels.html
vardef produce_label(expr i, n) =
  if     i=0:    s:="dotlabel.rt";
  elseif i=n/4:  s:="dotlabel.top";
  elseif i=n/2:  s:="dotlabel.lft";
  elseif i=3n/4: s:="dotlabel.bot";
  elseif i‹n/4:  s:="dotlabel.urt";
  elseif i‹n/2:  s:="dotlabel.ulft";
  elseif i‹3n/4: s:="dotlabel.llft";
  else:          s:="dotlabel.lrt";
  fi
  s&"(btex $P_{"&decimal i&"}$ etex, z["&decimal i&"]);"
enddef;


def cartouche(expr i,duration,ips)=
	u:=.2cm ;
	margin:=4cm ;
enddef ;
