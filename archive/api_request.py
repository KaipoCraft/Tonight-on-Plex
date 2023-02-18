# This document sends a request to the API

username = 'nesh5910@colorado.edu'
# This is the Key being used to access the account. You can find it by #TODO
password = 'cxRa4yA7vHp63nU'
plexServer = 'T9 Plex'

# import the library requests
from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer
from plexapi.media import TranscodeSession
from plexapi import utils

account = MyPlexAccount(username, password)
plex = account.resource(plexServer).connect()  # returns a PlexServer instance

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

# maybe ??? idk
def devices(self):
        """ Returns a list of all :class:`~plexapi.myplex.MyPlexDevice` objects connected to the server. """
        data = self.query(plex.key)
        return [plex(self, elem) for elem in data]


# get time stamp from main user on playlist


# Client class controls what is being watched
        # goToMedia(media, **params) - directs the client to a specified media object
        # pause(mtype='video') - pauses playback of the video
        # play(mtype='video') - starts playback of the video
        # seekTo(offset, mtype='video') - sets the offset of the video (in milliseconds)

# use media.Session and media.TranscodeSession
# streamers share rating key UUID assigned to content
# timestamp object

print(plex._session)

# whenever things aren't working, reload the page, open the networks tab in dev tools, and then search what pops up
# need to get to "client" object and find "timeline" object - that has the best info