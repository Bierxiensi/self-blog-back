#类的实例是 WSGI（Web Server Gateway Interface） 应用程序
from flask import Flask
app = Flask(__name__)
from flask_cors import CORS
CORS(app)
# from flask_cors import CORS
# # CORS(app, supports_credentials=True)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.run()