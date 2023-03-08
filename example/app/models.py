from django.db import models

# Create your models here.


class Model1(models.Model):
    username = models.CharField(max_length=255)
    user_id = models.IntegerField()

    def __str__(self):
        return self.username

        