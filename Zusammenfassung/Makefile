SHELL = /bin/sh
MAKE = /usr/bin/make

firstlevel := .
markdowns := $(foreach file,$(firstlevel),$(wildcard $(file)/*.md))

all: html pdf evince

pdf:
	# convert '---' to \newPage instead of <hr>
	for file in $(markdowns); do \
		cd "`dirname $$file`"; \
		sed \
			-e 's/'--------------------------------------------------------------------------------'/\\newpage/g' \
			-e 's/'€'/\\text{\\euro}/g' \
			-e 's/'£'/\\textsterling{}/g' \
			-e 's/'\ \"'/\\glqq\ /g' \
			-e 's/'\"\ '/\\grqq{\\ }/g' \
			"`basename $$file`" > "`basename $$file .md`".texEncoded; \
		markdown2pdf -C ./markdown2pdf.sty -o "`basename $$file .md`".pdf "`basename $$file .md`".texEncoded; \
		rm "`basename $$file .md`".texEncoded; \
	done

html:
	# escape special characters, compile markdown to html, delete escaped version
	for file in $(markdowns); do \
		cd "`dirname $$file`"; \
		sed \
			-e 's/'ä'/\&\#228;/g' \
			-e 's/'ö'/\&\#246;/g' \
			-e 's/'ü'/\&\#252;/g' \
			-e 's/'Ä'/\&\#196;/g' \
			-e 's/'Ö'/\&\#214;/g' \
			-e 's/'Ü'/\&\#220;/g' \
			-e 's/'ß'/\&\#223;/g' \
			-e 's/'€'/\&\#8364;/g' \
			-e 's/'®'/\&\#174;/g' \
			-e 's/'©'/\&\#169;/g' \
			"`basename $$file`" > "`basename $$file .md`".htmlEncoded; \
		markdown "`basename $$file .md`".htmlEncoded > "`basename $$file .md`".html; \
		rm "`basename $$file .md`".htmlEncoded; \
	done

evince: pdf
	for file in $(markdowns); do \
		evince "`basename $$file .md`".pdf; \
	done

none:
	python Non-ASCII-finder.py > "`basename $$file .md`".texEncoded; \
