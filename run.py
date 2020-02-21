from flask import Flask
from flask import render_template
from renz import Renz

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/whatsyourname')
def _whatsyourname():
    return "renz"

@app.route('/hello/<name>')
def hello(name=None):
    renz = Renz()
    description = renz.nameDescription(name, 19)
    return render_template('/template.html', name=description)


