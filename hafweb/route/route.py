from hafweb.app import app
from haf.config import BANNER_STRS
from hafweb.generator import GeneratorHtml, GeneratorApi
from hafweb.controller.controller import *
from flask import request
from hafweb.error import *


@app.route("/")
def index() -> str:
    return GeneratorHtml.g_index(banner=BANNER_STRS)


@app.route("/index")
def main_page() -> str:
    return GeneratorHtml.g_main()
