import sys
import gnupg
import json

if len(sys.argv) == 2:
    keyring = sys.argv[1]

gpg = gnupg.GPG(keyring=keyring, binary='/usr/local/MacGPG2/bin/gpg2')

keylist = []

for key in gpg.list_keys():
    fprint = key['fingerprint']
    keylist.add({'keyid': key['keyid'],
                 'fingerprint': ' '.join([fprint[x:x+4]
                                          for x in xrange(0, len(fprint), 4)]),
                 'uid': key['uids'], 'size': key['length'],
                 'algo': key['algo'], 'creation': key['date'],
                 'expires': key['expires']})

with open('keys.json', 'wb') as keyfile:
    json.dump(keylist, keyfile)
