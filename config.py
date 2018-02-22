import os
class Config(object):
    """
    Configurations
    """


class DevelomentConfig(Config):
    """
    Dev Config
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'd;adflsdfdfferjoioitr;d&d8&^'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/author_hunter'
    BASE_DIR = os.path.abspath(os.getcwd())
    CELERY_BROKER_URL = 'redis://localhost:6379/1'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'


class StagingConfig(Config):
    """
    Staging Config
    """
    DEBUG = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'f2t0vBJTLr1WE9zz8UWTI3Tpxwcif6ck'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Kyu^3&)eZ&aq@localhost/author_hunter'
    BASE_DIR = os.path.abspath(os.getcwd())
    CELERY_BROKER_URL = 'redis://localhost:6379/1'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
    

class ProductionConfig(Config):
    """
    Production Config
    """
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '93#Gbj6MgdahMa9x*74anQ&4=NX?+KRX'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:u22XaaCbD-KFjW[6@localhost/author_hunter'
    BASE_DIR = os.path.abspath(os.getcwd())
    CELERY_BROKER_URL = 'redis://localhost:6379/1'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'

app_config = {
    'dev': DevelomentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}