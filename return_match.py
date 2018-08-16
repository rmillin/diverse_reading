#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:30:46 2018

@author: pamela
"""

import preprocessing
import matching
import pickle
import time
import pandas as pd
from os.path import join

# book for testing
test_name = 'Moby Dick'

# get the book description
desc_input = matching.search_id(matching.search_name(test_name))

# load the trained tfidf model
data_fpath = '/Users/rmillin/Documents/Insight/diverse-reading/data'
tfidf_fname = 'trained_tfidf.sav'
filename = join(data_fpath, tfidf_fname)
with open(filename, 'rb') as pickle_file:
    trained_tfidf = pickle.load(pickle_file)

# load in the cleaned descriptions of diverse books
data_fname = 'cleaned_diverse_books.sav' # list
filename = join(data_fpath, data_fname)
with open(filename, 'rb') as pickle_file:
    diverse_data = pickle.load(pickle_file)

# find the best match from the diverse book descriptions
match = matching.find_best_match(desc_input, diverse_data, trained_tfidf)
        
data_fname = 'diverse_books_merged.json'
filename = join(data_fpath, data_fname)
diverse_data = pd.read_json(filename, orient='records')

print(diverse_data.iloc[match,:])

matching.concise_output(diverse_data.iloc[match])
