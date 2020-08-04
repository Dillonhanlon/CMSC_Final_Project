report.pdf: report.tex Recover_Binary.png orbit.png lightcurve_opt.png time_delay.png bibliography.bib
	latexmk -pdf

Recover_Binary.png: Recover_Binary.py LK
	python3 Recover_Binary.py

time_delay.png: Maelstrom_TimeDelay.py LK
	python3 Maelstrom_TimeDelay.py

lightcurve_opt.png: Maelstrom_lightcurve.py LK
	python3 Maelstrom_lightcurve.py

orbit.png: orbit.py LK
	python3 orbit.py

Lightcurve.png: LK
	python3	LK.py

LK: LK.py
	python3 LK.py

.PHONY: clean almost_clean

clean: almost_clean
	rm report.pdf
	rm Recover_Binary.png
	rm lightcurve_opt.png
	rm time_delay.png
	rm Lightcurve.png
	rm orbit.png

almost_clean:
	latexmk -c