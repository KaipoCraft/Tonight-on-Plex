from plexapi.myplex import MyPlexAccount    # import MyPlexAccount to allow us to log in to Plex to gain access to the API
from plexapi.server import PlexServer       # import PlexServer which will be instantiated when we run the connectAPI() function

# This class is in charge of connecting to the Plex API and getting the information from the main server
class Observer:
    def __init__(self, username, password, plexServer):
        self.username = username
        self.password = password
        self.plexServer = plexServer

    # connect to the Plex API and instantiate a PlexServer object
    def connectAPI(self):
        account = MyPlexAccount(self.username, self.password)
        server = account.resource(self.plexServer).connect()
        return server
    
    # get the media that is currently being watched on the main server
    def getMedia():
        media = _plexServer.library.all()
        for thing in media:
            print(thing.title)

    # get the current timestamp being watched on the main server
    # def getTimestamp():
        

    # run a test to see if the server is connected
    def test(self, server):
        media = server.library.all()
        for file in media:
            print(file.title)