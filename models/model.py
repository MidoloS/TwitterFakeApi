from flask import Flask, jsonify, request
import mysql.connector
import datetime

# Configuracion de MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="twitterfakeapi"
)

query = mydb.cursor()

query.execute('USE twitterfakeapi')

class User: 
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def createUser(self):
        # Cambio de valores del objeto
        first_name = str(request.json['first_name'])
        last_name = str(request.json['last_name'])
        email = str(request.json['email'])
        password = str(request.json['password'])
        
        # Consulta SQL
        query.execute("INSERT INTO users (first_name, last_name, email, password) VALUES(%s, %s, %s, %s)",
        (first_name, last_name, email, password))
        mydb.commit()

    def getUserAndPass(self):
        query.execute("SELECT email, password FROM users")
        data = query.fetchall()
        return data

    def getMails(self):
        query.execute("SELECT email FROM users")
        data = query.fetchall()
        return data

    def getId(self, email):
        query.execute("SELECT user_id FROM users WHERE email=%s", (email,))
        data = query.fetchall()
        return data

class Twitt:
    def __init__(self, id, owner, message, creation_timestamp):
        self.id = id
        self.owner = owner
        self.message = message
        self.creation_timestamp = creation_timestamp

    def createTwitt(self, token_data, user):
        # Cambio de valores del objeto
        message = str(request.json['message'])
        owner_name = user
        creation_timestamp = datetime.datetime.utcnow()

        # Consulta SQL
        query.execute("INSERT INTO twitts (owner_name, message, creation_timestamp) VALUES(%s, %s, %s)",
        (owner_name, message, creation_timestamp))
        mydb.commit()

    def getTwitt(self, token_data, owner_name):
        query.execute("SELECT * FROM twitts WHERE owner_name=%s", (owner_name,))
        data = query.fetchall()
        return data

    def deleteTwitt(self):
        query.execute("DELETE FROM twitts WHERE id = %s", (self.id,))
        mydb.commit()