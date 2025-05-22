from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/enviar", methods=["POST"])
def recibir_formulario():
    datos = request.get_json()

    nombre = datos.get("nombre")
    email = datos.get("email")
    mensaje = datos.get("mensaje")

    print(f"Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}")

    return jsonify({"mensaje": "Formulario recibido correctamente."}), 200

if __name__ == "__main__":
    app.run(debug=True)
