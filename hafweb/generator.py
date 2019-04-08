from jinja2.environment import TemplateStream
from jinja2 import Environment, FileSystemLoader
from hafweb.config import *
from hafweb.model.model import *
from hafweb.controller.controller import *
from hafweb.error import ErrorHandler
from datetime import datetime
import os


class GeneratorHtml(object):
    def __init__(self):
        pass

    @classmethod
    def get_template(cls, name: str):
        jj2_loader = FileSystemLoader(RESOURCE_PATH)
        jj2_env = Environment(loader=jj2_loader, trim_blocks=True, lstrip_blocks=True, autoescape=True)
        template = jj2_env.get_template(name)
        return template

    @classmethod
    def g_index(cls, banner: str) -> str:
        template_name = "index.html"
        index = GeneratorHtml.get_template(template_name)
        return index.render(banner=banner)

    @classmethod
    def split_main(cls, mains):
        m = {}
        for main in mains:
            names, year, month, day, time = main.name.split("-")
            name = ''.join(names)
            date_time = f"{year}-{month}-{day}-{time}"
            if name not in m.keys():
                m[name] = {}
            m[name][date_time] = main

    @classmethod
    def g_main(cls) -> str:
        template_name = "main.html"
        index = GeneratorHtml.get_template(template_name)
        main_today = Controller.get_main_today()
        main_all = {"passed": 0, "failed": 0, "error": 0, "skip": 0, "all": 0}
        suites = {}
        for m in main_today:
            suites[m.id] = (Controller.get_suite_by_main_id(m.id))
            main_all["passed"] += m.passed
            main_all["failed"] += m.failed
            main_all["error"] += m.error
            main_all["skip"] += m.skip
        main_all["all"] = main_all["passed"] + main_all["failed"] + main_all["error"] + main_all["skip"]
        return index.render(today=datetime.today().date(),main=main_today, suites=suites, all=main_all)


class GeneratorApi(object):
    def __init__(self):
        pass

    @classmethod
    def generate_api(cls, func, data, status=0):
        rev = {"name": func, "status": status, "data": []}
        for t in data:
            rev["data"].append(str(t))
        return json.dumps(rev)

    @classmethod
    def generate_error(cls, error: ErrorHandler):
        rev = {"name": error.name, "status": error.status, "data": [], "msg": error.message}
        return json.dumps(rev)

