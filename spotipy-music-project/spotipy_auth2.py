from flask import Flask, request
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id='7c0d4573b37f464ea22f821012fd1ead',
        client_secret='81cf0e62bda04efbb6ffbb716e7c7e3d',
        redirect_uri='http://localhost:8000/callback',
        scope='user-library-read'
    ))

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/callback')
def callback():
    auth_code = request.args.get('code')    
    sp.auth_manager.get_access_token(auth_code)
    return 'Authorization successful!'

if __name__ == '__main__':
    app.run(port=8000)

print("Genre options: "+ str(sp.recommendation_genre_seeds()))
genre = input("Enter genre: ")

recommendations = sp.recommendations(seed_genres=[genre], target_acousticness = 1)
#for i in recommendations["tracks"][0]["artists"]:
#    print(i["name"])
#print(recommendations["tracks"][0])

for i in recommendations["tracks"]:
    print(i["name"] + ": " + i["artists"][0]["name"])
#print(recommendations["tracks"][0]["name"])

#print(sp.current_user_playing_track.target_popularity)