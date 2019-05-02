from flask import Flask
import logging

import settings
settings.init()

from v1.admin import app as admin_api
from v1.images import app as images_api
from web.views import app as views_api



app = Flask(__name__)
app.register_blueprint(admin_api)
app.register_blueprint(images_api)
app.register_blueprint(views_api)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO)
        app.run(host="0.0.0.0", port=8080)
    except KeyboardInterrupt:
        print("bye!")
        exit()
