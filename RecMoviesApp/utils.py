# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 18:20:56 2019

@author: Fabretto
"""

import pandas as pd

import os

from .views import app
from flask import Flask

def LoadDataModel():
    # Assumes the datamodel file is one level above the instance path,
    # which defaults to 'instance'
    datamodel_filename = os.path.join(
        app.instance_path, app.config['DATA_MODEL_CSV'])
    return pd.read_csv(datamodel_filename,sep='\t',index_col=0)