from flask import Blueprint, render_template, redirect, request, flash, url_for
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash
from blog.models import User
from blog.forms.user import UserLoginForm

auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/login', methods=('GET',))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))

    return render_template('auth/login.html', form=UserLoginForm(request.form))


@auth.route('/login', methods=('POST',))
def login_post():
    form = UserLoginForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if not user:
            flash('User not found')
            return redirect(url_for('.login'))
        elif check_password_hash(user.password, form.password.data) is False:
            flash('Check your password')
            return redirect(url_for('.login'))

        login_user(user)
        return redirect(url_for('user.profile', pk=user.id))

    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))
