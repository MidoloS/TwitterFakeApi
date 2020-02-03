import requests
import json

headers = {'Content-Type': 'application/json'}

def show(response, url, method):
    print('Haciendo peticion %s a %s' % (method, url))
    if len(response.content) > 10:
        print('Body: ')
        print(response.content)

    if len(response.headers) > 10:
        print('Header: ')
        print(response.headers)
    
    print('Status: %s' % response.status_code)
    print('\n')
    return response.headers

def register(email, first_name, last_name, password):
    url = 'http://127.0.0.1:4000/api/v1/register'
    data = {
        "email":email,
        "first_name":first_name,
        "last_name":last_name,
        "password":password
    } 

    response = requests.post(url = url, data = json.dumps(data), headers = headers)
    show(response, url, 'POST')

def login(email, password):
    url = 'http://127.0.0.1:4000/api/v1/login'
    data = {
        "email":email,
        "password":password
    } 

    response = requests.get(url = url, data = json.dumps(data), headers = headers)
    return show(response, url, 'GET')

def getTwitts(user):
    url = 'http://127.0.0.1:4000/api/v1/%s/tweets' % user
    data = { } 

    response = requests.get(url = url, data = json.dumps(data), headers = headers)
    show(response, url, 'GET')

def createTwitt(user, twitt):
    url = 'http://127.0.0.1:4000/api/v1/%s/tweets' % user
    data = {'message':twitt} 

    response = requests.post(url = url, data = json.dumps(data), headers = headers)
    show(response, url, 'POST')

def deleteTwitt(twitt_id, user):
    url = 'http://127.0.0.1:4000/api/v1/%s/tweets/%s' % (user, twitt_id)
    print(url)

    response = requests.delete(url = url)
    show(response, url, 'DELETE')

# Ninguna de estas opciones daran respuesta ya que no tienen token
getTwitts('spacex')
createTwitt('spacex', 'Lanzamiento de 60 satelites')

# El mail debe ser unico
register("midolo.1912@gmail.com", "Sebastian", "Midolo", "secret")
register("midolo.1912@gmail.com", "Sebastian", "Midolo", "secret")

# Login con malas credenciales
headers = login("midolo.1912@gmail.comm", "wrong_password")

# Login con buenas credenciales
headers = login("midolo.1912@gmail.comm", "secret")

# Creacion de twitt con token
createTwitt('spacex', 'Lanzamiento de 60 satelites')

# Obtencion de twitts con token
getTwitts('spacex')

# Borrar twitt
deleteTwitt(0, 'spacex')

# Mostrar de nuevo
getTwitts('spacex')