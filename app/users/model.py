from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

from app import db

class test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name


    def __str__(self):
        return "test(id='%s')" % self.id

    def getAll(self):
        return self.query.all()

    def get(self, id):
        return self.query.filter_by(id=id).first()

    def add(self, test):
        db.session.add(test)
        return session_commit()

    def update(self):
        return session_commit()

    def delete(self, id):
        deleteRow = self.query.filter_by(id=id).delete()
        return session_commit()

    def output(self, test):
        return {
            'id': test.id,
            'name': test.name
        }

def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason