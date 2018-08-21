#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:30:46 2018
@author: pamela
"""

def return_match(book_title):
    import pickle
    import pandas as pd
    import preprocessing
    #import matching
    from search_book_name import search_id, search_name
    #from book_descriptions import book_descriptions
    from find_best_match import find_best_match
    from concise_output import concise_output


    # file_name = "/home/pamela/Documents/diverse_reading/diverse_data"
    # fileObject = open(file_name, 'rb')
    # diverse_data = pickle.load(fileObject)
    # fileObject.close()

    #load cleaned data- just descriptions
    file_name = '../cleaned_diverse_books.sav'
    fileObject = open(file_name, 'rb')
    diverse_data = pickle.load(fileObject)
    fileObject.close()

    # load the trained lda model
    pipeline_fname = '../lsa_pipeline.sav'
    filename = join(data_fpath, pipeline_fname)
    with open(filename, 'rb') as pickle_file:
        lsa_pipeline = pickle.load(pickle_file)

    #load diverse book dataframe
    file_name = '../diverse_books_merged.json'
    diverse_df = pd.read_json(file_name, orient='records')

    #clean desc_input- within find_best_match
    desc_input = search_id(search_name(book_title))

    #diverse_desc = book_descriptions(diverse_data)
    match = matching.find_best_match(desc_input, diverse_data, lsa_pipeline)
    return concise_output(diverse_df.iloc[match])
