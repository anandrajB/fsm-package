from .models import TransitionManager
import functools


# simple exception
class TransitionNotAllowed(Exception):
    pass




def scftransition(type):

    def wrapper_base(func):
        @functools.wraps(func)
        def inner_function(self):
            if type == "PROGRAM":
                TransitionManager.objects.get(type = "PROGRAM")
        return inner_function

    return wrapper_base






