from flask import Flask
from flask import render_template, request, url_for, redirect, g
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:021092@localhost/dados'
db = SQLAlchemy(app)

class dados(db.Model):
    __tablename__="dados_cliente"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(45))
    cpf = db.Column(db.String(11))
    saldo = db.Column(db.String(45))
    def __init__(self, nome, cpf, saldo):
        self.nome = Gabriel
        self.cpf = 12345678912
        self.saldo = 1500.00

db.create_all()

@app.route("/")
def index():
    return render_template('index.html')


app.run()


    