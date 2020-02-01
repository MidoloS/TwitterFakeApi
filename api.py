from flask import Flask, jsonify, request, Response, json
import mysql.connector
import jwt
import datetime
from functools import wraps
from models.model import User, Twitt
from hashlib import md5

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
        except:
            return jsonify({'message':'Session Expired'})

        return f(data, *args, **kwargs)

    return decorated




@app.route('/api/v1/register', methods=['POST'])
def register():
    if request:
        users = User('', '', '', '')
        users = users.getMails()
        for row in users:
            if request.json['email'] == row[0]:
                return jsonify({'message':'This mail is already claimed'}), 400

        user = User('', '', '', '')
        user.createUser()
        ids = user.getId(request.json['email'])
        return jsonify({
            'user_id': ids[0][0],
            'email': request.json['email'],
            'first_name': request.json['first_name'],
            'last_name': request.json['last_name']
        }), 201
    else:
        return jsonify({'message':'Data not found'}), 400

@app.route('/api/v1/login', methods=['GET'])
def login():
    users = User('', '', '', '')
    users = users.getUserAndPass()

    try:
        request.json['password'] or request.json['email']
    except:
        return jsonify({'message':'Credentials not found'}), 400
    

    for row in users:
        if request and request.json['password'] == row[1] and request.json['email'] == row[0]:
            token = jwt.encode({
                'email' : request.json['email'], 
                'password' : request.json['password'],
                #'exp' : datetime.datetime.utcnow() + datetime.timedelta(days=9999)
                }, app.config['SECRET_KEY'])
                
            token = token.decode('utf-8')

            response = jsonify({'token':token})
            response.headers['x-access-token'] = token
            return response
    return jsonify({'message':'Login error'}), 401
    

@app.route('/api/v1/<string:user>/tweets', methods=['GET'])
@token_required
def getTwitts(token_data, user):
    twitts = Twitt('', user, '', datetime.datetime.utcnow())
    twitts = twitts.getTwitt(token_data, user)
    if len(twitts) == 0:
        return jsonify({'message':'No content'}), 204

    res = []
    i = 0
    print(twitts[0])
    for twitt in twitts:
        print(twitt)
        print('\n')
        obj = {
            'id':twitt[0],
            'owner':twitt[1],
            'message':twitt[2],
            'creation_timestamp': twitt[3]
        }
        i += 1
        res.append(obj)
    return jsonify({"twitts":res})

@app.route('/api/v1/<string:user>/tweets', methods=['POST'])
@token_required
def createTwitt(token_data, user):
    twitts = Twitt('', user, '', datetime.datetime.utcnow())
    twitts.createTwitt(token_data, user)
    return '', 201

@app.route('/api/v1/<string:user>/tweets/<string:id>', methods=['DELETE'])
def delete(user, id):
    twitt = Twitt(id, '', '', '')
    twitt.deleteTwitt()
    return '', 200


if __name__ == '__main__':
    app.run(debug=True, port=4000)