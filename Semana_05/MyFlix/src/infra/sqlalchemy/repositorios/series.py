from sqlalchemy.orm import Session
from sqlalchemy import delete
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class Respositoriocadastro():

    def __init__(self, db: Session):
        self.db = db

    
    def criar(self, cadastro: schemas.Serie):
        db_cadastro = models.Serie(titulo=cadastro.titulo, ano=cadastro.ano,
                                        genero=cadastro.genero, qtd_temporadas=cadastro.qtd_temporadas)

        self.db.add(db_cadastro)
        self.db.commit()
        self.db.refresh(db_cadastro)
        return db_cadastro


    def listar(self):
        cadastro = self.db.query(models.Serie).all()
        return cadastro

    
    def exibir_por_id(self, id):
        exibir = self.db.query(models.Listar).filter(
            models.Listar.id == id
        ).first()
        return exibir


    def listar_titulo(self, titulo):
        exibir = self.db.query(models.Listar).filter(
            models.Listar.titulo == titulo
        ).first()
        return exibir


    #A função abaixo remove uma série de acordo com o ID informado, atráves do "operador morsa", a variável (exibir) recebe parte da expressão (função) (exibit_por_id).
    #Que realiza a seguinte função, com o banco de dados realiza a consulta via (query) passado como argumento o modelo Listar (models.Listar), é aplicado o método (filter()) que seleciona apenas os registros corretos de acordo com o ID informado e recebe como argumento o modelo listar buscando somente o ID e comparando com o informado no request, e por fim é aplicado o método (first()) que retorna a primeira ocorrência do registro correto selecionado pelo método (filter()).
    def remover_serie(self, id):
        exibir = self.db.query(models.Listar)
        if exibir := exibir.filter(
            models.Listar.id == id
            ).first():
            self.db.delete(exibir)
            self.db.commit()
            return {'Mensagem': f'Serie {exibir.titulo} removida com sucesso!.'} 
        return {'Mensagem': f'Serie {id} não encontrada!.'}
