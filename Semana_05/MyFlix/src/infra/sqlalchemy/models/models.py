from sqlalchemy import Column, Integer, String
from src.infra.sqlalchemy.config.database import Base


class Serie(Base):
    __tablename__ = 'Cadastro'

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    ano = Column(String)
    genero = Column(String)
    qtd_temporadas = Column(String)


class Listar(Serie):
    id: Integer
    titulo: String