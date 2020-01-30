# Evaluación Técnica Intac (Práctica)

 Esta es la parte practica de la evaluación técnica, no olvide completar la parte teórica

## Forma de trabajo
  * Cree un nuevo repositorio privado y agregue el archivo README.md enviado 
  * En su repositorio subas sus cambios a un nuevo branch
  * Cuando este list@ agregue al usuario matiasmpereira como colaborador
  * Cree un pull request de su branch a master y agregue al usuario matiasmpereira como reviewer
  * Aguarde nuestra respuestas
  * Nota: Se evaluará lo incluido hasta el ultimo commit del PR, luego de realizado este entenderemos que finalizó el examen

## Enunciado
  Estamos desarrollando una API que modela las caracteristicas básicos de Twitter, usted estará trabajando en algunos aspectos puntuales. Se necesita que la API disponga de los siguientes endpoints.

### Objetivos
  El objetivo es que desarrolle en Python los endpoints a continuación descritos, para esto puede usar cualquier framework excepto Django. El login debe retornar un token (sin expiracion), para los endpoints que indiquen "con TOKEN" se deberá enviar el mismo como header (de la forma que considere mas conveniente) en la petición. La información se debe persistir en una base de datos MySQL, puede usar un ORM si así lo desea. Si fuese necesario al realizar la entrega no olvide agregar el archivo con los comandos DDL para la base de datos. Los codigo de error HTTP deben estar alineados al estandar.
  Que restricciones funcionales observar en la API que construyo? Al usarla se debe tener alguna consideración en especifico? El uso incorrecto podría afectar de algún modo el modelo de datos?

### Register

> POST https://localhost/api/v1/register
* Request
  ```json
  {
   "email":"<USER_EMAIL>",
   "first_name":"<USER_FIRST_NAME>",
   "last_name":"<USER_LAST_NAME>",
   "password":"<PASSWORD>"
  }
  ```
* Response 
  ```json
  {
   "user_id":"<USER_ID>",
   "email":"<USER_EMAIL>",
   "first_name":"<USER_FIRST_NAME>",
   "last_name":"<USER_LAST_NAME>",
  }
  ```
  Status: 201


### Login

> POST https://localhost/api/v1/login
* Request
  ```json
  {
   "email":"<USER_EMAIL>",
   "password":"<PASSWORD>"
  }
  ```
* Response
  ```json
  {
   "token":"<USER_TOKEN>"
  }
  ```
  Status: 200


### Tweets con TOKEN

> GET https://localhost/api/v1/:user/tweets
* Response
  ```json
  {
   "tweets":[
     {
      "id":"<TWEET_ID>",
      "owner":"<USER_OWNER>",
      "message":"<TWEET_MESSAGE>",
      "creation_timestamp":"<CREATION_TIMESTAMP>"
     },
     {
      "id":"<TWEET_ID>",
      "owner":"<USER_OWNER>",
      "message":"<TWEET_MESSAGE>",
      "creation_timestamp":"<CREATION_TIMESTAMP>"
     }
   ]
  }
  ```
  Status: 200

> POST https://localhost/api/v1/:user/tweets
* Request
  ```json
  {
   "message":"<TWEET_MESSAGE>",
  }
  ```
* Response \
  Status: 201


> DELETE https://localhost/api/v1/:user/tweets/:id
* Response \
  Status: 200

