import json
import os
import sys
from msds.base.path import PATH_ROOT
from flask import render_template

def display_home():
    return render_template('backtest.html', name='zyd')

def display_data():
    with open(os.path.join(PATH_ROOT, '__btcache__/backtest.json')) as f:
        return json.load(f)
