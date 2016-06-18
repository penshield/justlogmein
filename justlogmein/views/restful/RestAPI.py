__author__ = 'snouto'

from system import *
from flask import request,session , Response
from itsdangerous import Serializer
import config
import flask
import datetime
from db.models import UserSite
from flask_security import utils
from json import dumps
import hashlib

@app.route('/rest/login',methods=['POST'])
def rest_login():
    username = request.form['username']
    password = request.form['password']
    user = user_datastore.find_user(username=username)
    if user is not None and utils.verify_password(password,user.password):
        session['current_active_user'] = user
        session['rest_user'] = {'user':user,'authorization':None}
        serializer = Serializer(secret_key=app.config['SECRET_KEY'],salt=config.SECURITY_PASSWORD_SALT)
        authorization_code = "%s-%s" % (user.username,user.email)
        authorization_code = serializer.dumps(authorization_code)
        found_sites = UserSite.objects(user=user)
        sites = []
        for found in found_sites:
            site = {'name':found.name,'url':found.url,'username':found.username,'password':found.password,'folder':found.folder
                    ,'settings':{'favourite':found.settings['favourite'],'autologin':found.settings['autologin'],'autofill':found.settings['autofill']},
                    'id':str(found.id)}
            sites.append(site)

        digester  = hashlib.md5()
        digester.update(authorization_code)
        account = {'name':user.name,'email':user.email,'username':user.username}
        authorization = digester.hexdigest()
        response = Response(dumps({'success':True,'sites':sites,'account':account,'authorization':authorization}),status=200,mimetype='application/json')
        response.headers['Authorization'] = digester.hexdigest()
        session['rest_user']['authorization'] = digester.hexdigest()
        response.set_cookie('authorization',value=digester.hexdigest(),expires=False)

        return response
    else:
         return flask.jsonify({'success':False})








