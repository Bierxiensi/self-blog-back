from test import controller
from flask import Blueprint
personInfo = Blueprint('personInfo',__name__)

@personInfo.route('/')
def index():
    print(2)
    return 'Index Page'

@personInfo.route('/hello',methods=['GET', 'POST'])
def hello():
    return controller.sel()
    # return 'Hello World'

@personInfo.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@personInfo.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
