#!/usr/bin/env python

command_id = { 'play': 'player_play_pause', 'next': 'player_next', 'prev': 'player_previous' }

def issueCmd(remoteDebuggingPort, cmd):
    assert cmd in command_id

    import webkit_remote_debugger
    from webkit_remote_debugger import WebkitRemoteDebugger

    tabs = webkit_remote_debugger.getTabs(port=remoteDebuggingPort)

    def onload(debugger):
        def callback(msg):
            print msg

        domId = command_id[cmd]
        play_pause = "document.getElementById('%s').click();" % domId
        debugger.remote(method='Runtime.evaluate',
                        params={'expression': play_pause },
                        callback=callback)

    grooveTabs = filter(lambda tab: tab['url'].find('grooveshark.com') != -1, tabs)
    assert len(grooveTabs) == 1, "Too many or too few grooveshark tabs found"

    grooveTab = grooveTabs[0]
    debugger = WebkitRemoteDebugger(grooveTab['webSocketDebuggerUrl'], onload=onload)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("port",
                        type=int,
                        help=("Google Chrome remote debugging port"
                              " (ex: google-chrome --remote-debugging-port=4242)"))
    parser.add_argument("cmd", choices=command_id.keys())
    args = parser.parse_args()

    issueCmd(args.port, args.cmd)
