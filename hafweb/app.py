
from flask import Flask
from flask_restful import abort, Api

app = Flask("haf-web")
api = Api(app)
