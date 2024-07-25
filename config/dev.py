from sqlalchemy.engine import make_url

from .default import *


APP_ENV = APP_ENV_DEVELOPMENT

SQLALCHEMY_DATABASE_URI = make_url('mariadb+pymysql://u257146646_test:testUGT2024@193.203.166.149:3306/u257146646_testUGT')