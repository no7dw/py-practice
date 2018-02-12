from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask import abort

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey Welcome!'

@app.route('/index/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/error')
def hello_error():
    abort(503)

def get_user_profile(userid):
    return jsonify(name='dengwei', password='123')

@app.route('/user/<userid>', methods=['POST', 'GET'])
def user_profile(userid):
    print(userid)
    if request.method == 'GET':
        return get_user_profile(userid)
    elif request.method == 'POST':
        return update_user_profile(userid)

def update_user_profile(userid):
    print (request.is_json)
    print(request.get_json(force=True))
    return 'Hey updated' 

if __name__ ==  'main':
    app.run()

