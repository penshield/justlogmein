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


def get_authorization(user):
    serializer = Serializer(secret_key=app.config['SECRET_KEY'],salt=config.SECURITY_PASSWORD_SALT)
    authorization_code = "%s-%s" % (user.username,user.email)
    authorization_code = serializer.dumps(authorization_code)
    digester  = hashlib.md5()
    digester.update(authorization_code)
    return digester.hexdigest()

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
            if found.fields is not None and len(found.fields) > 0:
                site['fields'] = []
                for field in found.fields:
                    site['fields'].append({
                        'name':field['name'],
                        'value':field['value'],
                        'type':str(field['type']).lower()
                    })
            else:
                site['fields'] = []
                site['fields'].append({'name':'username','type':'text','value':site['username']})
                site['fields'].append({'name':'password','type':'text','value':site['password']})
            sites.append(site)

        digester  = hashlib.md5()
        digester.update(authorization_code)
        authorization = digester.hexdigest()
        account = {'name':user.name,'email':user.email,'username':user.username,'authorization':authorization}
        response = Response(dumps({'success':True,'sites':sites,'account':account,'authorization':authorization}),status=200,mimetype='application/json')
        response.headers['Authorization'] = digester.hexdigest()
        session['rest_user']['authorization'] = digester.hexdigest()
        response.set_cookie('authorization',value=digester.hexdigest(),expires=False)

        return response
    else:
         return flask.jsonify({'success':False})


def saveRegistrationToken(gcm_registration_token, user,appType):

    try:
        gcm_settings = user.gcm
        if gcm_settings is None:
            gcm_settings = []
        if appType is None:
            appType ='chrome_plugin'

        if len(gcm_settings) > 0:
            to_remove = []
            for field in gcm_settings:
                if field['type'] == appType:
                    to_remove.append(field)

            for removed in to_remove:
                gcm_settings.remove(removed)

        gcm_settings.append({'type':appType,'registrationId':gcm_registration_token})
        user['gcm'] = gcm_settings
        #save the current user into the database
        user.save()
        return True
    except Exception,s:
        print "Received an Exception during Saving the Registration Token : %s" % s.message
        return False

@app.route('/rest/account/reload',methods=['POST'])
def account_reload():
    authorization_code = request.form['authorizationId']
    username = request.form['username']
    user = user_datastore.find_user(username=username)
    calculated_authorization = get_authorization(user)
    if calculated_authorization == authorization_code:
        found_sites = UserSite.objects(user=user)
        sites = []
        for found in found_sites:
            site = {'name':found.name,'url':found.url,'username':found.username,'password':found.password,'folder':found.folder
                    ,'settings':{'favourite':found.settings['favourite'],'autologin':found.settings['autologin'],'autofill':found.settings['autofill']},
                    'id':str(found.id)}
            if found.fields is not None and len(found.fields) > 0:
                site['fields'] = []
                for field in found.fields:
                    site['fields'].append({
                        'name':field['name'],
                        'value':field['value'],
                        'type':field['type']
                    })
            else:
                site['fields'] = []
                site['fields'].append({'name':'username','type':'text','value':site['username']})
                site['fields'].append({'name':'password','type':'text','value':site['password']})
            sites.append(site)
        response = {'success':True,'sites':sites}
        return flask.jsonify(response)
    else:
        return flask.jsonify({'success':False,'reason':'Unauthorized Request','code':405})

@app.route('/rest/gcm/register',methods=['POST'])
def gcm_register():
    authorizationCode = request.form['authorizationId']
    username = request.form['username']
    gcm_registration_token = request.form['registrationId']
    appType = request.form['appType']
    if authorizationCode is None or len(authorizationCode) <= 0:
        return flask.jsonify({'success':False,'reason':'UnAuthorized Request','code':405})
    else:
        user = user_datastore.find_user(username=username)

        if user is not None:
            calculated_auth_code = get_authorization(user)
            # now check the equality of the authorization code
            if authorizationCode == calculated_auth_code and gcm_registration_token is not None and len(gcm_registration_token) > 0:
                #do the registration in here
                result = saveRegistrationToken(gcm_registration_token,user,appType)
                if result:
                    return flask.jsonify({'success':True,'reason':'Registration Token was saved Successfully.','code':200})
                else:
                    return flask.jsonify({'success':False,'reason':'Unable to save Registration Token , Please try again Later','code':500})
            else:
                #the passed in authorization does not match the calculated one
                return flask.jsonify({'success':False,'code':405,'reason':'Access Denied,Probably, Malicious Request'})
        else:
            return flask.jsonify({'success':False,'reason':'Wrong username','code':500})




