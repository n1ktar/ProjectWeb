from distutils.log import error
from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_user, logout_user
from flask_migrate import Migrate
import json

from webapp.forms import LoginForm, RegistrationForm
from webapp.user import db, User

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        title = "Сайт знакомств"  
        return render_template('index.html', page_title=title)

    @app.route('/endpoint')
    def end():
        dict = {"message":"success"}
        json.dumps(dict)
        return dict

    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index')) 
        title = 'Авторизация'
        login_form = LoginForm()
        return render_template('user/login.html', page_title=title, form=login_form)

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter(User.username == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                flash('Вы успешно вошли на сайт')
                return redirect(url_for('index'))

        flash('Неправильные имя или пароль')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        flash('Вы успешно разлогинились')
        logout_user()
        return redirect(url_for('index'))

    @app.route('/register')
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('index')) 
        title = 'Регистрация'
        form = RegistrationForm()
        return render_template('user/registration.html', page_title=title, form=form)

    @app.route('/process-reg', methods = ['POST'])
    def process_reg():
        form = RegistrationForm()
        if form.validate_on_submit():
            new_user = User(username=form.username.data, email=form.email.data, role='user')
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash('Вы успешно зарегестрировались!')
            return redirect(url_for('login'))
        else:
            for field, errors in form.errors.items():
                for errors in errors:
                    flash('Ошибка в поле "{}": {}'.format(
                        getattr(form, field).label.text,
                        error
                    ))
        return redirect(url_for('register'))

    return app

