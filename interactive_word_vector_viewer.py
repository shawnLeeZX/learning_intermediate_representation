import os
import sys
# readline to utilize convenient command line shortcuts.
import readline

try:
    import cPickle as pickle
except:
    import pickle

if len(sys.argv) != 2:
    print '''Usage: python interactive_word_vector_viewer [FILE]
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
# Previous word for comparison.
previous_word = None
# Keep a log.
log_filename = 'vector_view.log'
if os.path.exists(log_filename):
    os.remove(log_filename)
log_file = open(log_filename, 'w')
try:
    while True:
        word = raw_input('Word vector look up: ')
        print 'Its vector is: ', vector_dict[word]
        print >> log_file, word, ': ', vector_dict[word]
        if previous_word != None:
            vector_difference = vector_dict[previous_word] - vector_dict[word]
            print 'Vector Difference', vector_difference
            print >> log_file, previous_word, '-', word, ': ', vector_dict[word]
        previous_word = word
except EOFError:
    sys.exit(0)
except KeyError:
    print word, ' is not in the dicitionary.'
finally:
    log_file.close()
    dict_file.close()
