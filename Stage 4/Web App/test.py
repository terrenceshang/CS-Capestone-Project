from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///database.db')
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

print(engine.table_names())

class AreaCentral(Base):
    __tablename__ = 'AreaCentral'

    trainNumber = Column('trainNumber', String(150), primary_key = True)
    workingTime = Column('workingTime', String(150), primary_key = True)
    departureStation = Column('departureStation', String(150))
    arrivalStation = Column('arrivalStation', String(150))
    timeOfDeparture = Column('timeOfDeparture', String(150), primary_key = True)
    route = Column('route', String(150))


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()


list = session.query(AreaCentral)
print(list[0])