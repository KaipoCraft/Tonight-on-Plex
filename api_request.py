# This document sends a request to the API

# import the library requests
import requests

from plexapi.myplex import MyPlexAccount
account = MyPlexAccount('nesh5910@colorado.edu', 'cxRa4yA7vHp63nU')
plex = account.resource('T9 Plex').connect()  # returns a PlexServer instance

# Example 1: List all unwatched movies.
movies = plex.library.section('Movies')
for video in movies.search(unwatched=True):
    print(video.title)