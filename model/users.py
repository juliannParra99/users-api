from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import String, Integer
from config.db import engine, meta_data

#aca se crea la tabla de la base de datos, junto con sus columnas.
users = Table('users', meta_data,
              Column('id', Integer,primary_key=True),
              Column('name',String(255),nullable= False),
              Column('username',String(255),nullable= False),
              Column('user_passw',String(255),nullable= False),)

#esto crea la tabla con los datos cargados en meta_data
meta_data.create_all(engine)