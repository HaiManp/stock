# -*- coding: utf-8 -*

from flask_cors import CORS
from flask import Flask
from server.core.backcore import *

app = Flask(__name__)
CORS(app, resources=r'/*')
app.register_blueprint(api, url_prefix='/api')
if __name__ == '__main__':
    app.run(port=9000, debug=True)
