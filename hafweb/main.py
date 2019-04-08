# encoding = 'utf-8'
from hafweb.route.route import *
from hafweb.route.route_api import *
from hafweb.controller.controller import *


def main():
    Controller.bind_all()
    ControllerApi.bind_all()
    app.run(debug=False, port=WEB_SERVER_PORT)