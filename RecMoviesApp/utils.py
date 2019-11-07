# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 18:20:56 2019

@author: Fabretto
"""

import pandas as pd

import os

def LoadDataModel():
    current_path=os.getcwd()
    datamodel = pd.read_csv(
            current_path+"\\datamodel.csv",sep='\t',index_col=0)
    return datamodel, current_path
