__author__ = 'snouto'

from views import *
from flask import render_template


@app.route('/')
@login_required
def index():
    return render_template("index.html")




