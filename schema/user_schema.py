#aca voy a crear el esquema para utilizarlo en router.py
from pydantic import BaseModel
from typing import Optional

# aca voy a crear el schema de como quiero que se esctructuren los datos que pasan hacia el servidor; el id se va a autogenrar,para que cada  fila tenga un identificador

#el id se va  autogenerar, y va a ser un primary key(definido en users.py)
#se importa typing para poder solicitar el id del usuario pero que genere la primary key, es decir, el usuario no tiene que generarlo sino que se autogenera
class UserSchema(BaseModel):
    id: Optional[str]
    name: str
    username: str
    passw: str
    
