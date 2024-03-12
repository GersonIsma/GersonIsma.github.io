from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: Optional[str]

@app.get("/")
def index():
    return {"message" : "Hola profe"}

@app.get("/libros")
def mostrar_libro(tituloLibro: Libro):
    return {"message": f"libro: {tituloLibro.titulo}, autor: {tituloLibro.autor}, paginas: {tituloLibro.paginas}"}

@app.post("/libros")
def insertar_libro(libro: Libro):
    return {"message": f"libro {libro.titulo} insertado"}