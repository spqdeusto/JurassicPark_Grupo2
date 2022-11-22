from sqlalchemy.orm import Session

from . import models, schemas


def get_dinosaurio(db: Session, nombre: str):
    return db.query(models.Dinosaurio).filter(models.Dinosaurio.nombre == nombre).first()

def get_todoterreno(db: Session, codigo: int):
    return db.query(models.Todoterreno).filter(models.Todoterreno.codigo == codigo).first()

def get_epecie(db: Session, especie: str):
    return db.query(models.Especie).filter(models.Especie.especie == especie).first()

def get_recinto(db: Session, nombre: str):
    return db.query(models.Recinto).filter(models.Recinto.nombre == nombre).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
