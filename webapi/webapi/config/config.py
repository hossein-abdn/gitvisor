from os import environ


class Config:
    ENV = environ.get("GITVISOR_WEBAPI_ENV", "production")
    DEBUG = bool(int(environ.get("GITVISOR_WEBAPI_DEBUG", "0")))
    TESTING = bool(int(environ.get("GITVISOR_WEBAPI_TESTING", "0")))
    SECRET_KEY = environ.get("GITVISOR_WEBAPI_SECRET_KEY", "secretkey")
