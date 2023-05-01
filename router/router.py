#en esta carpeta se van a establecer las distintas rutas
from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED
from schema.user_schema import UserSchema
from config.db import conn
from model.users import users
#esto se va a utilizar para encriptar el password del usuario
from werkzeug.security import generate_password_hash, check_password_hash

user = APIRouter()

@user.get('/')
def root():
    return {"message":"Hi, I'm fastApi with a router"}

#el http:201 indica que algo fue creado ene l servidor; es util para la documentacion seguir los diversos codigos http
@user.post('/api/user', status_code=HTTP_201_CREATED)
def create_user(data_user: UserSchema):
    
    new_user = data_user.dict()
    #el generate_password_hash recibe dos parametros: el texto que queremos codificar primero, y el seguindo el metodo de encriptacion, y la fuerza de codificacion .
    new_user["user_passw"] = generate_password_hash(data_user.user_passw,'pbkdf2:sha256:30',30)
    
    print(new_user)

    # conn.execute(users.insert().values(new_user))

    #va a retornar el status code cuando todo se cumpla como respuesta
    return Response(status_code=HTTP_201_CREATED)
    