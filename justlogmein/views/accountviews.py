__author__ = 'snouto'

from views import *
from flask import render_template, request, flash, url_for, redirect
from controllers.forms import RegisterationForm, ContactUpdateForm, GeneralInfoForm
from flask_security.recoverable import *
from flask_security.confirmable import *
from jinja2 import Template
from controllers.security import SecurityTokenManager

@app.route('/account/register', methods=['GET', 'POST'])
def register():

    from controllers.utilities import send_confirm_email
    form = RegisterationForm(request.form)

    if request.method == 'POST':

        if form.validate_on_submit():
            try:
                form.user.save()
                #now send a confirmation email
                token = generate_confirmation_token(form.user)
                link = "%s%s" % (request.host_url, 'account/confirmation')
                result = send_confirm_email(token,form.user,link)
                if result:

                    flash(u'Email Sent. Please Confirm your Email before Login')
                else:
                    flash(u'Registeration Successful.Now You can Login')

                return redirect(url_for('login'))

            except NotUniqueError, err:
                flash(u'The username already exists !')
                form.username.data = u""
                return render_template('account-register.html', form=form)


        else:

            flash(u"Please fill all Required Fields")

            return render_template("account-register.html", form=form)

    else:
        return render_template('account-register.html', form=form)


#################################################################################################################

"""

Resetting Account Password ViewController Methods

"""


@app.route('/account/doreset',methods=['POST'])
def do_reset():
    from controllers.forms import ResetPasswordForm

    if request.method == 'POST':
        form = ResetPasswordForm(request.form)
        token = request.form['token']

        if form.validate_on_submit() and token != None and len(token) > 0:

            if form.password.data != form.confirm.data:
                flash(u'Provided Passwords do not match, Please Try them again')
                return render_template('reset-password.html',form=form,model={'name':form.username.data,'token':token})

            expired , invalid , user = reset_password_token_status(token)

            if not expired and not invalid and user != None:
                user.password = utils.encrypt_password(form.password.data)
                user.save()
                flash(u'Password has been Changed Successfully.')
                return redirect(url_for('login'))
            else:
                flash(u'There is a problem , Please try resetting your Password again.')
                return redirect(url_for('reset'))
        else:
            flash(u'There is a problem, Please Try resetting your Password again.')
            return redirect(url_for('reset'))
    else:
        return render_template('forget-password.html')




@app.route('/account/reset')
def reset():
    from controllers.forms import ResetPasswordForm

    if request.method == 'POST':
        form = ResetPasswordForm(request.form)
        token = request.form['token']

        if form.validate_on_submit() and token != None and len(token) > 0:

            if form.password.data != form.confirm.data:
                flash(u'Provided Passwords do not match, Please Try them again')
                return render_template('reset-password.html',form=form,model={'name':form.username.data,'token':token})

            expired , invalid , user = reset_password_token_status(token)

            if not expired and not invalid and user != None:
                user.password = utils.encrypt_password(form.password.data)
                user.save()
                flash(u'Password has been Changed Successfully.')
                return redirect(url_for('login'))
            else:
                flash(u'There is a problem , Please try resetting your Password again.')
                return redirect(url_for('reset'))
    else:
        return render_template('forget-password.html')


@app.route('/account/recover/<token>')
def do_reset_token(token):

    from flask.ext.security.recoverable import reset_password_token_status
    from controllers.forms import ResetPasswordForm
    if request.method == 'GET':
        try:
                expired, invalid, user = reset_password_token_status(token=token)

                if not invalid and not expired:
                    model = {
                        "name":user.username,
                        "token" : token
                    }
                    form = ResetPasswordForm()
                    form.username.data = user.username
                    return render_template('reset-password.html',form=form,model=model)
                else:
                    return redirect(url_for('login'))

        except Exception , s:
            flash(u'Link seems bad or expired.')


    return redirect(url_for('login'))


@app.route('/account/reset/send')
def do_reset_password():
    from controllers.utilities import *
    if request.method == 'GET':
        email = request.args['email']
        if email != None and len(email) > 1:
            user = user_datastore.find_user(email=email)
            if user != None:
                link = "%s%s" % (request.host_url, 'account/recover')
                token = generate_reset_password_token(user)
                result = send_reset_email(token,user,link)
                if result:
                    flash(u'Password Reset Instructions have been sent Successfully')
                else:
                    flash(u'Unable to send the email , Please Try again !')
            else:
                flash(u'Provided Email Does not Exists !')
                return redirect(url_for('reset'))

    return redirect(url_for('login'))


################################################################################################################


"""
These two methods are responsible for updating the customer profile
from within the profile page

"""


@app.route('/account/contact/edit', methods=['POST'])
def update_contact():
    form = ContactUpdateForm(request.form)

    if form.validate_on_submit():
        flash(u"Your Account Basic Information was updated Successfully.")
    else:
        flash(u"There was a problem updating Your Account, Please Try again!")

    return redirect(url_for('user_profile'))


@app.route('/account/general/edit', methods=['POST'])
def update_general_info():
    form = GeneralInfoForm(request.form)

    if form.validate_on_submit():
        flash(u'Your Account General Information has been updated Successfully.')
    else:
        flash(u'There was a problem updating your Account information, Please Try again !')

    return redirect(url_for('user_profile'))
