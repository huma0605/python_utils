#!/usr/bin/python

# coding=utf8
# description     : Update dataframe values using another dataframe 
# author          : Shiu-Tang Li
# last update     : 06/13/2017
# version         : 0.1
# python_version  : 3.5.2

import pandas as pd
import numpy as np
from copy import deepcopy 

def update_data(df1, df2, key_column, sort = True):
    
    # Input:
    # df1:        target dataframe to be updated
    # df2:        used to update df1. Make sure all columns in df2 are in df1.
    # key_column: the primary key used to match df1 and df2
    # sort:       True:  output sorted revised dataframe by key_column  
    #             False: output revised dataframe, not sorted
    
    # Output:     updated dataframe
    
    # Example:
    # df1 =  pd.DataFrame({'a':[1,2,3], 'b': [4,5,6], 'c': [7,8,9]})
    # df2 =  pd.DataFrame({'a':[3,1],   'b': [9,2]})
    # updated_df = update_data(df1, df2, 'a', sort = True)
    
    match_index = df1.apply(lambda x: x[key_column] in df2[key_column].values, axis=1)
    matched     = deepcopy(df1[match_index])
    not_matched = deepcopy(df1[~match_index])
    
    for column in df2.columns:
        if column != key_column:
            del matched[column] 
        
    matched = matched.join(df2.set_index(key_column), on=key_column)
    df = pd.concat([matched, not_matched])
    
    if sort:
        return df.sort_values(key_column, inplace=False, ascending=True)
    else:
        return df
