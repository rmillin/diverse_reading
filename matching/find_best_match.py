#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 13:14:05 2018

@author: pamela
@purpose: match a given description to deescriptions of diverse books
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
from preprocessing import *

def find_best_match(to_match, diverse_desc, trained_tfidf):

    # make into a dataframe for preprocessing
    to_match = pd.DataFrame(to_match,columns=['description'])
    print(to_match)
    # preprocess
    to_match_clean = process_descriptions(to_match)
    print(to_match_clean)
    # tfidf
    to_match_tfidf = trained_tfidf.transform(to_match_clean[0])
    diverse_tfidf = trained_tfidf.transform(diverse_desc)

    # find most similar
    cosine_sim = linear_kernel(to_match_tfidf, diverse_tfidf).flatten()
    best_idx = cosine_sim.argsort()[-1]
    cosine_sim[best_idx]

    return best_idx
