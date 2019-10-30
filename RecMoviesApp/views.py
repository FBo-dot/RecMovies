# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:54:35 2019

@author: Fabretto
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"

if __name__ == "__main__":
    app.run()