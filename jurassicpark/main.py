from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import engine, true
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal

#models.Base.metadata.create_all(bind=engine)

# Para ejecutar servidor --> uvicorn JurasicPark:app --reload

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8081"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.post("/dinosaurio/create", response_model=schemas.Dinosaurio)
async def create_dinosaurios(dinosaurio: schemas.Dinosaurio, db: Session = Depends(get_db)):
    db_dinosaurio = crud.get_dinosaurio(db, nombre = dinosaurio.nombre)
    if db_dinosaurio:
        raise HTTPException(status_code=400, detail="Dinosaurio already registered")
    return crud.create_dinosaurio(db=db,dinosaurio=dinosaurio)

@app.get("/todoterrenos", response_model=list[schemas.Todoterreno])
async def get_todoterrenos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_todoterrenos(db, skip=skip, limit=limit)

@app.get("/todoterreno/{codigo}", response_model=schemas.Todoterreno)
async def get_todoterreno(codigo: int, db: Session = Depends(get_db)):
    return crud.get_todoterreno(db, codigo=codigo)

@app.post("/todoterreno/create", response_model=schemas.Todoterreno)
async def create_todoterrenos(todoterreno: schemas.Todoterreno, db: Session = Depends(get_db)):
    db_todoterreno = crud.get_todoterreno(db, codigo = todoterreno.codigo)
    if db_todoterreno:
        raise HTTPException(status_code=400, detail="Todoterreno already registered")
    return crud.create_todoterreno(db=db,todoterreno=todoterreno)

@app.get("/especie/{especie}", response_model=schemas.Especie)
async def get_especie(especie: str, db: Session = Depends(get_db)):
    return crud.get_epecie(db, especie=especie)

@app.get("/recintos", response_model=list[schemas.Recinto])
async def get_recintos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_recintos(db, skip=skip, limit=limit)

@app.get("/recinto/{nombre}", response_model=schemas.Recinto)
async def get_recinto(nombre: str, db: Session = Depends(get_db)):
    return crud.get_recinto(db, nombre=nombre)

@app.post("/recinto/create", response_model=schemas.Recinto)
async def create_especies(recinto: schemas.Recinto, db: Session = Depends(get_db)):
    db_recinto = crud.get_recinto(db, recinto = recinto.nombre)
    if db_recinto:
        raise HTTPException(status_code=400, detail="Recinto already registered")
    return crud.create_recinto(db=db,recinto=recinto)

@app.get("/changeelectricidad/{nombre}")
async def change_alarma(nombre: str, db: Session = Depends(get_db)):
    crud.change_sis_elec(db, nombre)
    return {"success" : True}

@app.get("/alarma")
async def get_alarma(db: Session = Depends(get_db)):
    return {"nivel": crud.check_alarma(db)}