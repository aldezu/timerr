# Generated by Django 3.0.2 on 2021-10-30 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timerr', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='excersises',
            name='id',
        ),
        migrations.AlterField(
            model_name='excersises',
            name='task',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
