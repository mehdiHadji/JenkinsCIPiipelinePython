import flask
from flask import Flask, request, make_response
from flask_cors import CORS


app = Flask(__name__)
app.config['DEBUG'] = True
CORS(app)



@app.route('/')
@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'


@app.route('/hello/<username>')
def hello_user(username):
    return 'Why Hello %s!\n' % username


if __name__ == '__main__':
	app.run(host='0.0.0.0')