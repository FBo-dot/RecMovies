# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 18:20:56 2019

@author: Fabretto
"""

import pandas as pd

from .views import app

def LoadDataModel():
    return pd.read_csv(app.config['DATA_MODEL_CSV'],sep='\t',index_col=0)