#personInfo
from flask import jsonify, request
from app.common import Common
from app.personInfo.model import Users

def init_api(app):
    @app.route('/')
    def getUsers():
        users = Users.getAll(Users)
        output = []
        for user in users:
            output.append(Users.output(Users,user))
        return jsonify(Common.trueReturn(Common, output))


