from django.db import models
from django.conf import settings
# from django.contrib.postgres.fields import ArrayField




# Create your models here.

class TransitionManager(models.Model):
    type = models.CharField(max_length = 255 , unique = True)
    state = models.CharField(max_length = 255)
    initial_state = models.CharField(max_length = 255)
    final_state = models.CharField(max_length = 255)
    sign_required = models.IntegerField()
    
    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = "1. TransitionManager"

    


class Workflowitems(models.Model):
    
    created_date = models.DateTimeField(auto_now_add=True)
    type = models.OneToOneField(TransitionManager, on_delete=models.CASCADE,blank=True, null=True)
    initial_state = models.CharField(max_length=50)
    interim_state = models.CharField(max_length=50)
    final_state = models.CharField(max_length=50)
    event_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # next_available_transitions = ArrayField(models.CharField(max_length=500,blank=True, null=True,default=None),blank=True, null=True,default = None)
    action = models.CharField(max_length=25 , blank=True, null=True)
    subaction = models.CharField(max_length=55 , blank=True, null=True)
    previous_action = models.CharField(max_length=55 , blank=True, null=True)
    model_type  = models.CharField(max_length=55)
    comments = models.CharField(max_length=500,blank=True, null=True)
    is_read = models.BooleanField(default=True,blank=True, null=True)

    class Meta:
        verbose_name_plural = "2. WorkFlowItem"


# WORKEVENTS
class workevents(models.Model):

    workitems = models.ForeignKey(Workflowitems, on_delete=models.CASCADE, related_name='workflowevent')
    from_state = models.CharField(max_length=50, default='DRAFT')
    action = models.CharField(max_length=25, blank=True, null=True)
    subaction = models.CharField(max_length=55 , blank=True, null=True)
    to_state = models.CharField(max_length=50, default='DRAFT')
    interim_state = models.CharField(max_length=50, default='DRAFT')
    event_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    end_value = models.CharField(max_length=55,blank=True, null=True)
    is_read = models.BooleanField(default=True,blank=True, null=True)
    final_value = models.CharField(max_length=55,blank=True, null=True)
    comments = models.CharField(max_length=500,blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=55)
    

    class Meta:
        verbose_name_plural = "3. WorkFlowEvent"



class Action(models.Model):
    description = models.CharField(max_length=255 , blank = True , null=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "4. Action"