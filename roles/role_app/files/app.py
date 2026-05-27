from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    env = os.getenv('ENV', 'unknown')
    return f"Hello from {hostname} in {env} environment!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
