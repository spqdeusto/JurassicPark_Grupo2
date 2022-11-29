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
    especie: str
class Todoterreno(BaseModel):
    codigo: int
    ruta: str
    pasajeros: int
    sis_seg: bool
    recinto: str

    class Config:
        orm_mode = True
class Recinto(BaseModel):
    codigo: int
    nombre: str
    especie: str
    sis_elec: bool
    todoterrenos: list[Todoterreno] = []

    class Config:
        orm_mode = True


