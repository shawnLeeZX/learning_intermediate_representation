#!/usr/bin/env python

import os

from sklearn import datasets
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets.base import get_data_home

def load_vocabulary(vocabulary_path):
    '''
    Load vocabulary from a file which contains one word for eacht into a list.
    
    Parameters
    ----------
    vocabulary_path: str
        the path to the vocabulary file.

    Returns
    -------
    vocabulary: list
        a list contains all the words needed.
    '''
    vocabulary_file = open(vocabulary_path, 'r')
    vocabulary = []
    for word in vocabulary_file:
        word = word.strip('\n')
        vocabulary += [ word ]

    return vocabulary

def load_data(subset):
    '''
    Fetch 20newsgroup data and return it in tf-idf matrix form.

    Parameters
    ----------
    subset: str
        subset of date to fetch, whose value can be train, test, and all.

    Returns
    -------
    A: array, shape (number of documents, number of words)
    vocab_matrix: array, shape (number of words, number of words)
        This is the matrix of eigenwords of words in the dictionary.
    vocabulary: list
        List contains vocabulary. Note that they actual word string.
    '''
    # Data preprocessing
    # ================================================================
    # Fetch 20newsgroups data, removing its header, footer and quotes.
    docs = datasets.fetch_20newsgroups(
            subset=subset,
            remove=('headers', 'footers', 'quotes')
            )
    # ================================================================

    # Convert the raw documents data into tf-idf matrix
    # ================================================================
    data_home = get_data_home()
    vocabulary_path = os.path.join(data_home, 'vocabulary.txt')
    vocabulary = load_vocabulary(vocabulary_path)

    vectorizer = TfidfVectorizer(
            vocabulary=vocabulary,
            norm='l2',
            use_idf=True,
            smooth_idf=True,
            sublinear_tf=True
            )
    docs_tfidf = vectorizer.fit_transform(docs.data)
    vocab_tfidf = vectorizer.transform(vocabulary)
    # ================================================================
    return docs_tfidf, vocab_tfidf, vocabulary

