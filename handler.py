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

    if 'view' in data.keys():
        view = __import__('views.' + data['view'], fromlist=[None])
        return json.dumps(view.render(data['data'], data['props']))
    elif 'action' in data.keys():
        listener = __import__('listeners.' + data['action'], fromlist=[None])
        listener.run(data['props'], data['event'], data['api'])
        return ""
    elif 'resource' in data.keys():
        return ""
    else:
        return json.dumps(manifest)
