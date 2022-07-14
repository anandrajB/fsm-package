from venzoscf.models import TransitionManager


class Venzoscf:
    # type : str
    # sign : int
    # action : str
    # id : int

    # def __init__(self, type: str, sign: int , action : str , id :int):
    #     self.type = type
    #     self.sign = sign
    #     self.action = action
    #     self.id = id

    #creates a wf_item
    def wf_item(self):
        area = self.type * self.sign
        print(f"The area of the rectangle is: {area}")


    # creates a wf_event
    def wf_event(self):
        perimeter = (self.type + self.sign) * 2
        print(f"The perimeter of the rectangle is: {perimeter}")


    ## CORE

    def transition(self, type  ):
        gets_model = TransitionManager.objects.get(type = type.upper())
        print(gets_model)
        print(f"The diagonal of the rectangle is:")
        return gets_model


    