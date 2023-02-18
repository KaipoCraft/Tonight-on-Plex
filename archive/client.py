from plexapi.myplex import MyPlexAccount    # import MyPlexAccount to allow us to log in to Plex to gain access to the API
from plexapi.server import PlexServer       # import PlexServer which will be instantiated when we run the connectAPI() function

class Client:
    # Client class to handle the connection to the Plex API
    # params: username, password, plexServer
    def __init__(self, username, password, plexServer):
        self.username = username
        self.password = password
        self.plexServer = plexServer

    # connects to the Plex API
    def connectAPI(self):
        account = MyPlexAccount(self.username, self.password)
        server = account.resource(self.plexServer).connect()  # returns a PlexServer instance
        return server
    
    # get a list of all the media on the server
    def getMedia(self, _plexServer):
        media = _plexServer.library.all()
        for thing in media:
            print(thing.title)

# TODO: recieve the timestamp from the main user