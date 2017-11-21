from flask import *
app = Flask(__name__, template_folder='templates',static_folder="static")

import controllers
import api


app.register_blueprint(api.api)
app.register_blueprint(controllers.views)

# from classifier import classifier

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)
