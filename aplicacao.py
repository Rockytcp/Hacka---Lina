from flask import Flask
from flask import render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text


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
    
    def get_nome(self):
        return self.nome
    
    def get_cpf(self):
        return self.cpf
    
    def get_saldo(self):
        return self.saldo

    def set_nome(self, nome):
        self.nome = ""

    def set_cpf(self, cpf):
        self.cpf = ""

    def set_saldo(self, saldo):
        self.saldo = ""

class dados1(db.Model):
    __tablename__="dados_cliente1"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(45))
    cpf = db.Column(db.String(11))
    saldo = db.Column(db.String(45))

    def __init__(self, nome, cpf, saldo):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
        
    def get_nome(self):
        return self.nome
    
    def get_cpf(self):
        return self.cpf
    
    def get_saldo(self):
        return self.saldo

    def set_nome(self, nome):
        self.nome = ""

    def set_cpf(self, cpf):
        self.cpf = ""

    def set_saldo(self, saldo):
        self.saldo = ""


db.create_all()

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db.session.execute("INSERT INTO dados_cliente1(nome) VALUES Gabriel")
        db.session.commit()
    return render_template('index.html')

@app.route("/delete")
def delete():
    db.session.execute("ALTER TABLE dados_cliente1 DROP saldo")
    return render_template('delete.html')


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


    