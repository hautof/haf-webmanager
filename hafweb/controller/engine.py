from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from hafweb.config import *
import functools
from contextlib import contextmanager
from haf.common.sigleton import *

class EngineMaker(metaclass=SingletonType):
    engine = None
    maker = None

    def __init__(self):
        super().__init__()

    def bind_sql_server(self, args):
        self.engine = create_engine(
            f"mysql+pymysql://{args.sql_server}")
        self.maker = sessionmaker(bind=self.engine)


engine_maker = EngineMaker()


@contextmanager
def session_close():
    try:
        session = engine_maker.maker()
        yield session
    finally:
        session.close()
