from django.contrib import admin
from venzoscf.models import TransitionManager, Workflowitems, workevents


# custom model admin for transition handling


class TransitionManagerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
        qs = Workflowitems.objects.create(type = obj, initial_state = obj.initial_state , interim_state = obj.interim_state , 
        event_user = obj.user , action = obj.action , model_type = obj.type )
        qss = workevents.objects.create(workitems = qs , from_state = obj.initial_state , to_state = obj.final_state , event_user = obj.user , action = obj.action )
        qs.save()
        qss.save()



admin.site.register(TransitionManager,TransitionManagerAdmin)
admin.site.register(Workflowitems)
admin.site.register(workevents)