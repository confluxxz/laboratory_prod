# Generated by Django 4.2.11 on 2024-06-05 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0004_alter_workitem_options_work_results_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='status_experiment',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Статсик'),
        ),
    ]