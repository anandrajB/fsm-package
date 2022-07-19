from django.http import HttpResponse
from venzoscf.models import TransitionManager , Action, workevents, workflowitems
from venzoscf.serializer import TransitionManagerserializer , Actionseriaizer, Workitemserializer, workeventslistserializer, workflowitemslistserializer
from venzoscf.middleware import get_current_user
from rest_framework.generics import ListAPIView , ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from venzoscf.exception import ModelNotfound, SignLengthError, TransitionNotAllowed
from venzoscf.states import sign_list, sub_action




def gets_wf_item(gets_model):
    ws = workflowitems.objects.get(transitionmanager=gets_model.id)
    return ws


class Venzoscf:

    # def __init__(self, type: str, sign: int , action : str , id :int):
    #     self.type = type
    #     self.sign = sign
    #     self.action = action
    #     self.id = id

    # creates a wf_item
    def wf_item(self):
        return None

    # creates a wf_event
    # def wf_event(self , stage , type):
    #     gets_model = TransitionManager.objects.get(type = type.upper())
    #     trans_length = int(stage) - int(gets_model.sign_required)
    #     print(trans_length)
    #     if trans_length != 1:
    #         trans_length_var = trans_length - 1
    #         print(trans_length_var)
    #     else:
    #         print(trans_length)
    #     return None

    # CORE

    def transition(self, type, action, stage, id=None):
        try:
            gets_model = TransitionManager.objects.get(type=type.upper())
            gets_action = Action.objects.get(description=action.upper())
        except:
            raise ModelNotfound(
                "no model found check transition manager and action table ")
    # sign length check
        if id is not None:
            gets_model_id = TransitionManager.objects.get(id=id)
        else:
            print("no transition model found on this id")
        if stage == gets_model.sub_sign:
            if gets_action.sign_required >= stage:
                def Transition_Handler():
                    gets_sign = gets_action.sign_required
                    if stage and gets_sign == 0:
                        print("1")
                        gets_model.sub_sign = stage
                        gets_model.save()
                        ws = workflowitems.objects.create(
                            initial_state=gets_action.from_state, interim_state=gets_action.to_state or sign_list[0], transitionmanager=gets_model or gets_model_id,
                            final_state=gets_action.to_state, action=action, subaction=sub_action[0], model_type=type.upper(), event_user=get_current_user())

                        workevents.objects.create(workflowitems=ws, event_user=get_current_user(),  initial_state=gets_action.from_state,
                                                  interim_state=gets_action.to_state, final_state=gets_action.to_state, action=action, subaction=sub_action[0], type=type.upper(), final_value="YES")

                    if stage == 0:
                        print("2")
                        gets_model.sub_sign = stage + 1
                        gets_model.save()
                        ws = workflowitems.objects.create(
                            initial_state=gets_action.from_state, interim_state=sign_list[
                                1], transitionmanager=gets_model or gets_model_id,
                            final_state=gets_action.to_state, action=action, subaction=sub_action[0], model_type=type.upper(), event_user=get_current_user())

                        workevents.objects.create(workflowitems=ws, event_user=get_current_user(),  initial_state=gets_action.from_state,
                                                  interim_state=sign_list[1], final_state=gets_action.to_state, action=action, subaction=sub_action[0], type=type.upper())
                    # final transition
                    elif stage == gets_sign:
                        print("3")
                        gets_model.sub_sign = stage
                        gets_model.save()
                        gets_wf = gets_wf_item(gets_model)
                        workflowitems.objects.filter(id=int(gets_wf.id)).update(
                            initial_state=gets_action.from_state, interim_state=gets_action.to_state, transitionmanager=gets_model.id or gets_model_id,
                            final_state=gets_action.to_state, action=action, subaction=sub_action[int(stage)], model_type=type.upper(), event_user=get_current_user())

                        workevents.objects.create(workflowitems=gets_wf, event_user=get_current_user(),  initial_state=gets_action.from_state,
                                                  interim_state=gets_action.to_state, final_state=gets_action.to_state, action=action, subaction=sub_action[int(stage)], type=type.upper(), final_value="YES")
                    # inbetween actions and trans
                    else:
                        print("4")
                        gets_wf = gets_wf_item(gets_model)
                        gets_model.sub_sign = stage + 1
                        gets_model.save()
                        workflowitems.objects.filter(id=int(gets_wf.id)).update(
                            initial_state=gets_action.from_state, interim_state=sign_list[
                                1 + stage], transitionmanager=gets_model or gets_model_id,
                            final_state=gets_action.to_state, action=action, subaction=sub_action[int(stage)], model_type=type.upper(), event_user=get_current_user())

                        workevents.objects.create(workflowitems=gets_wf, event_user=get_current_user(),  initial_state=gets_action.from_state,
                                                  interim_state=sign_list[1 + stage], final_state=gets_action.to_state, action=action, subaction=sub_action[int(stage)], type=type.upper())

                        # trans_length = int(stage) - int(gets_model.sign_required)
                        # if trans_length != 1 and int(stage) == int(gets_sign):
                        #     trans_length_var = trans_length - 1
                        # else:
                        # while stage == True:
                        #     try:
                        #             for item in sign_list:
                        #                 b = sign_list[1 + trans_length_var]
                        #                 print(b)
                        #                 c = b
                        #                 if b == sign_list[-1]:
                        #                     break
                        #             print("the value is ", c)
                        #     except:
                        #             print("cant do this ")
                        #     return None
                return Transition_Handler()
            else:
                raise SignLengthError(
                    "either the stage nor the sign_required length mismatching and the stage should not be zero ")
        else:
            raise TransitionNotAllowed(
                "TransitionNotAllowed check your sub_sign is 1 or null")


qs = Venzoscf()



def index(self):
    # transition2(stage = 
    return HttpResponse(str("hello world from venzo tech"))





### API ###

class DetailsListApiView(ListAPIView):
    queryset = TransitionManager.objects.all()
    serializer_class = TransitionManagerserializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, request):
        type = self.request.query_params.get('type')
        if type is None:
            queryset = TransitionManager.objects.all()
        queryset = TransitionManager.objects.filter(type=type)
        return queryset

    def list(self, request):
        queryset = self.get_queryset(self)
        serializer = TransitionManagerserializer(queryset, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)




class WorkFlowitemsListApi(ListAPIView):
    queryset = workflowitems.objects.all()
    serializer_class = Workitemserializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = workflowitems.objects.all()
        serializer = Workitemserializer(queryset, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)




class WorkEventsListApi(ListAPIView):
    queryset = workevents.objects.all()
    serializer_class = workeventslistserializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = workevents.objects.all()
        serializer = workeventslistserializer(queryset, many=True)
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
