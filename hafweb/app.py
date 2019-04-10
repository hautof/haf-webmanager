
from flask import Flask
from flask_restful import abort, Api

app = Flask("haf-web", static_url_path='/resource/',template_folder='/templates/')
api = Api(app)
