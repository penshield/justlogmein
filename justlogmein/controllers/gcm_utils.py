__author__ = 'snouto'

from config import GCM_PROJECT_ID , GCM_PROJECT_NUMBER , GCM_API_KEY
from gcm import GCM



def send_gcm_message(user,message,target):
    gcm = GCM(GCM_API_KEY)
    gcm_settings = user.gcm
    if gcm_settings is None:
        return False
    else:
        if target == 'all':
            registrationIds = []
            for field in gcm_settings:
                registrationId = field['registrationId']
                registrationIds.append(registrationId)
            gcm.json_request(registration_ids=registrationIds,data=message)
        else:
            result = False
            for field in gcm_settings:
                type = field['type']
                if type == target:
                    result = True
                    registrationId = field['registrationId']
                    gcm.json_request(registration_ids=[registrationId],data=message)
            return result


