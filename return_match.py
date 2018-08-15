#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:30:46 2018

@author: pamela
"""

import preprocessing
import matching
from os.path import join

fpath = '/Users/rmillin/Documents/Insight/diverse-reading/data'
fname = 'merged_diverse.json'

test_name = 'Moby Dick'
desc_input = matching.search_id(matching.search_name(test_name))
diverse_data = pd.read_json(join(fpath,fname))
diverse_desc = matching.book_descriptions(diverse_data)
match = find_best_match(desc_input, diverse_desc)

diverse_data.iloc[match]
concise_output(diverse_data.iloc[match])

"""
to do:
preprocess and merge the diverse lists
1. figure out which lists we actually want to keep
2. use pandas to merge them into single dataframe
3. clean and lemmatize this list
4. save the list in a single file to load here
