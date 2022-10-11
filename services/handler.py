import json
from http.server import BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        if self.headers.get('Authorization') is None:
            length = int(self.headers.get('Content-Length'))
            data = self.rfile.read(length).decode('utf-8')

            self.do_HEAD()
            self.wfile.write(json.dumps(data).encode('utf-8'))
            pass
        else:
            pass
