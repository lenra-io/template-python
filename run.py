#!/usr/bin/python

from services import handler
from http.server import HTTPServer

with HTTPServer(('', 8000), handler.Handler) as server:
    server.serve_forever()
