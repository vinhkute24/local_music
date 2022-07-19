
from flask import Flask
from .controller.UserCtrl import admin
from .controller.SongCtrl import song
from flask_jwt_extended import JWTManager
import os
from flask_cors import CORS




def create_app(test_config= None):
    app = Flask(__name__, instance_relative_config=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kamisama123@localhost:5432/music_server'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["JWT_ALGORITHM"] = "HS256"
    app.config["JWT_SECRET_KEY"]=os.environ.get('JWT_SECRET_KEY')

    

    from .models.base import db, migrate
    db.init_app(app)

    JWTManager(app)
    migrate.init_app(app)

    
    app.register_blueprint(admin)
    app.register_blueprint(song)

    CORS(app)
    

    
    return app

