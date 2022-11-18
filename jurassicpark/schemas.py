from xmlrpc.client import boolean
from pydantic import BaseModel
from pydantic import ValidationError

class Dinosaurio(BaseModel):
    nombre: str
    especie: str
    edad: int
    peso: float
    sexo: str
    es_agresivo: boolean
    recinto: str

class Especie(BaseModel):
    especie: str

class Todoterreno(BaseModel):
    codigo: int
    ruta: str
    pasajeros: int
    sis_seg: boolean
    recinto: str

class Recinto(BaseModel):
    nombre: str
    especie: str
    sis_elec: boolean
    dinosaurios: list[Dinosaurio] = []
    todoterrenos: list[Todoterreno] = []

