from fastapi import FastAPI
from pydantic import BaseModel
from router import dias
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#rutas
app.include_router(dias.router)

#autorizar uso de carpetas y archivos estaticos
app.mount('/assets', StaticFiles(directory="assets"), name= 'assets')

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

@app.post('/usuario')
async def post_usuario(usuario: Usuario):
    lista_usuarios.append(usuario)
    return usuario