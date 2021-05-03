from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, ProdutoSimples, Usuario
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.repositorios import RepositorioProduto, RepositorioUsuario

#criar_bd()

app = FastAPI()


@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=ProdutoSimples)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos', response_model=List[Produto])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos


#Remove o produto pelo id.
@app.delete('/produtos/{produto_id}', status_code=status.HTTP_200_OK)
def remover_produto(produto_id: str, db: Session=Depends(get_db)):
    remover = RepositorioProduto(db).remover_produto(produto_id)
    return remover


#Editar produtos.
@app.put('/produtos/{id}', response_model=ProdutoSimples)
def atualizar_produto(id: int, produto: Produto, session: Session = Depends(get_db)):
    RepositorioProduto(session).editar_produto(id, produto)
    produto.id = id
    return produto


#Cadastrar USUARIO
@app.post('/usuario', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuario(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar_user(usuario)
    return usuario_criado


#Lista os usuarios
@app.get('/usuario', response_model=List[Usuario])
def listar_usuario(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios