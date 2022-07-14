from rest_framework import serializers
from .models import TransitionManager , workevents , workflowitems


class Workeventsserializer(serializers.ModelSerializer):
    class Meta:
        model = workevents
        fields = [
            'id',
            'workitems',
            'action',
            'subaction',
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
            'workflowevent'
        ]




class TransitionManagerserializer(serializers.ModelSerializer):
    workflowitems = Workitemserializer(read_only=True)
    # workevents = Workeventsserializer(read_only=True)
    class Meta:
        model = TransitionManager
        fields = [
            'type',
            'from_state',
            'to_state',
            'sign_required',
            'workflowitems'
        ]



