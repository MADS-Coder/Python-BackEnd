from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI()

origins = ['http://localhost:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    for animal in bd_animais:
        if animal.id == id:
            return {'mensagem': f'{animal.nome} localizado com sucesso!.'}


@app.delete('/animais/{id}')
def remover_animais(id: str):
    ia = -1
    for i, animal in enumerate(bd_animais):
        print(animal.id, id)
        if animal.id == id:
            ia = i
            break

    if ia != -1:
        bd_animais.pop(ia)
        return {'mensagem': f'Animal {animal.nome} removido com sucesso!'}
    else:
        return {'mensagem': f'Não foi possível localizar o animal com o id {id}'}

