from sqlalchemy.engine import make_url

from .default import *


APP_ENV = APP_ENV_DEVELOPMENT

SQLALCHEMY_DATABASE_URI = make_url('postgresql://admin:revadiva2025@82.180.163.244:5432/hackaton_itiz25')