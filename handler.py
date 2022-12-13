import json
from http.server import BaseHTTPRequestHandler
from manifest import manifest


class Handler(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        data = {}
        if length != 0:
            data = json.loads(self.rfile.read(length))
            print(data)
            print(data.keys())

        if 'widget' in data.keys():
            widget = __import__('widgets.' + data['widget'], fromlist=[None])
            self.do_HEAD()
            self.wfile.write(bytes(json.dumps(widget.render(data["data"], data["props"])), 'utf-8'))
        elif 'action' in data.keys():

            listener = __import__('listeners.' + data['action'], fromlist=[None])
            self.do_HEAD()
            self.wfile.write(bytes(json.dumps(listener.run(data["props"], data["event"], data["api"])), 'utf-8'))
        elif 'resource' in data.keys():
            self.do_HEAD()
            pass
        else:
            self.do_HEAD()
            print(json.dumps(manifest))
            self.wfile.write(bytes(json.dumps(manifest), 'utf-8'))
