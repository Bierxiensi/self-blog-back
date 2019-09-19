from app import create_app
from flask_cors import CORS

app = create_app('app.config')
CORS(app, supports_credentials=True)

if __name__ == '__main__':
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])