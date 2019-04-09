from hafweb.config import Base
from sqlalchemy import *
import json


class ApiCase(Base):
    __tablename__ = "api_case"
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

    def __repr__(self):
        attr_list = ["id", "ids_id", "run", "dependent", "bench_name", "request_id", "response_id", "expect_id", "sqlinfo_id", "type", "suite_id", "detail_id"]
        rev = {}
        for attr in attr_list:
            rev[attr] = getattr(self, attr)
        return json.dumps(rev)


class ApiCaseExpect(Base):
    __tablename__ = "api_case_expect"
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


class ApiCaseIds(Base):
    __tablename__ = "api_case_ids"
    id = Column(Integer, primary_key=True)
    case_id = Column(Integer)
    case_sub_id = Column(Integer)
    case_name = Column(String)
    case_api_name = Column(String)

    def __repr__(self):
        attr_list = ["id", "case_id", "case_sub_id", "case_name", "case_api_name"]
        rev = {}
        for attr in attr_list:
            rev[attr] = getattr(self, attr)
        return json.dumps(rev)


class ApiCaseRequest(Base):
    __tablename__ = "api_case_request"
    id = Column(Integer, primary_key=True)
    header = Column(String)
    data = Column(String)
    url = Column(String)
    method = Column(String)
    protocol = Column(String)
    host_port = Column(String)

    def __repr__(self):
        attr_list = ["id", "header", "data", "url", "method", "protocol", "host_port"]
        rev = {}
        for attr in attr_list:
            rev[attr] = getattr(self, attr)
        return json.dumps(rev)


class ApiCaseResponse(Base):
    __tablename__ = "api_case_response"
    id = Column(Integer, primary_key=True)
    header = Column(String)
    body = Column(String)
    code = Column(Integer)

    def __repr__(self):
        attr_list = ["id", "header", "body", "code"]
        rev = {}
        for attr in attr_list:
            rev[attr] = getattr(self, attr)
        return json.dumps(rev)


class ApiCaseSqlinfo(Base):
    __tablename__ = "api_case_sqlinfo"
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


class ApiCaseSqlinfoChecklist(Base):
    __tablename__ = "api_case_sqlinfo_checklist"
    id = Column(Integer, primary_key=True)
    sql_response = Column(String)

    def __repr__(self):
        attr_list = ["id", "sql_response"]
        rev = {}
        for attr in attr_list:
            rev[attr] = getattr(self, attr)
        return json.dumps(rev)


class ApiCaseSqlinfoConfig(Base):
    __tablename__ = "api_case_sqlinfo_config"
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


class ApiCaseSqlinfoScript(Base):
    __tablename__ = "api_case_sqlinfo_script"
    id = Column(Integer, primary_key=True)
    sql_response = Column(String)

    def __repr__(self):
        attr_list = ["id", "sql_response"]
        rev = {}
        for attr in attr_list:
            rev[attr] = getattr(self, attr)
        return json.dumps(rev)


class ApiDetail(Base):
    __tablename__ = "api_detail"
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