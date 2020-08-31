import flask
from flask import jsonify, request
import numpy as np
import pandas as pd

app = flask.Flask(__name__)
app.config["DEBUG"] = True

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
    return 


@app.route('/robbery', methods=['GET'])
def robbery_loction():
    return

app.run()