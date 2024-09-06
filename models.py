from database import db

class Usuario(db.Model):
    __tablename__="usuario"
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    idade = db.Column(db.Integer)

    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade

    def __repr__(self):
        return "<Usuario {}>".format(self.nome)
    