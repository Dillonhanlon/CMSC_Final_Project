report.pdf: report.tex Recover_Binary.pdf bibliography.bib
	pdflatex report.tex

Recover_Binary.pdf: Recover_Planet.py LK.py
	python3 Recover_Planet.py

LK.py: LK.py
	python3 LK.py

.PHONY: clean almost_clean

clean: almost_clean
	rm report.pdf
	rm Recover_Binary.pdf

almost_clean:
	latexmk -c