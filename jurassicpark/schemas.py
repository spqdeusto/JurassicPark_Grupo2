from pydantic import BaseModel
from pydantic import ValidationError

class Dinosaurio(BaseModel):
    nombre: str
    especie: int
    edad: int
    peso: int
    sexo: str
    es_agresivo: bool 

    class Config:
        orm_mode = True
class Especie(BaseModel):
    id: int
    especie: str
    recinto: int
class Todoterreno(BaseModel):
    codigo: int
    ruta: bool
    pasajeros: int
    sis_seg: bool
    recinto: int

    class Config:
        orm_mode = True
class Recinto(BaseModel):
    codigo: int
    nombre: str
    sis_elec: bool
    especies: list[Especie] = []
    todoterrenos: list[Todoterreno] = []

    class Config:
        orm_mode = True


