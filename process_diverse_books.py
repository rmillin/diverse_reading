#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Loads in a dataframe containing all diverse books and cleans and lemmatizes
the summaries
"""

import pandas as pd
from preprocessing import *

savename = '/Users/rmillin/Documents/Insight/diverse-reading/diverse_books_merged.json'

df = pd.read_json(savename)

# eliminate any books with descriptions less than 500 characters to avoid
# matching on noise, then resave

keep = df.loc[:,'description'].apply(lambda x: len(x)>500)
print(keep)
df = df.loc[keep,:]
df.to_json(savename, orient='records')

fpath = '/Users/rmillin/Documents/Insight/diverse-reading/data'
fname = 'cleaned_diverse_books.sav'

pipeline = None
pipeline_fname = 'lsa_pipeline.sav'

process_descriptions(df, pipeline, fpath, fname, pipeline_fname)
