# export FLASK_APP=flask_app.py;flask run

from flask import Flask, render_template, request, flash, url_for
import os
import dataset
from flask_charts import GoogleCharts
from flask_charts import Chart

app = Flask(__name__)
charts = GoogleCharts(app)
app.config['TEMPLATES_AUTO_RELOAD'] = True
PATH = os.path.dirname(os.path.realpath(__file__)) + "/"
with open(PATH + "secrets.txt") as f:
    secret = f.read()
app.secret_key = secret
db = dataset.connect('sqlite:///{}/database.db'.format(PATH))


@app.route('/', methods=['GET'])
def main():
    my_chart = Chart("PieChart", "my_chart")#https://github.com/albinmedoc/flask-charts
    my_chart.data.add_column("string", "Person")
    my_chart.data.add_column("number", "Count")
    my_chart.data.add_row(["Albin", 3])
    my_chart.data.add_row(["Robert", 4])
    my_chart.data.add_row(["Daniel", 2.5])

    return render_template("game.html", my_chart=my_chart)


@app.route('/ranking', methods=['GET'])
def ranking():
    return render_template("ranking.html")
