from hafweb.controller.engine import *
from sqlalchemy import *
from datetime import datetime
from hafweb.model.model_app import *
import json


class ControllerApp(object):
    def __init__(self):
        pass

    @classmethod
    def bind_all(cls):
        apicase = AppCase()
        apicase.metadata.bind = engine_maker.engine
        case_expect = AppCaseExpect()
        case_expect.metadata.bind = engine_maker.engine
        case_ids = AppCaseIds()
        case_ids.metadata.bind = engine_maker.engine
        case_sqlinfo = AppCaseSqlinfo()
        case_sqlinfo.metadata.bind = engine_maker.engine
        case_sqlinfo_checklsit = AppCaseSqlinfoChecklist()
        case_sqlinfo_checklsit.metadata.bind = engine_maker.engine
        case_sqlinfo_config = AppCaseSqlinfoConfig()
        case_sqlinfo_config.metadata.bind = engine_maker.engine
        case_sqlinfo_script = AppCaseSqlinfoScript()
        case_sqlinfo_script.metadata.bind = engine_maker.engine
        case_detail = AppDetail()
        case_detail.metadata.bind = engine_maker.engine
        case_stage = AppCaseStage()
        case_stage.metadata.bind = engine_maker.engine
        case_stage_path = AppCaseStagePath()
        case_stage_path.metadata.bind = engine_maker.engine
        case_stage_result = AppCaseStageResult()
        case_stage_result.metadata.bind = engine_maker.engine
        case_caps = AppCaseCaps()
        case_caps.metadata.bind = engine_maker.engine

    @classmethod
    def get_case_all(cls):
        with session_close() as session:
            temp = session.query(AppCase).all()
            return temp

    @classmethod
    def get_case_by_suite_id(cls, id):
        with session_close() as session:
            temp = session.query(AppCase).filter(AppCase.suite_id==id).all()
            return temp

    @classmethod
    def get_case_expect_by_id(cls, id):
        with session_close() as session:
            temp = session.query(AppCaseExpect).filter(AppCaseExpect.id==id).all()
            return temp

    @classmethod
    def get_case_ids_by_id(cls, id):
        with session_close() as session:
            temp = session.query(AppCaseIds).filter(AppCaseIds.id==id).all()
            return temp

    @classmethod
    def get_case_caps_by_id(cls, id):
        with session_close() as session:
            temp = session.query(AppCaseCaps).filter(AppCaseCaps.id==id).all()
            return temp

    @classmethod
    def get_case_stage_by_case_id(cls, case_id):
        with session_close() as session:
            temp = session.query(AppCaseStage).filter(AppCaseStage.case_id==case_id).all()
            return temp

    @classmethod
    def get_case_stage_path_by_stage_id(cls, stage_id):
        with session_close() as session:
            temp = session.query(AppCaseStagePath).filter(AppCaseStagePath.stage_id==stage_id).all()
            return temp

    @classmethod
    def get_case_stage_path_by_id(cls, id):
        with session_close() as session:
            temp = session.query(AppCaseStageResult).filter(AppCaseStageResult.case_id==id).all()
            return temp

    @classmethod
    def get_case_sqlinfo_by_id(cls, id):
        with session_close() as session:
            temp = session.query(AppCaseSqlinfo).filter(AppCaseSqlinfo.id==id).all()
            return temp

    @classmethod
    def get_case_sqlinfo_checklist_by_id(cls, id):
        with session_close() as session:
            temp = session.query(AppCaseSqlinfoChecklist).filter(AppCaseSqlinfoChecklist.id==id).all()
            return temp

    @classmethod
    def get_case_sqlinfo_config_by_id(cls, id):
        with session_close() as session:
            temp = session.query(AppCaseSqlinfoConfig).filter(AppCaseSqlinfoConfig.id==id).all()
            return temp

    @classmethod
    def get_case_sqlinfo_script_by_id(cls, id):
        with session_close() as session:
            temp = session.query(AppCaseSqlinfoScript).filter(AppCaseSqlinfoScript.id==id).all()
            return temp

    @classmethod
    def get_case_detail_by_id(cls, id):
        with session_close() as session:
            temp = session.query(AppDetail).filter(AppDetail.id==id).all()
            return temp