import os

from data import load_data
from sklearn.decomposition import FastICA
try:
    import cPickle as pickle
except:
    import pickle

# Factor Analysis

# ================================================================
# Apply independent component analysis on the tf-idf matrix and transform raw
# documents into intermediate representation.
docs_tfidf, vocab_tfidf, vocabulary = load_data(subset='all')
n_components = 40
ica = FastICA(n_components=n_components)
ica.fit(docs_tfidf.toarray())
ica_words = ica.transform(vocab_tfidf.toarray())

# Create a dict to hold the new pca words.
ica_dict = dict(zip(vocabulary, ica_words))

# Store the intermediate representation pca words on disk.
ica_dict_filename = 'ica_dict.pk'
if not os.path.exists(ica_dict_filename):
    ica_dict_file = open(ica_dict_filename, 'w')
    pickle.dump(ica_dict, ica_dict_file)

# Store estimator on dist for further usage.
ica_estimator_filename = 'ica_estimator.pk'
if not os.path.exists(ica_estimator_filename):
    ica_estimator_file = open(ica_estimator_filename, 'w')
    pickle.dump(ica, ica_estimator_file)
# ================================================================


