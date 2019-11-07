# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:54:35 2019

@author: Fabretto
"""

from flask import Flask, url_for, request, jsonify

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

from .utils import LoadDataModel

import json
import pandas as pd

@app.route('/')
@app.route('/index/')
def index():
    return "Hello world !"
#    print(datamodel.head())
#    return json.dumps(datamodel.shape)
#    return jsonify([[label, content.count()] for label, content in datamodel.iteritems()])
#    return jsonify(*datamodel[0])
#    return datamodel.head().to_json(orient="records")
    
@app.route('/recmovie/')
def recmovie():
    datamodel, current_path = LoadDataModel()
    rec_imdbid = request.args.get('imdbid')
    rec_title_year = int(request.args.get('title_year'))
    cluster = datamodel[datamodel['imdbid'] == rec_imdbid]['cluster20'].item()
#    return json.dumps(cluster)
    return datamodel[
            (datamodel['cluster20'] == cluster) &
            (datamodel['title_year'] >= rec_title_year)].nlargest(5,
                   'imdb_score').to_json(orient='records')
#    return json.dumps(*cluster)
#    return datamodel.nlargest(5,'imdb_score').to_json(orient="records")
#    return rec_imdbid + ' ' + rec_title_year
  
#    return "Hello world !"
#    print(datamodel.head())
#    return json.dumps(datamodel.shape)
#    return jsonify([[label, content.count()] for label, content in datamodel.iteritems()])
#    return jsonify(*datamodel[0])
#    return datamodel.head().to_json(orient="records")
    
