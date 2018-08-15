#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 13:26:55 2018

@author: pamela
@Purpose: pull column of descriptions of diverse books to compare to
"""


def book_descriptions(df, fpath=None, fname=None):    
            
    # clean the summaries
    data = standardize_description(df)

    # lemmatize the summaries
    data = lemmatize_description(data)

    # save if requested
    if (fpath not None) and (fname not None):
        data.to_json(join(fpath,fname))

    # return as a list of descriptions
    return data['description'].tolist()

