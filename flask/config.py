# import os
class SystemConfig:
    DEBUG = True
    # .envから取得
    # テスト用
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@db:3306/reservation-db?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_ENGINE_OPTIONS = {"connect_args": {"charset": "utf8"}}


Config = SystemConfig
