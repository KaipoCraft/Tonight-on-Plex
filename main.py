from client import Client

class Main:
    # def __init__(self):
        # self._window = Window()
        # self._window.show()

    # def run(self):
    #     self._window.run()

    def setup():
        _client = Client('nesh5910@colorado.edu', 'cxRa4yA7vHp63nU', 'T9 Plex')
        server = _client.connectAPI()
        print(server._session)

    def setTimestamp():
        _client = client.__new__(Client())
        timestamp = _client.getTimestamp()


_main = Main
_main.setup()