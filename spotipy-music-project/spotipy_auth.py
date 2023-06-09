from flask import Flask, request
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

@app.route('/')
def home():
    return ' '

@app.route('/callback')
def callback():

    # Set up Spotipy with the correct client ID, client secret, and redirect URI
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id='7c0d4573b37f464ea22f821012fd1ead',
        client_secret='81cf0e62bda04efbb6ffbb716e7c7e3d',
        redirect_uri='http://localhost:8000/callback',
        scope='user-library-read'
    ))

    auth_url = sp.auth_manager.get_authorize_url()
    print("Please visit this URL to authorize the application: ", auth_url)

    auth_code = input("Enter the authorization code: ")

    sp.auth_manager.get_access_token(auth_code)
    
    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx + 1, track['artists'][0]['name'], "-", track['name'])

    return "Authorization successful!"

if __name__ == '__main__':
    app.run(port=8000)