from pydantic import BaseModel
from typing import Optional, List


class Cadastrar(BaseModel):
    id: Optional[str] = None
    titulo: str
    ano: str
    genero: str
    qtd_temporadas: str

    class Config:
        orm_mode = True


class Listar(BaseModel):
    id: Optional[str] = None
    titulo: str

    class Config:
        orm_mode = True