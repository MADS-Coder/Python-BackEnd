from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Serie
from src.infra.sqlalchemy.config.database import get_banco_dados, criar_banco_dados
from src.infra.sqlalchemy.repositorios.series import Respositoriocadastro


criar_banco_dados()

app = FastAPI()

#Envia os dados via JSON.
@app.post('/cadastros')
def criar_cadastro(cadastro: Serie, db: Session = Depends(get_banco_dados)):
    cadastro_criado = Respositoriocadastro(db).criar(cadastro)
    return cadastro_criado

#Realiza a busca dos dados cadastrados.
@app.get('/cadastros')
def listar_cadastros(db: Session = Depends(get_banco_dados)):
    cadastros = Respositoriocadastro(db).listar()
    return cadastros


#Realiza a busca dos dados cadastrados pelo TITULO.
@app.get('/cadastros/{titulo}')
def listar_por_titulo(titulo: str, db: Session = Depends(get_banco_dados)):
    serie = Respositoriocadastro(db).listar_titulo(titulo)
    return serie


#Atualiza a busca dos dados cadastrados pelo ID.
@app.put('/cadastros/{id}')
def listar_por_id(id: str, db: Session = Depends(get_banco_dados)):
    serie = Respositoriocadastro(db).exibir_por_id(id)
    return serie


@app.delete('/cadastros/{id}')
def remover(id: str, db: Session = Depends(get_banco_dados)):
    remover_serie = Respositoriocadastro(db).remover_serie(id)
    return remover_serie