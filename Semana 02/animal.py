from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI()

class Animal(BaseModel):
    id: Optional[str]
    nome: str
    idade: int
    sexo: str
    cor: str

bd_animais: List[Animal] = []

@app.post('/animais')
def cadastrar(animais: Animal):
    animais.id = str(uuid4())
    bd_animais.append(animais)
    return animais



@app.get('/animais')
def lista_animais():
    return bd_animais



@app.get('/animais/{id}')
def animal_id(id: str):
    indice = -1
    for i, animais in enumerate(bd_animais):
        if animais.id == indice:
            indice = i
            break
    return {'mensagem': f'{animais.nome} localizado com sucesso!.'}



@app.delete('/animais/{id}')
def remover_animais(id: str):
    ia = -1
    for i, animais in enumerate(bd_animais):
        print(animais.id, id)
        if animais.id == id:
            ia = i
            break

    if ia != -1:
        bd_animais.pop(ia)
        return {'mensagem': f'Animal {animais.nome} removido com sucesso!'}
    else:
        return {'mensagem': f'Não foi possível localizar o animal com o id {id}'}

