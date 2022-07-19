from django.contrib import admin
from venzoscf.models import Action, TransitionManager, workflowitems, workevents
# Register your models here.



admin.site.register(TransitionManager)
admin.site.register(workflowitems)
admin.site.register(workevents)
admin.site.register(Action)