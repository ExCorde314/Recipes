
all:
	pdflatex recipe_book.tex

vimsetup:
	ctags -R .
	
	@echo "set path+=$(shell pwd)/**\nset tags+=$(shell pwd)/tags" > _vimrc_local.vim
