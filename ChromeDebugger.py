import httplib2
import json
from ws4py.client.threadedclient import WebSocketClient

def getTabs(port, domain='localhost'):
    http = httplib2.Http()
    resp, content = http.request("http://%s:%s/json" % ( domain, port ))
    tabs = json.loads(content)
    return tabs

class ChromeDebugger(WebSocketClient):
    def __init__(self, webSocketDebuggerUrl, onload=None):
        WebSocketClient.__init__(self, webSocketDebuggerUrl)

        self.onload = onload
        self.pendingCallbacks = {}
        self.freeIds = []

        self.connect()

    def opened(self):
        if self.onload:
            self.onload(self)

    def closed(self, code, reason=None):
        print code, reason#<<<

    def received_message(self, m):
        msg = json.loads(str(m))

        assert 'id' in msg
        idee = msg['id']

        if idee in self.pendingCallbacks:
            self.pendingCallbacks[idee](msg)
            del self.pendingCallbacks[idee]
            self.freeIds.append(idee)

    def remote(self, method, params, callback=None):
        idee = None
        if len(self.freeIds) > 0:
            idee = self.freeIds.pop()
        else:
            idee = len(self.pendingCallbacks)
        self.pendingCallbacks[idee] = callback
        obj = { 'id': idee, 'method': method, 'params': params }
        self.send(json.dumps(obj))
