from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from hafweb.config import *
import functools
from contextlib import contextmanager


engine = create_engine(
    f"mysql+pymysql://{DB_MYSQL_USER}:{DB_MYSQL_PASSWORD}@{DB_MYSQL_HOST}:{DB_MYSQL_PORT}/{DB_MYSQL_NAME}")
maker = sessionmaker(bind=engine)

@contextmanager
def session_close():
    try:
        session = maker()
        yield session
    finally:
        session.close()
