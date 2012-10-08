#
# Copyright (c) 2012 IGN Entertainment, Inc.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import os
import hifi
import nltk
import pickle

from collections import defaultdict

_path = os.path.join(os.path.dirname(hifi.__file__), 'adjectives_en.pickle')
_english_adjectives = pickle.load(open(path, 'r'))

def top_adjectives_for_tokens(tokens, blacklist=[]):
    """
    Returns a dict of adjectives mapping to their frequency in the provided
    tokens.
    """
    top_adjectives = defaultdict(int)
    
    adjectives = filter(lambda t: t in _english_adjectives and \
                              not t in blacklist, 
                        tokens)
    for adjective in adjectives:
        top_adjectives[adjective] += 1
    return top_adjectives
