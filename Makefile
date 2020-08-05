report.pdf: report.tex output bibliography.bib
	latexmk -pdf


output: project.sh
	bash project.sh
# Recover_Binary.png: Recover_Binary.py LK
# 	python3 Recover_Binary.py

# time_delay.png: Maelstrom_TimeDelay.py LK
# 	python3 Maelstrom_TimeDelay.py

# lightcurve_opt.png: Maelstrom_lightcurve.py LK
# 	python3 Maelstrom_lightcurve.py

# orbit.png: orbit.py LK
# 	python3 orbit.py

# Lightcurve.png: LK
# 	python3	LK.py

# LK: LK.py
# 	python3 LK.py

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