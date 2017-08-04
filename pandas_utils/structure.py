#!/usr/bin/python

# coding=utf8
# description     : count number of missing values  
# author          : Shiu-Tang Li
# last update     : 07/08/2017
# version         : 0.1
# python_version  : 3.5.2

import pandas as pd
import numpy as np
    
def structure(df):
    
    # Input:
    # df:                target dataframe
    
    # Output:            a dataframe that shows 
    #                    1. the number of missing values in each column  
    #                    2. data types for each column
    
    missing_values = [df.isnull().sum(axis=0)[column] for column in df.columns] 
    return pd.DataFrame({'column_names':df.columns, 
                         'num_of_missing_values': missing_values,
                         'type': df.dtypes.values},
                          index = np.arange(len(df.columns)))