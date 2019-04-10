from hafweb.config import Base
from sqlalchemy import *
import json


class AppCase(Base):
    __tablename__ = "app_case"
    id = Column(Integer, primary_key=True)
    ids_id = Column(Integer)
    run = Column(Integer)
    dependent = Column(String)
    bench_name = Column(String)
    request_id = Column(Integer)
    response_id = Column(Integer)
    expect_id = Column(Integer)
    sqlinfo_id = Column(Integer)
    type = Column(Integer)
    suite_id = Column(Integer)
    detail_id = Column(Integer)
    caps_id = Column(Integer)

    def __repr__(self):
        attr_list = ["id", "ids_id", "run", "dependent", "bench_name", "request_id", "response_id", "expect_id", "sqlinfo_id", "type", "suite_id", "detail_id", "caps_id"]
        rev = {}
        for attr in attr_list:
            rev[attr] = getattr(self, attr)
        return json.dumps(rev)


class AppCaseExpect(Base):
    __tablename__ = "app_case_expect"
    id = Column(Integer, primary_key=True)
    response_id = Column(Integer)
    sql_check_func = Column(Integer)
    sql_response_result = Column(Integer)

    def __repr__(self):
        attr_list = ["id", "response_id", "sql_check_func", "sql_response_result"]
        rev = {}
        for attr in attr_list:
            rev[attr] = getattr(self, attr)
        return json.dumps(rev)


class AppCaseIds(Base):
    __tablename__ = "app_case_ids"
    id = Column(Integer, primary_key=True)
    case_id = Column(Integer)
    case_sub_id = Column(Integer)
    case_name = Column(String)
    case_app_name = Column(String)

    def __repr__(self):
        attr_list = ["id", "case_id", "case_sub_id", "case_name", "case_app_name"]
        rev = {}
        for attr in attr_list:
            rev[attr] = getattr(self, attr)
        return json.dumps(rev)


class AppCaseSqlinfo(Base):
    __tablename__ = "app_case_sqlinfo"
    id = Column(Integer, primary_key=True)
    scripts_id = Column(Integer)
    config = Column(String)
    config_id = Column(Integer)
    check_list_id = Column(Integer)

    def __repr__(self):
        attr_list = ["id", "scripts_id", "config", "config_id", "check_list_id"]
        rev = {}
        for attr in attr_list:
            rev[attr] = getattr(self, attr)
        return json.dumps(rev)


class AppCaseSqlinfoChecklist(Base):
    __tablename__ = "app_case_sqlinfo_checklist"
    id = Column(Integer, primary_key=True)
    sql_response = Column(String)

    def __repr__(self):
        attr_list = ["id", "sql_response"]
        rev = {}
        for attr in attr_list:
            rev[attr] = getattr(self, attr)
        return json.dumps(rev)


class AppCaseSqlinfoConfig(Base):
    __tablename__ = "app_case_sqlinfo_config"
    id = Column(Integer, primary_key=True)
    host = Column(String)
    port = Column(Integer)
    type = Column(String)
    username = Column(String)
    password = Column(String)

    def __repr__(self):
        attr_list = ["id", "host", "port", "type", "username", "password"]
        rev = {}
        for attr in attr_list:
            rev[attr] = getattr(self, attr)
        return json.dumps(rev)


class AppCaseSqlinfoScript(Base):
    __tablename__ = "app_case_sqlinfo_script"
    id = Column(Integer, primary_key=True)
    sql_response = Column(String)

    def __repr__(self):
        attr_list = ["id", "sql_response"]
        rev = {}
        for attr in attr_list:
            rev[attr] = getattr(self, attr)
        return json.dumps(rev)


class AppDetail(Base):
    __tablename__ = "app_detail"
    id = Column(Integer, primary_key=True)
    case_name = Column(String)
    result_check_response = Column(String)
    result_check_sql_response = Column(String)
    run_error = Column(String)
    result = Column(Integer)
    begin_time = Column(String)
    end_time = Column(String)
    log_dir = Column(String)
    runner = Column(Integer)

    def __repr__(self):
        attr_list = ["id", "case_name", "result_check_response", "case_name", "result_check_sql_response", "run_error", "result", "begin_time", "end_time", "log_dir", "runner"]
        rev = {}
        for attr in attr_list:
            rev[attr] = getattr(self, attr)
        return json.dumps(rev)


class AppCaseStage(Base):
    __tablename__ = "app_case_stage"
    id = Column(Integer, primary_key=True)
    stage_id = Column(Integer)
    name = Column(String)
    operation = Column(String)
    show_try = Column(String)
    time_sleep = Column(String)
    info = Column(String)
    result_id = Column(Integer)
    app_case_id = Column(Integer)
    run_count = Column(Integer)

    def __repr__(self):
        attr_list = ["id", "stage_id", "name", "time_sleep", "operation",
                     "show_try", "info", "result_id", "app_case_id", "run_count"]
        rev = {}
        for attr in attr_list:
            rev[attr] = getattr(self, attr)
        return json.dumps(rev)


class AppCaseStagePath(Base):
    __tablename__ = "app_case_stage_path"
    id = Column(Integer, primary_key=True)
    stage_id = Column(Integer)
    find_type = Column(String)
    find_value = Column(String)

    def __repr__(self):
        attr_list = ["id", "stage_id", "find_type", "find_value"]
        rev = {}
        for attr in attr_list:
            rev[attr] = getattr(self, attr)
        return json.dumps(rev)


class AppCaseStageResult(Base):
    __tablename__ = "app_case_stage_result"
    id = Column(Integer, primary_key=True)
    result = Column(String)
    exception = Column(String)

    def __repr__(self):
        attr_list = ["id", "result", "exception"]
        rev = {}
        for attr in attr_list:
            rev[attr] = getattr(self, attr)
        return json.dumps(rev)


class AppCaseCaps(Base):
    __tablename__ = "app_case_caps"
    id = Column(Integer, primary_key=True)
    automation_name = Column(String)
    platform_name = Column(String)
    platform_version = Column(String)
    device_name = Column(String)
    app_package = Column(String)
    app_activity = Column(String)
    no_reset = Column(String)

    def __repr__(self):
        attr_list = ["id", "automation_name", "platform_name", "platform_version", "device_name", "app_package", "app_activity", "no_reset"]
        rev = {}
        for attr in attr_list:
            rev[attr] = getattr(self, attr)
        return json.dumps(rev)