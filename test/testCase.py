import unittest
from jurassicpark import crud,schemas
from jurassicpark.database import local_SessionLocal


class testCase(unittest.TestCase):

    db : local_SessionLocal = local_SessionLocal()
    dinosaurioNuevo : schemas.Dinosaurio = schemas.Dinosaurio(nombre = "Prueba", especie = 1, edad = 100, peso = 200, sexo = "M", es_agresivo = True)

    def setUp(self):
        pass

    def tearDown(self):
        crud.delete_dinosaurio(self.db, self.dinosaurioNuevo.nombre)
        self.db.close()
   
    def test_dinosaurio_create(self):
        crud.create_dinosaurio(self.db, self.dinosaurioNuevo)
        dinosaurioNuevoBD = crud.get_dinosaurio(self.db, self.dinosaurioNuevo.nombre)
        self.assertTrue(dinosaurioNuevoBD)
   
    def test_dinosaurio_modificar(self):
        pass
    
    def test_dinosaurio_delete(self):
        pass
