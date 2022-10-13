from flask import Flask, request, jsonify
import requests
from funciones import add_film, day_film, films
import json

app = Flask(__name__)


@app.route('/')
def consultar():
    valor = films()
    return valor


@app.route('/add_films', methods=['POST'])
def add_films():
    request_body = request.get_json()
    url = f'https://api.telegram.org/bot{request_body["token"]}/getUpdates'

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    json_updates = json.loads(response.text)
    text = json_updates["result"][-1]["message"]["text"]
    add_film(text)
    return "Mensaje Recibido"


@app.route('/day_film', methods=['POST'])
def day_film():
    request_body = request.get_json()
    bot_token = request_body["token"]
    bot_chat_id = request_body["chat_id"]
    film = day_film()
    msg = film
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id + '&parse_mode=Markdown&text=' + msg
    response = requests.get(send_text)
    return "Mensaje Enviado"


if __name__ == '__main__':
    app.run()
