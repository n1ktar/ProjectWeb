from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
from webapp.user import db
from webapp.user import UserInfo

def save_changes(edit, form):
    

    edit.user_id= current_user.user_id
    edit.username= current_user.username
    edit.name=form.name.data
    edit.sex=form.sex.data
    edit.age=form.age.data
    edit.city=form.city.data
    edit.hobby=form.hobby.data
    edit.genre=form.genre.data
    edit.smoke=form.smoke.data
    edit.alko=form.alko.data
    edit.socity=form.socity.data
 
    # commit the data to the database
    db.session.commit()