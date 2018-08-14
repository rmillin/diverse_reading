#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 13:14:05 2018

@author: pamela
@purpose: match a given description to deescriptions of diverse books
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def find_best_match(to_match, diverse_desc):
    vectorizer = TfidfVectorizer()
    to_match = str(to_match)
    diverse_desc.insert(0,to_match)
    #desc_ex = nondiv_ex + descriptions
    tfidf = vectorizer.fit_transform(diverse_desc)
    cosine_sim = linear_kernel(tfidf[0:1], tfidf).flatten()
    best_idx = cosine_sim.argsort()[-2:-1]
    cosine_sim[best_idx]

    #return diverse_desc[int(best_idx)]
    return best_idx
