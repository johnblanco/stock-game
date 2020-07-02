# export FLASK_APP=flask_app.py;flask run

from flask import Flask, render_template, request, flash, url_for
import os
import dataset
from flask_charts import GoogleCharts
from flask_charts import Chart
from flask_login import LoginManager, login_required, logout_user, login_user, current_user
from werkzeug.utils import redirect

from login_form import LoginForm
from register_form import RegisterForm
from user import User

app = Flask(__name__)
charts = GoogleCharts(app)
app.config['TEMPLATES_AUTO_RELOAD'] = True
PATH = os.path.dirname(os.path.realpath(__file__)) + "/"
with open(PATH + "secrets.txt") as f:
    secret = f.read()
app.secret_key = secret
db = dataset.connect('sqlite:///{}/database.db'.format(PATH))
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    print("load_user {}".format(user_id))
    user = User(user_id)
    return user


@app.route('/register', methods=['POST'])
def register():
    register_form = RegisterForm(request.form)
    if register_form.validate():
        login_user(User(register_form.username.data))
        return redirect("/")

    return redirect("/login")


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        #TODO si no coinciden las contra, mostrar en pantalla
        login_user(User(login_form.username.data))
        return redirect("/")
    return render_template('login.html', login_form=login_form, register_form=RegisterForm())


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')


@app.route('/', methods=['GET'])
@login_required
def main():
    my_chart = Chart("LineChart", "my_chart")  # https://github.com/albinmedoc/flask-charts
    my_chart.data.add_column("number", "Dia")
    my_chart.data.add_column("number", "Precio")
    my_chart.data.add_row([0, 100])
    my_chart.data.add_row([1, 110])
    my_chart.data.add_row([2, 105])
    my_chart.data.add_row([3, 115])
    my_chart.data.add_row([4, 118])

    my_chart2 = Chart("LineChart", "my_chart2")  # https://github.com/albinmedoc/flask-charts
    my_chart2.data.add_column("number", "Dia")
    my_chart2.data.add_column("number", "Precio")
    my_chart2.data.add_row([0, 50])
    my_chart2.data.add_row([1, 60])
    my_chart2.data.add_row([2, 70])
    my_chart2.data.add_row([3, 115])
    my_chart2.data.add_row([4, 118])

    return render_template("game.html", my_chart=my_chart, my_chart2=my_chart2)


@app.route('/comprar', methods=['GET'])
def buy():
    return render_template("buy.html")


@app.route('/vender', methods=['GET'])
def sell():
    return render_template("sell.html")


@app.route('/ranking', methods=['GET'])
def ranking():
    return render_template("ranking.html")
