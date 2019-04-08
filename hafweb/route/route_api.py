from hafweb.app import app
from haf.config import BANNER_STRS
from hafweb.generator import GeneratorHtml, GeneratorApi
from hafweb.controller.controller import *
from flask import request
from hafweb.error import *


@app.route("/api/v1/main", methods=['GET', 'POST'])
def get_main_all_api() -> str:
    if request.method == "POST":
        date_time = request.form.get("date_time")
    else:
        date_time = request.args.get("date_time")
    if date_time is not None:
        mains = Controller.get_main_by_date(date_time)
    else:
        mains = Controller.get_main_all()
    return GeneratorApi.generate_api("get_main_all_api", mains, 0)


@app.route("/api/v1/main/today", methods=['GET', 'POST'])
def get_main_today_api() -> str:
    mains =  Controller.get_main_today()
    return GeneratorApi.generate_api("get_main_today_api", mains, 0)


@app.route("/api/v1/suite", methods=['GET', 'POST'])
def get_suite_by_main_id() -> str:
    if request.method == "POST":
        main_id = request.form.get("main_id")
    else:
        main_id = request.args.get("main_id")
    if main_id is not None:
        suites = Controller.get_suite_by_main_id(main_id)
        return GeneratorApi.generate_api("get_suite_by_main_id", suites)
    else:
        error = ErrorHandler("get_suite_by_main_id", "main_id is blank")
        return GeneratorApi.generate_error(error)


@app.route("/api/v1/summary", methods=['GET', 'POST'])
def get_summary_by_suite_id() -> str:
    if request.method == "POST":
        suite_id = request.form.get("suite_id")
    else:
        suite_id = request.args.get("suite_id")
    if suite_id is not None:
        suites = Controller.get_summary_by_suite_id(suite_id)
        return GeneratorApi.generate_api("get_summary_by_suite_id", suites)
    else:
        error = ErrorHandler("get_summary_by_suite_id", "suite_id is blank")
        return GeneratorApi.generate_error(error)


@app.route("/api/v1/case", methods=['GET', 'POST'])
def get_case() -> str:
    if request.method == "POST":
        suite_id = request.form.get("suite_id")
    else:
        suite_id = request.args.get("suite_id")
    if suite_id is not None:
        cases =  ControllerApi.get_case_by_suite_id( suite_id)
    else:
        cases =  ControllerApi.get_case_all()
    return GeneratorApi.generate_api("get_case_by_suite_id", cases)


@app.route("/api/v1/case/expect", methods=['GET', 'POST'])
def get_case_expect() -> str:
    if request.method == "POST":
        id = request.form.get("id")
    else:
        id = request.args.get("id")
    if id is not None:
        expects =  ControllerApi.get_case_expect_by_id(id)
        return GeneratorApi.generate_api("get_case_expect", expects)
    else:
        return str(ErrorHandler("get_case_expect", "id is blank"))


@app.route("/api/v1/case/ids", methods=['GET', 'POST'])
def get_case_ids() -> str:
    if request.method == "POST":
        id = request.form.get("id")
    else:
        id = request.args.get("id")
    if id is not None:
        ids = ControllerApi.get_case_ids_by_id(id)
        return GeneratorApi.generate_api("get_case_ids", ids)
    else:
        return GeneratorApi.generate_error(ErrorHandler("get_case_ids", "id is blank"))


@app.route("/api/v1/case/request", methods=['GET', 'POST'])
def get_case_request() -> str:
    if request.method == "POST":
        id = request.form.get("id")
    else:
        id = request.args.get("id")
    if id is not None:
        requests = ControllerApi.get_case_request_by_id(id)
        return GeneratorApi.generate_api("get_case_request", requests)
    else:
        return GeneratorApi.generate_error(ErrorHandler("get_case_request", "id is blank"))


@app.route("/api/v1/case/response", methods=['GET', 'POST'])
def get_case_response() -> str:
    if request.method == "POST":
        id = request.form.get("id")
    else:
        id = request.args.get("id")
    if id is not None:
        responses = ControllerApi.get_case_response_by_id(id)
        return GeneratorApi.generate_api("get_case_response", responses)
    else:
        return GeneratorApi.generate_error(ErrorHandler("get_case_response", "id is blank"))


@app.route("/api/v1/case/sqlinfo", methods=['GET', 'POST'])
def get_case_sqlinfo() -> str:
    if request.method == "POST":
        id = request.form.get("id")
    else:
        id = request.args.get("id")
    if id is not None:
        sqlinfos = ControllerApi.get_case_sqlinfo_by_id(id)
        return GeneratorApi.generate_api("get_case_sqlinfo", sqlinfos)
    else:
        return GeneratorApi.generate_error(ErrorHandler("get_case_sqlinfo", "id is blank"))


@app.route("/api/v1/case/sqlinfo/checklist", methods=['GET', 'POST'])
def get_case_sqlinfo_checklist() -> str:
    if request.method == "POST":
        id = request.form.get("id")
    else:
        id = request.args.get("id")
    if id is not None:
        checklists = ControllerApi.get_case_sqlinfo_checklist_by_id(id)
        return GeneratorApi.generate_api("get_case_sqlinfo_checklist", checklists)
    else:
        return GeneratorApi.generate_error(ErrorHandler("get_case_sqlinfo_checklist", "id is blank"))


@app.route("/api/v1/case/sqlinfo/config", methods=['GET', 'POST'])
def get_case_sqlinfo_config() -> str:
    if request.method == "POST":
        id = request.form.get("id")
    else:
        id = request.args.get("id")
    if id is not None:
        configs = ControllerApi.get_case_sqlinfo_config_by_id(id)
        return GeneratorApi.generate_api("get_case_sqlinfo_config", configs)
    else:
        return GeneratorApi.generate_error(ErrorHandler("get_case_sqlinfo_config", "id is blank"))


@app.route("/api/v1/case/sqlinfo/script", methods=['GET', 'POST'])
def get_case_sqlinfo_script() -> str:
    if request.method == "POST":
        id = request.form.get("id")
    else:
        id = request.args.get("id")
    if id is not None:
        scripts = ControllerApi.get_case_sqlinfo_script_by_id(id)
        return GeneratorApi.generate_api("get_case_sqlinfo_script", scripts)
    else:
        return GeneratorApi.generate_error(ErrorHandler("get_case_sqlinfo_script", "id is blank"))


@app.route("/api/v1/case/detail", methods=['GET', 'POST'])
def get_case_detail() -> str:
    if request.method == "POST":
        id = request.form.get("id")
    else:
        id = request.args.get("id")
    if id is not None:
        details = ControllerApi.get_case_detail_by_id(id)
        return GeneratorApi.generate_api("get_case_detail", details)
    else:
        return GeneratorApi.generate_error(ErrorHandler("get_case_detail", "id is blank"))