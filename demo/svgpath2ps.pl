#!/usr/bin/perl
$header=0;
$strokewd=1;
$strokelc=0;
$strokelj=0;
while(<>){
  chomp;
  if (/viewBox\s*=\s*"([0-9]+) ([0-9]+) ([0-9]+) ([0-9]+)"/){($ulx,$uly,$lrx,$lry)=($1,$2,$3,$4);}
  if (/width\s*=\s*"([0-9]+)"/){$wd=$1;}
  if (/height\s*=\s*"([0-9]+)"/){$ht=$1;}
  if (/stroke-width:\s*([^;\s]+)/){$strokewd=$1;}
  if (/stroke-linejoin:\s*round/){$strokelj=1;}
  if (/stroke-linejoin:\s*bevel/){$strokelj=2;}
  if (/stroke-linecap:\s*square/){$strokelc=2;}
  if (/stroke-linecap:\s*round/){$strokelc=1;}
  if (/<path.* d\s*=\s*/) {
    if (!$header){
      $header=1;
      print "%!PS-Adobe-3.0\n",
            "%%BoundingBox: $ulx $uly $lrx $lry\n",
            "%%EndComments\n",
            "/curpage 0 def\n",
            "/curpath [{}] def\n",
            "/setbbox {pop pop pop pop} def\n",
            "/printany {0 cvs print flush} def /printany load 0 256 string put\n",
            "/typepath {flattenpath{\n",
            "  gsave newpath curpath {exec} forall moveto false upath [ exch ] /curpath exch def grestore\n",
            "}{\n",
            "  gsave newpath curpath {exec} forall lineto false upath [ exch ] /curpath exch def grestore\n",
            "  /curpage curpage 1 add def\n",
            "  (\\n%%Page: ) print curpage printany ( ) print curpage printany (\\n) print\n",
            "  (0 $lry translate 1 -1 scale $strokewd setlinewidth $strokelj setlinejoin $strokelc setlinecap\\n) print\n",
            "  curpath {{printany ( ) print} forall} forall (stroke showpage) print\n",
            "}{}{} pathforall} def\n",
            "<</PageSize [$wd $ht]>> setpagedevice\n",
            "0 $lry translate 1 -1 scale $strokewd setlinewidth\n",
            "(%!PS-Adobe-3.0\\n) print\n",
            "(%%BoundingBox: $ulx $uly $lrx $lry\\n) print\n",
            "(%%EndComments\\n) print\n",
            "(<</PageSize [$wd $ht]>> setpagedevice) print\n";
    }
    s/^.*d\s*=\s*"([^"]*)".*$/$1/;
    s/-/ -/g;
    s/,/ /g;
    s/M\s?([0-9.-]+) ([0-9.-]+)/ $1 $2 moveto /g;
    s/m\s?([0-9.-]+) ([0-9.-]+)/ $1 $2 rmoveto /g;
    s/L\s?([0-9.-]+) ([0-9.-]+)/ $1 $2 lineto /g;
    s/l\s?([0-9.-]+) ([0-9.-]+)/ $1 $2 rlineto /g;
    s/C\s?([0-9.-]+) ([0-9.-]+) ([0-9.-]+) ([0-9.-]+) ([0-9.-]+) ([0-9.-]+)/ $1 $2 $3 $4 $5 $6 curveto /g;
    s/c\s?([0-9.-]+) ([0-9.-]+) ([0-9.-]+) ([0-9.-]+) ([0-9.-]+) ([0-9.-]+)/ $1 $2 $3 $4 $5 $6 rcurveto /g;
    s/^\s*//g;
    print;
    print "typepath stroke\n";
  }else{next;}
}
print "(\\n%%EOF\\n) print\n";
print "%%EOF\n";

