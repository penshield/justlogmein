__author__ = 'snouto'

from system import *
from flask import session
from flask.ext.security import utils
from db.models import  UserSite
import mongoengine

@app.before_first_request
def init_app():

    role = user_datastore.find_or_create_role(name='user',description='Simple and Normal user Role')
    """

    user = user_datastore.create_user(name="Mohamed Ibrahim",username='snoutos',password=utils.encrypt_password('snouto'),active=True,mobile='0537064873',roles=[role],email='csharpizer@gmail.com')
    site = UserSite(folder='Generic',name='Google',url='http://www.google.com',username='csharpizer@gmail.com',password='snouto',note='this is a simple note',
                    user_id=user)
    site.save()

    """



@login_manager.user_loader
def load_user(user_id):
    user = user_datastore.find_user(id=user_id)

    if user:
        session['current_active_user'] = user

    return user





