import flask
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='localhost')

