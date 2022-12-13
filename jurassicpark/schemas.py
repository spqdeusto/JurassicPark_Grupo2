from pydantic import BaseModel
from pydantic import ValidationError

class Dinosaurio(BaseModel):
    nombre: str
    especie: int
    edad: int
    peso: int
    sexo: str

    class Config:
        orm_mode = True
class Especie(BaseModel):
    id: int
    especie: str
    es_agresivo: bool 
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

    class Config:
        orm_mode = True


