from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/ana/')
def ana():
    return render_template('ana.html')

if __name__ == '__main__':
    app.run()
