import json

from operator import itemgetter
from collections import defaultdict

from sys import exit, argv
from example_blacklist import blacklist
from hifi.adjectives import top_adjectives_for_tokens

if len(argv) < 2:
    print 'usage: python example_top_adjectives.py <preprocessor-files>' 
    exit(-1)

top_adjectives = defaultdict(int)

paths = argv[1:]
for path in paths:
    with open(path, 'r') as f:
        adjectives = top_adjectives_for_tokens(json.load(f)['tokens'],
                                               blacklist)
        for adjective, frequency in adjectives.iteritems():
            top_adjectives[adjective] += frequency

frequencies = sorted(adjective_frequency.iteritems(),
                     key=itemgetter(1),
                     reverse=True)
import pprint
pprint.pprint(frequencies[:20])
