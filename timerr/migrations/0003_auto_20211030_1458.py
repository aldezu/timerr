# Generated by Django 3.0.2 on 2021-10-30 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timerr', '0002_auto_20211030_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='excersises',
            old_name='task',
            new_name='name',
        ),
    ]