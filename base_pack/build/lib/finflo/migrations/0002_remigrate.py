# Generated by Django 3.2.5 on 2022-10-14 10:50

import contextlib
from django.conf import settings
from django.db import migrations




# RUN ON MIGRATIONS  -- remigrate if work_model is updated 

def update_flow_model(apps, schema_editor):
    flowmodel = apps.get_model("finflo.Flowmodel")
    try:
        a = settings.FINFLO['WORK_MODEL']
        db_alias = schema_editor.connection.alias
        for model in a:
            print("FLOWS MIGRATING")
            flowmodel.objects.using(db_alias).update_or_create(description = model.lower())
    except:
        raise LookupError("Couldn't find work_model in settings.py check documentation")


# def updates_party_type_model(apps, schema_editor):
#     Party = apps.get_model("finflo.Party")
#     abstract_models = settings.FINFLO['PARTY_MODEL']
#     db_alias = schema_editor.connection.alias
#     with contextlib.suppress(Exception):
#         if abstract_models:
#             base_model_from_app = apps.get_model(abstract_models[0])
#             for iter in base_model_from_app.objects.all():
#                 Party.objects.using(db_alias).update_or_create(description = iter.name)
#             print("PARTY MODELS CREATED SUCCESSFULLY")


    
class Migration(migrations.Migration):

    dependencies = [
        ('finflo', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(update_flow_model),
        # migrations.RunPython(updates_party_type_model)
    ]