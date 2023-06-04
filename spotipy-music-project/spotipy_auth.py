import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

client_id = '7c0d4573b37f464ea22f821012fd1ead'
client_secret = '81cf0e62bda04efbb6ffbb716e7c7e3d'
redirect_uri = 'https://localhost:8000/callback'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

tracks = sp.current_user_top_tracks(limit=20)
results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])