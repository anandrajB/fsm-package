
class TransitionNotAllowed(Exception):

    """Raised when we got invalid result state"""
    
    def __init__(self, *args, **kwargs):
        self.object = kwargs.pop("object", None)
        self.method = kwargs.pop("method", None)
        super(TransitionNotAllowed, self).__init__(*args, **kwargs)




class TypeDoesNotExist(Exception):

   """Raised when we got invalid result state"""

class TypeEmpty(Exception):

    """Raised when we got invalid result state"""
