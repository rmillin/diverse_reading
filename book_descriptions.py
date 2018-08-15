#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 13:26:55 2018

@author: pamela
@Purpose: pull column of descriptions of diverse books to compare to
"""


def book_descriptions(df):
    
            
    # clean the summaries
    data = standardize_description(df)

    # lemmatize the summaries
    data = lemmatize_description(data)

    # return as a list of descriptions
    return data['description'].tolist()

