import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '7c0d4573b37f464ea22f821012fd1ead'
client_secret = '81cf0e62bda04efbb6ffbb716e7c7e3d'
#redirect_uri = 'http://localhost:8000/callback'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

username = 'e6rq5411r1n7pa11htjfom5qi'
playlists = sp.user_playlists(username)
#tracks = sp.current_user_top_tracks(limit=20, offset=0, time_range='medium_term')
#for playlist in playlists['items']:
    #print(playlist['name'])

print("Genre options: "+ str(sp.recommendation_genre_seeds()))
genre = input("Enter genre: ")

recommendations = sp.recommendations(seed_genres=[genre])
for i in recommendations["tracks"][0]["artists"]:
    print(i["name"])
#print(recommendations["tracks"][0])

for i in recommendations["tracks"]:
    print(i["name"] + ": " + i["artists"][0]["name"])
#print(recommendations["tracks"][0]["name"])