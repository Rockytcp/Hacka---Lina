from flask import Flask
from flask import render_template, request, url_for, redirect
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
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo

db.create_all()

@app.route("/")
def index():
    nome = "Gabriel"
    cpf = 12345678912
    saldo = 1500.00
    var = dados(nome, cpf, saldo)
    db.session.add(var)
    db.session.commit()
    return render_template('index.html')


'''@app.route("/registrar", methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nome = (request.form.get("nome"))
        cores = (request.form.get("cores"))
        estadio = (request.form.get("estadio"))
        if nome:
            var = dados(nome, cores, estadio)
            db.session.add(var)
            db.session.commit()
    return redirect(url_for("mensagem"))'''
    


app.run()


    