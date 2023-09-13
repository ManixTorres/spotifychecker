import spotipy

from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, render_template, request

app = Flask(__flaskk__)

client_id = 'dd734bbd1513415cbcc0a3d70b0824b9'
client_secret = 'Ee0604902059c46eab1013330daa70015E'
redirect_uri = 'http://blacksunrisen.club/'

def index():
    if request.method == 'post';
        spotify_username = request.form['username']


        top_tracks = sp.current_user_top_tracks(time_range)