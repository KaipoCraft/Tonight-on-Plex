from plexapi.myplex import MyPlexAccount    # import MyPlexAccount to allow us to log in to Plex to gain access to the API
from plexapi.server import PlexServer       # import PlexServer which will be instantiated when we run the connectAPI() function
from plexapi.media import TranscodeSession
from plexapi import utils

class Client:
    def __init__(self, username, password, plexServer):
        # self.host = host
        # self.port = port
        # self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.sock.connect((self.host, self.port))
        self.username = username
        self.password = password
        self.plexServer = plexServer

    def connectAPI(self):
        account = MyPlexAccount(self.username, self.password)
        plex = account.resource(self.plexServer).connect()  # returns a PlexServer instance
        return plex

    def send(self, data):
        self.sock.send(data)

    def receive(self):
        data = self.sock.recv(1024)
        return data

    def close(self):
        self.sock.close()