#!/usr/bin/env pythonfrom pprint import pprint as ppfrom flask import Flask, flash, redirect, render_template, request, url_forfrom pi import query_api
from flask import Flask, render_template, request, jsonify
import math
import random
import json

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/addnumber')
def add():
    shots = 100000
    incircle = 0
    x = request.args.get('x', 0, type=float)
    y = request.args.get('y', 0, type=float)
    z= request.args.get('z', 0, type=int)
    shots=z
    for i in range(0, shots):
        random1 = random.uniform(x, y)
        random2 = random.uniform(x, y)
        if( ( random1*random1 + random2*random2 ) < 1 ):
            incircle += 1
        output=4.0 * incircle/shots
        a=[{'output':output,'shots':shots}]
        print(output,z)
    return jsonify(result=output)
    


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
