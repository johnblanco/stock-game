# export FLASK_APP=flask_app.py;flask run

from flask import Flask, render_template, request, flash, url_for
import os
import dataset

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
PATH = os.path.dirname(os.path.realpath(__file__)) + "/"
with open(PATH + "secrets.txt") as f:
    secret = f.read()
app.secret_key = secret
db = dataset.connect('sqlite:///{}/database.db'.format(PATH))


@app.route('/', methods=['GET'])
def main():
    r = db['foo'].find_one()
    return render_template("main.html", bar=r['bar'])
