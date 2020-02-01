from flask import Flask, jsonify, request, Response, json
import mysql.connector
import jwt
import datetime
from functools import wraps
from models.model import User, Twitt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hOQxNq7kLkaoUb5B4dXd2t7r8DG9XVjL'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        print(request.headers)
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message':'Token is missing'})

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            print(data['username'])
        except:
            return jsonify({'message':'Session Expired'})

        return f(data, *args, **kwargs)

    return decorated




@app.route('/api/v1/register', methods=['POST'])
def register():
    # Tomar los valores de request.json y guardar en MySQL
    users = User('', '', '', '')
    users = users.getUsers()

    if request:
        for row in users:
            if request.json['email'] == row[3]:
                return jsonify({'message':'This mail is already claimed'}), 400

        user = User('', '', '', '')
        user.createUser()
        return request.json, 201
    else:
        return jsonify({'message':'Data not found'}), 400

@app.route('/api/v1/login', methods=['GET'])
def login():
    users = User('', '', '', '')
    users = users.getUsers()
    
    
    for row in users:
        # 1 Username
        # 4 Password
        print("\n")
        if request and request.json['password'] == row[4] and request.json['email'] == row[3]:
            token = jwt.encode({
                'email' : request.json['email'], 
                'password' : request.json['password'], 
                'exp' : datetime.datetime.utcnow() +
                datetime.timedelta(minutes=30)
                }, app.config['SECRET_KEY'])

            token = token.decode('utf-8')

            response = jsonify({'token':token})
            response.headers['x-access-token'] = token
            return response
    return 'Login Failed'

@app.route('/api/v1/<string:user>/tweets', methods=['GET'])
@token_required
def getTwitts(token_data, user):
    twitts = Twitt('', user, '', datetime.datetime.utcnow())
    twitts = twitts.getTwitt(token_data, user)
    return jsonify({"twitts":twitts})

@app.route('/api/v1/<string:user>/tweets', methods=['POST'])
@token_required
def createTwitt(token_data, user):
    twitts = Twitt('', user, '', datetime.datetime.utcnow())
    twitts.createTwitt(token_data)
    return request.json

@app.route('/api/v1/<string:user>/tweets/:id', methods=['DELETE'])
def delete(user, id):
    twitt = Twitt(id, '', '', datetime.datetime.utcnow())
    twitt.deleteTwitt()
    return '', 200


if __name__ == '__main__':
    app.run(debug=True, port=4000)