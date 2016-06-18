__author__ = 'snouto'
from flask import session
from flask_wtf import *
import system
from wtforms import StringField,PasswordField , DateField , SelectField
from wtforms.validators import *
from flask.ext.security import utils

class LoginForm(Form):
    username = StringField("username",validators=[DataRequired()])
    password = PasswordField("password",validators=[DataRequired()])


    def __init__(self,*args,**kargs):
        Form().__init__(*args,**kargs)





class RegisterationForm(Form):
    name = StringField("name",validators=[InputRequired()])
    username = StringField("username",validators=[InputRequired()])
    password = PasswordField("password",validators=[Required()])
    email = StringField("email",validators=[InputRequired()])
    mobile = StringField("mobile",validators=[InputRequired()])
    gender = SelectField(label="Gender",choices=[('1','Male'),('0','Female')],validators=[Required()])
    birthDate = DateField(label="Birth Date",format='%d/%m/%Y')



    def load_data(self,user):

        if user != None:
            self.name.data = user.name
            self.username.data = user.username
            self.password.data = user.password

            self.email.data = user.email
            self.mobile.data = user.mobile
            self.gender.data = str(user.gender)
            self.birthDate.data = user.birthdate



    def __init__(self,*args,**kargs):
        super(RegisterationForm,self).__init__(*args,**kargs)
        self.user = None


    def validate(self):
        rv = super(RegisterationForm,self).validate()

        if rv:
            user_g = 0
            if self.gender.data == "1":
                user_g = 1

            role = system.user_datastore.find_or_create_role(name='user')
            self.user = system.User(username=str(self.username.data),password=utils.encrypt_password(self.password.data),email=str(self.email.data),
                                    name=self.name.data,gender=int(user_g),birthdate= self.birthDate.data , active=True
                                    ,mobile=str(self.mobile.data),roles=[role])
            return True
        else:
            return False





class ContactUpdateForm(Form):

    email = StringField("email",validators=[InputRequired()])
    mobile = StringField("mobile",validators=[InputRequired()])

    def __init__(self,*args,**kargs):
        super(ContactUpdateForm,self).__init__(*args,**kargs)
        self.user = None


    def load_data(self,user):
        if user != None:
            self.email.data = user.email
            self.mobile.data = user.mobile


    def validate(self):
        rv = super(ContactUpdateForm,self).validate()

        if rv:
            self.user = session['current_active_user']

            if self.user != None:
                self.user.mobile = self.mobile.data
                self.user.email = self.email.data
                self.user.save()
                return True
            else:
                return False
        else:
            return False



class GeneralInfoForm(Form):
    name = StringField("name",validators=[InputRequired()])
    gender = SelectField(label="Gender",choices=[('1','Male'),('0','Female')],validators=[Required()])
    birthDate = DateField(label="Birth Date",format='%d/%m/%Y')

    def __init__(self,*args,**kargs):
        super(GeneralInfoForm,self).__init__(*args,**kargs)
        self.user = None

    def load_data(self,user):
        if user != None:
            self.name.data = user.name
            self.gender.data = user.gender
            self.birthDate.data = user.birthdate


    def validate(self):
        rv = super(GeneralInfoForm,self).validate()

        if rv:
            self.user = session['current_active_user']


            self.user = system.user_datastore.find_user(id=self.user.id)

            if self.user != None:
                self.user.name = self.name.data
                self.user.gender = int(self.gender.data)
                self.user.birthdate = self.birthDate.data
                self.user.save()
                return True
            else:
                return False

        else:
            return False


class ResetPasswordForm(Form):
    import wtforms.validators
    username = StringField("username")
    password = PasswordField("New Password",validators=[Required(),EqualTo('confirm',message="Passwords must match")])
    confirm = PasswordField("Repeat Password")

    def __init__(self,*args,**kargs):
        super(ResetPasswordForm,self).__init__(*args,**kargs)
        self.user = None

    def validate(self):
        return super(ResetPasswordForm,self).validate()
