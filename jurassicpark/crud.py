from sqlalchemy.orm import Session

from . import models, schemas

def get_dinosaurios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Dinosaurio).offset(skip).limit(limit).all()

def get_dinosaurio(db: Session, nombre: str):
    return db.query(models.Dinosaurio).filter(models.Dinosaurio.nombre == nombre).first()

def get_todoterrenos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todoterreno).offset(skip).limit(limit).all()

def get_todoterreno(db: Session, codigo: int):
    return db.query(models.Todoterreno).filter(models.Todoterreno.codigo == codigo).first()

def get_epecie(db: Session, especie: str):
    return db.query(models.Especie).filter(models.Especie.especie == especie).first()

def get_recintos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Recinto).offset(skip).limit(limit).all()

def get_recinto(db: Session, nombre: str):
    return db.query(models.Recinto).filter(models.Recinto.nombre == nombre).first()

def check_alarma(db: Session):
    db_max = db.query(models.Recinto).filter_by(sis_elec = False).\
            join(models.Recinto.todoterrenos).filter_by(ruta = True).\
            join(models.Recinto.dinosaurios).filter_by(es_agresivo = True).first()
    if db_max != None:
        return 3
    
    db_mid = db.query(models.Recinto).filter_by(sis_elec = False).\
            join(models.Recinto.dinosaurios).filter_by(es_agresivo = True).first()
    if db_mid != None:
        return 2
    
    db_low = db.query(models.Recinto).filter_by(sis_elec = False).\
            join(models.Recinto.dinosaurios).filter_by(es_agresivo = False).first()
    print(db_low)
    if db_low != None:
        return 1
    
    return 0

def get_dinosaurio_by_nombre(db: Session, nombre: str):
    return db.query(models.Dinosaurio).filter(models.Dinosaurio.nombre == nombre).first

def get_recinto_by_nombre(db: Session, nombre: str):
    return db.query(models.Recinto).filter(models.Recinto.nombre == nombre).first

def get_especie_by_especie(db: Session, especie: str):
    return db.query(models.Especie).filter(models.Especie.especie == especie).first

def get_todoterreno_by_codigo(db: Session, codigo: int):
    return db.query(models.Todoterreno).filter(models.Todoterreno.codigo == codigo).first


def create_dinosaurio(db: Session, dinosaurio: schemas.DinosaurioCreate):
    db_dinosaurio = models.Dinosaurio(nombre = dinosaurio.nombre, especie = dinosaurio.especie, edad = dinosaurio.edad, peso = dinosaurio.peso, sexo = dinosaurio.sexo, es_agresivo = dinosaurio.es_agresivo, recinto = dinosaurio.recinto)
    db.add(db_dinosaurio)
    db.commit()
    db.refresh(db_dinosaurio)
    return db_dinosaurio

def create_especie(db: Session, especie: schemas.EspecieCreate):
    db_especie = models.Especie(id = especie.id, especie = especie.especie)
    db.add(db_especie)
    db.commit()
    db.refresh(db_especie)
    return db_especie

def create_recinto(db: Session, recinto: schemas.RecintoCreate):
    db_recinto = models.Recinto(nombre = recinto.nombre, especie = recinto.especie, sis_elec = recinto.sis_elec, dinosaurios = recinto.dinosaurios, todoterrenos = recinto.todoterrenos)
    db.add(db_recinto)
    db.commit()
    db.refresh(db_recinto)
    return db_recinto

def create_todoterreno(db: Session, todoterreno: schemas.TodoterrenoCreate):
    db_todoterreno = models.Todoterreno(codigo = todoterreno.codigo, ruta = todoterreno.ruta, pasajeros = todoterreno.pasajeros, sis_seg = todoterreno.sis_seg, recinto = todoterreno.recinto)
    db.add(db_todoterreno)
    db.commit()
    db.refresh(db_todoterreno)
    return db_todoterreno