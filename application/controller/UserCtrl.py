from crypt import methods
from email.policy import default
from flask import Blueprint, jsonify, request
from flask.views import MethodView
import validators

from ..models.base import db

from ..models.user import User

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

admin = Blueprint('admin', __name__, url_prefix="/admin")



class UserRegister(MethodView):
    def get(self):
        pass    
    

    def post(self):
        email = request.json['email']
        username = request.json['username']
        password = request.json['password']

        if len(password) < 6 :
            return jsonify({'error' : "short password"}),400

        if len(username) < 3 :
            return jsonify({'error' : "short username"}),400
        
        if not validators.email(email):
            return jsonify({'error': "Email is not valid"}), 400
        
        if User.query.filter_by(email=email).first() is not None:
            return jsonify({"error": "email exit"})



        user = User(username=username, password=password, email=email)

        db.session.add(user)
        db.session.commit()

        return jsonify({
            'message' :'create user succesful',
            'user':{
                'username':username,
                'email':email
            }
        })

admin.add_url_rule('/register', methods=['POST'], view_func=UserRegister.as_view('register'))





class UserLogin(MethodView):
    def get(self):
        pass    
    

    def post(self):
        username = request.json.get('username','')
        password = request.json.get('password','')

        user = User.query.filter_by(username='username').first()

        if user :   
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)

        return jsonify({"error": "email exit"})

        


admin.add_url_rule('/login', methods=['POST'], view_func=UserLogin.as_view('login'))



@admin.route('/get_infor', methods=['POST', 'GET'])
def get_infor():
    pass


@admin.route('/')
def home():
    return "main page"
