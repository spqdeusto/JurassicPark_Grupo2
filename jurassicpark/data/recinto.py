from sqlalchemy import false
from jurassicpark.models import Especie


class Recinto:
   
    def __init__(self,nombre,especie,sis_elec,dinosaurios,todoterrenos):
        self.nombre = nombre
        self.especie = especie
        self.sis_elec = sis_elec
        self.dinosaurios = dinosaurios
        self.todoterrenos = todoterrenos

    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        self.nombre = nombre

    def getEspecie(self):
        return self.especie

    def setEspecie(self,especie):
        self.especie = especie

    def getSis_elec(self):
        return self.sis_elec

    def setSis_elec(self,sis_elec):
        self.sis_elec = sis_elec

    def getDinosaurios(self):
        return self.dinosaurios

    def setDinosaurios(self,dinosaurios):
        self.dinosaurios = dinosaurios

    def getTodoterrenos(self):
        return self.todoterrenos

    def setTodoterrenos(self,todoterrenos):
        self.todoterrenos = todoterrenos

    def addDinosaurioRecinto(self,dinosaurio):
        self.dinosaurios.append(dinosaurio)

    def removeDinosaurioRecinto(self,dinosaurio):
        self.dinosaurios.remove(dinosaurio)

    def addTodoterrenoRecinto(self,todoterreno):
        self.todoterrenos.append(todoterreno)

    def removeTodoterrenoRecinto(self,todoterreno):
        self.todoterrenos.remove(todoterreno)
   
