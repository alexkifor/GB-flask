from blog.app import db
from flask_login import UserMixin
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime




article_tag_associations_table = Table(
    'article_tag_association',
    db.metadata,
    db.Column('article_id', db.Integer, ForeignKey('articles.id'), nullable=False),
    db.Column('tag_id', db.Integer, ForeignKey('tags.id'), nullable=False),
)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    is_staff = db.Column(db.Boolean, default=False)

    author = relationship('Author', uselist=False, back_populates='user')

    def __str__(self):
        return f'{self.user.email} ({self.user.id})'

    def __init__(self, email, first_name, last_name, password, is_staff):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.is_staff = is_staff

class Author(db.Model):
    __tablename__='authors'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='author')
    article = relationship('Article', uselist=False, back_populates='author')

    def __str__(self):
        return self.user.email
    


class Article(db.Model):
    __tablename__='articles'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, ForeignKey('authors.id'), nullable=False)
    title = db.Column(db.String(255))
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship('Author', uselist=False, back_populates='article')
    tags = relationship('Tag', secondary=article_tag_associations_table, back_populates='articles')

    def __str__(self):
        return self.title

class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    articles = relationship('Article', secondary=article_tag_associations_table, back_populates='tags')

    def __str__(self):
        return self.name
