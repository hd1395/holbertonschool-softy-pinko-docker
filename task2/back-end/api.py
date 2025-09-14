# Simple Flask API for Task 1
from flask import Flask

app = Flask(__name__)

@app.route('/api/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Host on all interfaces so it's reachable from outside the container
    app.run(host='0.0.0.0', port=5252)
