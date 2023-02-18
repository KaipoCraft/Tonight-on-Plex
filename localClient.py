from observer import Observer
from plexapi.media import Session
from plexapi.media import Media
from plexapi.client import PlexClient

# This class is in charge of setting the media and timestamp of the media in the local version of Plex
class LocalClient:
    def __init__(self, username, password, plexServer):
        self._observer = Observer(username, password, plexServer)   # instantiate the Observer class
        self.server = self._observer.connectAPI()                     # returns a PlexServer instance

    # sets the timestamp of the media in the local version of Plex
    def setTimestamp(self):
        timestamp = self.server.getTimestamp()

    # sets the media in the local version of Plex
    def setMedia(self, media, offset):
        # moves the current client to a specified media
        self._observer.gotoMedia(media)
        # moves the current client to a specified time on the media
        self._observer.seekTo(offset, mtype='video')
        # plays the current media
        self._observer.play(mtype='video')

    # run tests with the poorly documented API
    def test(self):
        print(self.server._session)
        print("\n")
        media = self.server.library.all()
        for item in media:
            print(item.title)
        print("\n")
        for playlist in self.server.playlists():
            print(playlist.title)