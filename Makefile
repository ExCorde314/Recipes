
all:
	python recipe_book.py
	latex recipe_book.tex
	pdflatex recipe_book.tex

clean:
	find . -not -path '*/\.*' -name "*.aux" -type f -delete
	find . -not -path '*/\.*' -name "*.pdf" -type f -delete
	find . -not -path '*/\.*' -name "*.idx" -type f -delete
	find . -not -path '*/\.*' -name "*.dvi" -type f -delete
	find . -not -path '*/\.*' -name "*.toc" -type f -delete
	find . -not -path '*/\.*' -name "*.log" -type f -delete
