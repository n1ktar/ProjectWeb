from getpass import getpass
import sys

from webapp import create_app

from webapp.user import UserInfo, db, User

app = create_app()

with app.app_context():
    username = input('Введите имя пользователя:')

    if UserInfo.query.filter(UserInfo.username == username).count():
        print('Пользователь с таким именем уже заполнял анкету')
        sys.exit(0)
    
    name = input('Имя')
    sex = input('Пол')
    age = input('Возраст')
    city = input('Город')
    hobby = input('Ваше любимое хобби')
    genre = input('Ваш любимый жанр музыки')
    socity = input('Вы интроверт/экстраверт?')

    new_user = UserInfo(username=username, name=name, age=age, city=city, hobby=hobby, genre=genre, socity=socity )

    db.session.add(new_user)
    db.session.commit()
    print('Создана анкета с id={}'.format(new_user.user_id))