from finflo.transition import FinFlotransition 
from django.shortcuts import HttpResponse
from rest_framework.views import APIView

# EXAMPLE CODE
qs = FinFlotransition()

def index(self):
    # transition2(stage = 3)
    qs.transition(type = "INVOICE" , action = "DELETE" , stage = 2)
    return HttpResponse(str("data"))





class SampleTransitionMaker(APIView):

    def post(self,request,*args, **kwargs):
        qs(source= "some" , interim = "test" , final = "test" , action = "test" , subaction = "test")
        return HttpResponse("transition updated successfully")

