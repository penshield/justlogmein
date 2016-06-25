__author__ = 'snouto'
from flask import Flask
from config import *
from pymongo import ASCENDING , TEXT
from mongoengine import *
from flask.ext.mongoengine import MongoEngine
from flask.ext.security import Security, MongoEngineUserDatastore, \
    UserMixin, RoleMixin, login_required , AnonymousUser

from flask.ext.login import *
from flask_mail import Mail

app = Flask(__name__,template_folder=template_folder,static_folder=static_folder)

app.app_context().push()

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config["MONGODB_HOST"] = MONGODB_HOST
app.config['MONGODB_DB'] = MONGODB_DB
app.config['MONGODB_PORT'] = MONGODB_PORT


"""
The following section sets the overall configuration for flask-security
"""
app.config['SECURITY_PASSWORD_HASH'] = SECURITY_PASSWORD_HASH
app.config['SECURITY_PASSWORD_SALT'] = SECURITY_PASSWORD_SALT
app.config['SECURITY_CONFIRM_SALT'] = SECURITY_CONFIRM_SALT
app.config['SECURITY_RESET_SALT'] = SECURITY_RESET_SALT
app.config['SECURITY_CONFIRMABLE'] = True
app.config['SECURITY_RECOVERABLE'] = True
app.config['SECURITY_CHANGEABLE']  = SECURITY_CHANGEABLE


"""
The default settings for Mail
"""
app.config['MAIL_SERVER'] = MAIL_SERVER
app.config['MAIL_PORT'] = MAIL_PORT
app.config['MAIL_USE_TLS'] = MAIL_USE_TLS
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] =MAIL_PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = MAIL_DEFAULT_SENDER

appMail = Mail()
appMail.init_app(app)

# apply settings for default security views
app.config['SECURITY_LOGIN_URL']=SECURITY_LOGIN_URL
app.config['SECURITY_LOGOUT_URL']=SECURITY_LOGOUT_URL
app.config['SECURITY_REGISTER_URL']=SECURITY_REGISTER_URL
app.config['SECURITY_RESET_URL']=SECURITY_RESET_URL
app.config['SECURITY_CHANGE_URL']= SECURITY_CHANGE_URL
app.config['SECURITY_CONFIRM_URL']=SECURITY_CONFIRM_URL
app.config['SECURITY_CONFIRM_ERROR_VIEW'] = SECURITY_CONFIRM_ERROR_VIEW
app.config['SECURITY_POST_LOGOUT_VIEW']=SECURITY_POST_LOGOUT_VIEW
app.config['SECURITY_POST_CONFIRM_VIEW'] = SECURITY_POST_CONFIRM_VIEW

#set the template html pages
app.config['SECURITY_FORGOT_PASSWORD_TEMPLATE'] = SECURITY_FORGOT_PASSWORD_TEMPLATE
app.config['SECURITY_LOGIN_USER_TEMPLATE'] = SECURITY_LOGIN_USER_TEMPLATE
app.config['SECURITY_REGISTER_USER_TEMPLATE'] = SECURITY_REGISTER_USER_TEMPLATE
app.config['SECURITY_RESET_PASSWORD_TEMPLATE'] = SECURITY_RESET_PASSWORD_TEMPLATE
app.config['SECURITY_SEND_CONFIRMATION_TEMPLATE'] = SECURITY_SEND_CONFIRMATION_TEMPLATE


#now apply flask security
# Create database connection object
db = MongoEngine(app)


class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)

class User(db.Document, UserMixin):
    username = db.StringField(max_length=255,unique=True)
    name = db.StringField(max_length=255,required=True)
    email = db.StringField(max_length=255,required=True,unique=True)
    password = db.StringField(max_length=255,required=True)
    active = db.BooleanField(default=True)
    mobile = db.StringField(max_length=255,required=True)
    confirmed_at = db.DateTimeField()
    birthdate = db.DateTimeField(required=True)
    gender = db.IntField(required=True)
    roles = db.ListField(db.ReferenceField(Role), default=[])
    gcm = db.ListField(required=False,default=[])

User.ensure_index([('password',ASCENDING)],index_name='password_idx')
User.ensure_index([('mobile',ASCENDING)],index_name='mobile_idx')
User.ensure_index([('name',ASCENDING)],index_name='mobile_idx')
# Setup Flask-Security
user_datastore = MongoEngineUserDatastore(db, User, Role)


#create the system wide security
security = Security()
security.init_app(app,user_datastore)



"""
This section attaches the login manager of the application
"""
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'
login_manager.anonymous_user = AnonymousUser




