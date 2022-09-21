from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import pyodbc
#import SearchRoute
#sr = SearchRoute()

db = SQLAlchemy()
DB_NAME = "database.db"

#stationNames = open("./website/StationNames.txt", "r")
#AN_duration = open ("./website/Duration/Area North Duration.txt", "r")
#AC_duration = open ("./website/Duration/Area Central Duration.txt", "r")
#AS_duration = open ("./website/Duration/Area South Duration.txt", "r")
#AN_trainRoute = open ("./website/Duration/Area North Train Route.txt", "r")
#AC_trainRoute = open ("./website/Duration/Area Central Train Route.txt", "r")
#AS_trainRoute = open ("./website/Duration/Area South Train Route.txt", "r")
#stations = open ("./website/Duration/Station.txt", "r")

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'a'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    

    from .views import views
    from .auth import auth
    
 
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Station
    
    #create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
