from venzoscf.models import TransitionManager, Action, workflowitems, workevents
from venzoscf.middleware import get_current_user
from venzoscf.exception import ModelNotfound, SignLengthError, TransitionNotAllowed
from venzoscf.states import sign_list, sub_action
from venzoscf.choices import StateChoices


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


def transition2(stage, id=None):
    gets_action = Action.objects.get(description="SUBMIT")
    print(gets_action.sign_required)
    if stage != 0 and stage <= gets_action.sign_required:
        print("hello world")
    else:
        print("it works")
