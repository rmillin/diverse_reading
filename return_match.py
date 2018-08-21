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
test_name = 'lord of the flies'

# get the book description
desc_input = matching.search_id(matching.search_name(test_name))

# load the trained lda model
data_fpath = '/Users/rmillin/Documents/Insight/diverse-reading/data'
pipeline_fname = 'lsa_pipeline.sav'
filename = join(data_fpath, pipeline_fname)
with open(filename, 'rb') as pickle_file:
    lsa_pipeline = pickle.load(pickle_file)

# load in the cleaned descriptions of diverse books
data_fname = 'cleaned_diverse_books.sav' # list
filename = join(data_fpath, data_fname)
with open(filename, 'rb') as pickle_file:
    diverse_data = pickle.load(pickle_file)

# find the best match from the diverse book descriptions
match = matching.find_best_match(desc_input, diverse_data, lsa_pipeline)
        
data_fname = 'diverse_books_merged.json'
filename = join(data_fpath, data_fname)
diverse_data = pd.read_json(filename, orient='records')

for ind in match:
    print(diverse_data.loc[diverse_data.index[ind],'description'])

matching.concise_output(diverse_data.iloc[match])
