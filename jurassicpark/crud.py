from sqlalchemy.orm import Session

from . import models, schemas


### DINOSAURIOS ###

def get_dinosaurios(db: Session, limit: int = 100) -> list[models.Dinosaurio]:
    '''
    Método que devuelve una lista de dinosaurios.
    
        Parameters:
            db (Session): instancia de la BBDD
            limit  (int): número de dinosaurios devueltos
        
        Returns:
            Una lista de ``models.Dinosaurio``
            
    '''
    return db.query(models.Dinosaurio).limit(limit).all()

def get_dinosaurio(db: Session, nombre: str) -> models.Dinosaurio:
    '''
    Método que devuelve el dinosaurio que corresponde al nombre que le pasamos como parámetro.
    
        Parameters:
            db (Session): instancia de la BBDD
            nombre (str): el nombre del dinosaurio que queremos obtener
        
        Returns:
            Un objeto de tipo ``models.Dinosaurio``
            
    '''
    return db.query(models.Dinosaurio).filter(models.Dinosaurio.nombre == nombre).first()

def create_dinosaurio(db: Session, dinosaurio: schemas.Dinosaurio) -> models.Dinosaurio:
    '''
    Método que crea un objeto de tipo dinosaurio.
    
        Parameters:
            db (Session): instancia de la BBDD
            dinosaurio (``schemas.Dinosaurio``): el objeto de tipo dinosaurio que queremos insertar en la BBDD
        
        Returns:
            db_dinosaurio (``models.Dinosaurio``): una instancia del objeto de tipo ``models.Dinosaurio`` que hemos creado
            
    '''
    db_dinosaurio = models.Dinosaurio(nombre = dinosaurio.nombre, especie = dinosaurio.especie, edad = dinosaurio.edad, peso = dinosaurio.peso, sexo = dinosaurio.sexo, es_agresivo = dinosaurio.es_agresivo)
    db.add(db_dinosaurio)
    db.commit()
    db.refresh(db_dinosaurio)
    return db_dinosaurio

def delete_dinosaurio(db: Session, nombre: str):
    '''
    Método que elimina un dinosaurios.
    
        Parameters:
            db (Session): instancia de la BBDD
            nombre (str): el nombre del dinosaurio que queremos eliminar de la BBDD
            
    '''
    db.query(models.Dinosaurio).filter(models.Dinosaurio.nombre == nombre).delete()
    db.commit()

    

### TODOTERRENOS ###

def get_todoterrenos(db: Session, limit: int = 100) -> list[models.Todoterreno]:
    '''
    Método que devuelve una lista de todoterrenos.
    
        Parameters:
            db (Session): instancia de la BBDD
            limit  (int): número de todoterrenos devueltos
        
        Returns:
            Una lista de ``models.Todoterreno``
            
    '''
    return db.query(models.Todoterreno).limit(limit).all()

def get_todoterreno(db: Session, codigo: int) -> models.Todoterreno:
    '''
    Método que devuelve el todoterreno que corresponde al codigo que le pasamos como parámetro.
    
        Parameters:
            db (Session): instancia de la BBDD
            codigo (int): el codigo del todoterreno que queremos obtener
        
        Returns:
            Un objeto de tipo ``models.Todoterreno``
            
    '''
    return db.query(models.Todoterreno).filter(models.Todoterreno.codigo == codigo).first()

def create_todoterreno(db: Session, todoterreno: schemas.Todoterreno) -> models.Todoterreno:
    '''
    Método que crea un objeto de tipo todoterreno.
    
        Parameters:
            db (Session): instancia de la BBDD
            todoterreno (``schemas.Todoterreno``): el objeto de tipo todoterreno que queremos insertar en la BBDD
        
        Returns:
            db_todoterreno (``models.Todoterreno``): una instancia del objeto de tipo ``models.Todoterreno`` que hemos creado
            
    '''
    db_todoterreno = models.Todoterreno(codigo = todoterreno.codigo, ruta = todoterreno.ruta, pasajeros = todoterreno.pasajeros, sis_seg = todoterreno.sis_seg, recinto = todoterreno.recinto)
    db.add(db_todoterreno)
    db.commit()
    db.refresh(db_todoterreno)
    return db_todoterreno

def change_sis_seg(db: Session) -> None:
    '''
    Método que comprueba el nivel de alarma y activa/desactiva automáticamente el sistema de seguridad de todos los todoterrenos.
    
        Parameters:
            db (Session): instancia de la BBDD
    '''
    nivel = check_alarma(db)
    if nivel >= 2:
        for todoterreno in get_todoterrenos(db, 0, 100):
            todoterreno.sis_seg = True
    else:
        for todoterreno in get_todoterrenos(db, 0, 100):
            todoterreno.sis_seg = False

    db.commit()

def delete_todoterreno(db: Session, codigo: int) -> None:
    '''
    Método que elimina un todoterreno.
    
        Parameters:
            db (Session): instancia de la BBDD
            codigo (int): el codigo del todoterreno que queremos eliminar de la BBDD
            
    '''
    db.query(models.Todoterreno).filter(models.Todoterreno.codigo == codigo).delete()
    db.commit()

    

### ESPECIES ###

def get_epecie(db: Session, especie: str):
    '''
    Método que devuelve la especie que corresponde a la especie que le pasamos como parámetro.
    
        Parameters:
            db (Session): instancia de la BBDD
            especie (str): el nombre de la especie de la especie que queremos obtener
        
        Returns:
            Un objeto de tipo ``models.Especie``
            
    '''
    return db.query(models.Especie).filter(models.Especie.especie == especie).first()



### RECINTOS ###

def get_recintos(db: Session) -> list[models.Recinto]:
    '''
    Método que devuelve una lista de recintos.
    
        Parameters:
            db (Session): instancia de la BBDD

        Returns:
            Una lista de ``models.Recintos``
            
    '''
    return db.query(models.Recinto).all()

def get_recinto(db: Session, especie: int) -> models.Recinto:
    '''
    Método que devuelve el recinto que corresponde a la especie que le pasamos como parámetro.
    
        Parameters:
            db (Session): instancia de la BBDD
            especie (int): codigo de especie de los dinosaurios que se encuentran en el recinto que queremos obtener
        
        Returns:
            Un objeto de tipo ``models.Recinto``
    '''
    return db.query(models.Recinto).filter(models.Recinto.especie == especie).first()

def change_sis_elec(db: Session, especie: int) -> None:
    '''
    Método que activa y desactiva el sistema eléctrico de un recinto según su especie
    
        Parameters:
            db (Session): instancia de la BBDD
            especie (int): codigo de especie del recinto
    '''
    recinto = get_recinto(db, especie)
    recinto.sis_elec = not recinto.sis_elec
    db.commit()



### ALARMA ###

def check_alarma(db: Session) -> int:
    '''
    Método que comprueba el nivel de alerta del parque.
     - Alerta máxima: El sistema eléctrico de alguno de los dinosaurios "agresivos" falla y hay jeeps en ruta.
     - Alerta media: El sistema eléctrico de alguno de los dinosaurios "agresivos" falla.
     - Alerta baja: El sistema eléctrico de alguno de los dinosaurios "pacíficos" falla.

        Parameters:
                db (Session): instancia de la BBDD
        Returns:
            ``3``: Alerta máxima
            ``2``: Alerta media
            ``1``: Alerta baja
            ``0``: Sin alerta
    '''
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


