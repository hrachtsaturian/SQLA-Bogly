"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User (db.Model):
    def __repr__(self):
        p = self
        return f'User id={p.id}, first_name={p.first_name}, last_name={p.last_name}, image_url={p.image_url}'
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False, unique=True)
    last_name = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)

def connect_db(app):
    db.app = app
    db.init_app(app)