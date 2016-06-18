__author__ = 'snouto'

from views import *
from flask import render_template , request , session
from controllers.forms import  *

@app.route('/account/profile',methods=['GET'])
@login_required
def user_profile():

    form = RegisterationForm()

    user = session['current_active_user']

    form.load_data(user)

    return render_template("profile.html",form=form)

@app.route("/account/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

