from flask import Flask, request, jsonify
from models import db, Usuario, Puntuacion

app = Flask(__name__)
port = 5000
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/mibasededatos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def hello_world():
    return "sdfsfasdasd"

@app.route('/usuarios/<id_usuarios>')
def data(id_usuarios):
    print('Usuario: ',id_usuarios)
    return id_usuarios

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    nombre = request.form.get('nombre')
    usuario = Usuario.query.filter_by(nombre=nombre).first()
    if not usuario:
        usuario = Usuario(nombre=nombre)
        db.session.add(usuario)
        db.session.commit()
    session['usuario_id'] = usuario.id
    return redirect(url_for('select_dificultad'))


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
