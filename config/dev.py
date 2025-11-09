from sqlalchemy.engine import make_url

from .default import *


APP_ENV = APP_ENV_DEVELOPMENT

SQLALCHEMY_DATABASE_URI = 'postgresql://admin:123456@localhost:5432/hackton_2025'