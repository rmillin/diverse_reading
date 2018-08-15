#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:30:46 2018

@author: pamela
"""

import preprocessing
import matching
import panda as pd
from os.path import join

# book for testing
test_name = 'Moby Dick'

# get the book description
desc_input = matching.search_id(matching.search_name(test_name))

# load the trained tfidf model
data_fpath = '/Users/rmillin/Documents/Insight/diverse-reading/data'
tfidf_fname = 'trained_tfidf.sav'
with open(filename, 'rb') as pickle_file:
    trained_tfid = pickle.load(join(data_fpath, tfidf_fname))

# load in the cleaned descriptions of diverse books
data_fname = 'cleaned_diverse_books.json'
diverse_data = pd.read_json(join(data_fpath, data_fname))                              

# find the best match from the diverse book descriptions
match = find_best_match(desc_input, diverse_data, trained_tfidf)

diverse_data.iloc[match]
concise_output(diverse_data.iloc[match])

"""
to do:
preprocess and merge the diverse lists
1. figure out which lists we actually want to keep
2. use pandas to merge them into single dataframe
3. clean and lemmatize this list
4. save the list in a single file to load here
