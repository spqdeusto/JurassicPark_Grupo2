import unittest
from jurassicpark import crud,schemas
from jurassicpark.database import local_SessionLocal


class testCase(unittest.TestCase):

    db : local_SessionLocal = local_SessionLocal()
    dinosaurioNuevo : schemas.Dinosaurio = schemas.Dinosaurio(nombre = "Prueba", especie = 1, edad = 100, peso = 200, sexo = "M", es_agresivo = True)
    dinosaurioNuevo2 : schemas.Dinosaurio = schemas.Dinosaurio(nombre = "Prueba2", especie = 1, edad = 100, peso = 200, sexo = "M", es_agresivo = True)
    todoterrenoNuevo : schemas.Todoterreno = schemas.Todoterreno(codigo = 98988, ruta = True , pasajeros = 2, sis_seg = False, recinto = 2)
    todoterrenoNuevo2 : schemas.Todoterreno = schemas.Todoterreno(codigo = 98989, ruta = True , pasajeros = 2, sis_seg = False, recinto = 2)


    def setUp(self):
        pass

    def tearDown(self):
        crud.delete_dinosaurio(self.db, self.dinosaurioNuevo.nombre)
        crud.delete_todoterreno(self.db, self.todoterrenoNuevo.codigo)
        self.db.close()
   
    def test_dinosaurio_create(self):
        crud.create_dinosaurio(self.db, self.dinosaurioNuevo)
        dinosaurioNuevoBD = crud.get_dinosaurio(self.db, self.dinosaurioNuevo.nombre)
        self.assertTrue(dinosaurioNuevoBD)
   
    def test_dinosaurio_modificar(self):
        pass
    
    def test_dinosaurio_delete(self):
         crud.create_dinosaurio(self.db, self.dinosaurioNuevo2)
         crud.delete_dinosaurio(self.db, self.dinosaurioNuevo2.nombre)
         dinosaurioEliminado = crud.get_dinosaurio(self.db, self.dinosaurioNuevo2.nombre)
         self.assertIsNone(dinosaurioEliminado)

    def test_todoterreno_create(self):
        crud.create_todoterreno(self.db, self.todoterrenoNuevo)
        todoterrenoNuevoBD = crud.get_todoterreno(self.db, self.todoterrenoNuevo.codigo)
        self.assertTrue(todoterrenoNuevoBD)
   
    def test_todoterreno_modificar(self):
        pass
    
    def test_todoterreno_delete(self):
         crud.create_todoterreno(self.db, self.todoterrenoNuevo2)
         crud.delete_todoterreno(self.db, self.todoterrenoNuevo2.codigo)
         todoterrenoEliminado = crud.get_todoterreno(self.db, self.todoterrenoNuevo2.codigo)
         self.assertIsNone(todoterrenoEliminado)
        
