from flask import Flask
from flask_sslify import SSLify
from flask import request
import requests
from lxml import html
import flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    print(request.headers)

    return '<html> <body> <h1>My First Heading</h1> <p>My first paragraph.</p></body></html>'
    


if __name__ == '__main__':
    app.run()