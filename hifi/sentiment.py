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

import nltk

from collections import defaultdict
from hifi.preprocess import tokenize
from nltk.probability import FreqDist
from nltk.classify.util import apply_features


def _classifier_features_for_document(document):
    return {"contains(%s)" % w: w for w in set(document)}

def classifier_for_training_set(positive, negative, blacklist=[]):
    """
    Returns a Bayesian classifier for the given positive and negative sentences.
    """
    positive_feedback \
        = map(lambda s: (FreqDist(tokenize(s, blacklist)).keys(), 'positive'),
              positive)
    negative_feedback \
        = map(lambda s: (FreqDist(tokenize(s, blacklist)).keys(), 'negative'),
              negative)

    training_set = apply_features(_classifier_features_for_document,
                                  positive_feedback + negative_feedback)
    return nltk.classify.NaiveBayesClassifier.train(training_set)
    
def positive_sentiment_for_sentences(classifier, sentences, blacklist=[]):
    """
    Returns the ratio of positive sentiment for the given list of sentences
    between 0 and 1 inclusive.
    """
    statistics = defaultdict(int)

    for sentence in sentences:
        tokens = tokenize(sentence, blacklist)
        freq_dist = nltk.FreqDist(tokens)

        classification = classifier.classify(_classifier_features_for_document(freq_dist))
        statistics[classification] += 1

    if len(statistics) == 0:
        return 0

    positive = statistics['positive']
    negative = statistics['negative']

    return positive / float(positive + negative)
