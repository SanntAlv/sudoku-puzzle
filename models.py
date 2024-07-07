from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__='usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    puntuacion_total = db.Column(db.Integer, default=0, nullable=False)

class Puntuacion(db.Model):
    __tablename__ = 'puntuaciones'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    dificultad = db.Column(db.String(10), nullable=False)
    tiempo = db.Column(db.Integer, nullable=False)
    puntos = db.Column(db.Integer, nullable=False)

usuario = db.relationship('Usuario', backref=db.backref('puntuaciones', lazy=True)) #define la relacion