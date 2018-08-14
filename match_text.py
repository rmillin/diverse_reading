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
tfidf = vectorizer.fit_transform(descriptions)

test_vector = description.pop()


from sklearn.metrics.pairwise import linear_kernel
cosine_similarities = linear_kernel(tfidf[0:1], tfidf).flatten()
cosine_similarities
related_docs_indices = cosine_similarities.argsort()[:-5:-1]
related_docs_indices
cosine_similarities[related_docs_indices]

descriptions[0]
descriptions[138]
diverse_data.iloc[138]
diverse_data.iloc[0]

#nondiv_descriptions = list(non_diverse['description'])
#idx=0
#for description in nondiv_descriptions:
#        nondiv_descriptions[idx] = str(description)
#        idx += 1
#non_div_tfidf = vectorizer.fit_transform(nondiv_descriptions)
#test_similar = linear_kernel(non_div_tfidf[0:1], tfidf).flatten()

nondiv_ex = str(non_diverse['description'][0])
descriptions.insert(0,nondiv_ex)
#desc_ex = nondiv_ex + descriptions
tfidf_ex = vectorizer.fit_transform(descriptions)
cosine_test = linear_kernel(tfidf_ex[0:1], tfidf_ex).flatten()
related_docs_test = cosine_test.argsort()[:-5:-1]
cosine_test[related_docs_test]
related_docs_test
descriptions[1]
descriptions[211]
