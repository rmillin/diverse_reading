#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:07:24 2018

@author: pamela
"""

#from api_request import request
import requests
#import pandas as pd
from bs4 import BeautifulSoup as bs

def search_name(name):
    #name = 'The Hounds of Baskerville'#254656
    name_split = name.split()
    name_join = '+'.join(name_split)
    url_name = 'https://www.goodreads.com/search/index.xml?key=sydsjovGS88bdTfMwAI2Ug&q=' + name_join
    
    name_search = requests.get(url_name)
    soup_tmp = bs(name_search.content, features='xml')#parse file
    gr_id = soup_tmp.findAll('id')[1].get_text()
    return gr_id

def search_id(gr_id):
    url_id = 'https://www.goodreads.com/book/show/' + str(gr_id) + '.xml?key=sydsjovGS88bdTfMwAI2Ug'
    id_search = requests.get(url_id)

    id_soup = bs(id_search.content, features='xml')
    book_desc = id_soup.findAll('description')[0].get_text()
    
    return book_desc
    
search_name('The Hounds of Baskerville')

#test_name = '
#search_desc(search_name(test_name))
