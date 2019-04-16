from hafweb.controller.engine import *
from sqlalchemy import *
from datetime import datetime
from hafweb.model.model_token import *
import json


class ControllerToken(object):
    def __init__(self):
        pass

    @classmethod
    def bind_all(cls):
        token = Token()
        token.metadata.bind = engine_maker.engine

    @classmethod
    def get_user_name_all(cls):
        with session_close() as session:
            temp = session.query(Token).all()
            return temp

    @classmethod
    def get_password_by_name(cls, user_name):
        with session_close() as session:
            temp = session.query(Token).filter(Token.user_name==user_name).all()
            return temp

