# Generated by Django 2.1.2 on 2018-10-31 00:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import template.models
import template.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')
                 ),
                ('name',
                 models.CharField(
                     help_text='Required. 150 characters or fewer. Letters, digits, whitespaces and @/./+/-/_ only.',
                     max_length=150,
                     validators=[
                         template.validators.TemplateNameValidator()
                     ],
                     verbose_name='template name')
                 ),
                ('file',
                 models.FileField(
                     upload_to=template.models._user_directory_path,
                     verbose_name='template file')
                 ),
                ('user',
                 models.ForeignKey(
                     blank=True,
                     null=True,
                     on_delete=django.db.models.deletion.SET_NULL,
                     to=settings.AUTH_USER_MODEL,
                     verbose_name='owner')
                 ),
            ],
            options={
                'verbose_name': 'template',
                'verbose_name_plural': 'templates',
            },
        ),
    ]