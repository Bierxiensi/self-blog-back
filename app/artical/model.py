from app import db
from sqlalchemy.exc import SQLAlchemyError

class handlearticaloptions(db.Model):
    __tablename__ = 'artical'
    id = db.Column(db.Integer, primary_key=True)
    articalId = db.Column(db.Integer)
    title = db.Column(db.String(50),nullable=False)
    content = db.Column(db.String(30000), nullable=False)
    tag = db.Column(db.String(200),nullable=True)
    createTime = db.Column(db.String(50), nullable=False)
    updateTime = db.Column(db.String(50),nullable=False)
    createPeople = db.Column(db.String(20), nullable=True)

    def __init__(self, articalId , title, content, tag, createTime, updateTime, createPeople):
        self.articalId = articalId
        self.title = title
        self.content = content
        self.tag = tag
        self.createTime = createTime
        self.updateTime = updateTime
        self.createPeople = createPeople

    def getAll(self):
        # return db.session.query(self).order_by(self.articalId).all()
        """
        在 Flask 中的 SQLAlchemy 拥有 flask-sqlalchemy 和 sqlalchemy.orm 两种语法
        下为flask-sqlalchemy语法
        """
        return self.query.all()

    def getArticalById(self,articalId):
        return self.query.filter_by(articalId=articalId).first()

    def insert(self, info):
        db.session.add(info)
        return session_commit()

    def update(self, info):
        db.session.add(info)
        return session_commit()

    def delete(self, articalId):
        deleteRow = self.query.filter_by(articalId=articalId).delete()
        return session_commit()

    def output(self, artical):
        return {
            'articalId': artical.articalId,
            'title': artical.title,
            'content': artical.content,
            'tag': artical.tag,
            'createTime': artical.createTime,
            'updateTime': artical.updateTime,
            'createPeople': artical.createPeople
        }

def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason