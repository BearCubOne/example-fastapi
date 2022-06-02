from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings


# SQLALCHEMY_DATABASE_URL = 'postgresql://bierhe:bSmg8vXk6iLlxmSLivz7@gima-postgres.so.kadaster.nl:49187/gima'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         # conn = psycopg2.connect(host='gima-postgres.so.kadaster.nl', port='49187', database ='gima', user='bierhe', password='bSmg8vXk6iLlxmSLivz7', cursor_factory=RealDictCursor)
#         conn = psycopg2.connect(host='localhost', port='49153', database ='fastapi', user='postgres', password='postgrespw', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesfull!")
#         break
#     except Exception as error:
#         print("connection to database failed")
#         print("error: ", error)
#         time.sleep(2)