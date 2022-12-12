from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import engine, true
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal

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


### DINOSAURIOS ###        

@app.get("/dinosaurios", response_model=list[schemas.Dinosaurio])
async def get_dinosaurios(db: Session = Depends(get_db)):
    '''
    Método que devuelve una lista de dinosaurios.
    
        Parameters:
            db (Session): instancia de la BBDD
        
        Returns:
            Una lista de ``schemas.Dinosaurio``
            
    '''
    return crud.get_dinosaurios(db, limit=10)

@app.get("/dinosaurio/{nombre}", response_model=schemas.Dinosaurio)
async def get_dinosaurio(nombre: str, db: Session = Depends(get_db)):
    '''
    Método que devuelve el dinosaurio que corresponde al nombre que le pasamos como parámetro.
    
        Parameters:
            db (Session): instancia de la BBDD
            nombre (str): el nombre del dinosaurio que queremos obtener
        
        Returns:
            Un objeto de tipo ``schemas.Dinosaurio``
            
    '''
    return crud.get_dinosaurio(db, nombre=nombre)

@app.post("/dinosaurio/create", response_model=schemas.Dinosaurio)
async def create_dinosaurios(dinosaurio: schemas.Dinosaurio, db: Session = Depends(get_db)):
    '''
    Método que crea un objeto de tipo dinosaurio.
    
        Parameters:
            db (Session): instancia de la BBDD
            dinosaurio (``schemas.Dinosaurio``): el objeto de tipo dinosaurio que queremos insertar en la BBDD
        
        Returns:
            db_dinosaurio (``schemas.Dinosaurio``): una instancia del objeto de tipo ``schemas.Dinosaurio`` que hemos creado
            
    '''
    db_dinosaurio = crud.get_dinosaurio(db, nombre = dinosaurio.nombre)
    if db_dinosaurio:
        raise HTTPException(status_code=400, detail="Dinosaurio already registered")
    return crud.create_dinosaurio(db=db,dinosaurio=dinosaurio)

@app.delete("/dinosaurio/{nombre}")
async def delete_dinosaurio(nombre: str, db: Session = Depends(get_db)):
    '''
    Método que elimina un dinosaurios.
    
        Parameters:
            db (Session): instancia de la BBDD
            nombre (str): el nombre del dinosaurio que queremos eliminar de la BBDD
            
    '''
    crud.delete_dinosaurio(db, nombre=nombre)
    return {"message" : f"El dinosaurio {nombre} ha sido eliminado"}



### TODOTERRENOS ###

@app.get("/todoterrenos", response_model=list[schemas.Todoterreno])
async def get_todoterrenos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Método que devuelve una lista de todoterrenos.
    
        Parameters:
            db (Session): instancia de la BBDD
            limit  (int): número de todoterrenos devueltos
        
        Returns:
            Una lista de ``schemas.Todoterreno``
            
    '''
    return crud.get_todoterrenos(db, limit=limit)

@app.get("/todoterreno/{codigo}", response_model=schemas.Todoterreno)
async def get_todoterreno(codigo: int, db: Session = Depends(get_db)):
    '''
    Método que devuelve el todoterreno que corresponde al codigo que le pasamos como parámetro.
    
        Parameters:
            db (Session): instancia de la BBDD
            codigo (int): el codigo del todoterreno que queremos obtener
        
        Returns:
            Un objeto de tipo ``schemas.Todoterreno``
            
    '''
    return crud.get_todoterreno(db, codigo=codigo)

@app.post("/todoterreno/create", response_model=schemas.Todoterreno)
async def create_todoterrenos(todoterreno: schemas.Todoterreno, db: Session = Depends(get_db)):
    '''
    Método que crea un objeto de tipo todoterreno.
    
        Parameters:
            db (Session): instancia de la BBDD
            todoterreno (``schemas.Todoterreno``): el objeto de tipo todoterreno que queremos insertar en la BBDD
        
        Returns:
            db_todoterreno (``schemas.Todoterreno``): una instancia del objeto de tipo ``schemas.Todoterreno`` que hemos creado
            
    '''
    db_todoterreno = crud.get_todoterreno(db, codigo = todoterreno.codigo)
    if db_todoterreno:
        raise HTTPException(status_code=400, detail="Todoterreno already registered")
    return crud.create_todoterreno(db=db,todoterreno=todoterreno)

@app.get("/todoterreno/delete/{codigo}")
async def delete_todoterreno(codigo: int, db: Session = Depends(get_db)):
    '''
    Método que elimina un todoterreno.
    
        Parameters:
            db (Session): instancia de la BBDD
            codigo (int): el codigo del todoterreno que queremos eliminar de la BBDD
            
    '''
    crud.delete_todoterreno(db, codigo=codigo)
    return {"message" : f"El todoterreno {codigo} ha sido eliminado"}



### ESPECIES ###

@app.get("/especie/{especie}", response_model=schemas.Especie)
async def get_especie(especie: str, db: Session = Depends(get_db)):
    '''
    Método que devuelve la especie que corresponde a la especie que le pasamos como parámetro.
    
        Parameters:
            db (Session): instancia de la BBDD
            especie (str): el nombre de la especie de la especie que queremos obtener
        
        Returns:
            Un objeto de tipo ``schemas.Especie``
            
    '''
    return crud.get_epecie(db, especie=especie)



### RECINTOS ###

@app.get("/recintos", response_model=list[schemas.Recinto])
async def get_recintos(db: Session = Depends(get_db)):
    '''
    Método que devuelve una lista de recintos.
    
        Parameters:
            db (Session): instancia de la BBDD

        Returns:
            Una lista de ``schemas.Recintos``
            
    '''
    return crud.get_recintos(db)

@app.get("/recinto/{nombre}", response_model=schemas.Recinto)
async def get_recinto(nombre: str, db: Session = Depends(get_db)):
    '''
    Método que devuelve el recinto que corresponde a la especie que le pasamos como parámetro.
    
        Parameters:
            db (Session): instancia de la BBDD
            especie (int): codigo de especie de los dinosaurios que se encuentran en el recinto que queremos obtener
        
        Returns:
            Un objeto de tipo ``schemas.Recinto``
    '''
    return crud.get_recinto(db, nombre=nombre)

@app.get("/changeelectricidad/{especie}")
async def change_alarma(especie: int, db: Session = Depends(get_db)):
    crud.change_sis_elec(db, especie)
    crud.change_sis_seg(db)
    return {"success" : True}



### ALARMA ###

@app.get("/alarma")
async def get_alarma(db: Session = Depends(get_db)):
    return {"nivel": crud.check_alarma(db)}