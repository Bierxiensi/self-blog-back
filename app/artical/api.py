"""
author:zxy
time:2019-09-19
ToDo: CRUD for articals, core part
belong:artical package
"""
from flask import jsonify, request
from app.artical.model import handlearticaloptions
from app.common import Common

def init_api(app):
    @app.route('/artical/getAllAtricals')
    def getAllAtricals():
        articals = handlearticaloptions.getAll(handlearticaloptions)
        output = []
        for artical in articals:
            output.append(handlearticaloptions.output(articals, artical))
        return jsonify(Common.trueReturn(Common, output))

    @app.route('/artical/getAtricalById/<int:articalId>')
    def getAtricalById(articalId):
        artical = handlearticaloptions.getArticalById(handlearticaloptions, articalId)
        if artical is None:
            return jsonify(Common.falseReturn(Common, None, '找不到数据'))
        else:
            return jsonify(Common.trueReturn(Common, handlearticaloptions.output(handlearticaloptions, artical)))


    @app.route('/artical/insertArtical', methods=['POST'])
    def insertArtical():

        '''
        :return: Consulting the common.py in app package for details
        '''
        '''
         method 1 get params from form
        '''
        articalId = request.form.get('articalId')
        title = request.form.get('title')
        content = request.form.get('content')
        tag = request.form.get('tag')
        createTime = request.form.get('createTime')
        updateTime = request.form.get('updateTime')
        createPeople = request.form.get('createPeople')

        '''
         method 2 get params from url
        '''
        # articalId = request.args.get('articalId')
        # title = request.args.get('title')
        # content = request.args.get('content')
        # tag = request.args.get('tag')
        # createTime = request.args.get('createTime')
        # updateTime = request.args.get('updateTime')
        # createPeople = request.args.get('createPeople')
        artical = handlearticaloptions(articalId=articalId, title=title, content=content, tag=tag,createTime=createTime,
                                    updateTime=updateTime,createPeople=createPeople )
        result = handlearticaloptions.insert(handlearticaloptions, artical)
        print(42,request.form,result,artical.id)
        if artical.id:
            return jsonify(Common.trueReturn(Common, 'i like yz'))
        else:
            return jsonify(Common.falseReturn(Common, 'i like yz'))

    @app.route('/artical/updateArtical/<int:articalId>', methods=['PUT'])
    def updateArtical(articalId):
        artical = handlearticaloptions.getArticalById(handlearticaloptions, articalId)
        if artical is None:
            return jsonify(Common.falseReturn(Common, None, '找不到要修改的数据'))
        else:
            artical.title = request.form.get('title')
            artical.content = request.form.get('content')
            artical.tag = request.form.get('tag')
            artical.updateTime = request.form.get('updateTime')
            artical.createPeople = request.form.get('createPeople')
            result = handlearticaloptions.update(handlearticaloptions, artical)
            print(56,result)
            if artical.id:
                return getAtricalById(articalId)
            else:
                return jsonify(Common.falseReturn(Common, None, result))

    @app.route('/artical/deleteArtical/<int:articalId>', methods=['DELETE'])
    def deleteArtical(articalId):
        artical = handlearticaloptions.getArticalById(handlearticaloptions, articalId)
        if artical is None:
            return jsonify(Common.falseReturn(Common, None, '找不到要删除的数据'))
        else:
            result = handlearticaloptions.delete(handlearticaloptions, articalId)
            print(66,result)
            if result is None:
                return jsonify(Common.falseReturn(Common, None, '删除成功'))
            else:
                return jsonify(Common.trueReturn(Common, None, '删除失败'))
