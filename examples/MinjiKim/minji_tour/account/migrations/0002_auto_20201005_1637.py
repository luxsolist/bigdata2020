# Generated by Django 3.0.8 on 2020-10-05 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='userid',
            new_name='username',
        ),
    ]
