# Generated by Django 4.0.4 on 2023-11-16 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='research',
            name='date',
        ),
    ]
