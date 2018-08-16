#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:45:50 2018

@author: pamela
"""

def  concise_output(matches):
    import pandas as pd
    out = pd.DataFrame()
    out['Title'] = matches['title']
    out['Author'] = matches['author']
    out['Description'] = matches['description']
    
    return  out
