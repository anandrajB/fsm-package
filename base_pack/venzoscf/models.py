from django.db import models
from django.conf import settings
# from django.contrib.postgres.fields import ArrayField

from venzoscf.middleware import get_current_user



# Create your models here.

class TransitionManager(models.Model):
    type = models.CharField(max_length = 255 , unique = True)
    sub_sign = models.IntegerField(default = 1 , editable= False)

    # default 1 for initial submit and maker process

    def save(self, *args, **kwargs):
        self.type = self.type.upper()
        return super(TransitionManager,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = "1. TransitionManager"

    

 
class workflowitems(models.Model):
    
    created_date = models.DateTimeField(auto_now_add=True)
    transitionmanager = models.OneToOneField(TransitionManager, on_delete=models.CASCADE,blank=True, null=True )
    initial_state  = models.CharField(max_length=50,default = 'DRAFT')
    interim_state = models.CharField(max_length=50,default = 'DRAFT')
    final_state = models.CharField(max_length=50,default = 'DRAFT')
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
        ordering = ['id']


# WORKEVENTS
class workevents(models.Model):

    workflowitems = models.ForeignKey(workflowitems, on_delete=models.CASCADE , related_name='WorkFlowEvents')
    action = models.CharField(max_length=25, blank=True, null=True)
    subaction = models.CharField(max_length=55 , blank=True, null=True)
    initial_state  = models.CharField(max_length=50 , default = 'DRAFT')
    interim_state = models.CharField(max_length=50,default = 'DRAFT')
    final_state = models.CharField(max_length=50,default = 'DRAFT')
    event_user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE )
    end_value = models.CharField(max_length=55,blank=True, null=True)
    is_read = models.BooleanField(default=True,blank=True, null=True)
    final_value = models.CharField(max_length=55,blank=True, null=True)
    comments = models.CharField(max_length=500,blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=55)
    

    class Meta:
        verbose_name_plural = "3. WorkFlowEvent"
        ordering = ['id']



class Action(models.Model):
    description = models.CharField(max_length=255 , blank = True , null=True)
    type = models.ForeignKey(TransitionManager , on_delete = models.CASCADE)
    from_state = models.CharField(max_length=255 , default = "DRAFT")
    to_state = models.CharField(max_length=255 , default = "DRAFT")
    sign_required =  models.IntegerField(default = 1)

    def save(self, *args, **kwargs):
        self.description = self.description.upper()
        return super(Action,self).save(*args, **kwargs)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "4. Action"


