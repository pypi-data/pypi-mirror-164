import os
from os.path import join
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:  # 基本配置类
    SECRET_KEY = os.getenv(
        "SM_SECRET_KEY", 'd23s@L8Ya8T_^&@#dJKw$kacFECz(F7E$ASaprJkS$m7oKEL9qsfs^02Rlksf0DwA)etDFrj;)kYsa#je')
    API_PREFIX = os.environ.get("SM_API_PREFIX", "/mtxpagent")
    # HTML_ROOT_DIR = os.environ.get("SM_HTML_ROOT", "/var/www/html")
    LOG_DIR = join(os.getcwd(),"logs")


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(BaseConfig):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    WTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
