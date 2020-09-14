import flask
from flask import jsonify, request
import numpy as np
import pandas as pd

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False

gapminder = pd.read_csv("gapminder.csv")
gapminder_list = []
nrows = gapminder.shape[0]
for i in range(nrows):
    ser = gapminder.loc[i, :]
    row_dict = {}
    for idx, val in zip(ser.index, ser.values):
        if type(val) is str:
            row_dict[idx] = val
        elif type(val) is np.int64:
            row_dict[idx] = int(val)
        elif type(val) is np.float64:
            row_dict[idx] = float(val)
    gapminder_list.append(row_dict)
    
robbery = pd.read_csv("Taipei_Home_Robbery_10401_10907.csv")
robbery_list = []
nrows = robbery.shape[0]
for i in range(nrows):
    ser = robbery.loc[i, :]
    row_dict = {}
    for idx, val in zip(ser.index, ser.values):
        if type(val) is str:
            row_dict[idx] = val
        elif type(val) is np.int64:
            row_dict[idx] = int(val)
        elif type(val) is np.float64:
            row_dict[idx] = float(val)
    robbery_list.append(row_dict)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Git Flow Workshop!</h1>"

@app.route('/gapminder/all', methods=['GET'])
def gapminder_all():
    return jsonify(gapminder_list)


@app.route('/gapminder', methods=['GET'])
def country():
    if 'country' in request.args:
        country = request.args['country']
    else:
        return "Error: No country provided. Please specify a country."
    results = []

    for elem in gapminder_list:
        if elem['country'] == country:
            results.append(elem)
    return jsonify(results)

@app.route('/robbery/all', methods=['GET'])
def robbery_all():
    return jsonify(robbery_list)

@app.route('/robbery', methods=['GET'])
def robbery_query():
    date = ''
    location = ''
    if 'date' in request.args:
        date = request.args['date']

    if 'location' in request.args:
        location = request.args['location']
        
    results = []

    for elem in robbery_list:
        if date in str(elem['date']) and location in elem['location']:
            results.append(elem)

    if results == [] or date == location == '':
        return "No search result, and please input date format as 10901 or specify a location."
    return jsonify(results)

app.run()