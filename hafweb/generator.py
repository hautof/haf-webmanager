from jinja2.environment import TemplateStream
from jinja2 import Environment, FileSystemLoader
from hafweb.config import *
from hafweb.model.model import *
from hafweb.controller.controller import *
from hafweb.error import ErrorHandler
from datetime import datetime
from haf.config import PLATFORM_VERSION
from flask import make_response
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
    def split_main(cls, mains, filter=[]):
        m = {}
        for main in mains:
            *names, year, month, day, time = main.name.split("-")
            name = '-'.join(names)
            date_time = f"{year}-{month}-{day}-{time}"
            if len(filter) == 0 or name in filter:
                if name not in m.keys():
                    m[name] = {}
                m[name][date_time] = main
        return m

    @classmethod
    def g_main(cls, test_filter) -> str:
        template_name = "main.html"
        index = GeneratorHtml.get_template(template_name)
        main_today = Controller.get_main_all()
        main_all = {"passed": 0, "failed": 0, "error": 0, "skip": 0, "all": 0}
        mains = GeneratorHtml.split_main(main_today, test_filter)
        for key in mains.keys():
            tests = mains.get(key)
            for mkey in tests.keys():
                m = tests.get(mkey)
                main_all["passed"] += m.passed
                main_all["failed"] += m.failed
                main_all["error"] += m.error
                main_all["skip"] += m.skip
        main_all["all"] = main_all["passed"] + main_all["failed"] + main_all["error"] + main_all["skip"]
        return index.render(today=datetime.today().date(),main=main_today, all=main_all, hafversion=PLATFORM_VERSION, testname="ALL", mains=mains)

    @classmethod
    def g_main_today(cls, test_filter) -> str:
        template_name = "today.html"
        index = GeneratorHtml.get_template(template_name)
        main_today = Controller.get_main_today()
        main_all = {"passed": 0, "failed": 0, "error": 0, "skip": 0, "all": 0}
        mains = GeneratorHtml.split_main(main_today, test_filter)
        for key in mains.keys():
            tests = mains.get(key)
            for mkey in tests.keys():
                m = tests.get(mkey)
                main_all["passed"] += m.passed
                main_all["failed"] += m.failed
                main_all["error"] += m.error
                main_all["skip"] += m.skip
        main_all["all"] = main_all["passed"] + main_all["failed"] + main_all["error"] + main_all["skip"]
        return index.render(today=datetime.today().date(),main=main_today, all=main_all, hafversion=PLATFORM_VERSION, testname="TODAY", mains=mains)

    @classmethod
    def g_test(cls, test_id: int) -> str:
        template_name = "test.html"
        index = GeneratorHtml.get_template(template_name)
        main_today = Controller.get_main_by_test_id(test_id)
        main = main_today[0] if len(main_today)>0 else None
        suites = Controller.get_suite_by_main_id(main.id)
        summarys = []
        for suite in suites:
            summary = Controller.get_summary_by_suite_id(suite.id)[0]
            summarys.append(summary)
        all_cases = []
        for suite in suites:
            for case in ControllerApi.get_case_by_suite_id(suite.id):
                all_cases.append(case)

        results = []
        for case in all_cases:
            result = {}
            result["case"] = case
            case_id = ControllerApi.get_case_ids_by_id(case.ids_id)[0]
            result["ids"] = case_id
            case_request = ControllerApi.get_case_request_by_id(case.request_id)[0]
            result["request"] = case_request
            case_response = ControllerApi.get_case_response_by_id(case.response_id)[0]
            result["response"] = case_response
            case_expect = ControllerApi.get_case_expect_by_id(case.expect_id)[0]
            result["expect"] = case_expect
            case_sqlinfo = ControllerApi.get_case_sqlinfo_by_id(case.sqlinfo_id)[0]
            result["sqlinfo"] = case_sqlinfo
            case_detail = ControllerApi.get_case_detail_by_id(case.detail_id)[0]
            result["detail"] = case_detail
            results.append(result)

        *names, year, month, day, time = main.name.split("-")
        name = "-".join(names)
        return index.render(main=main_today, suites=summarys, all=main, hafversion=PLATFORM_VERSION, testname=name, results=results)

    @classmethod
    def g_main_one(cls, test_name: str) -> str:
        template_name = "main_one.html"
        index = GeneratorHtml.get_template(template_name)
        main_today = Controller.get_main_by_test_name(test_name)
        main_all = {"passed": 0, "failed": 0, "error": 0, "skip": 0, "all": 0}
        suites = {}
        for m in main_today:
            suites[m.id] = (Controller.get_suite_by_main_id(m.id))
            main_all["passed"] += m.passed
            main_all["failed"] += m.failed
            main_all["error"] += m.error
            main_all["skip"] += m.skip
        main_all["all"] = main_all["passed"] + main_all["failed"] + main_all["error"] + main_all["skip"]
        mains = GeneratorHtml.split_main(main_today, [test_name])
        return index.render(today=datetime.today().date(), main=main_today, suites=suites, all=main_all,
                            hafversion=PLATFORM_VERSION, testname=test_name, mains=mains)


class GeneratorApi(object):
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
                m[name][date_time] = main
        return m

    @classmethod
    def get_main(cls, test_filter) -> str:
        template_name = "main.html"
        main_today = Controller.get_main_all()
        main_all = {"passed": 0, "failed": 0, "error": 0, "skip": 0, "all": 0}
        mains = GeneratorApi.split_main(main_today, test_filter)
        for key in mains.keys():
            tests = mains.get(key)
            for mkey in tests.keys():
                m = tests.get(mkey)
                main_all["passed"] += m.passed
                main_all["failed"] += m.failed
                main_all["error"] += m.error
                main_all["skip"] += m.skip
        main_all["all"] = main_all["passed"] + main_all["failed"] + main_all["error"] + main_all["skip"]
        return main_all