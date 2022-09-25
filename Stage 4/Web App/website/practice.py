from website.models import Station, User
from . import db



class Practice():
    def func(self, num1, num2):
        #return Station.query.filter_by(stationName = 'Cape Town').first()
        query = "SELECT * FROM Station WHERE stationName = 'Cape Town' OR stationName = 'Botha'"#db.session.query(Station).where(Station.stationName == 'Cape Town')
        return db.session.execute(query).fetchall()
        #return db.query(Station).where(Station.stationName == 'Cape Town')

    def func2(self, num1, num2):
        return self.func(num1,num2)