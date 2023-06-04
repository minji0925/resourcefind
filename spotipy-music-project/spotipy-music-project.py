import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

client_id = '7c0d4573b37f464ea22f821012fd1ead'
client_secret = '81cf0e62bda04efbb6ffbb716e7c7e3d'
redirect_uri = 'https://localhost:8888/callback'

#auth_manager = SpotifyClientCredentials()
#sp = spotipy.Spotify(auth_manager=auth_manager)
#client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='user-library-read'))
#sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

#my username: e6rq5411r1n7pa11htjfom5qi
username = 'e6rq5411r1n7pa11htjfom5qi'
playlists = sp.user_playlists(username)
for playlist in playlists['items']:
    print(playlist['name'])