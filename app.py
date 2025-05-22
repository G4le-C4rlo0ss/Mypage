from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Permite que tu frontend pueda comunicarse con el backend

# Configura la base de datos PostgreSQL (cambia el valor en DATABASE_URL)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)  # En producción, encripta!

@app.route('/api/registro', methods=['POST'])
def registro():
    data = request.get_json()
    nombre = data.get('nombre')
    email = data.get('email')
    password = data.get('password')

    if not nombre or not email or not password:
        return jsonify({'message': 'Faltan datos'}), 400

    # Verificar si el email ya existe
    if Usuario.query.filter_by(email=email).first():
        return jsonify({'message': 'El email ya está registrado'}), 400

    nuevo_usuario = Usuario(nombre=nombre, email=email, password=password)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({'message': 'Registro exitoso'}), 201

if __name__ == '__main__':
    app.run(debug=True)
