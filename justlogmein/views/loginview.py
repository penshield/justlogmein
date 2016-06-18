__author__ = 'snouto'


from views import *
import flask
from urlparse import urlparse, urljoin
from flask.ext.login import login_user
from flask import render_template ,request , url_for

@app.route('/login',methods=['POST','GET'])
def do_login():
    #if the current request is post
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']

        remember_me = request.form.__dict__.get('remember-me',None)

        if remember_me != None:
            remember_me = True
        else:
            remember_me = False

        if username != "" and password != "":
            user = user_datastore.find_user(username=username)


            if user != None and utils.verify_password(password,user.password):

                login_user(user,remember=remember_me)
            else:
                flask.flash("Invalid username and/or password, Please try again !")
                return flask.redirect(url_for('login'))

            next = request.form['next']

            if next is not None and next !=u"None" and not is_safe_url(next):
                return flask.abort(400)
            return flask.redirect(next or flask.url_for('index'))

        return flask.redirect(url_for('login'))


    return flask.redirect(url_for('login'))





def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc









