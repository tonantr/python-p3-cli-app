from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import configparser


config = configparser.ConfigParser()
config.read('alembic.ini')
DATABASE_URL = config['alembic']['sqlalchemy.url']

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()



