from jinja2.environment import TemplateStream
from jinja2 import Environment, FileSystemLoader
from hafweb.config import *
from hafweb.model.model import *
from hafweb.controller.controller import *
from hafweb.error import ErrorHandler
from datetime import datetime
from haf.config import *
from flask import make_response
import os


class ViewMain(object):
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
        index = ViewMain.get_template(template_name)
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
        index = ViewMain.get_template(template_name)
        main_today = Controller.get_main_all()
        main_all = {"passed": 0, "failed": 0, "error": 0, "skip": 0, "all": 0}
        mains = ViewMain.split_main(main_today, test_filter)
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
        index = ViewMain.get_template(template_name)
        main_today = Controller.get_main_today()
        main_all = {"passed": 0, "failed": 0, "error": 0, "skip": 0, "all": 0}
        mains = ViewMain.split_main(main_today, test_filter)
        all_count = 0
        for key in mains.keys():
            tests = mains.get(key)
            for mkey in tests.keys():
                all_count += 1
                m = tests.get(mkey)
                main_all["passed"] += m.passed
                main_all["failed"] += m.failed
                main_all["error"] += m.error
                main_all["skip"] += m.skip
        main_all["all"] = main_all["passed"] + main_all["failed"] + main_all["error"] + main_all["skip"]
        return index.render(today=datetime.today().date(),main=main_today, all=main_all, hafversion=PLATFORM_VERSION, testname=datetime.today(), mains=mains, all_count=all_count)

    @classmethod
    def g_main_daily(cls, test_filter, date) -> str:
        template_name = "today.html"
        index = ViewMain.get_template(template_name)
        main_today = Controller.get_main_by_date(date)
        main_all = {"passed": 0, "failed": 0, "error": 0, "skip": 0, "all": 0}
        mains = ViewMain.split_main(main_today, test_filter)
        all_count = 0
        for key in mains.keys():
            tests = mains.get(key)
            for mkey in tests.keys():
                all_count += 1
                m = tests.get(mkey)
                main_all["passed"] += m.passed
                main_all["failed"] += m.failed
                main_all["error"] += m.error
                main_all["skip"] += m.skip
        main_all["all"] = main_all["passed"] + main_all["failed"] + main_all["error"] + main_all["skip"]
        return index.render(today=date,main=main_today, all=main_all, hafversion=PLATFORM_VERSION, testname=date, mains=mains, all_count=all_count)

    @classmethod
    def g_test(cls, test_id: int) -> str:
        template_name = "test.html"
        index = ViewMain.get_template(template_name)
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
        return index.render(main=main_today, suites=summarys, all=main, hafversion=PLATFORM_VERSION, testname=main.name, results=results, date_time=main.name, back_name=name, test_id=test_id)

    @classmethod
    def g_main_one(cls, test_name: str) -> str:
        template_name = "main_one.html"
        index = ViewMain.get_template(template_name)
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
        mains = ViewMain.split_main(main_today, [test_name])
        return index.render(today=datetime.today().date(), main=main_today, suites=suites, all=main_all,
                            hafversion=PLATFORM_VERSION, testname=test_name, mains=mains)

    @classmethod
    def g_case(cls, id: str, suite_name: str, test_id: int) -> str:
        template_name = "case.html"
        index = ViewMain.get_template(template_name)
        case_id, sub_id, case_name = id.split(".")
        all_cases = ControllerApi.get_case_history_by_id(case_id, sub_id, case_name, suite_name)

        main_all = {"passed": 0, "failed": 0, "error": 0, "skip": 0, "all": 0}
        results = []
        results_data = {}
        for i, case in enumerate(all_cases):
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
            if case_detail.result == str(RESULT_PASS):
                main_all["passed"] += 1
            elif case_detail.result == str(RESULT_FAIL):
                main_all["failed"] += 1
            elif case_detail.result == str(RESULT_ERROR):
                main_all["error"] += 1
            elif case_detail.result == str(RESULT_SKIP):
                main_all["skip"] += 1
            main_all["all"] += 1
            results_data[f"{case_detail.begin_time}"] = RESULT_GROUP.get(case_detail.result)
        return index.render(today=datetime.today().date(), all=main_all,
                            hafversion=PLATFORM_VERSION, results=results, test_name=f"{suite_name}.{id}", main_all=results_data, test_id=test_id)