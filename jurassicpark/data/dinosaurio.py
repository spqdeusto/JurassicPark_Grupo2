from sqlalchemy import false


class Dinosaurio:
   
    def __init__(self,nombre,especie,edad,peso,sexo,es_agresivo,recinto):
       self.nombre = nombre
       self.especie = especie
       self.edad = edad
       self.peso = peso
       self.sexo = sexo
       self.es_agresivo = es_agresivo
       self.recinto = recinto

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getEspecie(self):
        return self.especie

    def setEspecie(self, especie):
        self.especie = especie
    
    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
        self.peso = peso

    def getSexo(self):
        return self.sexo

    def setSexo(self, sexo):
        self.sexo = sexo

    def getEs_agresivo(self):
        return self.es_agresivo

    def setEs_agresivo(self, es_agresivo):
        self.es_agresivo = es_agresivo

    def getRecinto(self):
        return self.recinto

    def setRecinto(self, recinto):
        self.recinto = recinto


