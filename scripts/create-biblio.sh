#!/bin/bash

BIBLIO='demo'
TEX='nicolademo_publications'

rm -rf ${BIBLIO}.bib
cat bibitems/*.bib > ${BIBLIO}.bib

pdflatex ${TEX}.tex 
biber ${TEX}
pdflatex ${TEX}.tex 
pdflatex ${TEX}.tex 

rm -rf ${TEX}.aux
rm -rf ${TEX}.bbl
rm -rf ${TEX}.blg
rm -rf ${TEX}.log
