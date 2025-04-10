# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Reemplaza estos datos por los de tu base de datos
DATABASE_URL = "mysql+pymysql://cliente_user:claveFlastapi@localhost/clientesdb"


engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
    