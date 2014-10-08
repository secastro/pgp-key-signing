#!/usr/bin/python

import json
from time import gmtime, strftime
import re
import tenjin
from tenjin.helpers import *


def replace_at(t):
    return re.sub("@", " at ", t)

id2label = {'17': 'DSA', '1': 'RSA'}

keylist = []

with open('keys.json', 'rb') as keys_file:
    keys = json.load(keys_file)

    for key in keys:
        temp_key = dict()
        temp_key['creation'] = strftime("%F", gmtime(int(key['creation'])))
        temp_key['expires'] = 'Never' if key['expires'] == '' else strftime("%F", gmtime(int(key['expires'])))

        temp_key['algo'] = id2label.get(key['algo'], key['algo'])
        uids = []
        for uid in key['uid']:
            # Re-encode UIDs
            uids.append(replace_at(uid))
            # push(@u, &replace_at(encode_entities($uid)));

        temp_key['uid'] = uids
        temp_key['size'] = key['size']
        temp_key['fingerprint'] = key['fingerprint']
        keylist.append(temp_key)

# print keylist

template_context = dict(keylist=keylist,
                        last_update=strftime("%F %T", gmtime()))
engine = tenjin.Engine(path=['.'])

with open('printout.html', 'wb') as template_output:
    template_output.write(engine.render('printout.pyhtml', template_context))
