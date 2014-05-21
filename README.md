# Learning Intermediate Representation Using LSA, FA, ICA

This repo contains implementation of Latent Semantic Analysis, Factor Analysis,
and Independent Component Analysis using sklearn, which is a machine learning
library for python.

## data
`data.py` contains functions to load 20newsgroup data and convert it into
normalized tf-idf matrix.

## Methods
* lsa.py
* fa.py
* ica.py

## Tools
* interactive_word_vector_viewer.py
* nearest_vector_searcher.py
Those two tools are used to view the intermediate representation output.
`interactive_word_vector_viewer` will display the vector of the word input and
the difference from previous one. `nearest_vector_searcher` will return the word
that is two norm nearest to the input word.
