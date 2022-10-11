#!/usr/bin/python

from services.handler import Handler
from http.server import HTTPServer

with HTTPServer(('', 8000), Handler) as server:
    server.serve_forever()
