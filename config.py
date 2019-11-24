# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:22:23 2019

@author: Fabretto
"""

import os

# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"

# Datamodel path initialization
basedir = os.path.abspath(os.path.dirname(__file__))
DATA_MODEL_CSV = os.path.join(basedir, 'datamodel.csv')