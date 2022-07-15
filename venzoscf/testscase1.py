from venzoscf.models import TransitionManager , Action , workflowitems , workevents
from venzoscf.middleware import get_current_user
from venzoscf.exception import ModelNotfound , SignLengthError
from venzoscf.states import sign_list
from venzoscf.choices import StateChoices





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
    def wf_event(self , stage , type):
        gets_model = TransitionManager.objects.get(type = type.upper())
        trans_length = int(stage) - int(gets_model.sign_required)
        print(trans_length)
        if trans_length != 1:
            trans_length_var = trans_length - 1
            print(trans_length_var)
        else:
            print(trans_length)
        return None


    ## CORE

    def transition(self, type ,action , stage , id):
        try:
            gets_model = TransitionManager.objects.get(type = type.upper())
            gets_sign = gets_model.sign_required
            gets_action = Action.objects.get(description = action.upper())
        except: 
            raise ModelNotfound("no model found")
    # sign length check 
        if int(stage) <= int(gets_model.sign_required):
            def Transition_Handler():
                    if stage and gets_sign == 1:
                        ws = workflowitems.objects.create(type = gets_model , 
                        initial_state = gets_model.initial_state , interim_state = StateChoices.STATUS_AWAITING_SIGN_A,
                        final_state = gets_model.final_state , action = action , model_type = type , event_user = get_current_user())
                        workevents.objects.create(workitems = ws ,event_user = get_current_user() ,  from_state = gets_model.initial_state , action = action ,type = type)
                    else:
                        
                        trans_length = int(stage) - int(gets_model.sign_required)
                        if trans_length != 1 and int(stage) == int(gets_sign):
                            trans_length_var = trans_length - 1
                        else:
                            try:
                                    for item in sign_list:
                                        b = sign_list[1 + trans_length_var]
                                        print(b)
                                        c = b
                                        if b == sign_list[-1]:
                                            break
                                    print("the value is ", c)
                            except:
                                    print("cant do this ")
                            return None
                        # if stage and gets_sign == 2:
                        #     # qss = Workflowitems.objects.get(type = type)
                        #     # workevents.objects.create(workitems = qss.id , from_state = gets_model.initial_state , action = action ,
                        #     # event_user = request.user , type = type )
                        # else:
                        #     try : 
                        #         if stage == 1:
                        #             ws = Workflowitems.objects.create(type = gets_model , 
                        #             initial_state = gets_model.initial_state , interim_state = StateChoices.STATUS_AWAITING_SIGN_A,
                        #             final_state = gets_model.final_state , action = action , model_type = type )
                        #             we = workevents.objects.create(workitems = ws , from_state = gets_model.initial_state , action = action ,
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
            raise SignLengthError("either the stage nor the sign_required lenght mismatching")


    