from hafweb.app import app
from haf.config import BANNER_STRS
from hafweb.view.view import *
from hafweb.controller.controller import *
from flask import request
from hafweb.error import *


@app.route("/api/v1/main", methods=['GET', 'POST'])
def get_main_all_api() -> str:
    if request.method == "POST":
        date_time = request.form.get("date_time")
        test_name = request.form.get("test_name")
        if not date_time or not test_name:
            request_data = json.loads(request.data)
            date_time = request_data.get("date_time") or date_time
            test_name = request_data.get("test_name") or test_name
    else:
        date_time = request.args.get("date_time")
        test_name = request.args.get("test_name")
    if date_time is not None:
        mains = Controller.get_main_by_date(date_time)
    else:
        mains = Controller.get_main_all()
    if test_name is not None:
        temp = []
        for main in mains:
            *name, y, m, d, t = main.name.split("-")
            name = "-".join(name)
            print(name)
            if name == test_name:
                temp.append(main)
        mains = temp
    return ViewApi.get_main()
    return ViewApi.generate_api("get_main_all_api", mains, 200)


@app.route("/api/v1/main/today", methods=['GET', 'POST'])
def get_main_today_api() -> str:
    mains =  Controller.get_main_today()
    return ViewApi.generate_api("get_main_today_api", mains, 0)


@app.route("/api/v1/suite", methods=['GET', 'POST'])
def get_suite_by_main_id() -> str:
    if request.method == "POST":
        main_id = request.form.get("main_id")
    else:
        main_id = request.args.get("main_id")
    if main_id is not None:
        suites = Controller.get_suite_by_main_id(main_id)
        return ViewApi.generate_api("get_suite_by_main_id", suites)
    else:
        error = ErrorHandler("get_suite_by_main_id", "main_id is blank")
        return ViewApi.generate_error(error)


@app.route("/api/v1/summary", methods=['GET', 'POST'])
def get_summary_by_suite_id() -> str:
    if request.method == "POST":
        suite_id = request.form.get("suite_id")
    else:
        suite_id = request.args.get("suite_id")
    if suite_id is not None:
        suites = Controller.get_summary_by_suite_id(suite_id)
        return ViewApi.generate_api("get_summary_by_suite_id", suites)
    else:
        error = ErrorHandler("get_summary_by_suite_id", "suite_id is blank")
        return ViewApi.generate_error(error)


@app.route("/api/v1/case", methods=['GET', 'POST'])
def get_case() -> str:
    if request.method == "POST":
        suite_id = request.form.get("suite_id")
    else:
        suite_id = request.args.get("suite_id")
    if suite_id is not None:
        cases =  ControllerApi.get_case_by_suite_id(suite_id)
    else:
        cases =  ControllerApi.get_case_all()
    return ViewApi.generate_api("get_case_by_suite_id", cases)


@app.route("/api/v1/case/expect", methods=['GET', 'POST'])
def get_case_expect() -> str:
    if request.method == "POST":
        id = request.form.get("id")
    else:
        id = request.args.get("id")
    if id is not None:
        expects =  ControllerApi.get_case_expect_by_id(id)
        return ViewApi.generate_api("get_case_expect", expects)
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
        return ViewApi.generate_api("get_case_ids", ids)
    else:
        return ViewApi.generate_error(ErrorHandler("get_case_ids", "id is blank"))


@app.route("/api/v1/case/request", methods=['GET', 'POST'])
def get_case_request() -> str:
    if request.method == "POST":
        id = request.form.get("id")
    else:
        id = request.args.get("id")
    if id is not None:
        requests = ControllerApi.get_case_request_by_id(id)
        return ViewApi.generate_api("get_case_request", requests)
    else:
        return ViewApi.generate_error(ErrorHandler("get_case_request", "id is blank"))


@app.route("/api/v1/case/response", methods=['GET', 'POST'])
def get_case_response() -> str:
    if request.method == "POST":
        id = request.form.get("id")
    else:
        id = request.args.get("id")
    if id is not None:
        responses = ControllerApi.get_case_response_by_id(id)
        return ViewApi.generate_api("get_case_response", responses)
    else:
        return ViewApi.generate_error(ErrorHandler("get_case_response", "id is blank"))


@app.route("/api/v1/case/sqlinfo", methods=['GET', 'POST'])
def get_case_sqlinfo() -> str:
    if request.method == "POST":
        id = request.form.get("id")
    else:
        id = request.args.get("id")
    if id is not None:
        sqlinfos = ControllerApi.get_case_sqlinfo_by_id(id)
        return ViewApi.generate_api("get_case_sqlinfo", sqlinfos)
    else:
        return ViewApi.generate_error(ErrorHandler("get_case_sqlinfo", "id is blank"))


@app.route("/api/v1/case/sqlinfo/checklist", methods=['GET', 'POST'])
def get_case_sqlinfo_checklist() -> str:
    if request.method == "POST":
        id = request.form.get("id")
    else:
        id = request.args.get("id")
    if id is not None:
        checklists = ControllerApi.get_case_sqlinfo_checklist_by_id(id)
        return ViewApi.generate_api("get_case_sqlinfo_checklist", checklists)
    else:
        return ViewApi.generate_error(ErrorHandler("get_case_sqlinfo_checklist", "id is blank"))


@app.route("/api/v1/case/sqlinfo/config", methods=['GET', 'POST'])
def get_case_sqlinfo_config() -> str:
    if request.method == "POST":
        id = request.form.get("id")
    else:
        id = request.args.get("id")
    if id is not None:
        configs = ControllerApi.get_case_sqlinfo_config_by_id(id)
        return ViewApi.generate_api("get_case_sqlinfo_config", configs)
    else:
        return ViewApi.generate_error(ErrorHandler("get_case_sqlinfo_config", "id is blank"))


@app.route("/api/v1/case/sqlinfo/script", methods=['GET', 'POST'])
def get_case_sqlinfo_script() -> str:
    if request.method == "POST":
        id = request.form.get("id")
    else:
        id = request.args.get("id")
    if id is not None:
        scripts = ControllerApi.get_case_sqlinfo_script_by_id(id)
        return ViewApi.generate_api("get_case_sqlinfo_script", scripts)
    else:
        return ViewApi.generate_error(ErrorHandler("get_case_sqlinfo_script", "id is blank"))


@app.route("/api/v1/case/detail", methods=['GET', 'POST'])
def get_case_detail() -> str:
    if request.method == "POST":
        id = request.form.get("id")
    else:
        id = request.args.get("id")
    if id is not None:
        details = ControllerApi.get_case_detail_by_id(id)
        return ViewApi.generate_api("get_case_detail", details)
    else:
        return ViewApi.generate_error(ErrorHandler("get_case_detail", "id is blank"))


@app.route("/api/v1/case/history", methods=["GET", "POST"])
def get_case_history() -> str:
    if request.method == "POST":
        id = request.form.get("id")
        suite_name = request.form.get("suite_name")
    else:
        id = request.args.get("id")
        suite_name = request.args.get("suite_name")
    if id is not None:
        try:
            case_id, sub_id, case_name = id.split(".")
            details = ControllerApi.get_case_history_by_id(case_id, sub_id, case_name, suite_name)
            return ViewApi.generate_api("get_case_history", details)
        except Exception :
            return ViewApi.generate_error(ErrorHandler("get_case_history", "id is error"))
    else:
        return ViewApi.generate_error(ErrorHandler("get_case_history", "id is blank"))