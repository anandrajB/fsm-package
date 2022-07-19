from django.http import HttpResponse
from venzoscf.models import TransitionManager , Action, workevents, workflowitems
from venzoscf.serializer import TransitionManagerserializer , Actionseriaizer, Workitemserializer, workeventslistserializer, workflowitemslistserializer
from venzoscf.middleware import get_current_user
from rest_framework.generics import ListAPIView , ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from venzoscf.testscase1 import Venzoscf, transition2

from venzoscf.testscase1 import Venzoscf


qs = Venzoscf()





def index(self):
    # transition2(stage = 3)
    qs.transition(type = "INVOICE" , action = "submit" , stage = 0)
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
