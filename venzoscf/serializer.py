from rest_framework import serializers
from .models import TransitionManager , workevents , workflowitems , Action


class Workeventsserializer(serializers.ModelSerializer):
    class Meta:
        model = workevents
        fields = [
            'id',
            'workitems',
            'action',
            'subaction',
            'initial_state',
            'interim_state',
            'final_state',
        ]




class Workitemserializer(serializers.ModelSerializer):
    workflowevent = Workeventsserializer(many=True, read_only=True)
    class Meta:
        model = workflowitems
        fields = [
            'id',
            'transitionmanager',
            'initial_state',
            'interim_state',
            'final_state',
            'event_user',
            'workflowevent'
        ]




class TransitionManagerserializer(serializers.ModelSerializer):
    workflowitems = Workitemserializer(read_only=True)
    # workevents = Workeventsserializer(read_only=True)
    class Meta:
        model = TransitionManager
        fields = [
            'type',
            'workflowitems'
        ]



class Actionseriaizer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'