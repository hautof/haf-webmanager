from sqlalchemy.ext.declarative import declarative_base
import os

WEB_SERVER_PORT = 8081

RESOURCE_PATH = f"{os.path.dirname(__file__)}/resource"

Base = declarative_base()

MAIN_VERSION = 0
SUB_VERSION = 0
FIX_VERSION = 9

VERSION = f"{MAIN_VERSION}.{SUB_VERSION}.{FIX_VERSION}"