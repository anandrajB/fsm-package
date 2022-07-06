from django.db import models
from django.conf import settings
# from django.contrib.postgres.fields import ArrayField


def myuser(request):
        return request.user

# Create your models here.

class TransitionManager(models.Model):
    type = models.CharField(max_length = 255 , unique = True)
    state = models.CharField(max_length = 255)
    initial_state = models.CharField(max_length = 255)
    interim_state = models.CharField(max_length = 255)
    final_state = models.CharField(max_length = 255)
    action = models.CharField(max_length = 255)
    sign = models.IntegerField()
    
    def __str__(self):
        return self.type

    

    def save(self,request):
        if self.type is not None:
            qs = Workflowitems.objects.create(type = self.type.id , initial_state = self.initial_state , interim_state = self.intermediate_state , 
            event_user = myuser(request) , model_type = self.type )
            workevents.objecst.create(workitems = qs , from_state = self.initial_state , to_state = self.final_state , event_user = myuser(request))
        return super().save()



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
        verbose_name_plural = "WorkFlowItem"


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
        verbose_name_plural = "WorkFlowEvent"