from flask import Flask, jsonify, request, make_response
import mysql.connector
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hOQxNq7kLkaoUb5B4dXd2t7r8DG9XVjL'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        print('token' + token)
        if not token:
            return jsonify({'message':'Token is missing'})

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message':'Session Expired'})

        return f(*args, **kwargs)

    return decorated


# Configuracion de MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="twitterfakeapi"
)

query = mydb.cursor()

query.execute('USE twitterfakeapi')

@app.route('/api/v1/register', methods=['POST'])
def register():
    # Tomar los valores de request.json y guardar en MySQL
    first_name = str(request.json['first_name'])
    last_name = str(request.json['last_name'])
    email = str(request.json['email'])
    password = str(request.json['password'])
    print(first_name, last_name, email, password)
    query.execute("INSERT INTO users (first_name, last_name, email, password) VALUES(%s, %s, %s, %s)",
    (first_name, last_name, email, password))
    mydb.commit()
    return first_name, 201

@app.route('/api/v1/login', methods=['GET'])
def login():
    # Verificar si request.json es igual a la informacion en la base de datos

    if request and request.json['password'] == 'password':
        token = jwt.encode({
            'username' : request.json['username'], 
            'password' : request.json['password'], 
            'exp' : datetime.datetime.utcnow() +
            datetime.timedelta(minutes=30)
            }, app.config['SECRET_KEY'])
        return jsonify({'token':token.decode('utf-8')})
    else:
        return 'Login Failed'

@app.route('/api/v1/<string:user>', methods=['GET'])
@token_required
def getTwitts(user):
    # Enviar todos los twitts
    return 'twitts de ' + user 

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