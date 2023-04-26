#aca se crea la conexion a la db

from sqlalchemy import create_engine, MetaData

#se crea conexion a la db: create_engine, toma comoa rgumentos mi usuario y la db
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# conn = engine.connect()

meta_data = MetaData()