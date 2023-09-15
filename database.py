from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import configparser
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
alembic_ini_path = os.path.join(script_dir, 'alembic.ini')

config = configparser.ConfigParser()
config.read(alembic_ini_path)
DATABASE_URL = config['alembic']['sqlalchemy.url']

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()



