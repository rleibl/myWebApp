
from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route("/")
def index():
    return send_from_directory('static', 'index.html')