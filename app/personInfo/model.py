from app import db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)

    """
        __repr__ 与 __str__
        https://blog.csdn.net/sinat_41104353/article/details/79254149
         _repr__ 目的是为了表示清楚，是为开发者准备的。
        __str__ 目的是可读性好，是为使用者准备的。
        我的理解是 __repr__ 应该尽可能的表示出一个对象来源的类以及继承关系，
        方便程序员们了解这个对象。而 __str__ 就简单的表示对象
    """
    def __repr__(self):
        print(1)
        return 'User:%s' % self.name
    def __str__(self):
        print(2)
        return "select(id='%s')" % self.id

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def getAll(self):
        return self.query.all()

    def output(self, user):
        return {
            'id': user.id,
            'name': user.name
        }