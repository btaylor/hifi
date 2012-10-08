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

import re
import nltk

def preprocess(msg):
    """
    Filters out signatures and meaningless characters that might confuse a
    tokenizer.
    """
    # Dump signatures
    msg = msg.split('------------------')[0]
    msg = msg.split('Sent from my iPhone')[0]

    # Replace characters that punkt might get confused by, but are otherwise
    # meaningless
    msg = re.sub(r'[\'":;]', '', msg)
    return msg

def split_sentences(msg):
    """
    Splits a string into sentences, being mindful of parenthesis, hyphens and
    other non-sentence-breaking characters.
    """
    sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = sentence_detector.tokenize(msg)
    return filter(lambda s: s != '', map(lambda s: s.strip(), sentences))

def tokenize(msg, blacklist=[]):
    """
    Tokenizes, strips non-alphanumeric characters and removes stopwords (and
    optionally, blacklisted words) from a given string.
    """
    punkt = nltk.tokenize.punkt.PunktWordTokenizer()
    stopwords = nltk.corpus.stopwords.words('english')

    tokens = punkt.tokenize(msg.lower())
    tokens = filter(lambda t: t != '', \
                    map(lambda t: re.sub(r'[^A-Za-z0-9]', '', t), tokens))
    tokens = filter(lambda t: t not in stopwords and \
                              t not in blacklist, tokens)
    return tokens

def bigrams_for_message(sentences):
    """
    Returns a list of tuples containing stemmed bigrams and their corresponding
    sentence for a list of untokenized sentences.
    """
    stemmer = nltk.stem.PorterStemmer()

    # Extract bigrams along with their paired sentences
    message_bigrams = []
    for sentence in sentences:
        tokens = tokenize(sentence)

        # Stem the tokens
        tokens = map(lambda t: stemmer.stem(t), tokens)

        # Generate bigrams for all of the tokens
        bigrams = map(lambda g: ' '.join(g), nltk.util.bigrams(tokens))

        for t in bigrams:
            message_bigrams.append({'token': t, 'sentence': sentence})
    return message_bigrams
