from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

engine = create_engine('sqlite:///database.db')

#engine.execute('DROP TABLE IF EXISTS AreaCentral;')
meta = MetaData(bind=engine)

print(engine.table_names())

f = open("Area Central.txt", "r")
temp = f.read()
temp2 = temp.split("\n\n")

areaCentral = Table(
   'AreaCentral', meta, 
   Column('trainNumber', String(150), primary_key = True), 
   Column('workingTime', String(150), primary_key = True), 
   Column('departureStation', String(150)),
   Column('arrivalStation', String(150)),
   Column('timeOfDeparture', String(150), primary_key = True),
   Column('route', String(150))
)
#meta.create_all(engine)

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



import pandas as pd
print(pd.read_sql_table(table_name='AreaCentral', con=engine))
