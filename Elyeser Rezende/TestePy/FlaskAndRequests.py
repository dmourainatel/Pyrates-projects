import requests
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return(render_template('index.html',nome ='Pyrates Diego Moura'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
