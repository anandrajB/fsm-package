from django.contrib import admin
from venzoscf.models import Action, TransitionManager, Workflowitems, workevents
# Register your models here.



admin.site.register(TransitionManager)
admin.site.register(Workflowitems)
admin.site.register(workevents)
admin.site.register(Action)