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

    """def create_dinosaurio(db: Session, dinosaurio: schemas.Dinosaurio):
    db_dinosaurio = models.Dinosaurio(nombre = dinosaurio.nombre, especie = dinosaurio.especie, edad = dinosaurio.edad, peso = dinosaurio.peso, sexo = dinosaurio.sexo, es_agresivo = dinosaurio.es_agresivo, recinto = dinosaurio.recinto)
    db.add(db_dinosaurio)
    db.commit()
    db.refresh(db_dinosaurio)
    return db_dinosaurio"""
