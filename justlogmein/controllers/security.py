

from itsdangerous import Serializer
from config import *
import system

class SecurityTokenManager(object):
    def __init__(self):
        pass

    @staticmethod
    def generate_token_for(user,expiration=100):
        if user == None: return None
        serializer = Serializer(SECURITY_PASSWORD_SALT)
        token = serializer.dumps({"username":str(user.username),'id':str(user.id)}).decode('utf-8')
        return token


    @staticmethod
    def verify_token_for(token):

        if token == None or len(token) <= 0 : return False
        serializer = Serializer(SECURITY_PASSWORD_SALT)
        data = serializer.loads(token,SECURITY_PASSWORD_SALT)
        if data != None:
            id = data.id
            username = data.username
            email = data.email
            currentUser = system.user_datastore.find_user(id=id,username=username,email=email)
            if currentUser != None: return True
            else: return False
        return False


