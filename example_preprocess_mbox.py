import json

from os import path
from os import mkdir
from mailbox import mbox
from sys import exit, argv
from hifi.helpers import get_charset
from example_blacklist import blacklist
from hifi.preprocess import preprocess, tokenize, \
                            split_sentences, bigrams_for_message

if len(argv) != 2:
    print 'usage: python preprocess_mbox.py <mbox_file>' 
    exit(-1)

data_dir = path.abspath('./data')
if not path.isdir(data_dir):
    mkdir(data_dir)

mailbox = mbox(argv[1])
for index, message in enumerate(mailbox):
    payload = message.get_payload(decode=True)
    if not payload:
        continue;

    try:
        body = unicode(payload, get_charset(message), 'replace')
    except UnicodeEncodeError:
        continue

    if not body:
        continue

    clean_msg = preprocess(body)

    sentences = split_sentences(clean_msg)
    tokens = tokenize(clean_msg, blacklist)
    bigrams = bigrams_for_message(sentences)

    with open(path.join(data_dir, "preprocess-%0.4d.json" % (index + 1)), 'w') as f:
        f.write(json.dumps({
            'sentences': sentences,
            'tokens': tokens,
            'bigrams': bigrams
        }).encode('UTF-8'))
