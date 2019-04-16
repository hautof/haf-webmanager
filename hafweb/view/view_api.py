from jinja2.environment import TemplateStream
from jinja2 import Environment, FileSystemLoader
from hafweb.config import *
from hafweb.model.model import *
from hafweb.controller.controller import *
from hafweb.error import ErrorHandler
from datetime import datetime
from haf.config import PLATFORM_VERSION
from flask import make_response, jsonify
import os


class ViewApi(object):
    def __init__(self):
        pass

    @classmethod
    def genrate_api_pure(cls, data, status=200):
        response_all = make_response(data)
        response_all.headers['Access-Control-Allow-Origin'] = '*'
        response_all.headers['Connection'] = 'keep-alive'
        response_all.headers['Content-Type'] = 'application/json;'
        return response_all, 200 if status==200 else status

    @classmethod
    def generate_api(cls, func, data, status=0):
        rev = {"name": func, "status": status, "data": {}}
        if isinstance(data, list):
            rev["data"]["list"] = []
            for t in data:
                rev["data"]["list"].append(str(t))
        else:
            rev["data"] = str(data)
        response = json.dumps(rev)
        response_all = make_response(response)
        response_all.headers["Access-Control-Allow-Origin"] = '*'
        response_all.headers['Connection'] = 'keep-alive'
        response_all.headers['Content-Type'] = 'application/json;'
        return response_all, 200 if status==200 else status

    @classmethod
    def generate_error(cls, error: ErrorHandler):
        rev = {"name": error.name, "status": error.status, "data": [], "msg": error.message}
        response = json.dumps(rev)
        response_all = make_response(response)
        response_all.headers['Access-Control-Allow-Origin'] = '*'
        response_all.headers['Connection'] = 'keep-alive'
        response_all.headers['Content-Type'] = 'application/json;'
        return response_all, error.status

    @classmethod
    def split_main(cls, mains, filter=[]):
        m = {}
        for main in mains:
            *names, year, month, day, time = main.name.split("-")
            name = '-'.join(names)
            date_time = f"{year}-{month}-{day}-{time}"
            if len(filter) == 0 or name in filter:
                if name not in m.keys():
                    m[name] = {}
                m[name][date_time] = json.loads(str(main))
        return m

    @classmethod
    def get_main(cls, test_filter=[]) -> str:
        template_name = "main.html"
        main_today = Controller.get_main_all()
        main_all = {"passed": 0, "failed": 0, "error": 0, "skip": 0, "all": 0}
        mains = ViewApi.split_main(main_today, test_filter)
        for key in mains.keys():
            tests = mains.get(key)
            for mkey in tests.keys():
                m = tests.get(mkey)
                main_all["passed"] += m.get("passed")
                main_all["failed"] += m.get("failed")
                main_all["error"] += m.get("error")
                main_all["skip"] += m.get("skip")
        main_all["all"] = main_all["passed"] + main_all["failed"] + main_all["error"] + main_all["skip"]
        return make_response(jsonify({"data": mains, "summary": main_all}))
