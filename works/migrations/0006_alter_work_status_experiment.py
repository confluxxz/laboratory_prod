# Generated by Django 4.2.11 on 2024-06-05 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0005_work_status_experiment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='status_experiment',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Статсик'),
        ),
    ]
