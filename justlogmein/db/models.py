__author__ = 'snouto'


from system import *
from mongoengine.base import *


class UserSite(Document):

    folder = db.StringField(max_length=255,required=True)
    name = db.StringField(max_length=255,required=True)
    url = db.StringField(max_length=600,required=True)
    username=db.StringField(max_length=255,required=True)
    password=db.StringField(max_length=255,required=True)
    note=db.StringField(required=False)
    icon = db.StringField(required=False)
    settings = db.DictField(required=False,default={'favourite':False,'autofill':False,'autologin':False})
    fields = db.ListField(required=False)
    user = db.ReferenceField(User)


    meta = {
        'indexes':[{
                       'fields':['name','folder','user']
                   }]
        }





class Note(Document):

    name = db.StringField(required=True,max_length=255)
    folder = db.StringField(required=True,max_length=255)
    type = db.StringField(required=True,max_length=255)
    note = db.StringField(required=False)
    settings = db.DictField(required=False,default={'favorite':False,'require_reprompt':False})
    meta = {

            'indexes':[
                {
                    'fields':['name','folder','type']
                }

            ]

            }

    node_fields = db.ListField(DictField(),required=False)
    user_id = db.ReferenceField(User)



class FormFields(Document):
    profile_name = db.StringField(required=True,max_length=255)
    language = db.StringField(required=True,max_length=255)
    settings = db.DictField(required=False,default={'favorite':False,'require_reprompt':False})
    fields_definitions = db.ListField(DictField(),required=False)
    meta = {
        'indexes':[
            {
                'fields':['profile_name','language']
            }
        ]
    }
    user_id = db.ReferenceField(User)







