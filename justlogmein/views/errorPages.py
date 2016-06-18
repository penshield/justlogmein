__author__ = 'snouto'

from system import app
from flask import render_template

@app.errorhandler(405)
def error_405(e):
    return render_template('error.html') , 405


@app.errorhandler(404)
def error_404(e):
    return render_template('error.html') , 404


@app.errorhandler(500)
def error_500(e):
    return render_template('error.html') , 500

@app.errorhandler(403)
def error_403(e):
    return render_template('error.html') , 403

@app.errorhandler(410)
def error_410(e):
    return render_template('error.html') , 410

@app.errorhandler(400)
def error_400(e):
    return render_template('error.html') , 400