from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

LOCAL_SQLALCHEMY_DATABASE_URL = "mysql://root:example@localhost:3306/JurassicPark"

local_engine = create_engine(LOCAL_SQLALCHEMY_DATABASE_URL)

local_SessionLocal = sessionmaker(bind=local_engine)


DOCKER_SQLALCHEMY_DATABASE_URL = "mysql://root:example@jurassicpark-db:3306/JurassicPark"

docker_engine = create_engine(DOCKER_SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=docker_engine)

Base = declarative_base()