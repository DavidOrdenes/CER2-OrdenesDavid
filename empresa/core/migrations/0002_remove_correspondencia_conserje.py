# Generated by Django 4.1.2 on 2022-11-09 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='correspondencia',
            name='conserje',
        ),
    ]
