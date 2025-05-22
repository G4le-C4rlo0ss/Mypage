from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///access.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class AccessLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    ip = db.Column(db.String(50))
    user_agent = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/log_access', methods=['POST'])
def log_access():
    data = request.json
    new_log = AccessLog(
        email=data.get('email'),
        ip=data.get('ip'),
        user_agent=data.get('userAgent')
    )
    db.session.add(new_log)
    db.session.commit()
    return jsonify({"status": "logged"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
