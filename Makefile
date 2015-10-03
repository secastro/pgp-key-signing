EVENT=oarc-montreal-2015
KEYRING=./${EVENT}-keyring.txt
GPGOPT="--no-default-keyring"

all: refresh printout.html

refresh: keys.json

keys.json:
	for k in keys/*.asc; do \
        echo "Key file $$k" ;\
		gpg2 --keyring ${KEYRING} ${GPGOPT} --import "$$k" ;\
    done
	python list-keys.py ${KEYRING}

clean:
	rm -f ${KEYRING}

show:
	gpg2 --keyring ${KEYRING} ${GPGOPT} --list-keys

export:
	gpg2 --keyring ${KEYRING} ${GPGOPT} --export \
        --armor > ${EVENT}.asc


printout.html: keys.json list-keys.py printout.py printout.pyhtml
	python printout.py
