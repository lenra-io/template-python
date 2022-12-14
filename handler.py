import json
import sys
from manifest import manifest

def log(str):
    print(str, file=sys.stderr)

def handle(body):
    log(f"Body: {body}")
    data = {}
    if body != '':
        data = json.loads(body)

    log(f"data: {data}")

    if 'widget' in data.keys():
        widget = __import__('widgets.' + data['widget'], fromlist=[None])
        return json.dumps(widget.render(data["data"], data["props"]))
    elif 'action' in data.keys():
        listener = __import__('listeners.' + data['action'], fromlist=[None])
        listener.run(data["props"], data["event"], data["api"])
        return ""
    elif 'resource' in data.keys():
        return ""
    else:
        return json.dumps(manifest)
