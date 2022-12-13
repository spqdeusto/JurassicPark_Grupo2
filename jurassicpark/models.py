from sqlalchemy import Boolean, CheckConstraint, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base, local_engine

class Especie(Base):
    __tablename__ = "especie"

    id = Column(Integer, primary_key=True)
    especie = Column(String(25), nullable=False)
    es_agresivo = Column(Boolean(create_constraint=True), nullable=False)
    recinto = Column(Integer, ForeignKey("recinto.codigo", ondelete="CASCADE"))

class Dinosaurio(Base):
    __tablename__ = "dinosaurio"

    nombre = Column(String(100), primary_key=True)
    especie = Column(Integer, ForeignKey("especie.id", ondelete="CASCADE"), nullable=False)
    edad = Column(Integer)
    peso = Column(Integer)
    sexo = Column(String(2))


class Recinto(Base):
    __tablename__ = "recinto"

    codigo = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    sis_elec = Column(Boolean(create_constraint=True), nullable=False)

    especies = relationship("Especie")
    todoterrenos = relationship("Todoterreno")

class Todoterreno(Base):
    __tablename__ = "todoterreno"

    codigo = Column(Integer, primary_key=True)
    ruta = Column(Boolean(create_constraint=True), nullable=False)
    pasajeros = Column(Integer, CheckConstraint("pasajeros > 1 AND pasajeros < 6"))
    sis_seg = Column(Boolean(create_constraint=True), nullable=False)
    recinto = Column(Integer, ForeignKey("recinto.codigo", ondelete="CASCADE"), nullable=False)

#Base.metadata.create_all(bind=local_engine)