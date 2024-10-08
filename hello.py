from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '''

    <h1>Hello World!</h1>
    <h3>Welcome to my site!!</h3>

    '''

@app.route('/example/<text>')
def hello_world2(text):
    return f"<h1>just example</h1><h3>but stil the same site :D</h3><h3>{escape(text)}</h3>"