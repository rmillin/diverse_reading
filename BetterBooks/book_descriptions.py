#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 13:26:55 2018

@author: pamela
@Purpose: pull column of descriptions of diverse books to compare to
"""


def book_descriptions(df):
    
    descriptions = list(df['description'])
    idx=0
    for description in descriptions:
            descriptions[idx] = str(description)
            idx += 1
            
    return descriptions

