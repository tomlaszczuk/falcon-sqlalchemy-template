import os


class Config:
    SECRET_KEY = 'secret'  # change it
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ['TEST_SQLALCHEMY_DATABASE_URI']


class ProductionConfig(Config):
    pass


config_dict = {
    'DEVELOPMENT': DevelopmentConfig,
    'PRODUCTION': ProductionConfig,
    'TESTING': TestingConfig,

    'default': DevelopmentConfig
}
