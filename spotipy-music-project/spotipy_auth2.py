from flask import Flask, request
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#sp setup
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id='7c0d4573b37f464ea22f821012fd1ead',
        client_secret='81cf0e62bda04efbb6ffbb716e7c7e3d',
        redirect_uri='http://localhost:8000/callback',
        scope='playlist-modify-public'
    ))

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

#user authentication process when accessing a /callback link
@app.route('/callback')
def callback():
    auth_code = request.args.get('code')    
    sp.auth_manager.get_access_token(auth_code)
    return 'Authorization successful!'

if __name__ == '__main__':
    app.run(port=8000)

#print genre list
print("Genre options: "+ str(sp.recommendation_genre_seeds()))
genre = input("Enter genre: ")

#recommendations based on desired genre & target acousticness (ill add more options later)
recommendations = sp.recommendations(seed_genres=[genre], target_acousticness = 0.9)

#get current user and create a new playlist
user_info = sp.current_user()
user_id = user_info['id']
playlist = sp.user_playlist_create(user_id, 'Recommendations in '+genre, public=True, collaborative=False, description='Spotipy music recommendations')
playlist_id = playlist['id']

#print the recommended tracks and add each of them to the created playlist
for i in recommendations["tracks"]:
    print(i["name"] + ": " + i["artists"][0]["name"])
    sp.playlist_add_items(playlist_id, [i["uri"]])