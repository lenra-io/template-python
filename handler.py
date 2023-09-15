import json
import sys
import io
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
        return bytes(json.dumps(view.render(data.get('data', []), data.get('props', {}))), 'utf-8')
    elif 'listener' in data.keys():
        listener = __import__('listeners.' + data['listener'], fromlist=[None])
        listener.run(data.get('props', {}), data.get('event', {}), data['api'])
        return bytes("", 'utf-8')
    elif 'resource' in data.keys():
        with open("./resources/" + data['resource'], 'rb') as file:
            return file.read()
    else:
        return bytes(json.dumps(manifest), 'utf-8')
