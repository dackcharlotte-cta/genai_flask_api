from flask import Flask, render_template, request
from kat_spotify import get_songs

# app is a variable representing 
# our flask app
# __name__ is a python reserved 
# word
# telling Flask where our code
# lives
app = Flask(__name__)

default_year = '1999'

# set up our landing page
@app.route('/')
def index():
	my_songs = get_songs(default_year)
	return render_template('index.html', songs=my_songs, year=default_year)

# only use this when posting data!
@app.route('/', methods=['POST'])
def index_post():
	user_year = request.form['req_question']
	my_songs = get_songs(user_year)
	return render_template('index.html', songs=my_songs, year=user_year)