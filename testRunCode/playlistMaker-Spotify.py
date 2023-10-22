""""
Creator: Ethan Stevenson 
Title: Playlist Maker for Spotify
Purpose: Learning to work with Spoitpy library and creating playlist for my Spotify account so that I can utilize this information to make any Apple Music Playlist and Spotify Playlist and vice versa
"""

import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth

#Inforamtion for my Spotify account and windows machine
DEVICE_ID = "d7390bb1fd59b6ee0811700a4ee5be4c53b0e032"
CLIENT_ID = "aacef9dd894042cc88b52aba5aa1e9d6"
CLIENT_SECRET = "515d356ac5e6465b857628c155201bff"
REDIRECT = "http://localhost:8080"
SCOPE = "user-read-playback-state,user-modify-playback-state,playlist-read-private,playlist-modify-private,playlist-modify-public"

#Spotify Authorization 
spotify = sp.Spotify(auth_manager = SpotifyOAuth(client_id = CLIENT_ID, client_secret = CLIENT_SECRET, redirect_uri = REDIRECT, scope = SCOPE))

"""Testing Authorization
spotify.start_playback(device_id = DEVICE_ID, uris = ['spotify:track:45vW6Apg3QwawKzBi03rgD'])
"""

#Reading Playlist Data by grabbing track name, album name, and artist name
PLAYLIST_ID = "6nT8YtsENHvC3PKvSAtc9m"
FIELDS = "tracks.items(track(name,artists(name),album(name)))"
data = spotify.playlist(PLAYLIST_ID, FIELDS)["tracks"]["items"]
#print(data)

"""
print("Indexing just by tracks")
print(data["tracks"])

#At this point, can now start iterating over the songs in playlist
print("\nIndexing by tracks and items")
data["tracks"]["items"]
"""
# Loop prints in format "SONGNAME by ARTIST on ALBUM"
#for playlistEntry in data:
 #   print(playlistEntry["track"]["name"] + " by " + playlistEntry["track"]["artists"][0]["name"] + " on " + playlistEntry["track"]["album"]["name"])



#Creating playlist and adding songs to playlist
USER_ID = spotify.me()["id"]
PLAYLIST_NAME = "Test Playlist for Converter"
#createdPlaylist = spotify.user_playlist_create(USER_ID, "PLAYLIST_NAME")

#Searching for a song
SEARCH_PARAMETER = "track%3ACongratulations%2520artist%3APost%2520Malone"
songQuery = spotify.search(SEARCH_PARAMETER, 50)["tracks"]["items"]

for song in songQuery:
    print(song["name"] + " by " + song["artists"][0]["name"])
