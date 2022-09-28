from flask import Flask, request, jsonify
import requests
from funciones import capturar_texto, consultar_mes, resumen
import json

app = Flask(__name__)


@app.route('/')
def km():
    valor = consultar_mes()
    return valor


@app.route('/consultar', methods=['GET'])
def consultar():
    url = "https://api.telegram.org/bot5534433351:AAGQnST7oEFiIq6IhMh8nfEuL3UoNa0Ux-8/getUpdates"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    json_updates = json.loads(response.text)
    text = json_updates["result"][-1]["message"]["text"]
    capturar_texto(text)
    return "Mensaje Recibido"


@app.route('/avisar', methods=['POST'])
def avisar():
    request_body = request.get_json()
    bot_token = request_body["token"]
    bot_chat_id = "611152189"
    msg = "Mete los Kilometros"
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id + '&parse_mode=Markdown&text=' + msg
    response = requests.get(send_text)
    return "Mensaje Enviado"


@app.route('/resumen_mes', methods=['POST'])
def resumen_mes():
    km_ruta, media_ruta, media_ida, media_vuelta, km_totales = resumen()
    request_body = request.get_json()
    bot_token = request_body["token"]
    bot_chat_id = "611152189"
    msg = f'Este mes has hecho {km_ruta}km en la ruta, una media de {media_ruta}km diarios,en ir al almacen una media ' \
          f'de {media_ida}km desde casa y en la vuelta una media de {media_vuelta}km, lo que hacen un tot' \
          f'al de {km_totales}km. '
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id + '&parse_mode' \
                                                                                                     '=Markdown&text=' + msg
    response = requests.get(send_text)

    return "Resumen enviado"


if __name__ == '__main__':
    app.run()
