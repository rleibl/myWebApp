
from flask import Flask, send_from_directory
from flask import request

app = Flask(__name__, static_url_path='')

# -------------------------------------------------------------------
# Javascript files
# -------------------------------------------------------------------


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

# -------------------------------------------------------------------
# Static files
# -------------------------------------------------------------------


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

# -------------------------------------------------------------------
# API Endpoints
# -------------------------------------------------------------------


#
# Test command
#     curl -s -X POST -d '{foo:bar}' 'localhost:5000/api/echo?q=asdf' | jq
#     curl -v -X POST -H 'Content-Type: application/json' -d '{"foo":"bar"}' 'localhost:5000/api/echo?q=asdf' | jq
#
@app.route('/api/echo', methods=['GET', 'POST'])
def echo():
    d = dict()
    d['method'] = request.method
    d['path'] = request.path
    d['args'] = request.args  # URL args
    d['data'] = request.data.decode('UTF-8')  # raw data

    # if Content-Type is not set to application/json on the request, this will return 400
    d['json'] = request.json

    return d  # returning a dict automatically makes it a JSON response


# -------------------------------------------------------------------
# index
# -------------------------------------------------------------------
@app.route("/")
def index():
    return send_from_directory('static', 'index.html')
