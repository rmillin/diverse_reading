#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:30:46 2018
@author: pamela
"""

def return_match(book_title):
    import pickle

    file_name = "../diverse_data"
    fileObject = open(file_name, 'rb')
    diverse_data = pickle.load(fileObject)
    fileObject.close()

    #os.chdir('/home/pamela/Documents/diverse_reading/BetterBooks')
    from search_book_name import search_id, search_name
    from book_descriptions import book_descriptions
    from find_best_match import find_best_match
    from concise_output import concise_output


    desc_input = search_id(search_name(book_title))
    diverse_desc = book_descriptions(diverse_data)
    match = find_best_match(desc_input, diverse_desc)
    return concise_output(diverse_data.iloc[match])


return_match('1984')