from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import engine, true
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal

#models.Base.metadata.create_all(bind=engine)

# Para ejecutar servidor --> uvicorn JurasicPark:app --reload

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "myresult"}

@app.get("/dinosaurios", response_model=list[schemas.Dinosaurio])
async def get_dinosaurios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_dinosaurios(db, skip=skip, limit=limit)

@app.get("/dinosaurio/{nombre}", response_model=schemas.Dinosaurio)
async def get_dinosaurio(nombre: str, db: Session = Depends(get_db)):
    return crud.get_dinosaurio(db, nombre=nombre)

"""@app.post("/dinosaurio/create", response_model=schemas.DinosaurioCreate)
async def create_dinosaurios(dinosaurio: schemas.DinosaurioCreate, db: Session = Depends(get_db)):
    db_dinosaurio = crud.get_dinosaurio_by_nombre(db, nombre = dinosaurio.nombre)
    if db_dinosaurio:
        raise HTTPException(status_code=400, detail="Dinosaurio already registered")
    return crud.create_dinosaurio(db=db,dinosaurio=dinosaurio)"""

@app.get("/todoterrenos", response_model=list[schemas.Todoterreno])
async def get_todoterrenos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_todoterrenos(db, skip=skip, limit=limit)

@app.get("/todoterreno/{codigo}", response_model=schemas.Todoterreno)
async def get_todoterreno(codigo: int, db: Session = Depends(get_db)):
    return crud.get_todoterreno(db, codigo=codigo)

"""@app.post("/todoterreno/create", response_model=schemas.TodoterrenoCreate)
async def create_todoterrenos(todoterreno: schemas.TodoterrenoCreate, db: Session = Depends(get_db)):
    db_todoterreno = crud.get_todoterreno_by_codigo(db, codigo = todoterreno.codigo)
    if db_todoterreno:
        raise HTTPException(status_code=400, detail="Todoterreno already registered")
    return crud.create_todoterreno(db=db,todoterreno=todoterreno)"""

@app.get("/especie/{especie}", response_model=schemas.Especie)
async def get_especie(especie: str, db: Session = Depends(get_db)):
    return crud.get_epecie(db, especie=especie)

"""@app.post("/especie/create", response_model=schemas.EspecieCreate)
async def create_especies(especie: schemas.EspecieCreate, db: Session = Depends(get_db)):
    db_especie = crud.get_especie_by_especie(db, especie = especie.especie)
    if db_especie:
        raise HTTPException(status_code=400, detail="Especie already registered")
    return crud.create_especie(db=db,especie=especie)"""

@app.get("/recintos", response_model=list[schemas.Recinto])
async def get_recintos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_recintos(db, skip=skip, limit=limit)

@app.get("/recinto/{nombre}", response_model=schemas.Recinto)
async def get_recinto(nombre: str, db: Session = Depends(get_db)):
    return crud.get_recinto(db, nombre=nombre)

"""@app.post("/recinto/create", response_model=schemas.RecintoCreate)
async def create_especies(recinto: schemas.RecintoCreate, db: Session = Depends(get_db)):
    db_recinto = crud.get_recinto_by_nombre(db, recinto = recinto.nombre)
    if db_recinto:
        raise HTTPException(status_code=400, detail="Recinto already registered")
    return crud.create_recinto(db=db,recinto=recinto)"""

@app.get("/alarma")
async def get_alarma(db: Session = Depends(get_db)):
    return {"nivel": crud.check_alarma(db)}