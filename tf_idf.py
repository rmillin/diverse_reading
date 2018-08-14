#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 11:47:20 2018

@author: pamela
"""

from sklearn.feature_extraction.text import TfidfVectorizer

descriptions = list(diverse_data['description'])
idx=0
for description in descriptions:
        descriptions[idx] = str(description)
        idx += 1
        
vectorizer = TfidfVectorizer()
response = vectorizer.fit(descriptions)
response.vocabulary_


