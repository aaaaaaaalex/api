from mysql import connector
from flask import Blueprint, request, render_template
from io import BytesIO
from keras.backend import clear_session
from keras.models import model_from_json
from keras.optimizers import SGD
from keras.preprocessing import image as k_image
from os import path, makedirs, environ, walk
from PIL import Image as pimage, ImageFile
from datetime import datetime

import json
import logging
import numpy as np
import operator
import time

# project objects
from predictor import Predictor
from settings import GLOBALS
cursor = GLOBALS['db'].cursor()

# config
CONFIG_DIR = './'
with open(CONFIG_DIR+'config.json') as config_file:
    CONFIG = json.loads(config_file.read())

IMAGE_ASSETS_DIR = './assets/images/'
PREDICTOR = Predictor(CONFIG)

app = Blueprint('images-app', __name__, url_prefix='/v1')


# attempts to validate if a collection of bytes represents an image by parsing them with PIL.Image
# throws an exception if the data cannot be parsed
def __sanitise_image__(bytes_data):
    buf = BytesIO(bytes_data)
    img = pimage.open(buf)

    # move data from original image into new image, dropping redundant metadata to save space / avoid warnings
    buf_no_exif = BytesIO()
    img_no_exif = pimage.new(img.mode, img.size)

    img_no_exif.putdata( list(img.getdata()) )
    img_no_exif.save(buf_no_exif, format="jpeg")

    # drop all EXIF data as it is all redundant
    return buf_no_exif.getvalue()


def predictImage(imgID):
    cursor.execute("""
        SELECT imgURL FROM `Img`
        WHERE imgID = {}
    """.format(imgID))
    imgURL = cursor.fetchone()

    if not imgURL: return json.dumps({'message' : "Could not classify image, image with ID {} does not exist".format(imgID)}), 422
    else: imgURL = imgURL[0]

    img     = k_image.load_img( IMAGE_ASSETS_DIR+imgURL, target_size=(224,224))
    x_input = k_image.img_to_array(img)
    x_input = np.expand_dims(x_input, axis=0)
    x_input_norm = x_input/255

    classes, probs = PREDICTOR.predict(x_input_norm)
    class_probas = [ {'class': classname, 'probability': prob } for (classname, prob) in zip(classes, probs)]

    for class_proba in class_probas:
        cursor.execute("""
            SELECT cID FROM `Category`
            WHERE cName = "{}";
        """.format(class_proba['class']))
        classid = cursor.fetchone()[0]

        cursor.execute("""
            SELECT cID FROM `ImageCategory`
            WHERE cID = %s and imgID = %s;
        """, (classid, imgID))

        result = cursor.fetchone()
        if not result:
            cursor.execute("""
                INSERT INTO `ImageCategory`
                (icID, cID, imgID)
                VALUES (%s, %s, %s);
            """, (None, classid, imgID))

    GLOBALS['db'].commit()
    return class_probas


# upload an image for a userID (not yet authenticated)
@app.route('/newImage', methods=["POST"])
def addUserImage():
    now = time.time()
    imgdata = request.files['image']
    userID = request.form.get('userID')
    
    # validate
    #if userID is None : return json.dumps({'message': "Could not upload image: no userID given"}), 400
    try:
        imgdata = __sanitise_image__(imgdata.read())
    except(OSError) as err:
        return json.dumps({'message': "Could not upload image: image data is corrupted"}), 422

    # save
    relative_filepath = "{}/".format(userID) if userID else "0/"
    relative_filename = relative_filepath + str(int(time.time())) + ".jpg"

    local_filepath = IMAGE_ASSETS_DIR + relative_filepath
    local_filename = IMAGE_ASSETS_DIR + relative_filename

    if not path.exists(IMAGE_ASSETS_DIR): makedirs(IMAGE_ASSETS_DIR)
    if not path.exists(local_filepath): makedirs(local_filepath)

    with open(local_filename , 'wb') as f:
        f.write(imgdata)

    cursor.execute("""
        INSERT INTO `Img`
        (imgID, imgURL, userID, imgDatetime)
        VALUES (%s, %s, %s, %s);
    """, (None, relative_filename, userID, time.strftime("%Y-%m-%d %H:%M:%S")))
    GLOBALS['db'].commit()

    imgID = cursor.lastrowid
    predictions = predictImage(imgID)

    then = time.time()
    diff = then-now

    print(diff)

    return json.dumps({
        'imgID': imgID,
        'imgURL': '/assets/images/{}'.format(relative_filename),
        'predictions': predictions
    })


@app.route('/newCategory', methods=["POST"])
def newClass():
    return "<html><body><h1>Ouch, I <strong>stubbed</strong> my toe! :(</h1></body></html>"


@app.route('/getTags', methods=["GET"])
def getTags():
    
    return tags
