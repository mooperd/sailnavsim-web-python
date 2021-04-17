from sqlalchemy import Text, Integer, Column, String, Float, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class BoatLog(Base):
    __tablename__   = 'BoatLog'
    boatName        = Column(Text, nullable=False)
    time            = Column(Integer, nullable=False, primary_key=True)
    lat             = Column(Float, nullable=False)
    lon             = Column(Float, nullable=False)
    courseWater     = Column(Float, nullable=False)
    speedWater      = Column(Float, nullable=False)
    trackGround     = Column(Float, nullable=False)
    speedGround     = Column(Float, nullable=False)
    windDir         = Column(Float, nullable=False)
    windSpeed       = Column(Float, nullable=False)
    oceanCurrentDir = Column(Float)
    oceanCurrentSpeed = Column(Float)
    waterTemp       = Column(Float)
    temp            = Column(Float, nullable=False)
    dewpoint        = Column(Float, nullable=False)
    pressure        = Column(Float, nullable=False)
    cloud           = Column(Integer, nullable=False)
    visibility      = Column(Integer, nullable=False)
    precipRate      = Column(Float, nullable=False)
    precipType      = Column(Integer, nullable=False)
    boatStatus      = Column(Integer, nullable=False)
    boatLocation    = Column(Integer, nullable=False)
    waterSalinity   = Column(Float)
    oceanIce        = Column(Integer)
    distanceTravelled = Column(Float, nullable=False)
    damage          = Column(Float, nullable=False)
    windGust        = Column(Float, nullable=False)
    waveHeight      = Column(Float)

def dbconnect():
    engine = create_engine('sqlite:////home/andrew/sailnavsim-core/sailnavsim.sql', echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()