from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Configuracion de MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

query = mydb.cursor()

query.execute('CREATE DATABASE IF NOT EXISTS TwitterFakeApi')
query.execute('USE TwitterFakeApi')

@app.route('/api/v1/register', methods=['POST'])
def register():
    # Tomar los valores de request.json y guardar en MySQL
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    password = request.json['password']
    print(first_name, last_name, email, password)
    query.execute('INSERT INTO users (first_name, last_name, email, password) VALUES(%s, %s, %s, %s)',
    (first_name, last_name, email, password))
    return first_name

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