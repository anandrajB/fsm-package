from venzoscf.views import DetailsListApiView , ActionListApi, WorkEventsListApi, WorkFlowitemsListApi
from django.urls import path



urlpatterns = [
    path('action/',ActionListApi.as_view()),
    path('model/',DetailsListApiView.as_view()),
    path('workflowitems/',WorkFlowitemsListApi.as_view()),
    path('workevents/',WorkEventsListApi.as_view())
]
