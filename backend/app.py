from flask import Flask
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)



class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    posts = db.relationship('PostModel', backref='user', lazy=True)

    def __repr__(self):
        return f"User(name = {name}, email = {email})"

class PostModel(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    slugs = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"Post(mood = {mood}, description = {description}, user_id = {user_id})"


post_put_args = reqparse.RequestParser()
post_put_args.add_argument("mood", type=str, help="Mood of the post")

user_put_args = reqparse.RequestParser()
user_put_args.add_argument('name', type=str, help='Name is required', required=True)
user_put_args.add_argument('email', type=str, help='Email is required', required=True)
user_put_args.add_argument('password', type=str, help='Password is required', required=True)

user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String
}

class User(Resource):
    @marshal_with(user_fields)
    def get(self, user_id):
        result = UserModel.query.get(user_id)
        return result

    @marshal_with(user_fields)
    def post(self):
        args = user_put_args.parse_args()
        user = UserModel(name=args['name'], email=args['email'], password=args['password'])
        db.session.add(user)
        db.session.commit()
        return user, 201


api.add_resource(User, '/users/', '/users/<int:user_id>')



if __name__ == '__main__':
    app.run(debug=True)