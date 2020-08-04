report.pdf: report.tex Recover_Binary.pdf lightcurve_opt.pdf time_delay.pdf bibliography.bib
	pdflatex report.tex

Recover_Binary.pdf: Recover_Planet.py LK.py
	python3 Recover_Planet.py

time_delay.pdf: Maelstrom_TimeDelay.py LK.py
	python3 Maelstrom_TimeDelay.py

lightcurve_opt.pdf: Maelstrom_lightcurve.py LK.py
	python3 Maelstrom_lightcurve.py

orbit.pdf: orbit.py
	python3 orbit.py

Lightcurve.pdf: LK.py
	python3	LK.py

LK: LK.py
	python3 LK.py

.PHONY: clean almost_clean

clean: almost_clean
	rm report.pdf
	rm Recover_Binary.pdf
	rm lightcurve_opt.pdf
	rm time_delay.pdf
	rm Lightcurve.pdf
	rm orbit.pdf

almost_clean:
	latexmk -c