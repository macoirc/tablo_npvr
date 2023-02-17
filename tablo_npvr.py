#!/usr/bin/env python3
# tablo_npvr.py

import http.server
import socketserver
import requests
from urllib.parse import unquote, urlparse
from pathlib import PurePosixPath
 
PORT = 8050
tabloIP = '127.0.0.1'
 
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
      o = self.path
      opath = PurePosixPath(unquote(urlparse(o).path)).parts[1]
      if (opath == 'playlist.m3u'):
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
      elif (opath == 'watch'):
        ch = PurePosixPath(unquote(urlparse(o).path)).parts[2]
        url = 'http://' + tabloIP + ':8885/guide/channels/' + str(ch) + '/watch'
        chinfo = requests.post(url).json()
        self.send_response(302)
        self.send_header('Location',chinfo['playlist_url'])
        self.end_headers()
      else:
		message = "<html><body>Page Not Found.</body></html>"
		self.send_response(404)
		self.send_header('Content-Type', 'text/html')
		self.send_header('Content-Length', len(message))
		self.end_headers()
		self.wfile.write( bytes(message, "utf-8" ))
		self.close_connection = True
 
Handler = MyHttpRequestHandler
 
with socketserver.TCPServer(("", PORT), Handler) as httpd:
  print("Http Server Serving at port", PORT)
  httpd.serve_forever()
