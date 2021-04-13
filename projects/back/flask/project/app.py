import json

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['post', 'get'])
def hello_world():
    return 'Hello, World!!!!'


@app.route('/main/', methods=['get'])
def main_render():
    return render_template('index.html')


@app.route('/post/', methods=['post'])
def some_post():
    data = json.loads(request.data)
    return jsonify(data)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
