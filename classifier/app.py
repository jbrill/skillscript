from flask import *
app = Flask(__name__)

import api


app.register_blueprint(api.api)

# from classifier import classifier

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
