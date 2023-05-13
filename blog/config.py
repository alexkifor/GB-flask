import os

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "04_z_xwon#ad&++tr6ut5sva)iod!4m9ar=b5gxfjm=dz^agt2"


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    FLASK_ADMIN_SWATCH = 'solar'
    OPENAPI_URL_PREFIX = '/api/docs'
    OPENAPI_VERSION = '3.0.0'
    OPENAPI_SWAGGER_UI_PATH = '/'
    OPENAPI_SWAGGER_UI_VERSION = '3.51.1'
    
    


class TestingConfig(BaseConfig):
    TESTING = True

