class Gsom(object):
    
    @staticmethod
    def register(credential):
        def wrapper(className):
            obj = className()
            obj.credential = credential
            return obj
        return wrapper
    