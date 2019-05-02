from mysql import connector
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

    GLOBALS['db'] = db