
from flask import Flask
from .controller.UserCtrl import admin


def create_app(test_config= None):
    app = Flask(__name__, instance_relative_config=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kamisama123@localhost:5432/music_server'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .models.base import db, migrate
    db.init_app(app)
    migrate.init_app(app)

    
    app.register_blueprint(admin)
    

    
    return app

