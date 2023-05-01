import click
from werkzeug.security import generate_password_hash

from blog.extension import db


@click.command('create_users')
def create_users():
    from blog.models import User
    db.session.add(
        User(email='user_1@email.com', password=generate_password_hash('test123'),name='Alexander', is_staff=True)
    )
    db.session.commit()

@click.command('create-init-tags')
def create_init_tags():
    from blog.models import Tag
    from wsgi import app

    with app.app_context():
        tags = ('flask', 'django', 'python', 'gb', 'sqlite')
        for item in tags:
            db.session.add(Tag(name=item))
        db.session.commit()
    click.echo(f'Created tags: {", ".join(tags)}')