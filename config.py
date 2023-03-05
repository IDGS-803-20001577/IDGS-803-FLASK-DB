import os
from sqlalchemy import create_engine


class Config(object):
    SECRET_KEY='SUPER_SECRET_KEY'
    SESSION_COOKIE_SECURITY=False

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:1234@127.0.0.1/idgs803"
    SQLALCHEMY__TRACK_MODIFICATION=False