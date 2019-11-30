# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:54:35 2019

@author: Fabretto
"""

from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True 

import json
import pandas as pd

from .__init__ import datamodel

@app.route('/')
@app.route('/index/')
def index():
    df_result = datamodel.sample(n=5, random_state=42)
    lines = [dict(
            zip(df_result.columns,line)) for ndx, line in df_result.iterrows()]
    result = {'_choose_one': lines}

    result = jsonify(result)
    return result
       
#    return "Hello world !"
#    print(datamodel.head())
#    return json.dumps(datamodel.shape)
#    return jsonify([[label, content.count()] for label, content in datamodel.iteritems()])
#    return jsonify(*datamodel[0])
#    return datamodel.head().to_json(orient="records")
    
@app.route('/recmovie/')
def recmovie():
    rec_imdbid = request.args.get('imdbid')
    rec_title_year = int(request.args.get('title_year'))
    cluster = datamodel[datamodel['imdbid'] == rec_imdbid]['cluster20'].iloc[0]
    df_result = datamodel[
        (datamodel['cluster20'] == cluster) &
        (datamodel['title_year'] >= rec_title_year)].nlargest(5,
            'imdb_score')
    lines = [dict(
            zip(df_result.columns,line)) for ndx, line in df_result.iterrows()]
    result = {'_results': lines}

    result = jsonify(result)
    return result
#    return render_template('recmovie.html',result=result)

#    return json.dumps(cluster)
#    return json.dumps(*cluster)
#    return datamodel.nlargest(5,'imdb_score').to_json(orient="records")
#    return rec_imdbid + ' ' + rec_title_year
#    return "Hello world !"
#    print(datamodel.head())
#    return json.dumps(datamodel.shape)
#    return jsonify([[label, content.count()] for label, content in datamodel.iteritems()])
#    return jsonify(*datamodel[0])
#    return datamodel.head().to_json(orient="records")