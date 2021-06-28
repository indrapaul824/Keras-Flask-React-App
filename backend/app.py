import os
from flask import Flask, render_template, request
from werkzeug.wrappers import request
from reverseProxy import proxyRequest
from classifier import classifyImage

MODE = os.getenv('FLASK_ENV')
DEV_SERVER_URL = 'http://localhost:3000/'

app = Flask(__name__)

if MODE == "development":
    app = Flask(__name__, static_folder=None)

@app.route('/')
@app.route('/<path:path>')
def index(path=''):
    if MODE == "development":
        return proxyRequest(DEV_SERVER_URL, path)
    else:
        return render_template("index.html")


@app.route('/classify', methods=['POST'])
def classify():
    if (request.files['image']):
        file = request.files['image']

        res = classifyImage(file)
        print("Model Classification: " + res)
        return res