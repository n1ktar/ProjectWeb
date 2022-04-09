from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from webapp.user import User

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Запомнить меня', default=True, render_kw={"class": "form-checkinput"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})

class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    email =  StringField('Электронная почта', validators=[DataRequired(), Email()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})

    def validate_username(self, username):
        users_count = User.query.filter_by(username=username.data).count()
        if users_count > 0:
            raise ValidationError('Пользователь с таким именем уже зарегистрирован')
    
    def validate_email(self, email):
        users_count = User.query.filter_by(email=email.data).count()
        if users_count > 0:
            raise ValidationError(
                'Пользователь с такой электронной почтой уже зарегистрирован')

class AnswerForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()], render_kw={"class": "form-control"})
    sex = SelectField('Пол', validators=[DataRequired()], render_kw={"class": "form-select"}, choices=[('1', ""), ('m', "М"), ('f', "Ж")])
    age = StringField('Возраст', validators=[DataRequired()], render_kw={"class": "form-control"})
    city = StringField('Город', validators=[DataRequired()], render_kw={"class": "form-control"})
    hobby = SelectField('Ваше любимое хобби', validators=[DataRequired()], render_kw={"class": "form-select"}, choices=[('1',""), ('draw', "Рисование"), ('music', "Игра на музыкальных инструментах"),  ('dance', "Танцы"),  ('games', "Компьютерные игры"),  ('sport', "Спорт")])
    genre = SelectField('Ваш любимый жанр музыки', validators=[DataRequired()],  render_kw={"class": "form-select"}, choices=[('1', ""), ('rock', "Рок"), ('hip-hop', "Хип-Хоп"), ('pop', "Поп")])
    smoke = SelectField('Ваше отношение к курению?', validators=[DataRequired()], render_kw={"class": "form-select"}, choices=[('1', ""), ('positive', "Положительное"), ('neutral', "Нейтральное"), ('negative', "Негативное")])
    alko = SelectField('Ваше отношение к алкоголю?', validators=[DataRequired()], render_kw={"class": "form-select"}, choices=[('1', ""), ('positive', "Положительное"), ('neutral', "Нейтральное"), ('negative', "Негативное")])
    socity = SelectField('Вы интроверт/экстраверт?', validators=[DataRequired()], render_kw={"class": "form-select"}, choices=[('1', ""), ('intr', "Интроверт"), ('extr', "Экстраверт")])
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})

