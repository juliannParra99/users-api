#aca voy a crear el esquema de mi db para utilizarlo en router.py
from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id: Optional[str]
    name: str
    username: str
    passw: str
    
