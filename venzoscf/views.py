from django.http import HttpResponse

from venzoscf.choices import StateChoices
from .models import TransitionManager , Action, Workflowitems, workevents
import functools
from django.template import RequestContext
from django.db.models import Q
from django.shortcuts import render
from rest_framework.exceptions import APIException
from myapp.middleware import get_current_user


# simple exception
class TransitionNotAllowed(Exception):
    pass


class ActionNotFound(Exception):
    pass


class TypeDoesNotExist(Exception):
    pass

class TypeEmpty(Exception):
    pass

class ModelNotfound(APIException):
    pass

class MoreThanOneModel(Exception):
    pass

def myuser(request):
    return request.user

def scftransition(type ,action , stage ,id):
    try:
        gets_model = TransitionManager.objects.get(type = type.upper())
        gets_action = Action.objects.get(description = action)
        print(gets_model)
        print(gets_action)
    except: 
        raise ModelNotfound("no model found")
    def Transition_Handler():
        gets_sign = gets_model.sign_required
        if stage and gets_sign == 1:
            ws = Workflowitems.objects.create(type = gets_model , 
            initial_state = gets_model.initial_state , interim_state = StateChoices.STATUS_AWAITING_SIGN_A,
            final_state = gets_model.final_state , action = action , model_type = type , event_user = get_current_user())
            workevents.objects.create(workitems = ws ,event_user = get_current_user() ,  from_state = gets_model.initial_state , action = action ,
            type = type)
        else:
            raise TransitionNotAllowed('unable to do the transitions')
        # if stage and gets_sign == 2:
        #     # qss = Workflowitems.objects.get(type = type)
        #     # workevents.objects.create(workitems = qss.id , from_state = gets_model.initial_state , action = action ,
        #     # event_user = request.user , type = type )
        # else:
        #     raise TransitionNotAllowed("unable to do transition")
        # try : 
        #     if stage == 1:
        #         ws = Workflowitems.objects.create(type = gets_model , 
        #         initial_state = gets_model.initial_state , interim_state = StateChoices.STATUS_AWAITING_SIGN_A,
        #         final_state = gets_model.final_state , action = action , model_type = type )
        #         we = workevents.objects.create(workitems = ws , from_state = gets_model.initial_state , action = action ,
        #         type = type )
        #         ws.save()
        #         we.save()
        #     else:
        #         try:
        #             gets_ttwf = Workflowitems.objects.get(Q(type__type__contains=type) | Q(id=id))
        #         except:
        #             raise MoreThanOneModel("either the type has ")
        # except:
        #     raise APIException("There was a problem!")
    return Transition_Handler()
    


# def test():
#     type = "PROGRAM"
#     id = None
#     # try:
#     #     gets_wf = Workflowitems.objects.get(Q(type__type__contains=type)| Q(id=id))
#     #     print(gets_wf)
#     # except:
#     #     print("ok")
    
#     print(gets_wf)
#     return test



def index(self):
    scftransition(type = "PROGRAM",action = "SUBMIT" , stage = 1 ,id=None)
    return HttpResponse(str("data"))


