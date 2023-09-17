import spotipy

from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, render_template, request

app = Flask(__name__)

client_id = 'dd734bbd1513415cbcc0a3d70b0824b9'
client_secret = 'Ee0604902059c46eab1013330daa70015E'
redirect_uri = 'http://blacksunrisen.club/'

def index():
    if request.method == 'post':
        spotify_username = request.form['username']
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope="user-library-read user-read-recently-played"))
        top_tracks = sp.current_user_top_tracks(time_range="long_term", limit=1)
 
        if top_tracks['items']:
            most_listened_track = top_tracks['items'][0]
            track_name = most_listened_track['name']
            artist_name = most_listened_track['artists'][0]['name']

            album_id = most_listened_track['album']['id']
            album_details = sp.album(album_id)
            album_cover_url = album_details['images'][0]['url']

            return render_template('result.html', track_name=track_name, artist_name=artist_name, album_cover_url=album_cover_url)
        else:
            return render_template('result.html', error_message="Failure")
        

    return render_template(index.html)
    
if __name__ == '__main__':
    app.run(debug=True)        

