EVENT=oarc-los-angeles-2014
KEYRING=./${EVENT}-keyring.txt
GPGOPT="--no-default-keyring"

all: refresh keyring.html

refresh: keys.json

keys.json:
	for k in keys/*.asc; do \
        echo "Key file $$k" ;\
		gpg --keyring ${KEYRING} ${GPGOPT} --import "$$k" ;\
    done
	python list-keys.py ${KEYRING}

clean:
	rm -f ${KEYRING}

show:
	gpg --keyring ${KEYRING} ${GPGOPT} --list-keys

export:
	gpg --keyring ${KEYRING} ${GPGOPT} --export \
        --armor > ${EVENT}.asc


keyring.html: keys.json list-keys.py printout.pl printout.html
	perl printout.pl < keys.json > _$@
	mv _$@ $@

printout.ps: keyring.html
	/usr/bin/html2ps < $< > $@
