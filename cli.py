import sys
from handler import handle

def read_stdin():
    buffer = ''
    for line in sys.stdin:
        if 'Exit' == line.rstrip():
            break
        buffer += line
    return buffer



def run():
    body = read_stdin()
    result = handle(body)
    sys.stdout.buffer.write(result)