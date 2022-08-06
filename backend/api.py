from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    posts = db.relationship('PostModel', backref='user', lazy=True)

    def __repr__(self):
        return f"User(name = {name}, email = {email})"

class PostModel(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"Post(mood = {mood}, description = {description}, user_id = {user_id})"


post_put_args = reqparse.RequestParser()
post_put_args.add_argument("mood", type=str, help="Mood of the post")

names = {"tim": {'age': 19, 'gender': 'male'},
        "bill": {"age": 20, 'gender': 'male'}}

class Post(Resource):
    def get(self, name):
        return names[name]

api.add_resource(Post, '/post/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)