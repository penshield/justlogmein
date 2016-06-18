__author__ = 'snouto'

from config import *
from system import app , appMail
from flask_mail import Message
from jinja2 import Environment , FileSystemLoader



def send_reset_email(token,user,link):

    try:
            if token == None or len(token) <= 0 or user == None: return False
            url = "/".join([link,token])
            model = {
                "user":user,
                "msg":{

                    "header":EMAIL_MSG_RESET_HEADER,
                    "summary":EMAIL_MSG_RESET_SUMMARY,
                    "description":EMAIL_MSG_RESET_DESCRIPTION
                },
                "link":{
                    "href":url
                }
            }

            env = Environment(loader=FileSystemLoader(EMAIL_TEMPLATES_DIR))
            payload = env.get_template("reset.html").render({'model':model})
            msg = Message(subject=EMAIL_MSG_RESET_SUBJECT,recipients=[user.email],html=payload)
            appMail.send(msg)
            return True

    except Exception , s:
        return False



def send_confirm_email(token,user,link):
     try:
            if token == None or len(token) <= 0 or user == None: return False
            url = "/".join([link,token])
            model = {
                "user":user,
                "msg":{

                    "header":EMAIL_MSG_CONFIRM_HEADER,
                    "summary":EMAIL_MSG_CONFIRM_SUMMARY,
                    "description":EMAIL_MSG_CONFIRM_DESCRIPTION
                },
                "link":{
                    "href":url
                }
            }

            env = Environment(loader=FileSystemLoader(EMAIL_TEMPLATES_DIR))
            payload = env.get_template("confirmation.html").render({'model':model})
            msg = Message(subject=EMAIL_MSG_CONFIRM_SUBJECT,recipients=[user.email],html=payload)
            appMail.send(msg)
            return True
     except Exception , s:
        return False