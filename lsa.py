import os

from data import load_data
from sklearn.decomposition import TruncatedSVD
try:
    import cPickle as pickle
except:
    import pickle

# LSI

# ================================================================
# Apply truncated SVD on the tf-idf matrix and transform raw documents into
# intermediate representation.
docs_tfidf, vocab_tfidf, vocabulary = load_data(subset='all')
n_components = 40
lsa = TruncatedSVD(n_components=n_components)
lsa_doc = lsa.fit_transform(docs_tfidf)
lsa_words = lsa.transform(vocab_tfidf)

# Create a dict to hold the new pca words.
lsa_dict = dict(zip(vocabulary, lsa_words))

# Store the intermediate representation pca words on disk.
lsa_dict_filename = 'lsa_dict.pk'
if not os.path.exists(lsa_dict_filename):
    lsa_dict_file = open(lsa_dict_filename, 'w')
    pickle.dump(lsa_dict, lsa_dict_file)

# Store estimator on dist for further usage.
lsa_estimator_filename = 'lsa_estimator.pk'
if not os.path.exists(lsa_estimator_filename):
    lsa_estimator_file = open(lsa_estimator_filename, 'w')
    pickle.dump(lsa, lsa_estimator_file)
# ================================================================


