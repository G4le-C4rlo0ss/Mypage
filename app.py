from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Servidor Flask en Railway funcionando."

@app.route('/api/guardar', methods=['POST'])
def guardar():
    data = request.get_json()
    print(data)  # aquí puedes guardar en la base de datos
    return jsonify({'mensaje': 'Datos recibidos correctamente'}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
