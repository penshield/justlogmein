__author__ = 'snouto'

template_folder ="/media/snouto/rest/projects/justlogmein-project/justlogmein/templates"
static_folder="/media/snouto/rest/projects/justlogmein-project/justlogmein/static"

"""
The following is the MongoDB database connectivity parameters that are system wide applied
"""

MONGODB_HOST="192.168.1.4"
MONGODB_DB="justlogmein"
MONGODB_PORT=27017


"""
Application Settings
"""


SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT = 'de167f684ebe8a8a4c31c357896e18fa'
SECURITY_CONFIRM_SALT = SECURITY_PASSWORD_SALT
SECURITY_RESET_SALT = SECURITY_PASSWORD_SALT
SECURITY_CONFIRMABLE = True
SECURITY_RECOVERABLE = True


"""
Application Mail Settings
"""

MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = "apps@is.com.sa"
MAIL_PASSWORD = "M@safsafsaF"
MAIL_DEFAULT_SENDER = "apps@gmail.com"


"""
Application Security URLs
"""

SECURITY_LOGIN_URL = '/account/login'
SECURITY_LOGOUT_URL = '/account/logout'
SECURITY_REGISTER_URL = '/account/register'
SECURITY_RESET_URL = '/account/reset'
SECURITY_CHANGE_URL = '/account/change'
SECURITY_CONFIRM_URL = '/account/confirm'
SECURITY_CONFIRM_ERROR_VIEW = None
SECURITY_POST_LOGOUT_VIEW = '/account/login'
SECURITY_FORGOT_PASSWORD_TEMPLATE = 'forget-password.html'
SECURITY_LOGIN_USER_TEMPLATE = 'login.html'
SECURITY_REGISTER_USER_TEMPLATE ='account-register.html'
SECURITY_RESET_PASSWORD_TEMPLATE = 'forget-password.html'
SECURITY_POST_CONFIRM_VIEW = 'login'
SECURITY_SEND_CONFIRMATION_TEMPLATE = 'confirm-account.html'
SECURITY_CHANGE_PASSWORD_TEMPLATE = 'change-password.html'
SECURITY_CHANGEABLE = True



"""
The following are some template messages for reset and confirmation emails
"""
EMAIL_MSG_RESET_SUBJECT = ""
EMAIL_MSG_RESET_HEADER = """ """
EMAIL_MSG_RESET_SUMMARY =""" """
EMAIL_MSG_RESET_DESCRIPTION= """ """

# THE FOLLOWING IS FOR CONFIRMATION MESSAGE
EMAIL_MSG_CONFIRM_HEADER = """ """
EMAIL_MSG_CONFIRM_SUMMARY = """ """
EMAIL_MSG_CONFIRM_DESCRIPTION = """ """
EMAIL_MSG_CONFIRM_SUBJECT = ""
EMAIL_TEMPLATES_DIR = "/".join([template_folder,"email"])