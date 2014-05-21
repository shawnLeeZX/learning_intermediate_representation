import os

from data import load_data
from sklearn.decomposition import FactorAnalysis
try:
    import cPickle as pickle
except:
    import pickle

# Factor Analysis

# ================================================================
# Apply factor analysis on the tf-idf matrix and transform raw documents into
# intermediate representation.
docs_tfidf, vocab_tfidf, vocabulary = load_data(subset='all')
n_components = 40
fa = FactorAnalysis(n_components=n_components)
fa.fit(docs_tfidf.toarray())
fa_words = fa.transform(vocab_tfidf.toarray())

# Create a dict to hold the new pca words.
fa_dict = dict(zip(vocabulary, fa_words))

# Store the intermediate representation pca words on disk.
fa_dict_filename = 'fa_dict.pk'
if not os.path.exists(fa_dict_filename):
    fa_dict_file = open(fa_dict_filename, 'w')
    pickle.dump(fa_dict, fa_dict_file)

# Store estimator on dist for further usage.
fa_estimator_filename = 'fa_estimator.pk'
if not os.path.exists(fa_estimator_filename):
    fa_estimator_file = open(fa_estimator_filename, 'w')
    pickle.dump(fa, fa_estimator_file)
# ================================================================


