from werkzeug.security import generate_password_hash
from blog.app import create_app, db


# if __name__ == '__main__':
#     app.run(
#         host='0.0.0.0',
#         debug=True,
#     )

app = create_app()

# @app.cli.command('init-db')
# def init_db():
#     db.create_all()

@app.cli.command('create_users')
def create_users():
    from blog.models import User
    db.session.add(
        User(email='user_1@email.com', password=generate_password_hash('test123'),name='Alexander', is_staff=True)
    )
    db.session.commit()