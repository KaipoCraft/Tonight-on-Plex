from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer
from plexapi.media import TranscodeSession
from plexapi import utils

class Client:
    def __init__(username, password):
        # self.host = host
        # self.port = port
        # self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.sock.connect((self.host, self.port))
        self.username = username
        self.password = password

    def connectAPI():
        account = MyPlexAccount(self.username, self.password)
        plex = account.resource(plexServer).connect()  # returns a PlexServer instance
        return plex

    def send(self, data):
        self.sock.send(data)

    def receive(self):
        data = self.sock.recv(1024)
        return data

    def close(self):
        self.sock.close()