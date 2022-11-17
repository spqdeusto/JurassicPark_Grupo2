class Todoterreno:

    def __init__(self,codigo,ruta,pasajeros,sis_seg,recinto):
        self.codigo = codigo
        self.ruta = ruta
        self.pasajeros = pasajeros
        self.sis_seg = sis_seg
        self.recinto = recinto

    def getCodigo(self):
        return self.codigo

    def setCodigo(self,codigo):
        self.codigo = codigo

    def getRuta(self):
        return self.ruta

    def setRuta(self,ruta):
        self.ruta = ruta

    def getPasajeros(self):
        return self.pasajeros

    def setPasajeros(self,pasajeros):
        self.pasajeros = pasajeros

    def getSis_seg(self):
        return self.sis_seg

    def setSis_seg(self,sis_seg):
        self.sis_seg = sis_seg

    def getRecinto(self):
        return self.recinto

    def setRecinto(self,recinto):
        self.recinto = recinto