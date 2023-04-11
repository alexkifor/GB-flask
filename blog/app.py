from os import getenv, path
from json import load
from blog.extension import db, login_manager
from blog.models import User

from flask import Flask
from blog.user.views import user
from blog.article.views import article
from blog.auth.views import auth
from blog.index.views import index

CONFIG_PATH = getenv("CONFIG_PATH", path.join("../config.json"))

VIEWS = [
    user,
    index,
    article,
    auth,
]

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_file(CONFIG_PATH, load)
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app):
    db.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    for view in VIEWS:
        app.register_blueprint(view)

