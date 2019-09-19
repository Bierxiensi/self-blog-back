from flask import Flask
#对象关系映射（Object-Relational Mapper, ORM）框架
#将低层的数据库操作指令抽象成高层的面向对象操作
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.ext.declarative import declarative_base
import pymysql
# from sqlalchemy import create_engine
# engine = create_engine('mysql://root:@localhost:3306/zxyaily')
# Base = declarative_base()

#flask中使用ORM模型
db = SQLAlchemy()


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    db.init_app(app)

    # # 用户模块
    # from app.users.api import init_api
    # init_api(app)
    #
    # # 新闻模块
    # from app.news.api import init_api
    # init_api(app)
    from app.artical.api import init_api
    init_api(app)

    from app.personInfo.view import init_api
    init_api(app)

    return app

