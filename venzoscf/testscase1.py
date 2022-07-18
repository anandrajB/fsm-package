from venzoscf.models import TransitionManager , Action , workflowitems , workevents
from venzoscf.middleware import get_current_user
from venzoscf.exception import ModelNotfound , SignLengthError
from venzoscf.states import sign_list
from venzoscf.choices import StateChoices


def gets_wf_item(gets_model):
        ws = workflowitems.objects.get(type = gets_model)
        return ws



class Venzoscf:

    # def __init__(self, type: str, sign: int , action : str , id :int):
    #     self.type = type
    #     self.sign = sign
    #     self.action = action
    #     self.id = id

    #creates a wf_item
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


    ## CORE



    def transition(self, type ,action , stage , id = None):
        try:
            gets_model = TransitionManager.objects.get(type = type.upper())
            # gets_model_id = TransitionManager.objects.get(id = id )
            gets_action = Action.objects.get(description = action.upper())
        except: 
            raise ModelNotfound("no model found check transition manager and action table ")
    # sign length check 
        if stage == 0:
            def Transition_Handler():
                    gets_sign = gets_action.sign_required
                    if stage and gets_sign == 1:
                        ws = workflowitems.objects.create(
                        initial_state = gets_action.from_state , interim_state = gets_action.to_state or sign_list[0], transitionmanager = gets_model or gets_model_id, 
                        final_state = gets_action.to_state , action = action , model_type = type.upper() , event_user = get_current_user())

                        workevents.objects.create(workflowitems = ws ,event_user = get_current_user() ,  initial_state = gets_action.initial_state , 
                        interim_state = None,final_state = gets_action.to_state, action = action ,type = type.upper() , final_value =  "YES")
                    # final transition
                    if stage == gets_sign:
                        gets_wf = gets_wf_item(gets_model)
                        workflowitems.objects.filter(id = gets_wf).update(
                        initial_state = gets_model.initial_state , interim_state = gets_model.to_state,transitionmanager = gets_model or gets_model_id,
                        final_state = gets_model.final_state , action = action , model_type = type.upper() , event_user = get_current_user())

                        workevents.objects.create(workflowitems = gets_wf ,event_user = get_current_user() ,  initial_state = gets_action.initial_state ,
                        interim_state = gets_action.to_state ,final_state = gets_action.to_state,action = action ,type = type.upper() , final_value =  "YES")
                    # inbetween actions and trans
                    else:
                        workflowitems.objects.filter(id = gets_wf).update(
                        initial_state = gets_model.initial_state , interim_state = sign_list[stage],transitionmanager = gets_model or gets_model_id,
                        final_state = gets_model.final_state , action = action , model_type = type.upper() , event_user = get_current_user())

                        workevents.objects.create(workflowitems = gets_wf ,event_user = get_current_user() ,  initial_state = gets_action.initial_state ,
                        interim_state = sign_list[stage] ,final_state = gets_action.to_state,action = action ,type = type.upper())
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
                        
                        # if stage and gets_sign == 2:
                        #     # qss = Workflowitems.objects.get(type = type)
                        #     # workevents.objects.create(workflowitems = qss.id , from_state = gets_model.initial_state , action = action ,
                        #     # event_user = request.user , type = type )
                        # else:
                        #     try : 
                        #         if stage == 1:
                        #             ws = Workflowitems.objects.create(type = gets_model , 
                        #             initial_state = gets_model.initial_state , interim_state = StateChoices.STATUS_AWAITING_SIGN_A,
                        #             final_state = gets_model.final_state , action = action , model_type = type )
                        #             we = workevents.objects.create(workflowitems = ws , from_state = gets_model.initial_state , action = action ,
                        #             type = type )
                        #             ws.save()
                        #             we.save()
                        #         else:
                        #             try:
                        #                 gets_ttwf = Workflowitems.objects.get(Q(type__type__contains=type) | Q(id=id))
                        #             except:
                        #                 raise MoreThanOneModel("either the type has ")
                        #     except:
                        #         raise APIException("There was a problem!")`
            return Transition_Handler()
        else:
            raise SignLengthError("either the stage nor the sign_required length mismatching and the stage should not be zero ")


    