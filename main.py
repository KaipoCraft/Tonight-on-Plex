from client import Client

class Main:
    def __init__(self, username, password, plexServer):
        self._client = Client(username, password, plexServer)   # instantiate the Client class
        self.server = self._client.connectAPI()                 # returns a PlexServer instance

    # sets up the connection to the Plex API
    def setup(self):
        server = self._client.connectAPI()
        print(server._session)
        return server

    # sets the timestamp of the media in the local version of Plex
    def setTimestamp(self):
        timestamp = self._client.getTimestamp()

    # sets the media in the local version of Plex
    def setMedia(self):
        server = self.setup()
        self._client.getMedia(server)

    # run tests with the poorly documented API
    def test(self):
        print(self.server.account())

# Run the main class
_main = Main('nesh5910@colorado.edu', 'cxRa4yA7vHp63nU', 'T9 Plex')
_main.test()