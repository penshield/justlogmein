__author__ = 'snouto'




def logEnabled(func):
    def wrapped(*args,**kargs):
        """
        :param function: do something before the function call
        :return:
        """
        print ("%s was called " % func.__name__)
        result =  func(*args,**kargs)
        """
        Do something after the function call
        """
        return result

    return wrapped