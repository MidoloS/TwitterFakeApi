from flask import Flask, jsonify, request
import mysql.connector
import fakeData

app = Flask(__name__)

# Configuracion de MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

query = mydb.cursor()

query.execute('CREATE DATABASE TwitterFakeApi')

@app.route('/api/v1/register', methods=['POST'])
def register():
    # Tomar request.json y guardar en MySQL
    return request.json

@app.route('/api/v1/login', methods=['POST'])
def login():
    # Verificar si request.json es igual a la informacion en la base de datos
    return request.json

@app.route('/api/v1/:user/tweets', methods=['GET'])
def getTwitts():
    # Enviar todos los twitts
    return request.json

@app.route('/api/v1/:user/tweets', methods=['POST'])
def getMessage():
    # Mostrar mensaje de un twitt
    return request.json

@app.route('/api/v1/:user/tweets/:id', methods=['DELETE'])
def delete():
    # Borrar un twitt
    return request.json


if __name__ == '__main__':
    app.run(debug=True, port=4000)