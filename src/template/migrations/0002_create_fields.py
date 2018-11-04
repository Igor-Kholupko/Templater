# Generated by Django 2.1.2 on 2018-11-04 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('template', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='description',
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name='description'
            ),
        ),
        migrations.AddField(
            model_name='template',
            name='email',
            field=models.EmailField(
                help_text='Required if owner is anonymous user. Email allows to identify him in future.',
                max_length=150,
                verbose_name='email address'
            ),
        ),
        migrations.AddField(
            model_name='template',
            name='is_shared',
            field=models.BooleanField(
                default=False,
                help_text='This flag make template available to other user.',
                verbose_name='is shared'
            ),
        ),
    ]
