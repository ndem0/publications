#!/bin/bash

BIBLIO='demo'
TEX='my-pub'

rm -rf ${BIBLIO}.bib
cat *.bib > ${BIBLIO}.bib

pdflatex ${TEX}.tex 
biber ${TEX}
pdflatex ${TEX}.tex 
pdflatex ${TEX}.tex 

rm -rf ${TEX}.aux
rm -rf ${TEX}.bbl
rm -rf ${TEX}.blg
rm -rf ${TEX}.log
