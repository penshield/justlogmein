__author__ = 'snouto'

from system import *
from flask import request


class AccountManager(object):

    def __init__(self,request):
        self.request = request

    def __init__(self,user):
        self.user = user


    def register_current_user(self):
        try:
            self.user.save()
            return True
        except Exception , s:
            return False

    def register_user(self):

        try:
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            mobile = request.form['mobile']

            #now create a new user and save it into the database
            user = User(username=username,password=password,email=email,mobile=mobile)

            #now save the user into the database
            user.save()

            return True

        except Exception , s:
            return False


