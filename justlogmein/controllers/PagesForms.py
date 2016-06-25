__author__ = 'snouto'
from flask import session
from flask_wtf import *
import system
from wtforms import StringField,PasswordField , DateField , SelectField , BooleanField , TextAreaField ,HiddenField
from wtforms.validators import *
from flask.ext.security import utils


class UserSiteForm(Form):
    name = StringField("name",validators=[Required()])
    folder = StringField("folder",validators=[Required()])
    url = StringField("url",validators=[Required()])
    username = StringField("username",validators=[Required()])
    password = PasswordField("password",validators=[Required()])
    favourite = BooleanField("favourite")
    autofill = BooleanField("autofill")
    autologin = BooleanField("autologin")
    notes = TextAreaField("notes")
    icon = HiddenField("icon")
    site_id = HiddenField("site_id")
    fields = []


    def __init__(self,*args,**kargs):
        super(UserSiteForm,self).__init__(*args,**kargs)



    def load_site(self,site):
        if site is None:
            return None
        else:
            self.name.data = site.name
            self.folder.data = site.folder
            self.url.data = site.url
            self.username.data = site.username
            self.password.data = site.password
            self.favourite.data = site.settings['favourite']
            self.autofill.data = site.settings['autofill']
            self.autologin.data = site.settings['autologin']
            self.notes.data = site.note
            self.icon.data = site.icon
            self.site_id.data = site.id

            if site.fields is not None and len(site.fields) > 0:
                self.fields = site.fields

    def validate(self):
        return super(UserSiteForm,self).validate()

    def get_site(self):
        from db.models import UserSite
        site = UserSite()
        site.folder = self.folder.data
        site.name = self.name.data
        site.url = self.url.data
        site.username = self.username.data
        site.password = self.password.data
        site.note = self.notes.data
        site.icon = self.icon.data
        if self.site_id.data != None and len(self.site_id.data) > 0:
            site.id = self.site_id.data

        site.settings = {
            'favourite':self.favourite.data,
            'autologin':self.autologin.data,
            'autofill':self.autofill.data
        }

        if site.username is not None and site.password is not None:
            #append the username
            site.fields.append({'name':'username','type':'text','value':site.username})
            site.fields.append({'name':'password','type':'password','value':site.password})

        return site



class NoteForm(Form):
    pass



class FormFieldsForm(Form):
    pass

