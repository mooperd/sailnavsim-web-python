from sqlalchemy import Text, Integer, Column, String, Float, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__   = 'User'
    id              = Column(Integer, primary_key=True)
    name            = Column(String, nullable=False, unique=True)
    email           = Column(String, nullable=False, unique=True)

class Boat(Base):
    __tablename__   = 'Boat'
    id              = Column(Integer, primary_key=True)
    name            = Column(Text, nullable=False, unique=True)
    race            = Column(Text, nullable=False)
    desiredCourse   = Column(Float, nullable=False)
    started         = Column(Integer, nullable=False)
    boatType        = Column(Integer, nullable=False)
    isActive        = Column(Integer, nullable=False)
    boatFlags       = Column(Integer, nullable=False)
    race            = relation("BoatRace", backref="Boat")
    race_id         = Column(Integer, ForeignKey('BoatRace.id'))
    user            = relation("User", backref="User")
    user_id         = Column(Integer, ForeignKey('User.id'))


class BoatRace(Base):
    __tablename__   = 'BoatRace'
    id              = Column(Integer, primary_key=True)
    name            = Column(String, nullable=False, unique=True)
    startLat        = Column(Float, nullable=False)
    startLon        = Column(Float, nullable=False)

class BoatLog(Base):

    __table_args__ = (
        UniqueConstraint('boat_id', 'time'),
    )

    __tablename__   = 'BoatLog'
    time            = Column(Integer, nullable=False)
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
    compassMagDec   = Column(Float, nullable=False)
    invisibleLog    = Column(Integer, nullable=False)
    boat            = relation("Boat", backref="Boat")
    boat_id         = Column(Integer, ForeignKey('Boat.id'))

    __mapper_args__ = {
        "primary_key": [boat_id, time]
    }

def dbconnect():
    engine = create_engine('sqlite:////home/dev/sailnavsim-core/sailnavsim.sql', echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()