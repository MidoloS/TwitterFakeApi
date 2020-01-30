from flask import Flask, jsonify, request
import fakeData

app = Flask(__name__)

@app.route('/api/v1/register', methods=['POST'])
def register():
    return request.json

@app.route('/https://localhost/api/v1/login', methods=['POST'])
def login():
    return request.json

@app.route('/https://localhost/api/v1/:user/tweets', methods=['GET'])
def getTwitts():
    return request.json

@app.route('/https://localhost/api/v1/:user/tweets', methods=['POST'])
def getMessage():
    return request.json

@app.route('/https://localhost/api/v1/:user/tweets/:id', methods=['DELETE'])
def delete():
    return request.json


if __name__ == '__main__':
    app.run(debug=True, port=4000)