import json
from http.server import BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        length = int(self.headers.get('Content-Length'))
        data = json.loads(self.rfile.read(length))
        print(data)
        print(data["key1"])

        if data["widget"] is not None:
            import "widgets/${data["widget"]}"
            pass
        elif data["action"] is not None:
            pass
        elif data["resource"] is not None:
            pass
        else:
            pass

        self.do_HEAD()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        pass
