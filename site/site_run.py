import os
import flask
import sys
from flask import Flask,redirect
from flask import request
import generate_html

app = Flask(__name__, static_url_path='/static')

# @app.route('/')
# def hello():
#     # return flask.render_template("female_races.html")
  # return flask.render_template("index.html")


# @app.route('/races')
@app.route('/')
def index_page():
  print("hit index")
  return creation_landing_page()

@app.route('/creation')
def creation_landing_page():
  print('hit creation')
  return race_page()

@app.route('/creation/races')
def race_page():
  print('hit race')
  ability_dict, class_data, race_data = generate_html.loadData()
  image_path = "/static/images/races/female"
  template = generate_html.cardsHtmlOut(race_data, ability_dict, image_path, next_page='creation/classes', forwarding_param='race')
  return template

@app.route('/creation/classes')
def class_page():
  race = request.args.get('race')
  ability_dict, class_data, race_data = generate_html.loadData()
  image_path = "/static/images/classes"
  template = generate_html.cardsHtmlOut(class_data, ability_dict, image_path, prev_value='race={0}'.format(race), next_page='creation/combo', forwarding_param='rangers_class')
  return template

@app.route('/creation/combo')
def combo_page():
  race = request.args.get('race')
  rangers_class = request.args.get('rangers_class')
  ability_dict, class_data, race_data = generate_html.loadData()
  image_path = "/static/images/classes"
  template = generate_html.comboHtml(race_data, class_data, ability_dict, image_path, race, rangers_class)
  return template

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5015))
    app.run(host='0.0.0.0', port=port)