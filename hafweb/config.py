from sqlalchemy.ext.declarative import declarative_base
import os

WEB_SERVER_PORT = 8081

RESOURCE_PATH = f"{os.path.dirname(__file__)}/resource"

DB_MYSQL_HOST = "192.168.41.208"
DB_MYSQL_PORT = 3306
DB_MYSQL_USER = "root"
DB_MYSQL_PASSWORD = "testzhan123"
DB_MYSQL_NAME = "haf_publish"

Base = declarative_base()

MAIN_VERSION = 0
SUB_VERSION = 0
FIX_VERSION = 5

VERSION = f"{MAIN_VERSION}.{SUB_VERSION}.{FIX_VERSION}"