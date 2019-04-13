from flask import Flask

from v1.admin import app as admin_api
from v1.images import app as images_api
#import views

app = Flask(__name__)
app.register_blueprint(admin_api)
app.register_blueprint(images_api)

#app.register_blueprint(views)


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=8080)
    except KeyboardInterrupt:
        print("bye!")
        exit()