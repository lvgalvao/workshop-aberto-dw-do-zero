from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///surf_data.db'

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class SurfData(Base):
    __tablename__ = 'surf_data'
    id = Column(Integer, primary_key=True, index=True)
    beach = Column(String, index=True)
    timestamp = Column(DateTime)
    wave_height = Column(Float)
    temperature = Column(Float)
    wind_speed = Column(Float)

Base.metadata.create_all(bind=engine)
