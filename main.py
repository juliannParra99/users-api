from fastapi import FastAPI
from router.router import user

app = FastAPI()

#importa las rutas de la carpeta router
app.include_router(user)