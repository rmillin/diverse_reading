#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 11:23 2018

@author: thad
"""

def return_random_match(book_table = None,num_books = 3):
    """returns a random sample from the list and returns
    a random sample of n=num_books rows from the diverse_data
    list,if book_table is given the random list will not include
    the books in book_table"""
    import pickle

    file_name = "../diverse_data"
    fileObject = open(file_name, 'rb')
    diverse_data = pickle.load(fileObject)
    fileObject.close()

    from concise_output import concise_output
    if book_table is None:
        return concise_output(diverse_data.sample(num_books))
    else:
        diverse_data =  diverse_data.iloc[diverse_data.index.difference(book_table.index)]
        return concise_output(diverse_data.sample(num_books))

return_random_match()
