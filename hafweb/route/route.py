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
    test_filter = ""
    if request.method == "POST":
        test_filter = request.form.get("test_filter")
    else:
        test_filter = request.args.get("test_filter")
    return GeneratorHtml.g_main(test_filter.split(',') if test_filter else [])


@app.route("/today")
def main_page_today() -> str:
    test_filter = ""
    if request.method == "POST":
        test_filter = request.form.get("test_filter")
    else:
        test_filter = request.args.get("test_filter")
    return GeneratorHtml.g_main_today(test_filter.split(',') if test_filter else [])


@app.route("/test", methods=['GET'])
def test_page() -> str:
    if request.method == "POST":
        test_id = request.form.get("test_id")
    else:
        test_id = request.args.get("test_id")
    return GeneratorHtml.g_test(test_id)


@app.route("/main", methods=['GET'])
def main_one_page() -> str:
    if request.method == "POST":
        test_name = request.form.get("test_name")
    else:
        test_name = request.args.get("test_name")
    return GeneratorHtml.g_main_one(test_name)

