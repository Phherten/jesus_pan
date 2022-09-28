from flask import Flask, request, jsonify

from funciones import devolver_variables, agregar_datos

app = Flask(__name__)


@app.route('/añadir_km', methods=['POST'])
def agregar():  # put application's code here
    request_body = request.get_json()
    agregar_datos(request_body['km'])
    return jsonify({"mensaje": "km añadido"})


@app.route('/')
def km():
    valor = devolver_variables()
    return jsonify({"km": valor})


if __name__ == '__main__':
    app.run()
