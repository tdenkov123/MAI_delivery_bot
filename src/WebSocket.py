import httplib2
import http
import argparse

class WebSocket():
    def OpenSocket():
        h = httplib2.Http()
        resp, content = h.request("http://hltv.org/")
        print(content.decode())

if __name__ == '__main__':
    WebSocket.OpenSocket()