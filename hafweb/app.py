
from flask import Flask
from flask_restful import abort, Api
from flask_cors import CORS


app = Flask("haf-web")
api = Api(app)
CORS(app, supports_credentials=True)