from mysql import connector
from time import sleep
import json
import logging

def init():    
    global GLOBALS
    GLOBALS = {}

    # connect database
    while True:
        try:
            db = connector.connect(
                host="db",
                user="root",
                passwd="test",
                database='app'
            )
            logging.info("DB connection established!")
            break
        except connector.errors.InterfaceError:
            sleep(5)
            continue


    # config
    CONFIG_DIR = './'
    with open(CONFIG_DIR+'config.json') as config_file:
        CONFIG = json.loads(config_file.read())

    GLOBALS['config'] = CONFIG
    GLOBALS['db'] = db
    return