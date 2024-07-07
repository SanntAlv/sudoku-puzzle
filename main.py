from flask import Flask, request, jsonify
from models import db, Usuario, Puntuacion

app = Flask(__name__)
port = 5000
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/mibasededatos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/data/<section>')
def data(section):
    return section



if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
