from os import path
from flask import Blueprint, render_template
from jinja2.exceptions import TemplateNotFound

app = Blueprint('views-app', __name__)


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/<path>', methods=["GET"])
def getPage(path):
    try:
        return render_template(path)
    except TemplateNotFound:
        return render_template('404.html'), 404


@app.route('/assets/<path>', methods=["GET"])
def getAsset(path):
    if not path: path = "index.html"
    try:
        mime_type = "text/css; charset=utf-8" if path.endswith('.css') else "text/html; charset=utf-8"
        with open('./assets/'+path, 'rb') as asset:
            asset_bytes = asset.read()
            return asset_bytes, 200, {'Content-Type': mime_type}

    except OSError:
        return render_template('404.html'), 404
