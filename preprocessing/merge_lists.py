#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 11:32:02 2018

@author: pamela
"""
import pandas as pd

fname = '/Users/rmillin/Documents/Insight/diverse-reading/data/diverse_0_01_01.json'
data = pd.read_json(fname)
data.head()

savename = '/Users/rmillin/Documents/Insight/diverse-reading/data/diverse_books_merged.json'

diverse_data = pd.read_json(fname)

for num in range(1,58):
    try:
        file_name = '/Users/rmillin/Documents/Insight/diverse-reading/data/diverse_' +str(num) + '_01_01.json'
        data_temp = pd.read_json(file_name)
        diverse_data = pd.concat([diverse_data, data_temp], axis=0)
    except:
        print('Skipping ' + file_name)

diverse_data = diverse_data.drop_duplicates(subset=['title','author'])
diverse_data.to_json(savename, orient='records')
        
"""
for num in range(0,7):
    try:
        file_name = '/Users/rmillin/Documents/Insight/diverse-reading/data/diverse_ya_' +str(num) + '_01_25.json'
        data_temp = pd.read_json(file_name)
        diverse_data = pd.concat([diverse_data, data_temp], axis=0)
    except:
        print('Skipping ' + file_name)
        
diverse_data = diverse_data.drop_duplicates(subset=['title','author'])
diverse_data.to_json(savename, orient='records')

non_diverse = pd.read_json('/Users/rmillin/Documents/Insight/diverse-reading/data/western_ya_0_01_25.json')
for num in range(1,2):
    try:
        file_name = '/Users/rmillin/Documents/Insight/diverse-reading/data/western_ya_' +str(num) + '_01_25.json'
        data_temp = pd.read_json(file_name)
        non_diverse = pd.concat([non_diverse, data_temp], axis=0)
    except:
        print('Skipping ' + file_name)
for num in range(0,16):
    try:
        file_name = '/Users/rmillin/Documents/Insight/diverse-reading/data/western_' +str(num) + '_01_25.json'
        data_temp = pd.read_json(file_name)
        non_diverse = pd.concat([non_diverse, data_temp], axis=0)
    except:
        print('Skipping ' + file_name)
        

diverse_data.shape
non_diverse.shape

"""
