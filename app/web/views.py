from flask import Blueprint, render_template, send_from_directory
from jinja2.exceptions import TemplateNotFound
from mysql import connector
from os import path
from settings import GLOBALS
from urllib.parse import urlparse
import json
import logging


app = Blueprint('views-app', __name__)

cursor = GLOBALS['db'].cursor(buffered=True)
IMAGES_URL = "/assets/images/"
ASSETS_DIR = "./assets/"


def parseImgSrc(imgURL):
    hostname = urlparse(imgURL).hostname or None
    if hostname is None:
        imgURL = IMAGES_URL + imgURL

    return imgURL


def getRecentImages(num_images=15):
    cursor.execute("""
        SELECT imgID, userID, imgURL, imgDateTime
        FROM Img
        ORDER BY imgDateTime DESC;
        """)
    
    imgs = cursor.fetchmany(num_images)
    cursor.fetchall()

    return imgs


def getPopularTags(num_tags=-1):
    cursor.execute("""
        SELECT c.cName, count(ic.imgID) imgCount
        FROM Category c, ImageCategory ic
        WHERE c.cID = ic.cID
        GROUP BY c.cID
        ORDER BY imgCount DESC;
    """)

    if num_tags < 1: tags = cursor.fetchall()
    else:
        tags = cursor.fetchmany(num_tags)
        cursor.fetchall()

    return tags


def getTrainedModels(num_models=-1):
    cursor.execute("""
        SELECT modelCAccuracy, modelDateCreated, modelURL, modelName
        FROM Model;
    """)

    if num_models > 0:
        models = cursor.fetchmany(num_models)
    else:
        models = cursor.fetchall()

    return models


@app.route('/', methods=["GET"])
def index():
    imgs = getRecentImages()
    imgs = [{
        'href': "/images/{}".format(img[0]),
        'src' : parseImgSrc(img[2])
        } for img in imgs]

    return render_template('index.html', imgs=imgs)


@app.route('/dashboard', methods=["GET"])
def showDashboard():
    models = getTrainedModels()
    models = [{
        'modelCAccuracy': m[0],
        'modelDateCreated': m[1].strftime('%Y-%m-%d %H:%M:%S'),
        'modelURL': m[2],
        'modelName': m[3] } for m in models]

    popularTags = getPopularTags(num_tags=6)
    popularTags = [{
            'name': t[0],
            'count': t[1]} for t in popularTags ]

    return render_template('adminDashboard.html', 
                                args={
                                    'models': models,
                                    'tags'  : popularTags
                                    })


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
    imgURL = parseImgSrc(imgURL)

    cursor.execute("""
        SELECT c.cName, c.cID from Category c, ImageCategory ic
        WHERE c.cID = ic.cID
            AND ic.imgID = {};
    """.format(imgID))
    categories = cursor.fetchall()
    if categories: categories = [{
                            'name':c[0],
                            'id':c[1]} for c in categories] # unpack categories
    
    img = {
        'imgID': imgID,
        'imgURL': imgURL,
        'tags': categories
    }

    return render_template('imageview.html', img=img)