import os
from combojsonapi.spec import ApiSpecPlugin
from combojsonapi.event import EventPlugin
from combojsonapi.permission import PermissionPlugin
from blog.extension import db, login_manager, migrate, csrf, admin, api
from blog import commands
from blog.models import User

from flask import Flask
from blog.user.views import user
from blog.article.views import article
from blog.auth.views import auth
from blog.index.views import index
from blog.author.views import author



VIEWS = [
    user,
    index,
    article,
    auth,
    author,
]

cfg_name = os.environ.get('CONFIG_NAME')

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(f"blog.config.{cfg_name}")
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_api(app)
    return app

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    csrf.init_app(app)
    admin.init_app(app)
    api.plugins = [
        EventPlugin(),
        PermissionPlugin(),
        ApiSpecPlugin(
            app=app,
            tags={
                'Tag': 'Tag API',
                'User': 'User API',
                'Author': 'Author API',
                'Article': 'Article API',
            }
        ),
    ]
    
    api.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

def register_api(app: Flask):
    from blog.api.tag import TagList, TagDetail
    from blog.api.article import ArticleList, ArticleDetail
    from blog.api.user import UserList, UserDetail
    from blog.api.author import AuthorList, AuthorDetail
    

    api.route(TagList, 'tag_list', '/api/tags/', tag='Tag')
    api.route(TagDetail, 'tag_detail', '/api/tags/<int:id>', tag='Tag')
    
    api.route(UserList, 'user_list', '/api/users/', tag='User')
    api.route(UserDetail, 'user_detail', '/api/users/<int:id>', tag='User')

    api.route(AuthorList, 'author_list', '/api/authors/', tag='Author')
    api.route(AuthorDetail, 'author_detail', '/api/authors/<int:id>', tag='Author')

    api.route(ArticleList, 'article_list', '/api/articles/', tag='Article')
    api.route(ArticleDetail, 'article_detail', '/api/articles/<int:id>', tag='Article')



def register_blueprints(app: Flask):
    from blog import admin
    for view in VIEWS:
        app.register_blueprint(view)
    admin.register_views()


def register_commands(app: Flask):
    app.cli.add_command(commands.create_admin)
    app.cli.add_command(commands.create_init_tags)