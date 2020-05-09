
.PHONY: add
add:
	git add pubs/\*.*
	make git_add_hili
	git status

git_add_hili:
	git add log/icite/*.txt
	git add log/pmids/*.txt
	#git add log/exports/*.html
	#git add log/references/*.txt
	#git add src/papers/highlights/*.py
	#git add src/papers/flashcards/*.py
	#git add doc/papers/*.pdf
	find log/pubmed -type f | perl -ne 'if ($$_ !~ /p\d+\.txt/) {print}' | xargs git add -f


# ----------------------------------------------------------------------
pylint:
	@git status -uno | perl -ne 'if (/(\S+.py)/) {printf "echo $$1\npylint -r no %s\n", $$1}' | tee tmp_pylint
	chmod 755 tmp_pylint
	tmp_pylint

# lists make targets
list:
	@perl -ne 'if (/^([^#.]\S+):/) {print "$$1\n"}' makefile

clean_pyc:
	find . -name \*.pyc | xargs rm -f

clean:
	make clean_pyc
	rm -f tmp_pylint

# Copyright (C) 2020-present, DV Klopfenstein. All rights reserved.
