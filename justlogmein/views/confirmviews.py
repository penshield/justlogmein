__author__ = 'snouto'

from views import *
from system import *
from flask import request , flash,redirect , url_for
import datetime
from flask.ext.security.confirmable import *
from flask.ext.security.recoverable import *

@app.route('/account/doconfirm')
def confirm_account():

    if request.method =='GET':
        #get the email address that was passed
        email = request.args['email']

        if email != None:

            user = user_datastore.find_user(email=email)

            if user != None:
                send_confirmation_instructions(user)
                flash(u'Confirmation Email was Sent To your Address')



    return redirect(url_for('login'))


@app.route('/account/confirmation/<token>')
def do_confirmation(token):
    try:

        if request.method =='GET' and token != None and len(token) >=0:
            expired, invalid, user = confirm_email_token_status(token)
            if not expired and not invalid:
                user.confirmed_at = datetime.now()
                user.save()
                flash(u'Your Account has been Confirmed Successfully.')
            else:
                flash(u'Link seems bad or expired.')

    except Exception , s:
        flash(u'Link seems bad or expired')

    return redirect(url_for('login'))

















