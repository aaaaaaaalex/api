from mysql import connector
from flask import Blueprint, request
from time import sleep
import json
import logging

app = Blueprint('images-app', __name__, url_prefix='/v1')

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


@app.route('/newImage', methods=["POST"])
def addAllImages():
    URLS_path = "./dataset/url/{}/url.txt"
    with open('./dataset/classes.config') as fd:
        for cl in fd:
            classname = cl.strip('\n')
            if classname != '':
                cursor.execute("""
                    INSERT INTO `Category`
                        (`cID`, `cName`) 
                        VALUES (%s, %s);
                    """, (None, classname))
                classID = cursor.lastrowid

                with open (URLS_path.format(classname)) as urls:
                    for url in urls:
                        if url != "":
                            fmt_url = url.strip("\n\r")
                            cursor.execute("""
                                INSERT INTO `Img`
                                    (`imgID`, `imgURL`, `userID`)
                                    VALUES (%s, %s, %s)
                                """, (None, fmt_url, None))
                            imgID = cursor.lastrowid

                            logging.debug("classID: {}, classname: {}, imgID: {}, fmt_url: {}".format(classID, classname, imgID, fmt_url))
                            cursor.execute("""
                                INSERT INTO `ImageCategory`
                                    (icID, cID, imgID)
                                    VALUES (%s, %s, %s)
                                """, (None, classID, imgID))

    db.commit()
    return "<html><body><h1>good job, you did it!</h1></body></html>"


@app.route('/newCategory', methods=["POST"])
def newClass():
    return "<html><body><h1>Ouch, I <strong>stubbed</strong> my toe! :(</h1></body></html>"