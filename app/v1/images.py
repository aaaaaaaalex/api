from mysql import connector
from flask import Blueprint, request
from io import BytesIO
from os import path, makedirs
from PIL import Image as pimage, ImageFile
from time import sleep, time




import json
import logging

app = Blueprint('images-app', __name__, url_prefix='/v1')

IMAGE_ASSETS_PATH = '/assets/images/'

while True:
    try:
        db = connector.connect(
            host="db",
            user="root",
            passwd="test",
            database='app'
        )
        cursor = db.cursor()
        logging.info("DB connection established!")
        break
    except connector.errors.InterfaceError:
        sleep(5)
        continue


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


# upload an image for a userID (not yet authenticated)
@app.route('/newImage', methods=["POST"])
def addUserImage():
    imgdata = request.files['image']
    userID = request.form.get('userID')
    
    # validate
    #if userID is None : return json.dumps({'message': "Could not upload image: no userID given"}), 400
    try:
        imgdata = __sanitise_image__(imgdata.read())
    except(OSError) as err:
        return json.dumps({'message': "Could not upload image: image data is corrupted"}), 422

    # save
    filepath = IMAGE_ASSETS_PATH + "{}/".format(userID) if userID else IMAGE_ASSETS_PATH + "0/"
    filename = filepath + str(int(time())) + ".jpg"
    if not path.exists(IMAGE_ASSETS_PATH): makedirs(IMAGE_ASSETS_PATH)
    if not path.exists(filepath): makedirs(filepath)

    with open(filename , 'wb') as f:
        f.write(imgdata)

    cursor.execute("""
        INSERT INTO `Img`
        (imgID, imgURL, userID)
        VALUES (%s, %s, %s);
    """, (None, filename, userID))

    db.commit()
    return "<html><body><h1>good job, you did it!</h1></body></html>"


@app.route('/newCategory', methods=["POST"])
def newClass():
    return "<html><body><h1>Ouch, I <strong>stubbed</strong> my toe! :(</h1></body></html>"