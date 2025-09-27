from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base é a classe base para todos os modelos
SQLALCHEMY_DATABASE_URL = "sqlite:///fast_car_api.db"

# Conexão com o banco de dados
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(
    # autocommit => commit automaticamente
    # autoflush => atualiza automaticamente
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_session():
    """
    Cria uma nova sessão de banco de dados.
    """
    session = SessionLocal()
    try:
        yield session  # Fica aguardando o uso da sessão
    finally:
        session.close()
