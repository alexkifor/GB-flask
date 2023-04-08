from flask import Blueprint, render_template, redirect
from flask_login import login_required
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

#USERS = ['John', 'Michail', 'Anna']
# USERS = {
#     1: {'name': 'John',
#         'surname': 'Smitt',
#         'age': 31,
#         'gender': 'male',
#         'country': 'Australia',
#         'login': 'John_S'
#         },
#     2: {'name': 'Michael',
#         'surname': 'Brown',
#         'age': 26,
#         'gender': 'male',
#         'country': 'USA',
#         'login': 'Michael_B'
#         },
#     3: {'name': 'Anna',
#         'surname': 'Filippova',
#         'age': 35,
#         'gender': 'female',
#         'country': 'Russia',
#         'login': 'Anna_F'
#         }
# }

@user.route('/')
@login_required
def user_list():
    from blog.models import User
    users = User.query.all()
    return render_template(
        'users/list.html',
        users=users,
        )

@user.route('/<int:pk>')
@login_required
def profile(pk: int):
    from blog.models import User
    
    _user = User.query.filter_by(id=pk).one_or_none()
    if not _user:
        raise NotFound(f"User #{pk} doesn't exist!")

    return render_template(
        'users/profile.html',
        user=_user,
        )

