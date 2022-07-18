from django.http import HttpResponse
from venzoscf.choices import StateChoices
from venzoscf.serializer import Actionseriaizer, TransitionManagerserializer
from venzoscf.testscase1 import Venzoscf
from .models import TransitionManager , Action, workflowitems, workevents
from django.db.models import Q
from django.shortcuts import render
from rest_framework.exceptions import APIException
from venzoscf.middleware import get_current_user
from rest_framework.generics import ListAPIView , ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from venzoscf.exception import ModelNotfound , SignLengthError





sign_list = [
    "INITIAL_SUBMIT",
    "AWAITING_SIGN_A",
    "AWAITING_SIGN_B",
    "AWAITING_SIGN_C",
    "AWAITING_SIGN_E",
    "AWAITING_SIGN_F",
    "AWAITING_SIGN_G",
    "AWAITING_SIGN_H",
    "AWAITING_SIGN_I",
    "AWAITING_SIGN_J",
    "AWAITING_SIGN_K",
    "AWAITING_SIGN_L",
    "AWAITING_SIGN_M",
    "AWAITING_SIGN_N",
    "AWAITING_SIGN_O",
    "AWAITING_SIGN_P",
    "AWAITING_SIGN_Q",
    "AWAITING_SIGN_R",
    "AWAITING_SIGN_S",
    "AWAITING_SIGN_T",
    "AWAITING_SIGN_U",
    "AWAITING_SIGN_V",
    "AWAITING_SIGN_W",
    "AWAITING_SIGN_X",
    "AWAITING_SIGN_Y",
    "AWAITING_SIGN_Z",
]



def scftransition(type ,action , stage , id):  
    # db checking 
    try:
        gets_model = TransitionManager.objects.get(type = type.upper())
        gets_sign = gets_model.sign_required
        gets_action = Action.objects.get(description = action.upper())
    except: 
        raise ModelNotfound("no model found")
    # sign length check 
    if int(stage) <= int(gets_model.sign_required):
        def Transition_Handler():
            print("something")
                # if stage and gets_sign == 1:
                #     ws = workflowitems.objects.create(type = gets_model , 
                #     initial_state = gets_model.initial_state , interim_state = StateChoices.STATUS_AWAITING_SIGN_A,
                #     final_state = gets_model.final_state , action = action , model_type = type , event_user = get_current_user())
                #     workevents.objects.create(workitems = ws ,event_user = get_current_user() ,  from_state = gets_model.initial_state , action = action ,type = type)
                # else:
                #     v = 0
                #     try:
                #         for item in sign_list:
                #             b = sign_list[1 + v]
                #             print(b)
                #             c = b
                #             if b == sign_list[-1]:
                #                 break
                #         print("the value is ", c)
                #     except:
                #         print("cant do this ")
                # return None
                # # if stage and gets_sign == 2:
                # #     # qss = Workflowitems.objects.get(type = type)
                # #     # workevents.objects.create(workitems = qss.id , from_state = gets_model.initial_state , action = action ,
                # #     # event_user = request.user , type = type )
                # # else:
                # #     try : 
                # #         if stage == 1:
                # #             ws = Workflowitems.objects.create(type = gets_model , 
                # #             initial_state = gets_model.initial_state , interim_state = StateChoices.STATUS_AWAITING_SIGN_A,
                # #             final_state = gets_model.final_state , action = action , model_type = type )
                # #             we = workevents.objects.create(workitems = ws , from_state = gets_model.initial_state , action = action ,
                # #             type = type )
                # #             ws.save()
                # #             we.save()
                # #         else:
                # #             try:
                # #                 gets_ttwf = Workflowitems.objects.get(Q(type__type__contains=type) | Q(id=id))
                # #             except:
                # #                 raise MoreThanOneModel("either the type has ")
                # #     except:
                # #         raise APIException("There was a problem!")
        return Transition_Handler()
    else:
        raise SignLengthError("either the stage nor the sign_required lenght mismatching")
    


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

qs = Venzoscf()

def index(self):
    
    return HttpResponse(str("data"))





### API ###

class DetailsListApiView(ListAPIView):
    queryset = TransitionManager.objects.all()
    serializer_class = TransitionManagerserializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = TransitionManager.objects.all()
        serializer = TransitionManagerserializer(queryset, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)





# action create and list api 


class ActionListApi(ListCreateAPIView):
    queryset = Action.objects.all()
    serializer_class = Actionseriaizer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Action.objects.all()
        serializer = Actionseriaizer(queryset, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = Actionseriaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "failure", "data": serializer.errors},status=status.HTTP_204_NO_CONTENT)
