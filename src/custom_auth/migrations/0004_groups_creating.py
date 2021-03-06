# Generated by Django 2.1.2 on 2018-11-11 15:47

from django.db import migrations
from django.db.models import Q


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Group = apps.get_model("custom_auth", "Group")
    Permission = apps.get_model("auth", "Permission")
    db_alias = schema_editor.connection.alias
    q = Permission.objects.using(db_alias).filter(Q(codename__iendswith="template") | Q(codename__iexact="view_user"))
    admins_group = Group(name="Administrators")
    admins_group.save(using=db_alias)
    [admins_group.permissions.add(permission) for permission in q]


def reverse_func(apps, schema_editor):
    # reverse_func() should delete group.
    Group = apps.get_model("custom_auth", "Group")
    db_alias = schema_editor.connection.alias
    Group.objects.using(db_alias).filter(name="Administrators").delete()


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0003_back_to_original_group'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
