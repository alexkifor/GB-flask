from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

#USERS = ['John', 'Michail', 'Anna']
USERS = {
    1: {'name': 'John',
        'surname': 'Smitt',
        'age': 31,
        'gender': 'male',
        'country': 'Australia',
        'login': 'John_S'
        },
    2: {'name': 'Michael',
        'surname': 'Brown',
        'age': 26,
        'gender': 'male',
        'country': 'USA',
        'login': 'Michael_B'
        },
    3: {'name': 'Anna',
        'surname': 'Filippova',
        'age': 35,
        'gender': 'female',
        'country': 'Russia',
        'login': 'Anna_F'
        }
}

@user.route('/')
def user_list():
    return render_template(
        'users/list.html',
        users=USERS,
        )

@user.route('/<int:pk>')
def get_user(pk: int):
    try:
        user_name = USERS[pk]['name']
    except KeyError:
        #raise NotFound(f'User id {pk} not found')
        return redirect('/users/')
    user_name = USERS[pk]['name']
    user_surname = USERS[pk]['surname']
    user_age = USERS[pk]['age']
    user_gender = USERS[pk]['gender']
    user_country = USERS[pk]['country']
    user_login = USERS[pk]['login']
    return render_template(
        'users/details.html',
        user_name=user_name,
        user_surname=user_surname,
        user_age=user_age,
        user_gender=user_gender,
        user_country=user_country,
        user_login=user_login
        )

