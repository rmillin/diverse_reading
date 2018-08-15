#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Loads in a dataframe containing all diverse books and cleans and lemmatizes
the summaries
"""

import pandas as pd
import preprocessing as preproc

savename = 'data/diverse_books_merged.json'

df = pd.read_json(savename)

fpath = '/Users/rmillin/Documents/Insight/diverse-reading/data'
fname = 'cleaned_diverse_books.json'

book_descriptions(df, fpath=None, fname=None)
