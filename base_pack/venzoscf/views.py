from .models import TransitionManager
import functools
from .exceptions import TransitionNotAllowed , TypeDoesNotExist , TypeEmpty




def scftransition(type,sign,*args,**kwargs):
    gets_model = TransitionManager.objects.get(type = type)
    if gets_model.exists():
        for len_arr in range(1,):
            return None
    return scftransition








