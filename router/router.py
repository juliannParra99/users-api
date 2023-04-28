#en esta carpeta se van a establecer las distintas rutas
from fastapi import APIRouter
from schema.user_schema import UserSchema
from config.db import conn
from model.users import users

user = APIRouter()

@user.get('/')
def root():
    return {"message":"Hi, I'm fastApi with a router"}


@user.post('/api/user')
def create_user(data_user: UserSchema):
    # print(data_user) 

    #guardo los datos de data_user en formato dictionario, para poder acceder a los datos por medio de la clave-valor
    new_user = data_user.dict()


    #aca se van  a pasar los datos que se pasan por parametro a nuestra base de datos, por lo que creamos una conexion, importando de config.db 'conn'

    print(new_user)
    # conn.execute(users.insert().values(new_user))

    return 'Success!'
    