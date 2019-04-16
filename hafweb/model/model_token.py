from hafweb.config import Base
from sqlalchemy import *
import json


class Token(Base):
    __tablename__ = "token"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    user_id = Column(Integer)
    token = Column(String)

    def __repr__(self):
        attr_list = ["id", "username", "password", "user_id", "token"]
        rev = {}
        for attr in attr_list:
            rev[attr] = getattr(self, attr)
        return json.dumps(rev)