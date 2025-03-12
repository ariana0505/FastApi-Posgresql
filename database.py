# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión a la base de datos PostgreSQL
DATABASE_URL = "postgresql://alvaro:alvaro@localhost:5459/course_db"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Crear una sesión local para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()