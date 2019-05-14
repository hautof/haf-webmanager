from hafweb.app import app
from haf.config import BANNER_STRS
from hafweb.view.view import *
from hafweb.controller.controller import *
from flask import request
from hafweb.error import *


@app.route("/")
def index() -> str:
    return ViewMain.g_index(banner=BANNER_STRS)


@app.route("/index")
def main_page() -> str:
    test_filter = ""
    if request.method == "POST":
        test_filter = request.form.get("test_filter")
    else:
        test_filter = request.args.get("test_filter")
    print("app route /index")
    return ViewMain.g_main(test_filter.split(',') if test_filter else [])


@app.route("/today")
def main_page_today() -> str:
    test_filter = ""
    if request.method == "POST":
        test_filter = request.form.get("test_filter")
    else:
        test_filter = request.args.get("test_filter")
    return ViewMain.g_main_today(test_filter.split(',') if test_filter else [])


@app.route("/daily")
def main_page_daily() -> str:
    test_filter = ""
    date = ""
    if request.method == "POST":
        test_filter = request.form.get("test_filter")
        date = request.form.get("date")
    else:
        test_filter = request.args.get("test_filter")
        date = request.args.get("date")
    if date=="" or date is None:
        return ViewMain.g_main_today(test_filter.split(',') if test_filter else [])
    return ViewMain.g_main_daily(test_filter.split(',') if test_filter else [], date)



@app.route("/test", methods=['GET'])
def test_page() -> str:
    if request.method == "POST":
        test_id = request.form.get("test_id")
    else:
        test_id = request.args.get("test_id")
    return ViewMain.g_test(test_id)


@app.route("/main", methods=['GET'])
def main_one_page() -> str:
    if request.method == "POST":
        test_name = request.form.get("test_name")
    else:
        test_name = request.args.get("test_name")
    return ViewMain.g_main_one(test_name)


@app.route("/case", methods=['GET'])
def case_history_page() -> str:
    if request.method == "POST":
        id = request.form.get("id")
        test_id = request.form.get("test_id")
        suite_name = request.form.get("suite_name")
    else:
        id = request.args.get("id")
        test_id = request.args.get("test_id")
        suite_name = request.args.get("suite_name")
    return ViewMain.g_case(id, suite_name, test_id)

