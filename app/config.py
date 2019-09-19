"""
Created by zxy on 2019/9/8
"""
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_DB = 'zxyaily'

DEBUG = True
PORT = 5000
HOST = "127.0.0.1"

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_DB