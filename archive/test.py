from observer import Subscriber
from plexapi.media import Session
from plexapi.media import Media
from plexapi.client import PlexClient

class Test:
    def __init__(self, username, password, plexServer):
        self.server = Subscriber(username, password, plexServer).connectAPI()
        self._client = PlexClient(server=self.server, data=None, initpath="https://75-166-147-241.0a5b0bade7bb4d9fb6c87a1cf5f691b7.plex.direct:18840/:/timeline?ratingKey=18", baseurl="https://app.plex.tv/", identifier=None, token=None, connect=True, session=None, timeout=None)
    
    def getMedia():
        # find the media object from the master server
        Media.T

    def setMedia(self, media, offset):
        # moves the current client to a specified media
        self._client.gotoMedia(media)
        # moves the current client to a specified time on the media
        self._client.seekTo(offset, mtype='video')
        # plays the current media
        self._client.play(mtype='video')

_main = Test('nesh5910@colorado.edu', 'cxRa4yA7vHp63nU', 'T9 Plex')
_main.setMedia()
# _main.setMedia(Media(_main.server, initpath=None, parent=None), '400000')
# print(type(Subscriber('nesh5910@colorado.edu', 'cxRa4yA7vHp63nU', 'T9 Plex').connectAPI()._session))