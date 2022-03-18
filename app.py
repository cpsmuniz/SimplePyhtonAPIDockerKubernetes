from flask import Flask, request
from datetime import datetime
import json
import socket

app = Flask(__name__)


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


@app.route('/', methods=['GET'])
def example_route():
    return json.dumps({
        "timestamp": str(datetime.now()),
        "hostname": get_ip(),
        "engine": "python3.8",
        "visitor ip": request.remote_addr
    })


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=3000)