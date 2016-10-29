import flask
from flask import render_template
from flask import request
from flask import url_for
from flask import jsonify

import CONFIG

import json

app = flask.Flask(__name__)
app.secret_key = CONFIG.secret_key

list = open('POI.txt','r')
points = list.readlines()



@app.route("/")
@app.route("/index")
def index():
	flask.session['points'] = points
	return flask.render_template('map.html')
  
  
if __name__ == "__main__": 
    app.debug = True
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
else:
    app.debug=False

