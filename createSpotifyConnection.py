import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def create_spotify_connection(keys_filename='spotifyKeys'):

    keys_file = open(keys_filename)

    keys = json.load(keys_file)

    client_credentials_manager = SpotifyClientCredentials(keys['client_key'], keys['client_secret'])

    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    return spotify
