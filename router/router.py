#en esta carpeta se van a establecer las distintas rutas
from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED,HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from schema.user_schema import UserSchema, DataUser
from config.db import engine
from model.users import users
#esto se va a utilizar para encriptar el password del usuario
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List

user = APIRouter()

@user.get('/')
def root():
    return {"message":"Hi, I'm fastApi with a router"}

#devuelve una lista con los valores de la db
@user.get('/api/user',response_model=List[UserSchema])
def get_users():
    with engine.connect() as conn:
        result = conn.execute(users.select()).fetchall()
        return result


#solicitud para pedir un unico usuario dependiendo su id.
#en este caso no va a devolvers una lista, sino un unico usuario, por lo que uso user schema
@user.get('/api/user/{user_id}',response_model=UserSchema)
def get_user(user_id: str):
    with engine.connect() as conn:
        #esto genera una consulta sql aqui, sin tener que escribir la consulta directamente
        result = conn.execute(users.select().where(users.c.id == user_id)).first()

        return result 






#el http:201 indica que algo fue creado ene l servidor; es util para la documentacion seguir los diversos codigos http
@user.post('/api/user', status_code=HTTP_201_CREATED)
def create_user(data_user: UserSchema):
    #with garantiza que constantemente se este cerrando nuestra conexion a la db para que no consuma tanto rendimiento.: es buena practica a la hora de realizar conexiones a db
    with engine.connect() as conn:
        new_user = data_user.dict()
        new_user["user_passw"] = generate_password_hash(data_user.user_passw,'pbkdf2:sha256:30',30)
        
        print(new_user)

        conn.execute(users.insert().values(new_user))

        #va a retornar el status code cuando todo se cumpla como respuesta
        return Response(status_code=HTTP_201_CREATED)
    
#ruta que va a comparar usuarios y constraseñas y verificar si el usuario realmente existe dentro de nuestra DB: Pero en la actualidad hay mejores maneras de realizar esto emdiante los tokens de json que permite hacer un logeo mas seguro.
@user.post('api/user/login', status_code=200)
def user_login(data_user:DataUser):
    with engine.connect() as conn:
        #aca vamos a verificar si el 'username' que esta en nuestra DB como columna, coincide con el user_name que esta pasando el usuario, para ver si existe o no
        result = conn.execute(users.select().where(users.c.username == data_user.user_name)).first()

        if result != None:
        #check_password_hash devuelve un bool
            check_passw = check_password_hash(result[3], data_user.user_passw)
            #si check_passw da true, osea si coincidieron los valores.
            if check_passw:
                return {
                    "status": 200,
                    "message": "Access success"
                }
            return {
                    "status": HTTP_401_UNAUTHORIZED,
                    "message": "Access success"
                }




    
@user.put('api/user/{user_id}',response_model=UserSchema)
def update_user(data_update:UserSchema,user_id:str):
    with engine.connect() as conn:
        #aqui estamos encriptando el password que se pasa.
        encryp_passw = generate_password_hash(data_update.user_passw, 'pbkdf2:sha256:30',30)
        #aqui estamos actualizando los valores en nuestra DB
        conn.execute(users.update().values(name= data_update.name ,username= data_update.username,user_passw= encryp_passw).where(users.c.id == user_id))

        #aca mostramos el usuario que se acaba de actualizar para devolverlo
        result = conn.execute(users.select().where(users.c.id == user_id)).first()

        return result
    
@user.delete('api/user/{user_id}',status_code=HTTP_204_NO_CONTENT)
def delete_user(user_id:str):
    with engine.connect() as conn:
        conn.execute(users.delete().where(users.c.id == user_id))

        return Response(status_code=HTTP_204_NO_CONTENT)

