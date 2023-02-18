# This document sends a request to the API

username = 'nesh5910@colorado.edu'
apikey = 'cxRa4yA7vHp63nU'

# import the library requests
from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer
from plexapi.media import TranscodeSession
account = MyPlexAccount(username, apikey)
plex = account.resource('T9 Plex').connect()  # returns a PlexServer instance

# Example 1: List all unwatched movies.
# movies = plex.library.section('Movies')
# for video in movies.search(unwatched=True):
#     print(video.title)

media = plex.library.all()
for thing in media:
    print(thing.title)

# for playlist in plex.playlists():
#     print(playlist.title)

# print(plex.playlists()[0].title)

# get playlist

# get users on server

# get time stamp from main user on playlist

# use media.Session and media.TranscodeSession
# streamers share rating key UUID assigned to content
# timestamp object

print(plex._session)

# whenever things aren't working, reload the page, open the networks tab in dev tools, and then search what pops up
# need to get to "client" object and find "timeline" object - that has the best info