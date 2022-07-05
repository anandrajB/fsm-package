from django.db import models

# Create your models here.

class TransitionManager(models.Model):
    type = models.CharField(max_length = 255 , unique = True)
    state = models.CharField(max_length = 255)
    initial_state = models.CharField(max_length = 255)
    interim_state = models.CharField(max_length = 255)
    final_state = models.CharField(max_length = 255)
    action = models.CharField(max_length = 255)
    

    def __str__(self):
        return self.type

    def save(self):
        if self.type is not None:
            workflowitems.objects.create()
        return super().save()



class workflowitems(models.Model):
    type = models.OneToOneField(TransitionManager,on_delete= models.CASCADE)
    intial_state = models.CharField(max_length=255)
    interim_state = models.CharField(max_length = 255)
    final_state = models.CharField(max_length = 255)

    def __str__(self):
        return self.id



class workevents(models.Model):
    workitems = models.ForeignKey(workflowitems , on_delete= models.CASCADE)
    intial_state = models.CharField(max_length=255)
    interim_state = models.CharField(max_length = 255)
    final_state = models.CharField(max_length = 255)

    def __str__(self):
        return self.intial_state