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
    

def lemmatize_description(data):

    import nltk
    import re
    from nltk.corpus import stopwords, wordnet
    from nltk.tokenize import word_tokenize
    from nltk.stem import WordNetLemmatizer

    def tokenize_text(word_tokens):
        return [w for w in word_tokens if not w in stop_words]    

    def lemmatize_text(word_tokens):
        # right now this treats all words as nouns and only gets rid of plurals;
        # this can be changed by first getting the part of speech for each word
        lemmatizer = WordNetLemmatizer()
        # function to convert to POS usable by WordNetLemmatizer (from treebank tags returned by nltk.pos_tag)
        def get_wordnet_pos(treebank_tag):
            if treebank_tag.startswith('J'):
                return wordnet.ADJ
            elif treebank_tag.startswith('V'):
                return wordnet.VERB
            elif treebank_tag.startswith('N'):
                return wordnet.NOUN
            elif treebank_tag.startswith('R'):
                return wordnet.ADV
            else:
                return wordnet.NOUN # since this is anyway the default.
            
        # tag POS of words, convert for lemmatizer, lemmatize
        pos_tag = nltk.pos_tag(word_tokens)
        return [lemmatizer.lemmatize(word_tokens[ind], get_wordnet_pos(pos_tag[ind][1])) for ind in range(len(word_tokens))]
        

    stop_words = set(stopwords.words('english'))

    # convert to lower case
    data['description'] = data['description'].apply(lambda x:x.lower())

    # eliminate numbers
    data['description'] = data['description'].apply(lambda x:re.sub("[\d]", " ",  x))

    # tokenize
    data['description'] = data['description'].apply(lambda x:re.sub("[^\w]", " ",  x).split())

    # remove stopwords
    data['description'] = data['description'].apply(lambda x:tokenize_text(x))
    print(data['description'])

    # lemmatize
    data['description'] = data['description'].apply(lambda x:lemmatize_text(x))
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



def process_descriptions(df, fpath=None, fname=None):

    from os.path import join
    import pickle
            
    # clean the summaries
    data = standardize_description(df)

    # lemmatize the summaries
    data = lemmatize_description(data)

    # convert to single string separated by spaces (for tfidf)
    data['description'] = data['description'].apply(lambda x:' '.join(x))

    # return as a list of descriptions
    data = data['description'].tolist()
    
    # save if requested
    if ((fpath!=None) and (fname!=None)):
       pickle.dump(data, open(join(fpath,fname), 'wb'))

    return data


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

