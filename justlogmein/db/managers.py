__author__ = 'snouto'

from db.models import UserSite , Note , FormFields

"""
This is the manager class that will handle CRUD operations against Users' Sites
"""
class UserSitesManager(object):

    def __init__(self,user):
        self.user = user

    def remove_site(self,id):
        #TODO : remove the user's form based on the passed in id
        pass

    def get_AllSites(self):
        #TODO : Get all user's sites stored in the database
        pass
    def get_site(self,id):
        pass



"""
This is the manager class that will handle CRUD operations against Users' Notes
"""
class NotesManager(object):

    def __init__(self,user):
        self.user = user

    def add_note(self,noteForm):
        self.note = Note()
        #Fill here the current node data
        pass

    def remove_note(self,id):
        #TODO : remove the current user's note based on the passed in id
        pass

    def update_note(self,noteForm):
        #TODO : update here the following note , remember the note id is included within the passed in form
        pass

    def get_allnotes(self):
        #TODO : brings all available stored notes
        pass


"""
This is the manager class that will handle CRUD operations against User's FormFields
"""

class FormFieldSManager(object):

    def __init__(self,user):
        self.user = user

    def add_formfields(self,formFieldsForm):
        #TODO : Implement this function
        self.form = FormFields()

    def remove_formfields(self,id):
        #TODO : implement this function
        pass


    def update_formfields(self,formFieldsForm):
        #TODO : implement this function
        pass

    def get_allformfieldds(self):
        #TODO : implement this function
        pass
