from http.server import BaseHTTPRequestHandler
from handler import handle
from http.server import HTTPServer


class Handler(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        body = self.rfile.read().decode('utf-8')
        result = handle(body)

        self.do_HEAD()
        self.wfile.write(bytes(result, 'utf-8'))

def run():
    with HTTPServer(('', 8000), Handler) as server:
        server.serve_forever()