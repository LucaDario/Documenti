PARSER = ../../../Tools/glossary/Parse.py
GENERATOR = ../../../Tools/glossary/MakeGlossary.py
CORRECTOR = ../../../Tools/glossary/FixMarkup.py

update :
	$(PARSER) ../..
	$(GENERATOR) ../..

fix :
	$(CORRECTOR) ../..

pdf :
	pdflatex Glossario.tex
	rm Glossario.aux Glossario.log Glossario.out Glossario.toc