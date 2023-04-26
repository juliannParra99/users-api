#en esta carpeta se van a establecer las distintas rutas
from fastapi import APIRouter
from schema.user_schema import UserSchema

user = APIRouter()

@user.get('/')
def root():
    return {"message":"Hi, I'm fastApi with a router"}


@user.post('api/user')
def create_user(data_user: UserSchema):
    print(data_user) 
    