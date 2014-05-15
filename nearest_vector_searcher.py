import os
import sys
import math
# readline to utilize convenient command line shortcuts.
import readline
import numpy as np

try:
    import cPickle as pickle
except:
    import pickle

if len(sys.argv) != 2:
    print '''Usage: python nearest_vector_searcher [FILE]
    Note:
    ========================
    File is the pickle file stored the { word: vector } dict.
    ======================='''
    exit(1)

# Check existence of the dictionary file.
dict_filename = sys.argv[1]
if not os.path.exists(dict_filename):
    print dict_filename, 'not exists.'
    exit(1)

# Load dict into memory.
dict_file = open(dict_filename, 'r')
vector_dict = pickle.load(dict_file)

# Start CLI viewer.
try:
    while True:
        word_target = raw_input('Word vector look up: ')
        vector = vector_dict[word_target]
        similar_word = None
        distance = float('inf')
        for word in vector_dict:
            if word == word_target:
                continue
            new_distance = np.linalg.norm(vector - vector_dict[word])
            if distance > new_distance:
                distance = new_distance
                similar_word = word
        print 'The most similar word: ', similar_word
except EOFError:
    sys.exit(0)
except KeyError:
    print word, ' is not in the dicitionary.'
finally:
    dict_file.close()
