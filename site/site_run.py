import os
import flask
import sys
from flask import Flask,redirect
import generate_html

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def hello():
    return flask.render_template("index.html")

@app.route('/races')
def race_page():
  ability_dict, class_data, race_data = generate_html.loadData()
  image_path = "/static/images/race/female"
  template = generate_html.standardHtmlOut(race_data, ability_dict, image_path)
  return template

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)