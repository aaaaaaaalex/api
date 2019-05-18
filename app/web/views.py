from flask import Blueprint, render_template, send_from_directory
from jinja2.exceptions import TemplateNotFound
from mysql import connector
from os import path
from settings import GLOBALS
from urllib.parse import urlparse
import logging


app = Blueprint('views-app', __name__)

cursor = GLOBALS['db'].cursor()
ASSETS_URL = "/assets/"
ASSETS_DIR = "./assets/"

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/<path>', methods=["GET"])
def getPage(path):
    try:
        return render_template(path)
    except TemplateNotFound:
        return render_template('404.html'), 404


@app.route('/assets/<path:path>', methods=["GET"])
def getAsset(path):
    return send_from_directory(ASSETS_DIR, path)


@app.route('/images/<imgID>', methods=["GET"])
def showImage(imgID):
    cursor.execute("""
        SELECT imgURL FROM Img
        WHERE imgID = {};
    """.format(imgID))
    imgURL = cursor.fetchone()

    if not imgURL: return render_template('404.html'), 404
    else: imgURL = imgURL[0]

    hostname = urlparse(imgURL).hostname or None
    if hostname is None:
        imgURL = ASSETS_URL + imgURL


    cursor.execute("""
        SELECT c.cName from Category c, ImageCategory ic
        WHERE c.cID = ic.cID
            AND ic.imgID = {};
    """.format(imgID))
    categories = cursor.fetchall()
    if categories: categories = [c[0] for c in categories] # unpack categories
    
    img = {
        'imgID': imgID,
        'imgURL': imgURL,
        'tags': categories
    }

    return render_template('imageview.html', img=img)