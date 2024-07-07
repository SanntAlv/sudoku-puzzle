from flask import Flask, request, jsonify
from models import db, Usuario, Puntuacion

app = Flask(__name__)
port = 5000
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgresql@localhost:5432/mibasededatos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def hello_world():
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)