#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 13:26:55 2018

@author: pamela
@Purpose: pull column of descriptions of diverse books to compare to
"""

def standardize_description(data):

    """
    This function will remove repeated sentences from the description, remove
    punctuation, parse into words, remove stopwords, and lemmatize the remaining
    words.

    input: a dataframe with a "description" column"
    ouptut: the same dataframe with the cleaned descriptions

    """

    import pandas as pd

    # clean the summaries
    data['description'] = data['description'].apply(clean_description)
    
    # flatten summary lists into strings
    data['description'] = data['description'].apply(lambda x: "".join(x) if isinstance(x,list) else str(x))

    return data
    

def stem_description(data):

    import nltk
    import re
    import time
    from nltk.corpus import stopwords, wordnet
    from nltk.tokenize import word_tokenize
    from nltk.stem.snowball import SnowballStemmer
    from nltk.tag import StanfordNERTagger
    print(type(data['description'][0]))
    def tokenize_text(word_tokens):
        return [w for w in word_tokens if not w in stop_words]    

    def stem_text(word_tokens):
        # right now this treats all words as nouns and only gets rid of plurals;
        # this can be changed by first getting the part of speech for each word
        stemmer = SnowballStemmer("english")
        # function to convert to POS usable by WordNetLemmatizer (from treebank tags returned by nltk.pos_tag)
        # convert to wordnet tags and lemmatize
        indrange = range(len(word_tokens))
        stems = [stemmer.stem(word_tokens[ind]) for ind in indrange]
        return stems
        
    print(type(data['description'][0]))
    stop_words = set(stopwords.words('english'))
    print(type(data['description'][0]))
    
#    # convert to lower case
#    data['description'] = data['description'].apply(lambda x:x.lower())
    # eliminate numbers
    data['description'] = data['description'].apply(lambda x:re.sub("[\d]", " ",  x))
    #data = data.sub("[\d]", " ",  x)
    # tokenize
    data['description'] = data['description'].apply(lambda x:re.sub("[^\w]", " ",  x).split())
    #data = data.sub("[^\w]", " ",  x).split()
    # remove stopwords
    data['description'] = data['description'].apply(lambda x:tokenize_text(x))
    #data = data.tokenize_text()

    print(data['description'])
    # remove names
    def remove_names(word_tokens):
        keep_tokens = [word for word in word_tokens if (not word[0].isupper()) ]
        print(keep_tokens)
        return keep_tokens

    data['description'] = data['description'].apply(lambda x:remove_names(x))
    print(data['description'])
  
    # lemmatize
    data['description'] = data['description'].apply(lambda x:stem_text(x))
    print(data['description'])
  
    return data


def clean_description(description):
    
    """
    This function will remove repeated sentences from a description.

    input: a description from "goodreads", consisting of a list of strings
    or a single string
    ouptut: if a list, the same description with repeated cells eliminated
    if a string, outputs the original string
    """
    if isinstance(description,list):
        ind2 = 0
        ind1=len(description)-1
        while ind1>=0 and ind2<len(description):
            while ind2<ind1:
                if description[ind2] in description[ind1]:
                    description.remove(description[ind2])
                    ind1-=1
                else:
                    ind2+=1
            ind1-=1
            ind2=0
    return description



def preprocess_lsa(data):    
# data is a dataframe with a "description" column

# lsa transform to get lower dimensional representation
# in theory will result in synonyms being grouped, polynyms being distinguished

    import re
    import pandas as pd
    from nltk.corpus import stopwords
    
    # remove names
    def remove_names(word_tokens):
        keep_tokens = [word for word in word_tokens if (not word[0].isupper()) ]
        return keep_tokens


    def remove_stop(word_tokens):
        return [w for w in word_tokens if not w in stop_words]    

    # eliminate numbers
    data['description'] = data['description'].apply(lambda x:re.sub("[\d]", " ",  x))

    # tokenize
    data['description'] = data['description'].apply(lambda x:re.sub("[^\w]", " ",  x).split())

    # remove stopwords
    stop_words = set(stopwords.words('english'))
    data['description'] = data['description'].apply(lambda x:remove_stop(x))

    # remove capitalized words
    data['description'] = data['description'].apply(lambda x:remove_names(x))
    
    # flatten to strings for pipeline
    data['description'] = data['description'].apply(lambda x: " ".join(x) if isinstance(x,list) else str(x))
    print(data.loc[0,'description'])
    
    return data


def perform_lsa(data, n_components, lsa_pipeline=None, fpath=None, pipeline_fname=None): 
    from sklearn.decomposition import TruncatedSVD
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.feature_extraction.text import TfidfTransformer
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import Normalizer
    from os.path import join
    import pickle

    if ((lsa_pipeline==None) and (fpath!=None) and (pipeline_fname!=None)):
        # create pipeline for performing tf-idf and lsa
        vectorizer = TfidfVectorizer(max_df=0.5, min_df=10) # words occur in fewer than half of the documents and at least 10 documents
        svd = TruncatedSVD(n_components)
        normalizer = Normalizer(copy=False)
        lsa_pipeline = make_pipeline(vectorizer, svd, normalizer)

        # perform LSA pipeline
        lsa_pipeline.fit(data['description'])
        pickle.dump(lsa_pipeline, open(join(fpath,pipeline_fname), 'wb'))

    transformed_data = lsa_pipeline.transform(data['description'])

    return transformed_data, lsa_pipeline



def process_descriptions(df, pipeline=None, fpath=None, fname=None, pipeline_fname=None):

    print('datatype')
    print(df.loc[0,'description'])

    from os.path import join
    import pickle
    import time

    # clean the summaries
    data = standardize_description(df)

    """
    # lemmatize the summaries
    data = stem_description(df)
    print('done stemming')

    """

    # preprocess for LSA
    data = preprocess_lsa(data)
    if ((fpath!=None) and (fname!=None)):
        pickle.dump(data, open(join(fpath,fname), 'wb'))

    # lsa pipeline
    n_components = 50
    transformed_data = perform_lsa(data, n_components, pipeline, fpath, pipeline_fname)

    return transformed_data


"""
def generate_tfidf(descriptions, fpath=None, fname=None):

    from sklearn.feature_extraction.text import TfidfVectorizer
    from os.path import join
    import pickle

    vectorizer = TfidfVectorizer()
    response = vectorizer.fit(descriptions)

    # save if requested
    if ((fpath!=None) and (fname!=None)):
        pickle.dump(response, open(join(fpath,fname), 'wb'))

    # return as a list of descriptions
    return response
"""

