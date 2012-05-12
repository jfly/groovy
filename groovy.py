import ChromeDebugger

tabs = ChromeDebugger.getTabs(port=4242)

print tabs#<<<

def onload(debugger):
    def callback(msg):
        print msg
    debugger.remote(method='Runtime.evaluate', params={'expression': 'alert("HIYA");' }, callback=callback)

wsUrl = tabs[0]['webSocketDebuggerUrl']#<<<
debugger = ChromeDebugger.ChromeDebugger(wsUrl, onload=onload)
