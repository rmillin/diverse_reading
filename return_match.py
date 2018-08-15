#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:30:46 2018

@author: pamela
"""

import preprocessing
import matching

test_name = 'Moby Dick'
desc_input = matching.search_id(matching.search_name(test_name))
diverse_desc = matching.book_descriptions(diverse_data)
match = find_best_match(desc_input, diverse_desc)

diverse_data.iloc[match]
concise_output(diverse_data.iloc[match])

