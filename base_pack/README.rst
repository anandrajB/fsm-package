================
quick start
================

INSTALLED_APPS = [
    ...
    'venzoscf',
]


===============
admin.py
===============
# add this to your admin.py 

from django.contrib import admin
from venzoscf.admin import TransitionManagerAdmin
from venzoscf.models import TransitionManager , workflowitems , workevents

admin.site.register(TransitionManager,TransitionManagerAdmin)


===========
setup
===========

1. add your package in INSTALLED_APPS

2. apply migrations  

3. enjoy your transitions