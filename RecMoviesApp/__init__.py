# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:22:23 2019

@author: Fabretto
"""

from flask import Flask # Flask needed

from .views import app  # Flask app instantiation needed

from .utils import LoadDataModel

# Load the data model for movies recommendation
datamodel = LoadDataModel()