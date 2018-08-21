#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 13:14:05 2018

@author: pamela
@purpose: match a given description to deescriptions of diverse books
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from preprocessing import *

def find_best_match(to_match_str, diverse_desc, lsa_pipeline):

    # make into a dataframe for preprocessing
    # could change to avoid this
    to_match = pd.DataFrame()
    to_match['description'] = [to_match_str]#,columns=['description'])
    # preprocess, lsa
    to_match_lsa = process_descriptions(to_match, pipeline=lsa_pipeline)
    diverse_lsa = perform_lsa(diverse_desc, [], lsa_pipeline=lsa_pipeline)
    # find most similar
    cosine_sim = cosine_similarity(to_match_lsa[0], diverse_lsa[0]).flatten()
    best_idx = cosine_sim.argsort()[:-4:-1]
    # print(cosine_sim.shape)
    # print(best_idx)
    # print(cosine_sim.max())
    # print(cosine_sim[best_idx])

    return best_idx
