from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_DATABASE_URL = "sqlite:///./olist.db"

engine = create_engine(
    SQL_DATABASE_URL, connect_args={"check_same_thread": False}
) # cria a conexção com o banco sqlite

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # cria a seção com o banco de dados

Base = declarative_base() # classe base para a criação dos schemas do banco de dados