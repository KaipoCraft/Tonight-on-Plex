# This document sends a request to the API

# import the library requests
from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer
from plexiapi.media import TranscodeSession
account = MyPlexAccount('nesh5910@colorado.edu', 'cxRa4yA7vHp63nU')
plex = account.resource('T9 Plex').connect()  # returns a PlexServer instance

# Example 1: List all unwatched movies.
# movies = plex.library.section('Movies')
# for video in movies.search(unwatched=True):
#     print(video.title)

# make a request for the playlist
# make a request for where the keys are and match that
# playlist = plex.playlist.items()
# for thing in playlist:
#     print(thing.title)

# media = plex.library.all()
# for thing in media:
#     print(thing.title)

# for playlist in plex.playlists():
#     print(playlist.title)

# print(plex.playlists()[0].title)

# get playlist

# get users on server

# get time stamp from main user on playlist

# use media.Session and media.TranscodeSession
# streamers share rating key UUID assigned to content
# timestamp object

print(plexiapi.media.TranscodeSession.key)