from sqlalchemy.orm import Session
from sqlalchemy import delete, update, select
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioProduto():

    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(nome=produto.nome,
                                    detalhes=produto.detalhes,
                                    preco=produto.preco,
                                    disponivel=produto.disponivel,
                                    usuario_id=produto.usuario_id
                                    )
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto
               

    def editar_produto(self, produto_id: int, produto: schemas.Produto):
        update_stmt = update(models.Produto).where(models.Produto.id == produto_id).values(nome=produto.nome, detalhes=produto.detalhes, preco=produto.preco, disponivel=produto.disponivel)
        self.db.execute(update_stmt)
        self.db.commit()
        

    def listar(self):
        produtos = self.db.query(models.Produto).all()
        return produtos


    def remover_produto(self, id_produto):
        exibir = self.db.query(models.Produto)
        if exibir := exibir.filter(
            models.Produto.id == id_produto
            ).first():
            self.db.delete(exibir)
            self.db.commit()
            return {'Mensagem': f'Produto {exibir.nome} removido com sucesso!.'}
        return {'Mensagem': f'Produto {id} não encontrado!.'}


class RepositorioUsuario():
    
    def __init__(self, db: Session):
        self.db = db


    def criar_user(self, usuario: schemas.Usuario):
        db_usuario = models.Usuario(nome=usuario.nome, senha=usuario.senha, telefone=usuario.telefone)
        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario
    

    def listar(self):
        stmt = select(models.Usuario)
        usuarios = self.db.execute(stmt).scalars().all()
        return usuarios
