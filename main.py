# ATLAS Institute CU Boulder
# T9 Hacks Hackathon
# Tonight, on Plex
#
# Authors:  Neill Kaipo Shikada, William Harris, Quil Cummings, Lila Hunter-Reay
#
# This extension of the Plex API allows for the creation of a local Plex server that can be controlled by a main server.
# It integrates engaging questions into the process of watching media with a wide audience.
#
# Not fully functional at this point, however we've achieved the main functionality of probing the server for media
# and constructed a sample .json file that can be used to create a Plex server calendar of showings.
#
# output to users:          timestamp
#                           timestamps of questions
#                           questions
#                           data view of the viewers to show at the end of the media
# input to main server:     responses to questions

from observer import Observer
from localClient import LocalClient
from plexapi.media import Media

class Main:
    def __init__(self, username, password, plexServer):
        self._observer = Observer(username, password, plexServer)           # instantiate the Observer
        self._localClient = LocalClient(username, password, plexServer)     # instantiate the LocalClient

    # the main function that runs the program
    def run(self):
        # instantiated the server object
        server = self._observer.connectAPI()
        # gets the information from the main server
        # self._observer().getMedia(server)
        # sets the media and timestamp of the media in the local version of Plex
        self._localClient.test()
        
_main = Main('nesh5910@colorado.edu', 'cxRa4yA7vHp63nU', 'T9 Plex')
_main.run()