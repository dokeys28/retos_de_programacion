from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class Usuario(BaseModel):
    nombre: str
    edad: int
    

lista_usuarios = [Usuario(nombre ='Luis', edad = 28),
                  Usuario(nombre ='Rosa', edad = 57)]


@app.get('/')
async def home():
    return 'Hola'

@app.get('/usuarios')
async def get_usuarios():
    return lista_usuarios

@app.get('/usuario/{nombre}')
async def get_usuario(nombre):
    for usuario in lista_usuarios:
        if usuario.nombre == nombre:
            return usuario

@app.post('/usuario/{nombre},{edad}')
async def post_usuario(nombre, edad):
    usuario = Usuario(nombre= nombre, edad= edad)
    lista_usuarios.append(usuario)
    return usuario